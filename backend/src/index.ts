import { app } from './app';
import { connectDatabase } from './services/database';
import { logger } from './utils/logger';
import { config } from './config';
import { startWorkflowWorker } from './services/queueService';

const port = config.port;

connectDatabase()
  .then(() => {
    startWorkflowWorker();
    app.listen(port, () => {
      logger.info(`Backend server running on http://localhost:${port}`);
    });
  })
  .catch((error) => {
    logger.error('Database connection failed', error);
    process.exit(1);
  });
