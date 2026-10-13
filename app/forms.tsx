'use client';

import { useActionState, useState, useTransition } from 'react';
import { createExperiment, saveInfo, setFlags, uploadVersion } from './actions';
import type { Experiment } from '@/lib/db';

export function CreateForm() {
  const [error, action, pending] = useActionState(createExperiment, null);
  return (
    <form action={action} style={{ display: 'flex', gap: 8, flexWrap: 'wrap' }}>
      <input name="name" className="input" placeholder="Experiment name, e.g. Daily Three" required style={{ flex: 1, minWidth: 220 }} />
      <button className="btn primary" disabled={pending}>{pending ? 'Creating…' : 'New experiment'}</button>
      {error && <p className="err" style={{ width: '100%', margin: 0 }}>{error}</p>}
    </form>
  );
}

export function InfoForm({ e }: { e: Experiment }) {
  const [msg, action, pending] = useActionState(saveInfo.bind(null, e.slug), null);
  return (
    <form action={action}>
      <label className="label" htmlFor="name">Name</label>
      <input id="name" name="name" className="input" defaultValue={e.name} />
      <label className="label" htmlFor="about">About</label>
      <textarea id="about" name="about" className="textarea" defaultValue={e.about} placeholder="What the feature is." />
      <label className="label" htmlFor="audience">Who it's for</label>
      <textarea id="audience" name="audience" className="textarea" defaultValue={e.audience} />
      <label className="label" htmlFor="scenario">Scenario</label>
      <textarea id="scenario" name="scenario" className="textarea" defaultValue={e.scenario} placeholder="Testers read this before they start." />
      <label className="label" htmlFor="flow">Flow (one step on each line)</label>
      <textarea id="flow" name="flow" className="textarea" style={{ minHeight: 110 }} defaultValue={e.flow.join('\n')} />
      <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginTop: 10 }}>
        <button className="btn" disabled={pending}>{pending ? 'Saving…' : 'Save'}</button>
        {msg && <span className="ok">{msg}</span>}
      </div>
    </form>
  );
}

export function LiveToggle({ slug, live, canGoLive }: { slug: string; live: boolean; canGoLive: boolean }) {
  const [pending, start] = useTransition();
  return (
    <button
      className="btn"
      style={{ width: '100%', justifyContent: 'space-between' }}
      disabled={pending || (!live && !canGoLive)}
      title={!canGoLive ? 'Upload a version and add flow steps first.' : undefined}
      onClick={() => start(() => setFlags(slug, !live, null))}
    >
      <span className={`pill ${live ? 'live' : ''}`}><span className="dot" />{live ? 'Live test' : 'Test off'}</span>
      <span className="small muted">{live ? 'Stop test' : 'Start test'}</span>
    </button>
  );
}

export function ArchiveButton({ slug }: { slug: string }) {
  const [pending, start] = useTransition();
  return (
    <button
      className="btn danger"
      style={{ width: '100%' }}
      disabled={pending}
      onClick={() => {
        if (confirm('Archive this experiment? The test link stops. You can restore it from the archive list.')) start(() => setFlags(slug, false, true));
      }}
    >
      Archive experiment
    </button>
  );
}

export function RestoreButton({ slug }: { slug: string }) {
  const [pending, start] = useTransition();
  return (
    <button className="btn" disabled={pending} onClick={(ev) => { ev.preventDefault(); start(() => setFlags(slug, null, false)); }}>
      Restore
    </button>
  );
}

export function UploadForm({ slug }: { slug: string }) {
  const [error, action, pending] = useActionState(uploadVersion.bind(null, slug), null);
  return (
    <form action={action} style={{ display: 'grid', gap: 8 }}>
      <input name="file" type="file" accept=".html,.htm,text/html" className="input" required />
      <input name="note" className="input" placeholder="What changed (optional)" />
      <button className="btn" disabled={pending}>{pending ? 'Uploading…' : 'Upload new version'}</button>
      {error && <p className="err" style={{ margin: 0 }}>{error}</p>}
    </form>
  );
}

export function CopyField({ value }: { value: string }) {
  const [done, setDone] = useState(false);
  return (
    <div style={{ display: 'flex', gap: 6 }}>
      <input className="input small" readOnly value={value} onFocus={(e) => e.currentTarget.select()} />
      <button
        type="button"
        className="btn"
        onClick={async () => {
          await navigator.clipboard.writeText(value);
          setDone(true);
          setTimeout(() => setDone(false), 1500);
        }}
      >
        {done ? 'Copied' : 'Copy'}
      </button>
    </div>
  );
}
