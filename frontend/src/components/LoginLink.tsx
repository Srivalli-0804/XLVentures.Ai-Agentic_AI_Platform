import { Link } from 'react-router-dom';

export function LoginLink() {
  return (
    <Link to="/login" className="rounded-3xl border border-slate-700 bg-slate-950/70 px-4 py-2 text-sm text-slate-200 transition hover:border-brand-500">
      Sign in
    </Link>
  );
}
