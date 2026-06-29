import { Queue, Worker, QueueScheduler, JobsOptions } from 'bullmq';
import IORedis from 'ioredis';
import { config } from '../config';
import { runWorkflowJob } from '../workflows/workflowJob';

const connection = new IORedis(config.redisUrl);
export const workflowQueue = new Queue('workflow-queue', { connection });
new QueueScheduler('workflow-queue', { connection });

export const startWorkflowWorker = () => {
  new Worker('workflow-queue', runWorkflowJob, { connection });
};

export const addWorkflowToQueue = async (data: any, options?: JobsOptions) => {
  return workflowQueue.add('run-workflow', data, options);
};
