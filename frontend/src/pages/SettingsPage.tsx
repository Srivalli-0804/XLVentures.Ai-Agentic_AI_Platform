export function SettingsPage() {
  return (
    <div className="mx-auto max-w-5xl space-y-6">
      <div className="rounded-3xl border border-slate-800 bg-slate-900/80 p-6">
        <h1 className="text-3xl font-semibold text-white">Workspace settings</h1>
        <p className="mt-2 text-slate-400">Configure your ICP, triggers and workflow defaults for the platform.</p>
      </div>

      <div className="grid gap-4 lg:grid-cols-2">
        <div className="rounded-3xl border border-slate-800 bg-slate-950/70 p-6">
          <h2 className="text-xl font-semibold text-white">Business profile</h2>
          <div className="mt-4 space-y-4 text-slate-300">
            <div>
              <p className="font-semibold text-white">Business domain</p>
              <p className="text-sm text-slate-400">SaaS, Consulting, AI Services</p>
            </div>
            <div>
              <p className="font-semibold text-white">Ideal Customer Profile</p>
              <p className="text-sm text-slate-400">Mid-market AI engineering and data-driven SaaS organizations</p>
            </div>
          </div>
        </div>

        <div className="rounded-3xl border border-slate-800 bg-slate-950/70 p-6">
          <h2 className="text-xl font-semibold text-white">Workflow criteria</h2>
          <div className="mt-4 space-y-4 text-slate-300">
            <p className="text-sm">Funding, hiring, expansion, leadership changes, product launches</p>
            <p className="text-sm">Country: US, CA, UK</p>
            <p className="text-sm">Industry: Software, Fintech, Healthcare</p>
          </div>
        </div>
      </div>
    </div>
  );
}
