'use server';

import { cookies } from 'next/headers';
import { redirect } from 'next/navigation';
import { revalidatePath } from 'next/cache';
import { rpc } from '@/lib/db';
import { COOKIE, requireAdmin } from '@/lib/auth';

const str = (f: FormData, k: string) => String(f.get(k) ?? '').trim();

export async function login(_: string | null, form: FormData): Promise<string | null> {
  const token = str(form, 'token');
  if (!token || !(await rpc<boolean>('admin_check', { p_token: token }))) return 'Token is not correct.';
  (await cookies()).set(COOKIE, token, {
    httpOnly: true,
    secure: process.env.NODE_ENV === 'production',
    sameSite: 'lax',
    path: '/',
    maxAge: 60 * 60 * 24 * 30,
  });
  redirect('/');
}

export async function logout() {
  (await cookies()).delete(COOKIE);
  redirect('/login');
}

export async function createExperiment(_: string | null, form: FormData): Promise<string | null> {
  const token = await requireAdmin();
  const name = str(form, 'name');
  const slug = name.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '').slice(0, 60);
  if (slug.length < 3) return 'Use a name with 3 or more letters or digits.';
  try {
    await rpc('admin_create', { p_token: token, p_slug: slug, p_name: name });
  } catch (e) {
    return (e as Error).message.includes('duplicate') ? 'An experiment with this name exists.' : (e as Error).message;
  }
  redirect(`/x/${slug}`);
}

export async function saveInfo(slug: string, _: string | null, form: FormData): Promise<string | null> {
  const token = await requireAdmin();
  const flow = str(form, 'flow').split('\n').map((s) => s.trim()).filter(Boolean);
  await rpc('admin_update', {
    p_token: token,
    p_slug: slug,
    p_name: str(form, 'name') || slug,
    p_about: str(form, 'about'),
    p_audience: str(form, 'audience'),
    p_scenario: str(form, 'scenario'),
    p_flow: flow,
  });
  revalidatePath(`/x/${slug}`);
  return 'Saved.';
}

export async function setFlags(slug: string, live: boolean | null, archived: boolean | null) {
  const token = await requireAdmin();
  await rpc('admin_set_flags', { p_token: token, p_slug: slug, p_live: live, p_archived: archived });
  if (archived === true) redirect('/');
  revalidatePath(`/x/${slug}`);
  revalidatePath('/');
}

export async function uploadVersion(slug: string, _: string | null, form: FormData): Promise<string | null> {
  const token = await requireAdmin();
  const file = form.get('file');
  if (!(file instanceof File) || file.size === 0) return 'Select an HTML file.';
  if (file.size > 3_000_000) return 'The file is too large. The maximum is 3 MB.';
  const html = await file.text();
  const n = await rpc<number>('admin_add_version', { p_token: token, p_slug: slug, p_html: html, p_note: str(form, 'note') });
  revalidatePath(`/x/${slug}`);
  redirect(`/x/${slug}?v=${n}`);
}

// Tester actions: public. The database functions accept only live experiments
// and in-range step numbers.

export async function startSession(slug: string, tester: string): Promise<string> {
  return rpc<string>('test_start', { p_slug: slug, p_tester: tester.slice(0, 80) });
}

export async function recordStep(session: string, step: number): Promise<void> {
  await rpc('test_step', { p_session: session, p_step: step });
}

export async function finishSession(session: string, rating: number | null, comment: string): Promise<void> {
  const r = rating && rating >= 1 && rating <= 5 ? Math.round(rating) : null;
  await rpc('test_finish', { p_session: session, p_rating: r, p_comment: comment.slice(0, 4000) });
}
