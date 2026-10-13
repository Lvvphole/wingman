import Link from 'next/link';
import { requireAdmin } from '@/lib/auth';
import { rpc, type ExperimentSummary } from '@/lib/db';
import { logout } from './actions';
import { CreateForm, RestoreButton } from './forms';

export const dynamic = 'force-dynamic';

export default async function Home({ searchParams }: { searchParams: Promise<{ archived?: string }> }) {
  const token = await requireAdmin();
  const archived = (await searchParams).archived === '1';
  const items = await rpc<ExperimentSummary[]>('admin_list', { p_token: token, p_archived: archived });

  return (
    <main style={{ maxWidth: 860, margin: '0 auto', padding: '32px 16px' }}>
      <header style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 20 }}>
        <div>
          <h1 style={{ fontSize: 22 }}>Wingman Lab</h1>
          <p className="muted" style={{ margin: '2px 0 0' }}>Publish a prototype, send the test link, read the signal.</p>
        </div>
        <form action={logout}><button className="btn">Sign out</button></form>
      </header>

      {!archived && <div className="card" style={{ padding: 16, marginBottom: 20 }}><CreateForm /></div>}

      <div style={{ display: 'flex', gap: 8, marginBottom: 12 }}>
        <Link href="/" className={`pill ${!archived ? 'live' : ''}`}>Active</Link>
        <Link href="/?archived=1" className={`pill ${archived ? 'live' : ''}`}>Archived</Link>
      </div>

      <div className="list">
        {items.length === 0 && <p className="muted">{archived ? 'No archived experiments.' : 'No experiments yet. Create one above.'}</p>}
        {items.map((x) => (
          <Link key={x.id} href={`/x/${x.slug}`} className="card row">
            <div>
              <div style={{ fontWeight: 600 }}>{x.name}</div>
              <div className="small muted">{x.versions} version{x.versions === 1 ? '' : 's'} · {x.sessions} session{x.sessions === 1 ? '' : 's'}</div>
            </div>
            {archived ? <RestoreButton slug={x.slug} /> : (
              <span className={`pill ${x.live ? 'live' : ''}`}><span className="dot" />{x.live ? 'Live' : 'Off'}</span>
            )}
          </Link>
        ))}
      </div>
    </main>
  );
}
