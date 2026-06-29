import React from "react";

export interface Prospect {
  id: string;
  company_name: string;
  score: number;
  industry: string;
  status: string;
}

interface Props {
  prospect: Prospect;
}

const ProspectCard: React.FC<Props> = ({ prospect }) => {
  return (
    <div className="prospect-card">
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", gap: 8 }}>
        <h4 style={{ margin: 0 }}>{prospect.company_name}</h4>
        <span className="badge badge-live">{prospect.score}</span>
      </div>
      <p className="muted small" style={{ margin: "8px 0 10px" }}>{prospect.industry}</p>
      <span className="badge badge-queued">{prospect.status}</span>
    </div>
  );
};

export default ProspectCard;