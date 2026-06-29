import { Job } from 'bullmq';
import { Planner } from '../planner/planner';
import { agents } from '../agents';
import { WorkflowRunModel } from '../models/WorkflowRun';
import { companyService } from '../services/companyService';
import { memoryService } from '../services/memoryService';

const planner = new Planner(agents);

export const runWorkflowJob = async (job: Job) => {
  const { workflowId, goal, payload } = job.data;
  let workflowRun = await WorkflowRunModel.findById(workflowId);
  if (!workflowRun) {
    workflowRun = await WorkflowRunModel.create({
      name: `workflow-${Date.now()}`,
      status: 'running',
      steps: [],
      outputPayload: payload || {}
    });
  } else {
    workflowRun.status = 'running';
    workflowRun.jobId = String(job.id);
    await workflowRun.save();
  }

  const result = await planner.plan(goal, payload || {});

  if (Array.isArray(result.output?.enrichedCompanies)) {
    await companyService.saveCompanies(result.output.enrichedCompanies as any[]);
    for (const company of result.output.enrichedCompanies as any[]) {
      if (company.name) {
        await memoryService.saveEntry('company', company.name, company, ['company', 'workflow']);
      }
    }
  }

  workflowRun.steps = result.history.map((item) => ({
    agent: item.agent,
    status: item.status,
    message: item.message
  }));
  workflowRun.outputPayload = result.output;

  if (result.pendingApproval) {
    workflowRun.status = 'pendingApproval';
  } else {
    workflowRun.status = result.success ? 'completed' : 'failed';
  }

  await workflowRun.save();
  await memoryService.saveEntry('plannerHistory', workflowRun.id, { history: result.history }, ['planner', 'workflow']);

  return result;
};
