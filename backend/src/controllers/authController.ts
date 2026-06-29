import { Request, Response, NextFunction } from 'express';
import { authService } from '../services/authService';

export const login = async (req: Request, res: Response, next: NextFunction) => {
  try {
    const { email, password } = req.body;
    const auth = await authService.authenticate(email, password);
    if (!auth) {
      return res.status(401).json({ message: 'Invalid credentials' });
    }

    res.json(auth);
  } catch (error) {
    next(error);
  }
};

export const getProfile = async (req: Request, res: Response, next: NextFunction) => {
  try {
    const user = (req as Request & { user?: { id: string; email: string; role: string } }).user;
    if (!user) {
      return res.status(401).json({ message: 'Authentication required' });
    }

    res.json({ email: user.email, role: user.role });
  } catch (error) {
    next(error);
  }
};
