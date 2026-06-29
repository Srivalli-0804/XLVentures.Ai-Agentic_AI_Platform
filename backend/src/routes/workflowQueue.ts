import { Router } from 'express';
import { enqueueWorkflow } from '../controllers/workflowQueueController';
import { authorize } from '../middleware/roleMiddleware';

export const workflowQueueRouter = Router();

workflowQueueRouter.post('/run', authorize(['admin', 'sales']), enqueueWorkflow);
