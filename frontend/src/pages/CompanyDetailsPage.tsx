import { useParams } from 'react-router-dom';
import { useQuery } from '@tanstack/react-query';
import { Company, fetchCompanyDetails } from '../services/api';

export function CompanyDetailsPage() {
  const { id } = useParams();
  const { data, isLoading } = useQuery<Company>({
    queryKey: ['company', id],
    queryFn: () => fetchCompanyDetails(id ?? ''),
    enabled: Boolean(id)
  });

  if (isLoading) {
    return <div className="text-center text-slate-300">Loading company details...</div>;
  }

  return (
    <div className="mx-auto max-w-5xl space-y-6">
      <div className="rounded-3xl border border-slate-800 bg-slate-900/80 p-6">
        <div className="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
          <div>
            <h1 className="text-3xl font-semibold text-white">{data?.name}</h1>
            <p className="mt-2 text-slate-400">{data?.industry || 'Industry unknown'}</p>
          </div>
          <div className="rounded-3xl bg-slate-950/70 px-4 py-2 text-sm text-slate-200">{data?.status || 'N/A'}</div>
        </div>

        <div className="mt-6 grid gap-4 sm:grid-cols-2">
          <div className="rounded-3xl border border-slate-800 bg-slate-950/70 p-5">
            <p className="text-sm uppercase text-slate-400">Website</p>
            <p className="mt-2 text-white">{data?.website || 'None'}</p>
          </div>
          <div className="rounded-3xl border border-slate-800 bg-slate-950/70 p-5">
            <p className="text-sm uppercase text-slate-400">Location</p>
            <p className="mt-2 text-white">{data?.location || 'None'}</p>
          </div>
          <div className="rounded-3xl border border-slate-800 bg-slate-950/70 p-5">
            <p className="text-sm uppercase text-slate-400">Revenue</p>
            <p className="mt-2 text-white">{data?.revenue || 'Unknown'}</p>
          </div>
          <div className="rounded-3xl border border-slate-800 bg-slate-950/70 p-5">
            <p className="text-sm uppercase text-slate-400">Employees</p>
            <p className="mt-2 text-white">{data?.employees ?? 'Unknown'}</p>
          </div>
        </div>
      </div>

      <div className="rounded-3xl border border-slate-800 bg-slate-900/80 p-6">
        <h2 className="text-xl font-semibold text-white">Company overview</h2>
        <p className="mt-4 text-slate-300">{data?.summary || 'No overview available yet.'}</p>
      </div>

      <div className="grid gap-4 lg:grid-cols-2">
        <div className="rounded-3xl border border-slate-800 bg-slate-950/70 p-6">
          <h2 className="text-xl font-semibold text-white">Technologies</h2>
          <div className="mt-4 flex flex-wrap gap-2">
            {data?.technologies?.map((tech) => (
              <span key={tech} className="rounded-full bg-slate-800 px-3 py-1 text-sm text-slate-300">
                {tech}
              </span>
            ))}
            {!data?.technologies?.length && <p className="text-sm text-slate-400">No technology data available.</p>}
          </div>
        </div>

        <div className="rounded-3xl border border-slate-800 bg-slate-950/70 p-6">
          <h2 className="text-xl font-semibold text-white">Contact & trigger</h2>
          <div className="mt-4 space-y-3 text-slate-300">
            <p>
              <span className="font-semibold text-white">Trigger:</span> {data?.trigger || 'None'}
            </p>
            <p>
              <span className="font-semibold text-white">Source:</span> {data?.source || 'Unknown'}
            </p>
            {data?.contacts?.length ? (
              <div>
                <p className="font-semibold text-white">Contacts</p>
                <ul className="mt-2 space-y-2 text-slate-300">
                  {data.contacts.slice(0, 3).map((contact, index) => (
                    <li key={index} className="rounded-2xl border border-slate-800 bg-slate-900/80 p-3">
                      <div>{String(contact.title || 'Contact')}</div>
                      <div className="text-sm text-slate-400">{String(contact.email || contact.linkedin || 'No email')}</div>
                    </li>
                  ))}
                </ul>
              </div>
            ) : (
              <p className="text-sm text-slate-400">No contact enrichment data available yet.</p>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
