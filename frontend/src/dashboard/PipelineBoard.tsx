import React from "react";
import ProspectCard, { Prospect } from "./ProspectCard";

interface Props {
  prospects: Prospect[];
}

const PipelineBoard: React.FC<Props> = ({ prospects }) => {
  const columns = ["Discovered", "Qualified", "Enriched", "Recommended"];

  return (
    <div className="card">
      <div className="hero-row">
        <div>
          <h2 style={{ margin: 0 }}>Pipeline board</h2>
          <p className="muted small">A visual overview of accounts moving across the workflow.</p>
        </div>
        <div className="stat-pill">{prospects.length} accounts tracked</div>
      </div>
      <div className="grid grid-2" style={{ gridTemplateColumns: "repeat(auto-fit, minmax(220px, 1fr))" }}>
        {columns.map((column) => (
          <div key={column} className="card" style={{ padding: 14 }}>
            <h3 style={{ margin: "0 0 10px" }}>{column}</h3>
            <div>
              {prospects.filter((p) => p.status === column).length === 0 ? (
                <div className="muted small">No companies in this stage yet.</div>
              ) : prospects.filter((p) => p.status === column).map((prospect) => (
                <ProspectCard key={prospect.id} prospect={prospect} />
              ))}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default PipelineBoard;