import React from "react";
import { AnalyticsSummary } from "../lib/types";

interface Props {
  metrics: AnalyticsSummary;
}

const MetricsPanel: React.FC<Props> = ({
  metrics
}) => {
  const cards = [
    {
      title: "Discovered",
      value: metrics.discovered_companies
    },
    {
      title: "Qualified",
      value: metrics.qualified_companies
    },
    {
      title: "Enriched",
      value: metrics.enriched_companies
    },
    {
      title: "Recommendations",
      value:
        metrics.recommendations_generated
    },
    {
      title: "Pending Approval",
      value: metrics.approvals_pending
    }
  ];

  return (
    <div className="grid grid-cols-5 gap-4">
      {cards.map((card) => (
        <div
          key={card.title}
          className="bg-white shadow rounded-lg p-4"
        >
          <h3 className="text-gray-500 text-sm">
            {card.title}
          </h3>

          <p className="text-2xl font-bold mt-2">
            {card.value}
          </p>
        </div>
      ))}
    </div>
  );
};

export default MetricsPanel;