import { Schema, model, Document } from 'mongoose';

export interface CompanyDocument extends Document {
  name: string;
  industry: string;
  location?: string;
  website?: string;
  summary?: string;
  status?: string;
  revenue?: string;
  employees?: number;
  technologies?: string[];
  trigger?: string;
  source?: string;
  contacts?: Array<Record<string, unknown>>;
  createdAt: Date;
  updatedAt: Date;
}

const companySchema = new Schema<CompanyDocument>(
  {
    name: { type: String, required: true },
    industry: { type: String, required: true },
    location: String,
    website: String,
    summary: String,
    status: String,
    revenue: String,
    employees: Number,
    technologies: [String],
    trigger: String,
    source: String,
    contacts: [Schema.Types.Mixed]
  },
  { timestamps: true }
);

export const CompanyModel = model<CompanyDocument>('Company', companySchema);
