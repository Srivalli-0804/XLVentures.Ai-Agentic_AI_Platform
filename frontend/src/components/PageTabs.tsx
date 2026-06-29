import { NavLink } from 'react-router-dom';

const tabs = [
  { to: '/', label: 'Dashboard' },
  { to: '/monitor', label: 'Monitor' },
  { to: '/planner', label: 'Planner' },
  { to: '/approvals', label: 'Approvals' },
  { to: '/builder', label: 'Builder' },
  { to: '/companies', label: 'Companies' },
  { to: '/profile', label: 'Profile' },
  { to: '/settings', label: 'Settings' }
];

export function PageTabs() {
  return (
    <div className="mb-6 flex flex-wrap gap-3">
      {tabs.map((tab) => (
        <NavLink
          key={tab.to}
          to={tab.to}
          className={({ isActive }) =>
            `rounded-3xl px-4 py-2 text-sm transition ${isActive ? 'bg-brand-500 text-white' : 'bg-slate-800 text-slate-300 hover:bg-slate-700'}`
          }
        >
          {tab.label}
        </NavLink>
      ))}
    </div>
  );
}
