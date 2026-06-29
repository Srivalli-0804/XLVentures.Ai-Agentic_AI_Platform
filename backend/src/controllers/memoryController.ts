import { Request, Response, NextFunction } from 'express';
import { memoryService } from '../services/memoryService';

export const getMemoryEntries = async (_req: Request, res: Response, next: NextFunction) => {
  try {
    const entries = await memoryService.getEntries();
    res.json(entries);
  } catch (error) {
    next(error);
  }
};
