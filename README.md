# Agentic AI Platform for B2B Customer Discovery

# TEAM DETAILS
TEAM NAME : Eclipse
TEAM MEMBERS : Srija, Abhisree, Srivalli

# GITHUB REPOSITORY LINK
https://github.com/Srivalli-0804/XLVentures.Ai-Agentic_AI_Platform/tree/final

## Overview
This project is a reusable Agentic AI Platform for B2B customer discovery and prospect intelligence. It combines a frontend dashboard with a backend orchestration engine that uses AI-style agents, workflow queuing, shared memory, and human approval.

## Key Features
- Dynamic planner-based agent orchestration
- Reusable agent architecture
- Shared memory for deduplication and workflow history
- Role-based access and approval workflow
- Company discovery and enrichment pipeline
- Dashboard monitoring and workflow status tracking

## Project Structure
- `frontend/`: React + TypeScript + Vite + Tailwind UI
- `backend/`: Express + TypeScript API, MongoDB persistence, BullMQ queue
- `redis-8.8.0/`: bundled Redis binaries for local use

## Demo Users
- `admin@example.com` / `Admin123!`
- `sales@example.com` / `Sales123!`
- `viewer@example.com` / `Viewer123!`

## Architecture Summary
The platform consists of three main layers:

1. **Frontend UI**
   - User login and role-based access
   - Workflow builder and discovery run controls
   - Approval queue for admin review
   - Company results and monitoring views

2. **Backend API**
   - Auth, role validation, and route protection
   - Workflow queue endpoint for asynchronous job dispatch
   - Workflow status and approval endpoints
   - Company and memory persistence

3. **Agent Orchestration**
   - Planner engine orchestrates agents sequentially
   - Agents process goals and payloads through a shared pipeline
   - Human approval can pause workflows before finalization
   - Enriched prospects are persisted in MongoDB

## Core Flow
1. A user queues a workflow by goal or starts a discovery run.
2. Backend creates a `WorkflowRun` record and enqueues a job in BullMQ.
3. The worker executes `runWorkflowJob`, and the planner runs agents.
4. Company data flows through agents and is enriched.
5. If new companies exist, they are saved to MongoDB.
6. Workflows can pause for human approval before final recommendations.

## Agents in the System
The backend includes several reusable agents:
- `MonitorAgent`: generates initial company candidates from triggers
- `ICPMatchingAgent`: matches companies to the ideal customer profile
- `ValidationAgent`: filters valid company records
- `CompanyEnrichmentAgent`: enriches company metadata
- `PersonaFinderAgent`: identifies decision-maker personas
- `ContactEnrichmentAgent`: adds contact details
- `RecommendationAgent`: produces action recommendations
- `HumanApprovalAgent`: requests admin approval
- `ExportAgent`: creates an export output

## Important Files
- `frontend/src/pages/WorkflowBuilderPage.tsx` — custom workflow builder
- `frontend/src/pages/CompanyResultsPage.tsx` — discovery run flow
- `frontend/src/pages/ApprovalQueuePage.tsx` — human approval UI
- `frontend/src/services/api.ts` — frontend backend API wrapper
- `backend/src/routes/index.ts` — API route definitions
- `backend/src/workflows/workflowJob.ts` — queue worker execution
- `backend/src/planner/planner.ts` — agent orchestration
- `backend/src/agents/` — reusable agent implementations
- `backend/src/services/companyService.ts` — company persistence

## Setup Instructions
### Prerequisites
- Node.js
- MongoDB
- Redis (or use bundled Redis)

### Backend
```bash
cd backend
npm install
npm run seed
npm run seed:data
npm run dev
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

The frontend runs on `http://localhost:5173`, and the backend runs on `http://localhost:4000`.

## How to Use
1. Login as `admin` or `sales`.
2. Use the workflow builder to queue a goal-based workflow.
3. Or click `Start new discovery run` to trigger prospect discovery.
4. Open the approval queue as an admin to approve or reject pending workflows.
5. Review enriched company data and the monitoring dashboard.

## Business Use Case
This platform targets B2B SaaS sales discovery. It is built to:
- Monitor business triggers for new prospects
- Identify companies matching an ICP
- Validate and enrich company details
- Find relevant decision-makers
- Enrich contact profiles with email, phone, and LinkedIn-style data
- Generate actionable sales recommendations
- Include human approval for decision control

## Notes
- The platform is designed for extensibility: new agents can be added by implementing the `Agent` interface and registering them in the agent list.
- The planner architecture supports configurable goals and dynamic payload passing.
- Shared memory prevents duplicate processing of the same companies.
