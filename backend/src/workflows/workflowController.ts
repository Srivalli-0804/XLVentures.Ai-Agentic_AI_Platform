import { Request, Response, NextFunction } from 'express';
import { Planner } from '../planner/planner';
import { agents } from '../agents';
import { WorkflowRunModel } from '../models/WorkflowRun';
import { companyService } from '../services/companyService';
import { memoryService } from '../services/memoryService';

const planner = new Planner(agents);

export const runWorkflow = async (req: Request, res: Response, next: NextFunction) => {
  try {
    const { goal, payload } = req.body;
    const existingRun = await WorkflowRunModel.create({
      name: `workflow-${Date.now()}`,
      status: 'running',
      goal,
      steps: []
    });

    const result = await planner.plan(goal, payload || {});

    if (Array.isArray(result.output?.enrichedCompanies)) {
      await companyService.saveCompanies(result.output.enrichedCompanies as any[]);
      for (const company of result.output.enrichedCompanies as any[]) {
        if (company.name) {
          await memoryService.saveEntry('company', company.name, company, ['company', 'workflow']);
        }
      }
    }

    await memoryService.saveEntry('plannerHistory', existingRun.id, { history: result.history }, ['planner', 'workflow']);

    existingRun.status = result.success ? 'completed' : 'failed';
    existingRun.steps = result.history.map((item) => ({
      agent: item.agent,
      status: item.status,
      message: item.message
    }));
    await existingRun.save();

    res.json(result);
  } catch (error) {
    next(error);
  }
};

export const getWorkflowStatus = async (_req: Request, res: Response, next: NextFunction) => {
  try {
    const runs = await WorkflowRunModel.find().sort({ createdAt: -1 }).limit(10).lean();
    res.json(runs);
  } catch (error) {
    next(error);
  }
};
