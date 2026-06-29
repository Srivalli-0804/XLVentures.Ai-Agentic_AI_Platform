import { connectDatabase } from '../services/database';
import { authService } from '../services/authService';
import { UserModel } from '../models/User';

const defaultUsers = [
  { email: 'admin@example.com', password: 'Admin123!', role: 'admin' as const },
  { email: 'sales@example.com', password: 'Sales123!', role: 'sales' as const },
  { email: 'viewer@example.com', password: 'Viewer123!', role: 'viewer' as const }
];

async function seedUsers() {
  await connectDatabase();

  for (const user of defaultUsers) {
    const existing = await UserModel.findOne({ email: user.email });
    if (existing) {
      console.log(`User already exists: ${user.email}`);
      continue;
    }

    await authService.createUser(user.email, user.password, user.role);
    console.log(`Created user: ${user.email} (${user.role})`);
  }

  console.log('\nSeed complete. Use the credentials above to log in.');
  process.exit(0);
}

seedUsers().catch((error) => {
  console.error('Seed failed:', error);
  process.exit(1);
});
