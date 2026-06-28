export const API_BASE_URL =
  import.meta.env.VITE_API_URL ||
  "http://localhost:8000/api";

export const PIPELINE_STAGES = [
  "Discovered",
  "Qualified",
  "Scored",
  "Enriched",
  "Contacts",
  "Validated",
  "Recommended"
];

export const WORKFLOW_STATUS = {
  PENDING: "pending",
  RUNNING: "running",
  COMPLETED: "completed",
  FAILED: "failed"
};

export const APPROVAL_STATUS = {
  PENDING: "pending",
  APPROVED: "approved",
  REJECTED: "rejected"
};

export const DEFAULT_PAGE_SIZE = 20;

export const APP_NAME = "ProspectIQ";