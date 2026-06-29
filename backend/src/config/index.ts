import dotenv from 'dotenv';

dotenv.config();

export const config = {
  port: process.env.PORT || 4000,
  mongoUri: process.env.MONGO_URI || 'mongodb://localhost:27017/agentic-ai',
  jwtSecret: process.env.JWT_SECRET || 'change-this-secret',
  redisUrl: process.env.REDIS_URL || 'redis://localhost:6379'
};
