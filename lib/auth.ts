import 'server-only';
import { cookies } from 'next/headers';
import { redirect } from 'next/navigation';
import { rpc } from './db';

export const COOKIE = 'lab_admin';

export async function getToken(): Promise<string | null> {
  return (await cookies()).get(COOKIE)?.value ?? null;
}

/** Returns the admin token, or redirects to /login when it is missing or invalid. */
export async function requireAdmin(): Promise<string> {
  const token = await getToken();
  if (!token || !(await rpc<boolean>('admin_check', { p_token: token }))) redirect('/login');
  return token;
}
