import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import WorkflowStudio from "./pages/WorkflowStudio";
import Analytics from "./pages/Analytics";
import Settings from "./pages/Settings";
import ProspectDetails from "./pages/ProspectDetails";
import "./index.css";

const AppShell = () => {
  return (
    <div className="app-shell">
      <nav className="topbar">
        <div>
          <h1>ProspectIQ</h1>
          <p>Agentic AI prospect intelligence</p>
        </div>
        <div className="topbar-links">
          <a href="/">Dashboard</a>
          <a href="/workflow">Workflow Studio</a>
          <a href="/analytics">Analytics</a>
          <a href="/settings">Settings</a>
        </div>
      </nav>
      <main className="page-content">
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/workflow" element={<WorkflowStudio />} />
          <Route path="/analytics" element={<Analytics />} />
          <Route path="/settings" element={<Settings />} />
          <Route path="/prospects/:id" element={<ProspectDetails />} />
        </Routes>
      </main>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <BrowserRouter>
      <AppShell />
    </BrowserRouter>
  </React.StrictMode>
);
