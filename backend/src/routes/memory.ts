import { Router } from 'express';
import { getMemoryEntries } from '../controllers/memoryController';

export const memoryRouter = Router();

memoryRouter.get('/', getMemoryEntries);
