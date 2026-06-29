import React from "react";

export interface AgentTrace {
  id: string;
  agent_name: string;
  action: string;
  result: string;
  timestamp?: string;
}

interface Props {
  traces: AgentTrace[];
}

const AgentTracePanel: React.FC<Props> = ({ traces }) => {
  return (
    <div className="card">
      <div className="hero-row">
        <div>
          <h2 style={{ margin: 0 }}>Agent trace</h2>
          <p className="muted small">Detailed reasoning and outcomes for each AI agent.</p>
        </div>
      </div>
      <div>
        {traces.map((trace) => (
          <div key={trace.id} className="trace-item">
            <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
              <h3 style={{ margin: 0 }}>{trace.agent_name}</h3>
              <span className="badge badge-live">{trace.result}</span>
            </div>
            <p className="muted small" style={{ margin: "8px 0 4px" }}>{trace.action}</p>
            <div className="small muted">{trace.timestamp || "Just now"}</div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default AgentTracePanel;