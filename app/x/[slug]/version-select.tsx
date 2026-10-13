'use client';

import { useRouter } from 'next/navigation';

export function VersionSelect({ slug, tab, current, versions }: { slug: string; tab: string; current: number; versions: number[] }) {
  const router = useRouter();
  if (versions.length === 0) return <div className="select muted small">No versions yet</div>;
  return (
    <select
      className="select"
      value={current}
      onChange={(e) => router.push(`/x/${slug}?tab=${tab}&v=${e.target.value}`)}
      aria-label="Version"
    >
      {versions.map((n) => <option key={n} value={n}>Version {n}{n === versions[0] ? ' (latest)' : ''}</option>)}
    </select>
  );
}
