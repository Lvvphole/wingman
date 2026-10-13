import 'server-only';
import { createClient, type SupabaseClient } from '@supabase/supabase-js';

let client: SupabaseClient | null = null;

function db(): SupabaseClient {
  if (client) return client;
  const url = process.env.SUPABASE_URL;
  const key = process.env.SUPABASE_PUBLISHABLE_KEY;
  if (!url || !key) throw new Error('SUPABASE_URL and SUPABASE_PUBLISHABLE_KEY must be set');
  client = createClient(url, key, { auth: { persistSession: false, autoRefreshToken: false } });
  return client;
}

export async function rpc<T>(fn: string, args: Record<string, unknown>): Promise<T> {
  const { data, error } = await db().rpc(fn, args);
  if (error) throw new Error(error.message);
  return data as T;
}

export type Experiment = {
  id: string;
  slug: string;
  name: string;
  about: string;
  audience: string;
  scenario: string;
  flow: string[];
  live: boolean;
  archived: boolean;
  created_at: string;
};

export type Version = { id: string; number: number; note: string; created_at: string; html: string };

export type Session = {
  id: string;
  tester: string;
  steps: number[];
  rating: number | null;
  comment: string | null;
  started_at: string;
  ended_at: string | null;
  version_number: number;
};

export type ExperimentDetail = { experiment: Experiment; versions: Version[]; sessions: Session[] };

export type ExperimentSummary = {
  id: string;
  slug: string;
  name: string;
  live: boolean;
  archived: boolean;
  created_at: string;
  versions: number;
  sessions: number;
};

export type TestPayload = { name: string; scenario: string; flow: string[]; html: string; version: number };
