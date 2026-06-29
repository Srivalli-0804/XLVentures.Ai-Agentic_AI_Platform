import { Router } from 'express';
import { approveWorkflow, deleteWorkflow } from '../controllers/workflowApprovalController';
import { authorize } from '../middleware/roleMiddleware';

export const approvalRouter = Router();

approvalRouter.post('/', authorize(['admin']), approveWorkflow);
approvalRouter.delete('/:workflowId', authorize(['admin']), deleteWorkflow);
