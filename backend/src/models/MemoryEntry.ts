import { Schema, model, Document } from 'mongoose';

export type MemoryEntryType = 'company' | 'contact' | 'apiResponse' | 'plannerHistory';

export interface MemoryEntryDocument extends Document {
  type: MemoryEntryType;
  key: string;
  payload: Record<string, unknown>;
  tags: string[];
  createdAt: Date;
  updatedAt: Date;
}

const memoryEntrySchema = new Schema<MemoryEntryDocument>(
  {
    type: { type: String, required: true },
    key: { type: String, required: true, index: true },
    payload: { type: Schema.Types.Mixed, required: true },
    tags: { type: [String], default: [] }
  },
  { timestamps: true }
);

export const MemoryEntryModel = model<MemoryEntryDocument>('MemoryEntry', memoryEntrySchema);
