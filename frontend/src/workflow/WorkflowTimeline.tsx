import React from "react";

export interface WorkflowStep {
  id: string;
  agent: string;
  status: string;
  timestamp: string;
  details?: string;
}

interface Props {
  steps: WorkflowStep[];
}

const WorkflowTimeline: React.FC<Props> = ({ steps }) => {
  return (
    <div className="card">
      <div className="hero-row">
        <div>
          <h2 style={{ margin: 0 }}>Workflow timeline</h2>
          <p className="muted small">Trace every agent decision in real time.</p>
        </div>
      </div>
      <div>
        {steps.map((step) => (
          <div key={step.id} className="timeline-item">
            <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
              <h3 style={{ margin: 0 }}>{step.agent}</h3>
              <span className="badge badge-live">{step.status}</span>
            </div>
            <p className="muted small" style={{ margin: "8px 0 4px" }}>{step.details || "Completed"}</p>
            <div className="small muted">{step.timestamp}</div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default WorkflowTimeline;