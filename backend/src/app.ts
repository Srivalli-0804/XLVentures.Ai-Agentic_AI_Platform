import express from 'express';
import cors from 'cors';
import helmet from 'helmet';
import rateLimit from 'express-rate-limit';
import { json } from 'express';
import { router } from './routes';
import { errorHandler } from './middleware/errorHandler';

export const app = express();

app.use(helmet());
app.use(cors());
app.use(json());
app.use(
  rateLimit({
    windowMs: 60 * 1000,
    max: 100
  })
);

app.use('/api', router);
app.use(errorHandler);
