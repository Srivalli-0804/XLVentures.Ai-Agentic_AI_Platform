import { useState } from 'react';
import { useMutation } from '@tanstack/react-query';
import { queueWorkflow, WorkflowQueueResponse } from '../services/api';
import { useAuthStore } from '../store/authStore';
import { PageTabs } from '../components/PageTabs';

export function WorkflowBuilderPage() {
  const [goal, setGoal] = useState('Find SaaS companies hiring AI engineers');
  const [message, setMessage] = useState<string | null>(null);
  const { role } = useAuthStore();
  const mutation = useMutation<WorkflowQueueResponse, unknown, { goal: string }>({
    mutationFn: ({ goal }) => queueWorkflow(goal),
    onSuccess: (data) => setMessage(`Workflow queued with job ${data.jobId} and workflow ${data.workflowId}`),
    onError: () => setMessage('Unable to queue workflow. Check permissions.')
  });

  const canQueue = role === 'admin' || role === 'sales';

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    mutation.mutate({ goal });
  };

  return (
    <div className="mx-auto max-w-7xl space-y-6">
      <PageTabs />
      <section className="rounded-3xl border border-slate-800 bg-slate-900/80 p-6">
        <div>
          <p className="text-sm uppercase text-slate-400">Workflow builder</p>
          <h1 className="mt-2 text-3xl font-semibold text-white">Queue a new workflow</h1>
        </div>
        <form className="mt-6 space-y-4" onSubmit={handleSubmit}>
          <label className="block text-slate-300">
            <span className="text-sm">User goal</span>
            <textarea
              className="mt-2 w-full rounded-3xl border border-slate-700 bg-slate-950/70 px-4 py-3 text-white outline-none focus:border-brand-500"
              value={goal}
              onChange={(e) => setGoal(e.target.value)}
              rows={5}
            />
          </label>
          <button
            type="submit"
            disabled={!canQueue}
            className="rounded-3xl bg-brand-500 px-5 py-3 text-white transition hover:bg-brand-400 disabled:opacity-50"
          >
            Queue workflow
          </button>
          {!canQueue && (
            <p className="text-sm text-yellow-300">Only admin and sales users can queue workflows.</p>
          )}
          {message && <p className="text-sm text-slate-300">{message}</p>}
          <p className="text-xs text-slate-500">Admin and sales users can queue workflows; admin approval may be required later.</p>
        </form>
      </section>
    </div>
  );
}
