'use client';

import { useActionState } from 'react';
import { login } from '../actions';

export default function Login() {
  const [error, action, pending] = useActionState(login, null);
  return (
    <main style={{ display: 'grid', placeItems: 'center', minHeight: '100vh', padding: 16 }}>
      <form action={action} className="card" style={{ width: '100%', maxWidth: 380, padding: 24 }}>
        <h1 style={{ fontSize: 20 }}>Wingman Lab</h1>
        <p className="muted" style={{ marginTop: 4 }}>Enter the admin token.</p>
        <label className="label" htmlFor="token">Admin token</label>
        <input id="token" name="token" type="password" className="input" autoComplete="current-password" required />
        {error && <p className="err">{error}</p>}
        <button className="btn primary" style={{ width: '100%', marginTop: 16 }} disabled={pending}>
          {pending ? 'Checking…' : 'Sign in'}
        </button>
      </form>
    </main>
  );
}
