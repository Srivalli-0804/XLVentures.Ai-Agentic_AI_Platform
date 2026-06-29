import { Router } from 'express';
import { healthRouter } from './health';
import { companiesRouter } from './companies';
import { workflowsRouter } from './workflows';
import { workflowQueueRouter } from './workflowQueue';
import { memoryRouter } from './memory';
import { agentsRouter } from './agents';
import { approvalRouter } from './approval';
import { authRouter } from './auth';
import { statsRouter } from './stats';
import { authMiddleware } from '../middleware/authMiddleware';

export const router = Router();

router.use('/health', healthRouter);
router.use('/auth', authRouter);
router.use(authMiddleware);
router.use('/companies', companiesRouter);
router.use('/company', companiesRouter);
router.use('/workflow', workflowsRouter);
router.use('/workflow/queue', workflowQueueRouter);
router.use('/memory', memoryRouter);
router.use('/agents', agentsRouter);
router.use('/workflow/approve', approvalRouter);
router.use('/stats', statsRouter);
