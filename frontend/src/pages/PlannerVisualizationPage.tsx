import { useQuery } from '@tanstack/react-query';
import { fetchAgents, AgentInfo } from '../services/api';

export function PlannerVisualizationPage() {
  const { data: agents } = useQuery<AgentInfo[]>({ queryKey: ['agents'], queryFn: fetchAgents, staleTime: 1000 * 60 });

  return (
    <div className="mx-auto max-w-7xl space-y-6">
      <section className="rounded-3xl border border-slate-800 bg-slate-900/80 p-6">
        <div>
          <p className="text-sm uppercase text-slate-400">Planner visualization</p>
          <h1 className="mt-2 text-3xl font-semibold text-white">Agent flow graph</h1>
        </div>
      </section>

      <section className="grid gap-4 xl:grid-cols-3">
        {agents?.map((agent) => (
          <div key={agent.name} className="rounded-3xl border border-slate-800 bg-slate-950/70 p-5">
            <p className="text-sm uppercase text-slate-400">Agent</p>
            <h2 className="mt-2 text-xl font-semibold text-white">{agent.name}</h2>
            <p className="mt-3 text-slate-300">{agent.description}</p>
          </div>
        ))}
      </section>
    </div>
  );
}
