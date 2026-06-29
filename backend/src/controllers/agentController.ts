import { Request, Response } from 'express';
import { agents } from '../agents';

export const listAgents = (_req: Request, res: Response) => {
  res.json(agents.map((agent) => ({ name: agent.name, description: agent.description })));
};
