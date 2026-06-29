import { NavLink } from 'react-router-dom';
import { useAuthStore } from '../store/authStore';

export function Header() {
  const token = useAuthStore((state) => state.token);

  return (
    <header className="border-b border-slate-800 bg-slate-950/95 backdrop-blur">
      <div className="mx-auto flex max-w-7xl items-center justify-between px-6 py-4">
        <div>
          <p className="text-2xl font-semibold text-white">Agentic AI</p>
          <p className="text-sm text-slate-400">B2B prospect intelligence orchestration</p>
        </div>

        <nav className="flex items-center gap-4 text-slate-300">
          <NavLink to="/" className="hover:text-white" end>
            Dashboard
          </NavLink>
          <NavLink to="/companies" className="hover:text-white">
            Companies
          </NavLink>
          <NavLink to="/monitor" className="hover:text-white">
            Monitor
          </NavLink>
          <NavLink to="/planner" className="hover:text-white">
            Planner
          </NavLink>
          <NavLink to="/approvals" className="hover:text-white">
            Approvals
          </NavLink>
          <NavLink to="/settings" className="hover:text-white">
            Settings
          </NavLink>
          {!token && (
            <NavLink to="/login" className="rounded-3xl border border-slate-700 bg-slate-950/70 px-3 py-2 text-sm text-slate-200 transition hover:border-brand-500">
              Sign in
            </NavLink>
          )}
        </nav>
      </div>
    </header>
  );
}
