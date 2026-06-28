import React from "react";

import MetricsPanel from "../dashboard/MetricsPanel";

const Analytics = () => {
  const metrics = {
    discovered_companies: 124,
    qualified_companies: 86,
    enriched_companies: 71,
    recommendations_generated: 53,
    approvals_pending: 12
  };

  return (
    <div className="p-6 space-y-6">
      <h1 className="text-3xl font-bold">
        Analytics Dashboard
      </h1>

      <MetricsPanel
        metrics={metrics}
      />

      <div className="bg-white rounded-lg shadow p-6">
        <h2 className="text-xl font-semibold mb-3">
          Pipeline Overview
        </h2>

        <div className="space-y-2">
          <div>
            Discovery → Qualification
          </div>

          <div>
            Qualification →
            Enrichment
          </div>

          <div>
            Enrichment →
            Recommendation
          </div>

          <div>
            Recommendation →
            Approval
          </div>
        </div>
      </div>
    </div>
  );
};

export default Analytics;