import { Schema, model, Document } from 'mongoose';

export type UserRole = 'admin' | 'sales' | 'viewer';

export interface UserDocument extends Document {
  email: string;
  passwordHash: string;
  role: UserRole;
  createdAt: Date;
  updatedAt: Date;
}

const userSchema = new Schema<UserDocument>(
  {
    email: { type: String, required: true, unique: true },
    passwordHash: { type: String, required: true },
    role: { type: String, required: true, enum: ['admin', 'sales', 'viewer'], default: 'viewer' }
  },
  { timestamps: true }
);

export const UserModel = model<UserDocument>('User', userSchema);
