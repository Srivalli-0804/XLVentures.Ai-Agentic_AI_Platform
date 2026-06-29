import bcrypt from 'bcryptjs';
import jwt from 'jsonwebtoken';
import { UserModel, UserDocument, UserRole } from '../models/User';
import { config } from '../config';

export const authService = {
  authenticate: async (email: string, password: string) => {
    const user = await UserModel.findOne({ email });
    if (!user) {
      return null;
    }

    const isValid = await bcrypt.compare(password, user.passwordHash);
    if (!isValid) {
      return null;
    }

    const token = jwt.sign({ id: user.id, email: user.email, role: user.role }, config.jwtSecret, {
      expiresIn: '8h'
    });

    return { token, user: { id: user.id, email: user.email, role: user.role } };
  },
  createUser: async (email: string, password: string, role: UserRole = 'viewer') => {
    const passwordHash = await bcrypt.hash(password, 10);
    return UserModel.create({ email, passwordHash, role });
  }
};
