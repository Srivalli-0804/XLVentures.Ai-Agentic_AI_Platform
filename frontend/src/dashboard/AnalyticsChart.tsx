import React from "react";

interface MetricPoint {
  label: string;
  value: number;
  color: string;
}

interface Props {
  data: MetricPoint[];
}

const AnalyticsChart: React.FC<Props> = ({ data }) => {
  const max = Math.max(...data.map((item) => item.value), 1);

  return (
    <div className="card">
      <div className="hero-row">
        <div>
          <h3 style={{ margin: 0 }}>Signal intensity</h3>
          <p className="muted small">A quick view of how the pipeline is trending.</p>
        </div>
      </div>
      <div style={{ display: "grid", gap: 12 }}>
        {data.map((item) => (
          <div key={item.label}>
            <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 6 }}>
              <span>{item.label}</span>
              <span className="muted small">{item.value}</span>
            </div>
            <div className="chart-track">
              <div
                className="chart-bar-fill"
                style={{ width: `${(item.value / max) * 100}%`, background: item.color }}
              />
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default AnalyticsChart;
