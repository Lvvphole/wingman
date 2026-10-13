# wingman

Wingman Lab: publish a phone prototype, send testers a link, and read the results.

## Pages

| Path | Who | Purpose |
| --- | --- | --- |
| `/login` | Admin | Sign in with the admin token. |
| `/` | Admin | List, create, archive and restore experiments. |
| `/x/[slug]` | Admin | Prototype, Testing and Signal tabs. Project info, live test toggle, version upload. |
| `/t/[slug]` | Tester | Public test page. Name, flow checklist, rating and comment. |

## Prototype format

A version is one self-contained HTML file (maximum 3 MB). It runs in a sandboxed iframe with no access to the app origin.
To record a flow step automatically, the prototype calls:

```js
parent.postMessage({ type: 'lab:step', step: 1 }, '*');
```

Testers can also check steps by hand. `public/sample-prototype.html` is an example.

## Data

Supabase project `experiment-lab`. Schema: `supabase/001_init_lab.sql`.
Row-level security is on with no table policies. All access goes through `SECURITY DEFINER` functions:

- `admin_*` functions require the admin token. The database stores only its SHA-256 hash.
- `test_*` functions accept only live, non-archived experiments and step numbers inside the flow.

## Environment

| Variable | Value |
| --- | --- |
| `SUPABASE_URL` | Supabase project URL |
| `SUPABASE_PUBLISHABLE_KEY` | Supabase publishable key (server-side use only) |

## Develop

```sh
npm install
npm run dev
```
