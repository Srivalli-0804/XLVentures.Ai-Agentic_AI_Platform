import { Link } from 'react-router-dom';
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query';
import { Company, fetchCompanies, queueWorkflow, WorkflowQueueResponse } from '../services/api';

export function CompanyResultsPage() {
  const queryClient = useQueryClient();
  const { data } = useQuery<Company[]>({
    queryKey: ['companies'],
    queryFn: fetchCompanies,
    staleTime: 1000 * 60
  });

  const mutation = useMutation<WorkflowQueueResponse, unknown, { goal: string }>({
    mutationFn: ({ goal }) => queueWorkflow(goal),
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ['workflowStatus'] })
  });

  return (
    <div className="mx-auto max-w-7xl space-y-6">
      <div className="rounded-3xl border border-slate-800 bg-slate-900/80 p-6">
        <div className="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
          <div>
            <p className="text-sm uppercase text-slate-400">Company search</p>
            <h1 className="mt-2 text-3xl font-semibold text-white">Prospect pipeline</h1>
          </div>
          <button
            onClick={() => mutation.mutate({ goal: 'Discover new AI-ready prospect companies with high expansion potential' })}
            disabled={mutation.isPending}
            className="rounded-3xl bg-brand-500 px-5 py-3 text-white transition hover:bg-brand-400 disabled:opacity-50"
          >
            {mutation.isPending ? 'Discovering…' : 'Start new discovery run'}
          </button>
        </div>
        {mutation.isSuccess && (
          <p className="mt-4 text-sm text-emerald-300">Discovery workflow queued successfully.</p>
        )}
        {mutation.isError && (
          <p className="mt-4 text-sm text-rose-300">Unable to queue discovery run. Check your permissions.</p>
        )}
      </div>

      <div className="grid gap-4 xl:grid-cols-3">
        {data?.map((company) => (
          <Link
            key={company._id}
            to={`/companies/${company._id}`}
            className="rounded-3xl border border-slate-800 bg-slate-950/70 p-5 transition hover:border-brand-500"
          >
            <p className="text-sm text-slate-400">{company.industry || 'Unknown industry'}</p>
            <h2 className="mt-2 text-xl font-semibold text-white">{company.name}</h2>
            <p className="mt-2 text-sm text-slate-400">{company.summary || 'No description available.'}</p>
          </Link>
        ))}
      </div>
    </div>
  );
}
