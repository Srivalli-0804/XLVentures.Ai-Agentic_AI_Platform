import { useState } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import { loginRequest } from '../services/api';
import { useAuthStore } from '../store/authStore';

export function LoginPage() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState<string | null>(null);
  const setAuth = useAuthStore((state) => state.setAuth);
  const navigate = useNavigate();

  const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    try {
      const result = await loginRequest(email, password);
      setAuth(result.token, result.user.email, result.user.role);
      setError(null);
      navigate('/', { replace: true });
    } catch (err) {
      setError('Login failed. Check credentials.');
    }
  };

  return (
    <div className="mx-auto max-w-md rounded-3xl border border-slate-800 bg-slate-900/80 p-8">
      <h1 className="text-3xl font-semibold text-white">Sign in</h1>
      <form className="mt-6 space-y-4" onSubmit={handleSubmit}>
        <label className="block text-slate-300">
          <span className="text-sm">Email</span>
          <input
            type="email"
            className="mt-2 w-full rounded-3xl border border-slate-700 bg-slate-950/70 px-4 py-3 text-white outline-none focus:border-brand-500"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </label>
        <label className="block text-slate-300">
          <span className="text-sm">Password</span>
          <input
            type="password"
            className="mt-2 w-full rounded-3xl border border-slate-700 bg-slate-950/70 px-4 py-3 text-white outline-none focus:border-brand-500"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </label>
        {error && <p className="text-sm text-red-400">{error}</p>}
        <button className="w-full rounded-3xl bg-brand-500 px-4 py-3 text-white transition hover:bg-brand-400" type="submit">
          Login
        </button>
      </form>
    </div>
  );
}
