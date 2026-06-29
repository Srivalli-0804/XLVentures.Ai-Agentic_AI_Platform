# Architecture Overview

## Platform Goal
The Agentic AI Platform is built to provide a reusable B2B prospect discovery and intelligence system. It enables users to queue AI workflows, orchestrate specialized agents, store shared memory, and manage human approval.

## High-Level Architecture

### Frontend
- Built with React, Vite, TypeScript, and Tailwind CSS.
- Provides authenticated UI for:
  - Login
  - Dashboard
  - Workflow builder
  - Company discovery and results
  - Workflow monitoring
  - Approval queue
  - User profile and settings
- Uses React Query for data fetching and state synchronization.
- Proxy configuration forwards `/api` calls to the backend at `http://localhost:4000`.

### Backend
- Built with Express and TypeScript.
- Core middleware:
  - `authMiddleware` for JWT authentication.
  - `roleMiddleware` for admin/sales authorization.
- Uses MongoDB for persistent data storage and Redis + BullMQ for job queueing.
- Key backend responsibilities:
  - Authentication and role-based access control.
  - Workflow queuing and job management.
  - Agent-based workflow execution.
  - Company persistence and memory history.

### Data Flow
1. User initiates a workflow from the frontend.
2. Frontend POSTs to `/api/workflow/queue/run`.
3. Backend creates `WorkflowRun` in MongoDB and enqueues a BullMQ job.
4. BullMQ worker consumes the job and executes `runWorkflowJob`.
5. The planner orchestrates agent execution and manages payload flow.
6. If company data is generated, it is persisted via `companyService`.
7. Workflow status updates are saved and exposed to the frontend.

## Agent Orchestration

Agents are modular classes from `backend/src/agents`:
- `MonitorAgent`
- `ICPMatchingAgent`
- `ValidationAgent`
- `CompanyEnrichmentAgent`
- `PersonaFinderAgent`
- `ContactEnrichmentAgent`
- `RecommendationAgent`
- `HumanApprovalAgent`
- `ExportAgent`

### Planner Responsibilities
- The planner receives a `goal` and initial payload.
- It executes agents sequentially.
- It merges each agent's output into the payload.
- It filters duplicate companies using memory.
- If an agent requests approval, the workflow pauses as `pendingApproval`.

## Shared Memory
- The platform uses memory entries to store:
  - company data
  - planner history
  - workflow events
- This supports deduplication and auditability.

## Persistence
- MongoDB models include:
  - `User`
  - `Company`
  - `WorkflowRun`
  - `MemoryEntry`
- `companyService` saves enriched company records via bulk upsert.

## Key Components
- `backend/src/services/queueService.ts` — BullMQ queue creation and worker registration.
- `backend/src/workflows/workflowJob.ts` — job execution and persistence.
- `backend/src/planner/planner.ts` — dynamic orchestration of agents.
- `backend/src/agents/*` — reusable agent implementations.
- `frontend/src/pages` — main user flows.

## Extensibility
- New agents can be added by implementing the `Agent` interface in `backend/src/agents/`.
- The planner automatically supports additional agents in the orchestrated list.
- Workflow goals are configurable, enabling new discovery and business use cases.

## Deployment Notes
- Backend defaults:
  - `PORT=4000`
  - `MONGO_URI=mongodb://localhost:27017/agentic-ai`
  - `REDIS_URL=redis://localhost:6379`
- Frontend runs on port `5173`.
- The frontend proxy forwards API traffic to backend server.

## Summary
This architecture is designed to be a reusable agentic platform, allowing business users to define discovery goals, execute workflows, enrich and validate prospects, and manage human approval in a cohesive UI.
