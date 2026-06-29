import { Router } from 'express';
import { approveWorkflow } from '../controllers/workflowApprovalController';
import { authorize } from '../middleware/roleMiddleware';

export const approvalRouter = Router();

approvalRouter.post('/', authorize(['admin']), approveWorkflow);
