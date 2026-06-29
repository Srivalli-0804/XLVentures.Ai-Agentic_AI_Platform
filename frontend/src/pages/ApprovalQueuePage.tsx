import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { fetchWorkflowStatus, approveWorkflow, WorkflowRun } from '../services/api';
import { useAuthStore } from '../store/authStore';

export function ApprovalQueuePage() {
  const queryClient = useQueryClient();
  const role = useAuthStore((state) => state.role);
  const { data: runs } = useQuery<WorkflowRun[]>({ queryKey: ['workflowStatus'], queryFn: fetchWorkflowStatus, staleTime: 1000 * 30 });
  const approveMutation = useMutation({
    mutationFn: ({ workflowId, action }: { workflowId: string; action: 'approve' | 'reject' }) => approveWorkflow(workflowId, action),
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ['workflowStatus'] })
  });

  return (
    <div className="mx-auto max-w-7xl space-y-6">
      <section className="rounded-3xl border border-slate-800 bg-slate-900/80 p-6">
        <div>
          <p className="text-sm uppercase text-slate-400">Approval queue</p>
          <h1 className="mt-2 text-3xl font-semibold text-white">Human review</h1>
        </div>
      </section>

      <section className="grid gap-4">
        {runs?.map((run) => (
          <div key={run._id} className="rounded-3xl border border-slate-800 bg-slate-950/70 p-5">
            <div className="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
              <div>
                <p className="font-semibold text-white">{run.name}</p>
                <p className="text-sm text-slate-400">Status: {run.status}</p>
              </div>
              {role === 'admin' ? (
                <div className="flex gap-2">
                  <button
                    disabled={run.status !== 'pendingApproval'}
                    className="rounded-3xl bg-brand-500 px-5 py-3 text-white transition hover:bg-brand-400 disabled:opacity-50"
                    onClick={() => approveMutation.mutate({ workflowId: run._id, action: 'approve' })}
                  >
                    Approve
                  </button>
                  <button
                    disabled={run.status !== 'pendingApproval'}
                    className="rounded-3xl bg-slate-700 px-5 py-3 text-white transition hover:bg-slate-600 disabled:opacity-50"
                    onClick={() => approveMutation.mutate({ workflowId: run._id, action: 'reject' })}
                  >
                    Reject
                  </button>
                </div>
              ) : (
                <p className="text-sm text-slate-400">Admin approval required</p>
              )}
            </div>
          </div>
        ))}
      </section>
    </div>
  );
}
