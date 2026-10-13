-- experiment-lab: initial schema
-- Applied to Supabase project experiment-lab (wyiqpoboudsqvsmglabo) in 7 migrations (lab_01..lab_07).

create extension if not exists pgcrypto with schema extensions;

create table public.admin_config (id int primary key default 1 check (id = 1), token_hash text not null);
insert into public.admin_config (token_hash) values ('2ade870aa4d28686f8cc8997f47a52d5e383fba31dd52a2c9ada56bb6d33703b');

create table public.experiments (
  id uuid primary key default gen_random_uuid(),
  slug text unique not null check (slug ~ '^[a-z0-9-]{3,60}$'),
  name text not null,
  about text not null default '',
  audience text not null default '',
  scenario text not null default '',
  flow jsonb not null default '[]'::jsonb,
  live boolean not null default false,
  archived boolean not null default false,
  created_at timestamptz not null default now()
);
create table public.versions (
  id uuid primary key default gen_random_uuid(),
  experiment_id uuid not null references public.experiments(id) on delete cascade,
  number int not null,
  html text not null,
  note text not null default '',
  created_at timestamptz not null default now(),
  unique (experiment_id, number)
);
create table public.sessions (
  id uuid primary key default gen_random_uuid(),
  experiment_id uuid not null references public.experiments(id) on delete cascade,
  version_id uuid not null references public.versions(id) on delete cascade,
  tester text not null default '',
  steps int[] not null default '{}',
  rating int check (rating between 1 and 5),
  comment text,
  started_at timestamptz not null default now(),
  ended_at timestamptz
);
create index on public.versions (experiment_id, number desc);
create index on public.sessions (experiment_id, started_at desc);

alter table public.admin_config enable row level security;
alter table public.experiments enable row level security;
alter table public.versions enable row level security;
alter table public.sessions enable row level security;

create or replace function public._is_admin(p_token text) returns boolean
language sql stable security definer set search_path = public, extensions as $$
  select exists (select 1 from admin_config where token_hash = encode(extensions.digest(coalesce(p_token,''), 'sha256'), 'hex'));
$$;

create or replace function public._require_admin(p_token text) returns void
language plpgsql stable security definer set search_path = public as $$
begin if not public._is_admin(p_token) then raise exception 'unauthorized' using errcode = '28000'; end if; end $$;

create or replace function public.admin_check(p_token text) returns boolean
language sql stable security definer set search_path = public as $$ select public._is_admin(p_token) $$;

create or replace function public.admin_list(p_token text, p_archived boolean default false) returns jsonb
language plpgsql stable security definer set search_path = public as $$
begin perform _require_admin(p_token);
return coalesce((select jsonb_agg(jsonb_build_object('id',e.id,'slug',e.slug,'name',e.name,'live',e.live,'archived',e.archived,'created_at',e.created_at,
  'versions',(select count(*) from versions v where v.experiment_id=e.id),
  'sessions',(select count(*) from sessions s where s.experiment_id=e.id)) order by e.created_at desc)
  from experiments e where e.archived = p_archived), '[]'::jsonb);
end $$;

create or replace function public.admin_get(p_token text, p_slug text) returns jsonb
language plpgsql stable security definer set search_path = public as $$
declare e experiments; begin perform _require_admin(p_token);
select * into e from experiments where slug = p_slug; if not found then return null; end if;
return jsonb_build_object('experiment', to_jsonb(e),
  'versions', coalesce((select jsonb_agg(jsonb_build_object('id',v.id,'number',v.number,'note',v.note,'created_at',v.created_at,'html',v.html) order by v.number desc) from versions v where v.experiment_id=e.id),'[]'::jsonb),
  'sessions', coalesce((select jsonb_agg(to_jsonb(s) || jsonb_build_object('version_number',(select number from versions where id=s.version_id)) order by s.started_at desc) from sessions s where s.experiment_id=e.id),'[]'::jsonb));
end $$;

create or replace function public.admin_create(p_token text, p_slug text, p_name text) returns text
language plpgsql security definer set search_path = public as $$
begin perform _require_admin(p_token);
insert into experiments (slug, name) values (p_slug, p_name); return p_slug; end $$;

create or replace function public.admin_update(p_token text, p_slug text, p_name text, p_about text, p_audience text, p_scenario text, p_flow jsonb) returns void
language plpgsql security definer set search_path = public as $$
begin perform _require_admin(p_token);
if jsonb_typeof(p_flow) <> 'array' then raise exception 'flow must be an array'; end if;
update experiments set name=p_name, about=p_about, audience=p_audience, scenario=p_scenario, flow=p_flow where slug=p_slug; end $$;

create or replace function public.admin_set_flags(p_token text, p_slug text, p_live boolean, p_archived boolean) returns void
language plpgsql security definer set search_path = public as $$
begin perform _require_admin(p_token);
update experiments set live=coalesce(p_live, live), archived=coalesce(p_archived, archived) where slug=p_slug; end $$;

create or replace function public.admin_add_version(p_token text, p_slug text, p_html text, p_note text) returns int
language plpgsql security definer set search_path = public as $$
declare eid uuid; n int; begin perform _require_admin(p_token);
if length(p_html) > 3000000 then raise exception 'prototype too large (max 3 MB)'; end if;
select id into eid from experiments where slug=p_slug for update; if eid is null then raise exception 'not found'; end if;
select coalesce(max(number),0)+1 into n from versions where experiment_id=eid;
insert into versions (experiment_id, number, html, note) values (eid, n, p_html, coalesce(p_note,'')); return n; end $$;

create or replace function public.test_get(p_slug text) returns jsonb
language sql stable security definer set search_path = public as $$
  select jsonb_build_object('name',e.name,'scenario',e.scenario,'flow',e.flow,'html',v.html,'version',v.number)
  from experiments e join lateral (select * from versions where experiment_id=e.id order by number desc limit 1) v on true
  where e.slug=p_slug and e.live and not e.archived;
$$;

create or replace function public.test_start(p_slug text, p_tester text) returns uuid
language plpgsql security definer set search_path = public as $$
declare e experiments; vid uuid; sid uuid; begin
select * into e from experiments where slug=p_slug and live and not archived; if not found then raise exception 'test not live'; end if;
select id into vid from versions where experiment_id=e.id order by number desc limit 1; if vid is null then raise exception 'no version'; end if;
insert into sessions (experiment_id, version_id, tester) values (e.id, vid, left(coalesce(p_tester,''),80)) returning id into sid; return sid; end $$;

create or replace function public.test_step(p_session uuid, p_step int) returns void
language plpgsql security definer set search_path = public as $$
begin
update sessions s set steps = (select array_agg(distinct x order by x) from unnest(s.steps || p_step) x)
where s.id=p_session and s.ended_at is null and p_step >= 1
  and p_step <= (select jsonb_array_length(flow) from experiments where id=s.experiment_id); end $$;

create or replace function public.test_finish(p_session uuid, p_rating int, p_comment text) returns void
language plpgsql security definer set search_path = public as $$
begin update sessions set ended_at=now(), rating=p_rating, comment=left(coalesce(p_comment,''),4000) where id=p_session and ended_at is null; end $$;

revoke all on function public._is_admin(text), public._require_admin(text) from public, anon, authenticated;
