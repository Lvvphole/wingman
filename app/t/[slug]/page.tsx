import type { Metadata } from 'next';
import { rpc, type TestPayload } from '@/lib/db';
import { Tester } from './tester';

export const dynamic = 'force-dynamic';
export const metadata: Metadata = { title: 'Prototype test', robots: { index: false } };

export default async function TestPage({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const data = await rpc<TestPayload | null>('test_get', { p_slug: slug });
  if (!data) {
    return (
      <main style={{ display: 'grid', placeItems: 'center', minHeight: '100vh', padding: 16 }}>
        <div className="empty">
          <h1 style={{ fontSize: 18, marginBottom: 6 }}>This test is not open</h1>
          <p>The link is wrong, or the test has stopped. Ask the person who sent it.</p>
        </div>
      </main>
    );
  }
  return <Tester slug={slug} data={data} />;
}
