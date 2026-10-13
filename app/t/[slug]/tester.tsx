'use client';

import { useEffect, useRef, useState } from 'react';
import { finishSession, recordStep, startSession } from '../../actions';
import type { TestPayload } from '@/lib/db';

type Phase = 'intro' | 'testing' | 'feedback' | 'done';

export function Tester({ slug, data }: { slug: string; data: TestPayload }) {
  const [phase, setPhase] = useState<Phase>('intro');
  const [name, setName] = useState('');
  const [session, setSession] = useState<string | null>(null);
  const [steps, setSteps] = useState<number[]>([]);
  const [rating, setRating] = useState<number | null>(null);
  const [comment, setComment] = useState('');
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const frame = useRef<HTMLIFrameElement>(null);
  const sessionRef = useRef<string | null>(null);
  sessionRef.current = session;

  function mark(step: number) {
    if (!Number.isInteger(step) || step < 1 || step > data.flow.length) return;
    setSteps((prev) => (prev.includes(step) ? prev : [...prev, step].sort((a, b) => a - b)));
    if (sessionRef.current) recordStep(sessionRef.current, step).catch(() => undefined);
  }

  // Steps the prototype reports with parent.postMessage({ type: 'lab:step', step: n }, '*').
  useEffect(() => {
    function onMessage(ev: MessageEvent) {
      if (ev.source !== frame.current?.contentWindow) return;
      const m = ev.data as { type?: string; step?: number } | null;
      if (m && m.type === 'lab:step' && typeof m.step === 'number') mark(m.step);
    }
    window.addEventListener('message', onMessage);
    return () => window.removeEventListener('message', onMessage);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  async function begin() {
    setBusy(true);
    setError(null);
    try {
      setSession(await startSession(slug, name.trim()));
      setPhase('testing');
    } catch {
      setError('The test could not start. Refresh the page and try again.');
    } finally {
      setBusy(false);
    }
  }

  async function submit() {
    if (!session) return;
    setBusy(true);
    setError(null);
    try {
      await finishSession(session, rating, comment.trim());
      setPhase('done');
    } catch {
      setError('Your feedback was not sent. Try again.');
    } finally {
      setBusy(false);
    }
  }

  return (
    <main className="tester">
      <section className="stage">
        <div className="phone">
          {phase === 'intro' ? (
            <div style={{ display: 'grid', placeItems: 'center', height: '100%', color: '#a1a1aa', textAlign: 'center', padding: 24 }}>
              Start the test to open the prototype.
            </div>
          ) : (
            <iframe ref={frame} title={data.name} srcDoc={data.html} sandbox="allow-scripts allow-forms allow-modals" />
          )}
        </div>
      </section>

      <aside className="card panel">
        <span className="pill">Prototype test</span>
        <h1 style={{ fontSize: 20, margin: '10px 0 4px' }}>{data.name}</h1>

        {phase === 'intro' && (
          <>
            {data.scenario && <p className="muted">{data.scenario}</p>}
            <label className="label" htmlFor="tname">Your name (optional)</label>
            <input id="tname" className="input" value={name} onChange={(e) => setName(e.target.value)} maxLength={80} />
            <button className="btn primary" style={{ width: '100%', marginTop: 14 }} onClick={begin} disabled={busy}>
              {busy ? 'Starting…' : 'Start test'}
            </button>
          </>
        )}

        {phase === 'testing' && (
          <>
            <p className="muted">Do these steps in the prototype. Check each step when you complete it.</p>
            {data.flow.map((label, i) => {
              const done = steps.includes(i + 1);
              return (
                <div key={i} className="step">
                  <button className={`check ${done ? 'done' : ''}`} aria-label={`Step ${i + 1} done`} aria-pressed={done} onClick={() => mark(i + 1)}>
                    {done ? '✓' : ''}
                  </button>
                  <span style={{ textDecoration: done ? 'line-through' : undefined, color: done ? 'var(--muted)' : undefined }}>{label}</span>
                </div>
              );
            })}
            <button className="btn primary" style={{ width: '100%', marginTop: 14 }} onClick={() => setPhase('feedback')}>
              I'm finished
            </button>
          </>
        )}

        {phase === 'feedback' && (
          <>
            <label className="label">How useful is this feature?</label>
            <div className="stars">
              {[1, 2, 3, 4, 5].map((n) => (
                <button key={n} className={rating === n ? 'on' : ''} onClick={() => setRating(n)} aria-pressed={rating === n}>{n}</button>
              ))}
            </div>
            <p className="small muted" style={{ margin: '4px 0 0' }}>1 = not useful, 5 = very useful</p>
            <label className="label" htmlFor="comment">What worked? What was confusing?</label>
            <textarea id="comment" className="textarea" style={{ minHeight: 120 }} value={comment} onChange={(e) => setComment(e.target.value)} maxLength={4000} />
            <div style={{ display: 'flex', gap: 8, marginTop: 14 }}>
              <button className="btn" onClick={() => setPhase('testing')}>Back</button>
              <button className="btn primary" style={{ flex: 1 }} onClick={submit} disabled={busy}>{busy ? 'Sending…' : 'Send feedback'}</button>
            </div>
          </>
        )}

        {phase === 'done' && <p>Thank you. Your feedback was sent. You can close this page.</p>}
        {error && <p className="err">{error}</p>}
      </aside>
    </main>
  );
}
