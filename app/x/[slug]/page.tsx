import Link from 'next/link';
import { headers } from 'next/headers';
import { notFound } from 'next/navigation';
import { requireAdmin } from '@/lib/auth';
import { rpc, type ExperimentDetail, type Session } from '@/lib/db';
import { logout } from '../../actions';
import { ArchiveButton, CopyField, InfoForm, LiveToggle, UploadForm } from '../../forms';
import { VersionSelect } from './version-select';

export const dynamic = 'force-dynamic';

type Tab = 'prototype' | 'testing' | 'signal';
const TABS: { id: Tab; label: string }[] = [
  { id: 'prototype', label: 'Prototype' },
  { id: 'testing', label: 'Testing' },
  { id: 'signal', label: 'Signal' },
];

const fmt = (iso: string) => new Date(iso).toLocaleString('en-US', { month: 'short', day: 'numeric', hour: 'numeric', minute: '2-digit' });
const mins = (s: Session) => (s.ended_at ? Math.max(0, (Date.parse(s.ended_at) - Date.parse(s.started_at)) / 60000) : null);

export default async function ExperimentPage({
  params,
  searchParams,
}: {
  params: Promise<{ slug: string }>;
  searchParams: Promise<{ tab?: string; v?: string }>;
}) {
  const token = await requireAdmin();
  const { slug } = await params;
  const sp = await searchParams;
  const tab: Tab = (['prototype', 'testing', 'signal'] as const).find((t) => t === sp.tab) ?? 'prototype';

  const data = await rpc<ExperimentDetail | null>('admin_get', { p_token: token, p_slug: slug });
  if (!data) notFound();
  const { experiment: e, versions, sessions } = data;

  const vNum = Number(sp.v) || versions[0]?.number || 0;
  const version = versions.find((v) => v.number === vNum) ?? versions[0];
  const vSessions = version ? sessions.filter((s) => s.version_number === version.number) : [];

  const h = await headers();
  const origin = `${h.get('x-forwarded-proto') ?? 'https'}://${h.get('host')}`;
  const testUrl = `${origin}/t/${e.slug}`;

  return (
    <div className="ws">
      <aside className="card side">
        <Link href="/" className="small muted" style={{ padding: '0 6px 8px' }}>← All experiments</Link>
        <h1>{e.name}</h1>
        <VersionSelect slug={e.slug} tab={tab} current={version?.number ?? 0} versions={versions.map((v) => v.number)} />
        <nav className="nav" style={{ marginTop: 12 }}>
          {TABS.map((t) => (
            <Link key={t.id} href={`/x/${e.slug}?tab=${t.id}${version ? `&v=${version.number}` : ''}`} className={tab === t.id ? 'on' : ''}>
              {t.label}
            </Link>
          ))}
        </nav>
        <div className="foot">
          <form action={logout}><button className="btn" style={{ width: '100%' }}>Sign out</button></form>
        </div>
      </aside>

      <section className="card main">
        {tab === 'prototype' && (
          <div className="stage">
            {version ? (
              <div className="phone">
                <iframe title={`${e.name} version ${version.number}`} srcDoc={version.html} sandbox="allow-scripts allow-forms allow-modals" />
              </div>
            ) : (
              <div className="empty">
                <h2 style={{ fontSize: 16, marginBottom: 6 }}>No prototype yet</h2>
                <p>Upload an HTML file in the panel on the right. A sample is at <a href="/sample-prototype.html" style={{ color: 'var(--accent)' }} download>/sample-prototype.html</a>.</p>
              </div>
            )}
          </div>
        )}

        {tab === 'testing' && (
          <div>
            <h2 style={{ fontSize: 16 }}>Sessions{version ? ` · version ${version.number}` : ''}</h2>
            <p className="muted small">Each row is one tester who opened the test link.</p>
            {vSessions.length === 0 ? <p className="muted">No sessions yet. Start the test and send the link.</p> : (
              <table className="t">
                <thead><tr><th>Tester</th><th>Started</th><th>Steps</th><th>Rating</th><th>Minutes</th><th>Comment</th></tr></thead>
                <tbody>
                  {vSessions.map((s) => (
                    <tr key={s.id}>
                      <td>{s.tester || <span className="muted">Anonymous</span>}</td>
                      <td>{fmt(s.started_at)}</td>
                      <td>{s.steps.length}/{e.flow.length}</td>
                      <td>{s.rating ?? <span className="muted">—</span>}</td>
                      <td>{mins(s)?.toFixed(1) ?? <span className="muted">open</span>}</td>
                      <td style={{ maxWidth: 320 }}>{s.comment || <span className="muted">—</span>}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            )}
          </div>
        )}

        {tab === 'signal' && <Signal flow={e.flow} sessions={vSessions} version={version?.number} />}
      </section>

      <aside className="card info">
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <h2>Project info</h2>
          <span className="pill">{versions.length} version{versions.length === 1 ? '' : 's'}</span>
        </div>
        <InfoForm e={e} />

        <span className="label">Test</span>
        <LiveToggle slug={e.slug} live={e.live} canGoLive={versions.length > 0 && e.flow.length > 0} />
        {e.live && <div style={{ marginTop: 8 }}><CopyField value={testUrl} /></div>}
        <p className="small muted" style={{ margin: '6px 0 0' }}>Testers always get the latest version.</p>

        <span className="label">Upload a new version</span>
        <UploadForm slug={e.slug} />
        <details style={{ marginTop: 8 }}>
          <summary className="small muted" style={{ cursor: 'pointer' }}>Record flow steps from the prototype</summary>
          <p className="small muted">Testers can check steps by hand. To record a step automatically, add this call in the prototype at the point where the step is complete:</p>
          <pre className="small" style={{ background: 'var(--soft)', padding: 8, borderRadius: 8, overflow: 'auto' }}>{`parent.postMessage({ type: 'lab:step', step: 1 }, '*')`}</pre>
        </details>

        <span className="label">Danger zone</span>
        <ArchiveButton slug={e.slug} />
        <p className="small muted" style={{ margin: '6px 0 0', textAlign: 'center' }}>Hides it from the list and stops the test. Reversible.</p>
      </aside>
    </div>
  );
}

function Signal({ flow, sessions, version }: { flow: string[]; sessions: Session[]; version?: number }) {
  const n = sessions.length;
  const finished = sessions.filter((s) => s.ended_at);
  const allSteps = sessions.filter((s) => flow.length > 0 && s.steps.length === flow.length).length;
  const ratings = finished.map((s) => s.rating).filter((r): r is number => r != null);
  const avg = ratings.length ? ratings.reduce((a, b) => a + b, 0) / ratings.length : null;
  const pct = (k: number) => (n ? Math.round((k / n) * 100) : 0);
  const comments = finished.filter((s) => s.comment);

  return (
    <div style={{ display: 'grid', gap: 20 }}>
      <div>
        <h2 style={{ fontSize: 16 }}>Signal{version ? ` · version ${version}` : ''}</h2>
        <p className="muted small" style={{ margin: '2px 0 0' }}>Calculated from the sessions for this version.</p>
      </div>
      <div className="stats">
        <div className="card stat"><span className="small muted">Sessions</span><b>{n}</b></div>
        <div className="card stat"><span className="small muted">Finished</span><b>{pct(finished.length)}%</b></div>
        <div className="card stat"><span className="small muted">All steps done</span><b>{pct(allSteps)}%</b></div>
        <div className="card stat"><span className="small muted">Avg rating</span><b>{avg ? avg.toFixed(1) : '—'}</b></div>
      </div>
      <div className="card" style={{ padding: 16 }}>
        <h3 style={{ fontSize: 14, marginBottom: 10 }}>Step completion</h3>
        {flow.length === 0 && <p className="muted small">Add flow steps in Project info.</p>}
        {flow.map((label, i) => {
          const k = sessions.filter((s) => s.steps.includes(i + 1)).length;
          return (
            <div key={i} style={{ marginBottom: 12 }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', gap: 12 }} className="small">
                <span>{i + 1}. {label}</span>
                <span className="muted" style={{ fontVariantNumeric: 'tabular-nums' }}>{k}/{n} · {pct(k)}%</span>
              </div>
              <div className="bar" style={{ marginTop: 4 }}><i style={{ width: `${pct(k)}%` }} /></div>
            </div>
          );
        })}
      </div>
      <div className="card" style={{ padding: 16 }}>
        <h3 style={{ fontSize: 14, marginBottom: 10 }}>Feedback ({comments.length})</h3>
        {comments.length === 0 && <p className="muted small">No comments yet.</p>}
        {comments.map((s) => (
          <blockquote key={s.id} style={{ margin: '0 0 12px', paddingLeft: 12, borderLeft: '3px solid var(--line)' }}>
            <div>{s.comment}</div>
            <div className="small muted">{s.tester || 'Anonymous'}{s.rating ? ` · ${s.rating}/5` : ''}</div>
          </blockquote>
        ))}
      </div>
    </div>
  );
}
