import { Request, Response, NextFunction } from 'express';
import { WorkflowRunModel } from '../models/WorkflowRun';

export const approveWorkflow = async (req: Request, res: Response, next: NextFunction) => {
  try {
    const { workflowId, action } = req.body;
    const workflow = await WorkflowRunModel.findById(workflowId);
    if (!workflow) {
      return res.status(404).json({ message: 'Workflow not found' });
    }

    if (workflow.status !== 'pendingApproval') {
      return res.status(400).json({ message: 'Workflow is not awaiting approval' });
    }

    workflow.status = action === 'approve' ? 'completed' : 'failed';
    await workflow.save();

    res.json({ success: true, status: workflow.status });
  } catch (error) {
    next(error);
  }
};
