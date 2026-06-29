import { Route, Routes } from 'react-router-dom';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { DashboardPage } from './pages/DashboardPage';
import { CompanyResultsPage } from './pages/CompanyResultsPage';
import { CompanyDetailsPage } from './pages/CompanyDetailsPage';
import { SettingsPage } from './pages/SettingsPage';
import { LoginPage } from './pages/LoginPage';
import { WorkflowMonitorPage } from './pages/WorkflowMonitorPage';
import { ApprovalQueuePage } from './pages/ApprovalQueuePage';
import { PlannerVisualizationPage } from './pages/PlannerVisualizationPage';
import { WorkflowBuilderPage } from './pages/WorkflowBuilderPage';
import { UserProfilePage } from './pages/UserProfilePage';
import { Header } from './components/Header';
import { RequireAuth } from './components/RequireAuth';

const queryClient = new QueryClient();

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <div className="min-h-screen bg-slate-950 text-slate-100">
        <Header />
        <main className="px-6 py-6">
          <Routes>
            <Route path="/login" element={<LoginPage />} />
            <Route
              path="/"
              element={
                <RequireAuth>
                  <DashboardPage />
                </RequireAuth>
              }
            />
            <Route
              path="/monitor"
              element={
                <RequireAuth>
                  <WorkflowMonitorPage />
                </RequireAuth>
              }
            />
            <Route
              path="/planner"
              element={
                <RequireAuth>
                  <PlannerVisualizationPage />
                </RequireAuth>
              }
            />
            <Route
              path="/approvals"
              element={
                <RequireAuth>
                  <ApprovalQueuePage />
                </RequireAuth>
              }
            />
            <Route
              path="/builder"
              element={
                <RequireAuth>
                  <WorkflowBuilderPage />
                </RequireAuth>
              }
            />
            <Route
              path="/profile"
              element={
                <RequireAuth>
                  <UserProfilePage />
                </RequireAuth>
              }
            />
            <Route
              path="/companies"
              element={
                <RequireAuth>
                  <CompanyResultsPage />
                </RequireAuth>
              }
            />
            <Route
              path="/companies/:id"
              element={
                <RequireAuth>
                  <CompanyDetailsPage />
                </RequireAuth>
              }
            />
            <Route
              path="/settings"
              element={
                <RequireAuth>
                  <SettingsPage />
                </RequireAuth>
              }
            />
          </Routes>
        </main>
      </div>
    </QueryClientProvider>
  );
}

export default App;
