import { Schema, model, Document } from 'mongoose';

export interface WorkflowRunDocument extends Document {
  name: string;
  status: 'pending' | 'running' | 'pendingApproval' | 'completed' | 'failed';
  jobId?: string;
  requestedBy?: string;
  requiresApproval?: boolean;
  outputPayload?: Record<string, unknown>;
  steps: Array<{ agent: string; status: string; message?: string }>;
  createdAt: Date;
  updatedAt: Date;
}

const workflowRunSchema = new Schema<WorkflowRunDocument>(
  {
    name: { type: String, required: true },
    status: { type: String, required: true, default: 'pending' },
    jobId: { type: String },
    requestedBy: { type: String },
    requiresApproval: { type: Boolean, default: true },
    outputPayload: { type: Schema.Types.Mixed },
    steps: [{ agent: String, status: String, message: String }]
  },
  { timestamps: true }
);

export const WorkflowRunModel = model<WorkflowRunDocument>('WorkflowRun', workflowRunSchema);
