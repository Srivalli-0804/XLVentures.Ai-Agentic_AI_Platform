# Button Functionality and Usage

This document describes the buttons found in the app UI, including what they do, when to use them, and how they behave in the current implementation.

## Builder Page Button

### Queue workflow
- **Location:** `frontend/src/pages/WorkflowBuilderPage.tsx`
- **Route:** POST `/api/workflow/queue/run`
- **Permissions:** `admin` or `sales` on both frontend and backend.
- **Inputs:** 
  - `goal` text from the textarea.
  - optional `payload` object if extended later.
- **Outputs:** Shows success message with `jobId` and `workflowId`, or error message if permissions fail.
- **Server-side effects:** 
  - Creates a `WorkflowRun` in MongoDB with status `pending`.
  - Enqueues a BullMQ workflow job for async processing.
- **When to use:** Use this to schedule a new automated workflow using a custom user goal.

## Companies Page Button

### Start new discovery run
- **Location:** `frontend/src/pages/CompanyResultsPage.tsx`
- **Route:** POST `/api/workflow/queue/run`
- **Permissions:** `admin` or `sales`.
- **Inputs:** No manual input in the UI; uses a hard-coded discovery goal:
  - `Discover new AI-ready prospect companies with high expansion potential`
- **Outputs:** 
  - Success: `Discovery workflow queued successfully.`
  - Error: `Unable to queue discovery run. Check your permissions.`
- **Server-side effects:** Queues a workflow run that may discover and persist new companies to the database.
- **When to use:** Use this for a quick prospect discovery workflow focused on AI-ready expansion opportunities.

## Approvals Page Buttons

### Approve
- **Location:** `frontend/src/pages/ApprovalQueuePage.tsx`
- **Route:** POST `/api/workflow/approve`
- **Permissions:** `admin` only.
- **Inputs:** 
  - `workflowId` for the specific workflow run.
  - `action` set to `approve`.
- **Outputs:** Server returns `{ success: true, status: 'completed' }`.
- **Effects:** Changes the workflow run status from `pendingApproval` to `completed`.
- **When to use:** Approve workflows that are awaiting human review and should be accepted.

### Reject
- **Location:** `frontend/src/pages/ApprovalQueuePage.tsx`
- **Route:** POST `/api/workflow/approve`
- **Permissions:** `admin` only.
- **Inputs:** 
  - `workflowId` for the workflow run.
  - `action` set to `reject`.
- **Outputs:** Server returns `{ success: true, status: 'failed' }`.
- **Effects:** Changes the workflow run status from `pendingApproval` to `failed`.
- **When to use:** Reject workflows that should not proceed due to poor results or incorrect output.

## Important Notes

- `Launch new workflow` and `Review approval queue` buttons are present in the Dashboard UI but currently do not perform navigation or API calls in this version.
- `Queue workflow` and `Start new discovery run` both use the same backend queuing endpoint, but the discovery button uses a fixed goal.
- Approval actions only update workflow status; they do not retrigger or continue the workflow.
- The backend worker may save discovered companies to the database when the workflow result includes `enrichedCompanies`.
