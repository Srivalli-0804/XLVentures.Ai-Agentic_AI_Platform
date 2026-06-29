import { Request, Response, NextFunction } from 'express';
import { CompanyModel } from '../models/Company';
import { MemoryEntryModel } from '../models/MemoryEntry';
import { WorkflowRunModel } from '../models/WorkflowRun';
import { agents } from '../agents';

export const getStats = async (_req: Request, res: Response, next: NextFunction) => {
  try {
    const [companyCount, memoryCount, workflowCount, runningWorkflow] = await Promise.all([
      CompanyModel.countDocuments(),
      MemoryEntryModel.countDocuments(),
      WorkflowRunModel.countDocuments(),
      WorkflowRunModel.exists({ status: 'running' })
    ]);

    const recentWorkflows = await WorkflowRunModel.find()
      .sort({ createdAt: -1 })
      .limit(5)
      .lean();

    res.json({
      workflows: workflowCount,
      companies: companyCount,
      agents: agents.length,
      memory: memoryCount,
      plannerStatus: runningWorkflow ? 'Running' : 'Idle',
      recentWorkflows: recentWorkflows.map((workflow) => ({
        id: workflow._id?.toString() ?? '',
        name: workflow.name,
        status: workflow.status
      }))
    });
  } catch (error) {
    next(error);
  }
};
