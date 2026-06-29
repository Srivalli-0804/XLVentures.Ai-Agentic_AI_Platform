import { Request, Response, NextFunction } from 'express';
import { addWorkflowToQueue } from '../services/queueService';
import { WorkflowRunModel } from '../models/WorkflowRun';

export const enqueueWorkflow = async (req: Request, res: Response, next: NextFunction) => {
  try {
    const { goal, payload } = req.body;
    const userId = (req as Request & { user?: { id?: string } }).user?.id;
    const workflowRun = await WorkflowRunModel.create({
      name: `workflow-${Date.now()}`,
      status: 'pending',
      goal,
      requestedBy: userId,
      requiresApproval: true,
      steps: []
    });

    const job = await addWorkflowToQueue({ workflowId: workflowRun.id, goal, payload });
    workflowRun.jobId = String(job.id);
    await workflowRun.save();

    res.json({ jobId: job.id, workflowId: workflowRun.id, goal, status: 'queued' });
  } catch (error) {
    if (error instanceof Error) {
      return res.status(503).json({ message: `Unable to queue workflow: ${error.message}` });
    }
    next(error);
  }
};
