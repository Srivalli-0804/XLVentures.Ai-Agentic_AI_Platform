# Agentic AI Platform Summary

## What this project is
A B2B prospect discovery platform that combines AI workflow orchestration, data enrichment, and human approval.

- Frontend: React + Vite + Tailwind
- Backend: Express + TypeScript + MongoDB + BullMQ + Redis
- Purpose: let sales/admin users queue AI workflows that discover and enrich company prospects, then monitor progress and approval.

## Why it exists
Sales teams need a way to run repeatable discovery workflows, turn AI-generated prospect data into structured company records, and keep a human approval gate for sensitive decisions.

## Workflow overview
1. User action
   - A logged-in `admin` or `sales` user clicks `Start new discovery run` or submits a workflow goal.
   - The frontend sends `POST /api/workflow/queue/run` to the backend.

2. Backend queueing
   - The backend creates a new `WorkflowRun` record in MongoDB.
   - It enqueues the job in BullMQ using Redis.
   - The endpoint returns the queued job ID and workflow ID.

3. Worker execution
   - A BullMQ worker consumes the queued job.
   - It runs `runWorkflowJob`, marking the workflow `running`.
   - The backend planner executes agents sequentially.

4. AI/data processing
   - Each agent receives the workflow goal and payload.
   - The planner filters duplicates using stored memory.
   - Agents perform data enrichment and return results.
   - If agents return new company data, that data is saved via `companyService.saveCompanies(...)`.
   - Company records are persisted in MongoDB.

5. Memory and history
   - The platform saves memory entries for companies, planner decisions, and workflow history.
   - This supports de-duplication and auditability.

6. Approval handling
   - If an agent requests approval, the workflow is marked `pendingApproval`.
   - The approval queue is exposed to `admin` users.
   - After approval, the workflow continues or finalizes.

## What is happening and why
- `frontend/src/pages/CompanyResultsPage.tsx` and `WorkflowBuilderPage.tsx` let users queue workflows.
- `frontend/src/services/api.ts` sends requests through `/api` proxy to the backend.
- `backend/src/routes/index.ts` secures API routes with auth and role middleware.
- `backend/src/services/queueService.ts` connects BullMQ to Redis and starts the worker.
- `backend/src/workflows/workflowJob.ts` runs the job and saves output to MongoDB.
- `backend/src/planner/planner.ts` orchestrates AI agents, detects duplicates, and manages approval flow.

## Need and result
- Need: automated prospect discovery with human oversight.
- Result: a queued workflow system that produces structured company prospect records, logs AI planner history, and enables monitoring/approval.

## Key files
- `frontend/src/pages/CompanyResultsPage.tsx` — queue discovery runs
- `frontend/src/pages/WorkflowBuilderPage.tsx` — custom workflow builder
- `backend/src/services/queueService.ts` — BullMQ queue and worker
- `backend/src/workflows/workflowJob.ts` — executes the workflow job
- `backend/src/planner/planner.ts` — agent orchestration and approval handling
- `backend/src/services/database.ts` — MongoDB connect
- `backend/src/config/index.ts` — environment configuration

## Startup requirements
- MongoDB running and reachable at `MONGO_URI` or `mongodb://localhost:27017/agentic-ai`
- Redis running and reachable at `REDIS_URL`, ideally Redis >= 5.0.0
- Backend on `http://localhost:4000`
- Frontend on `http://localhost:5173`
