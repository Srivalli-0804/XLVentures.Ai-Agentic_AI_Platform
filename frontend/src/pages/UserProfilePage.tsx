import { useQuery } from '@tanstack/react-query';
import { fetchUserProfile, UserProfile } from '../services/api';
import { PageTabs } from '../components/PageTabs';

export function UserProfilePage() {
  const { data } = useQuery<UserProfile>({ queryKey: ['userProfile'], queryFn: fetchUserProfile, staleTime: 1000 * 60 });

  return (
    <div className="mx-auto max-w-7xl space-y-6">
      <PageTabs />
      <section className="rounded-3xl border border-slate-800 bg-slate-900/80 p-6">
        <div>
          <p className="text-sm uppercase text-slate-400">Profile</p>
          <h1 className="mt-2 text-3xl font-semibold text-white">Current user</h1>
        </div>
        <div className="mt-6 rounded-3xl border border-slate-800 bg-slate-950/70 p-6">
          <p className="text-sm text-slate-400">Email</p>
          <p className="mt-2 text-xl text-white">{data?.email}</p>
          <p className="mt-4 text-sm text-slate-400">Role</p>
          <p className="mt-2 text-xl text-white">{data?.role}</p>
        </div>
      </section>
    </div>
  );
}
