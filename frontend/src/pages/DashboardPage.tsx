import { useQuery } from '@tanstack/react-query';
import { fetchDashboardStats, DashboardStats } from '../services/api';

export function DashboardPage() {
  const { data } = useQuery<DashboardStats>({
    queryKey: ['dashboardStats'],
    queryFn: fetchDashboardStats,
    staleTime: 1000 * 60
  });

  const metrics = [
    { label: 'workflows', value: data?.workflows ?? '--' },
    { label: 'companies', value: data?.companies ?? '--' },
    { label: 'agents', value: data?.agents ?? '--' },
    { label: 'memory', value: data?.memory ?? '--' }
  ];

  return (
    <div className="mx-auto max-w-7xl space-y-6">
      <section className="rounded-3xl border border-slate-800 bg-slate-900/80 p-6 shadow-xl shadow-slate-950/20">
        <div className="flex items-center justify-between gap-4">
          <div>
            <p className="text-sm uppercase text-slate-400">Workflow summary</p>
            <h1 className="mt-2 text-3xl font-semibold text-white">Agent Execution Overview</h1>
          </div>
          <div className="rounded-3xl bg-slate-800 px-4 py-2 text-slate-200">Live</div>
        </div>
        <div className="mt-8 grid gap-4 sm:grid-cols-2 xl:grid-cols-4">
          {metrics.map(({ label, value }) => (
            <div key={label} className="rounded-3xl border border-slate-800 bg-slate-950/60 p-5">
              <p className="text-sm text-slate-400">{label}</p>
              <p className="mt-3 text-3xl font-semibold text-white">{value}</p>
            </div>
          ))}
        </div>
      </section>

      <section className="grid gap-6 xl:grid-cols-2">
        <div className="rounded-3xl border border-slate-800 bg-slate-900/80 p-6">
          <p className="text-sm uppercase text-slate-400">Planner status</p>
          <div className="mt-6 space-y-4">
            <div className="rounded-3xl bg-slate-950/70 p-5">
              <p className="text-lg font-semibold text-white">{data?.plannerStatus ?? 'Idle'}</p>
              <p className="mt-2 text-sm text-slate-400">Current workflow execution state and recent event timeline.</p>
            </div>
          </div>
        </div>

        <div className="rounded-3xl border border-slate-800 bg-slate-900/80 p-6">
          <p className="text-sm uppercase text-slate-400">Recent workflows</p>
          <div className="mt-4 space-y-3">
            {data?.recentWorkflows?.map((work) => (
              <div key={work.id} className="rounded-3xl border border-slate-800 bg-slate-950/70 p-4">
                <p className="font-semibold text-white">{work.name}</p>
                <p className="text-sm text-slate-400">{work.status}</p>
              </div>
            ))}
          </div>
        </div>
      </section>
    </div>
  );
}
