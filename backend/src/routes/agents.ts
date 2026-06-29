import { Router } from 'express';
import { listAgents } from '../controllers/agentController';

export const agentsRouter = Router();

agentsRouter.get('/', listAgents);
