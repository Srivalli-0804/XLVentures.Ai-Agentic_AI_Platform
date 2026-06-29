admin@example.com / Admin123!
sales@example.com / Sales123!
viewer@example.com / Viewer123!
# Agentic AI Platform for B2B Customer Discovery and Prospect Intelligence

A reusable platform for orchestrating AI agents in B2B sales prospect intelligence workflows.

## Structure

- `frontend/`: React + Vite + Tailwind dashboard
- `backend/`: Express + TypeScript API

## Getting Started

1. Install dependencies:
   ```bash
   npm install
   ```

2. Seed default users and sample company data:
   ```bash
   cd backend
   npm run seed
   npm run seed:data
   ```

3. Start development:
   ```bash
   npm run dev
   ```

4. Backend runs on `http://localhost:4000`
5. Frontend runs on `http://localhost:5173`

## Login

- `admin@example.com` / `Admin123!`
- `sales@example.com` / `Sales123!`
- `viewer@example.com` / `Viewer123!`

## Platform features

- AI-driven workflow queue with data enrichment and approval flow
- Prospect company catalog with enriched metadata
- Workflow and planner monitoring dashboard
- Stateful memory history for company and planner data
