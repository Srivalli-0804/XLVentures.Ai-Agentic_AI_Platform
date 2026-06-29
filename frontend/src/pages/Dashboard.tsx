import React, { useEffect, useState } from "react";
import PipelineBoard from "../dashboard/PipelineBoard";
import WorkflowTimeline from "../workflow/WorkflowTimeline";
import AgentTracePanel from "../agents/AgentTracePanel";
import AnalyticsChart from "../dashboard/AnalyticsChart";
import { getProspects, getWorkflowTimeline, getAgentTrace } from "../services/prospectService";

const Dashboard = () => {
  const [prospects, setProspects] = useState<any[]>([]);
  const [timeline, setTimeline] = useState<any[]>([]);
  const [traces, setTraces] = useState<any[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const loadData = async () => {
      try {
        const [prospectData, timelineData, traceData] = await Promise.all([
          getProspects("demo-workflow"),
          getWorkflowTimeline("demo-workflow"),
          getAgentTrace("demo-workflow")
        ]);

        setProspects(prospectData);
        setTimeline(timelineData);
        setTraces(traceData);
      } catch (error) {
        console.error(error);
      } finally {
        setLoading(false);
      }
    };

    loadData();
  }, []);

  const metrics = [
    { label: "Qualified accounts", value: prospects.filter((p) => p.status === "Qualified").length, tone: "live" },
    { label: "Recommended outreach", value: prospects.filter((p) => p.status === "Recommended").length, tone: "queued" },
    { label: "Live workflow steps", value: timeline.length, tone: "live" }
  ];

  const chartData = [
    { label: "Discovery", value: prospects.filter((p) => p.status === "Discovered").length, color: "#38bdf8" },
    { label: "Qualification", value: prospects.filter((p) => p.status === "Qualified").length, color: "#818cf8" },
    { label: "Recommendation", value: prospects.filter((p) => p.status === "Recommended").length, color: "#34d399" }
  ];

  return (
    <div>
      <div className="hero-row">
        <div>
          <div className="stat-pill">⚡ Live agentic pipeline</div>
          <h2 style={{ margin: "8px 0 6px", fontSize: "1.8rem" }}>Operations hub for high-intent prospects</h2>
          <p className="muted">Discover, qualify, enrich, and recommend with a cohesive AI-led workflow.</p>
        </div>
        <button className="primary">Run a fresh sweep</button>
      </div>

      <div className="grid grid-3" style={{ marginBottom: 16 }}>
        {metrics.map((metric) => (
          <div className="card" key={metric.label}>
            <div className={`badge ${metric.tone === "live" ? "badge-live" : "badge-queued"}`}>{metric.tone === "live" ? "● Live" : "⏳ Queued"}</div>
            <div className="metric-value">{metric.value}</div>
            <div className="metric-label">{metric.label}</div>
          </div>
        ))}
      </div>

      {loading ? <div className="card">Loading your pipeline...</div> : <PipelineBoard prospects={prospects} />}
      <div className="grid grid-2" style={{ marginTop: 16 }}>
        <AnalyticsChart data={chartData} />
        <AgentTracePanel traces={traces} />
      </div>
      <div style={{ marginTop: 16 }}>
        <WorkflowTimeline steps={timeline} />
      </div>
    </div>
  );
};

export default Dashboard;