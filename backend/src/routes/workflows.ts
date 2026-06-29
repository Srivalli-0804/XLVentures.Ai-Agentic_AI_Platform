import { Router } from 'express';
import { runWorkflow, getWorkflowStatus } from '../workflows/workflowController';

export const workflowsRouter = Router();

workflowsRouter.post('/run', runWorkflow);
workflowsRouter.get('/status', getWorkflowStatus);
