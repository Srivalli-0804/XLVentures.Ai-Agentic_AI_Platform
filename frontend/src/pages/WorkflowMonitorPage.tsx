import { useQuery } from '@tanstack/react-query';
import { fetchWorkflowStatus, fetchMemoryEntries, fetchAgents, WorkflowRun, MemoryEntry, AgentInfo } from '../services/api';

export function WorkflowMonitorPage() {
  const { data: runs } = useQuery<WorkflowRun[]>({ queryKey: ['workflowStatus'], queryFn: fetchWorkflowStatus, staleTime: 1000 * 30 });
  const { data: memory } = useQuery<MemoryEntry[]>({ queryKey: ['memoryEntries'], queryFn: fetchMemoryEntries, staleTime: 1000 * 60 });
  const { data: agents } = useQuery<AgentInfo[]>({ queryKey: ['agents'], queryFn: fetchAgents, staleTime: 1000 * 60 });

  return (
    <div className="mx-auto max-w-7xl space-y-6">
      <section className="rounded-3xl border border-slate-800 bg-slate-900/80 p-6">
        <div className="flex items-center justify-between gap-4">
          <div>
            <p className="text-sm uppercase text-slate-400">Workflow monitor</p>
            <h1 className="mt-2 text-3xl font-semibold text-white">Execution pipeline</h1>
          </div>
        </div>

        <div className="mt-6 grid gap-4 xl:grid-cols-3">
          <div className="rounded-3xl border border-slate-800 bg-slate-950/70 p-5">
            <p className="text-sm text-slate-400">Active runs</p>
            <p className="mt-3 text-3xl font-semibold text-white">{runs?.filter((item) => item.status === 'running').length ?? 0}</p>
          </div>
          <div className="rounded-3xl border border-slate-800 bg-slate-950/70 p-5">
            <p className="text-sm text-slate-400">Pending approvals</p>
            <p className="mt-3 text-3xl font-semibold text-white">{runs?.filter((item) => item.status === 'pendingApproval').length ?? 0}</p>
          </div>
          <div className="rounded-3xl border border-slate-800 bg-slate-950/70 p-5">
            <p className="text-sm text-slate-400">Memory items</p>
            <p className="mt-3 text-3xl font-semibold text-white">{memory?.length ?? 0}</p>
          </div>
        </div>
      </section>

      <section className="rounded-3xl border border-slate-800 bg-slate-900/80 p-6">
        <h2 className="text-xl font-semibold text-white">Recent workflow runs</h2>
        <div className="mt-4 space-y-3">
          {runs?.map((run) => (
            <div key={run._id} className="rounded-3xl border border-slate-800 bg-slate-950/70 p-4">
              <div className="flex items-center justify-between gap-3">
                <p className="font-semibold text-white">{run.name}</p>
                <span className="rounded-full bg-slate-800 px-3 py-1 text-xs uppercase text-slate-300">{run.status}</span>
              </div>
              <p className="mt-2 text-sm text-slate-400">{new Date(run.createdAt).toLocaleString()}</p>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
}
