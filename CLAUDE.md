# RESURRECTION

Biotech product in the DATA PRODUCTS project.

## Product spec

- A persistent autonomous AI scientist works in public on one question about aging at a time, for example why naked mole rats barely age, or which existing drugs extend mouse lifespan across studies.
- It runs daily analyses on open datasets (GEO, GTEx, the mouse lifespan intervention studies), forms and kills hypotheses, and posts findings with code.
- Backers vote on its next question. Subscribers get every notebook and can commission private runs. Agents call it per run.
- Daily compute is capped to what subscriptions cover, because the agent compute cost is the main risk.
- Analysis on public aging data only: no pathogen work, no wet lab, no medical advice.
- Spend evidence: Edison Scientific's Kosmos charges $200 per research run, and about 30,000 researchers and biotech users have tried it. It is private and sold to scientists. This one is public, persistent, cheap and steered by the longevity crowd on X.

## Endpoints (stubs)

| Route | Price | Purpose |
|---|---|---|
| `POST /api/v1/runs` | x402, `PRICE_PRIVATE_RUN` (placeholder; per-run price not yet set) | Commission a private run |
| `GET /api/v1/questions/current` | free | The question it is working on now |
| `POST /api/v1/questions/vote` | free to backers | Vote on the next question |
| `GET /api/v1/findings` | free | Public findings with code links |
| MCP `commission_run` | x402, same price | Agent version of a private run |
| MCP `current_question`, `findings` | free | Agent read access |

## Guardrails (binding)

Public aging datasets only. No pathogen work, no wet lab protocols, no medical advice. The daily compute budget (`DAILY_COMPUTE_CAP_USD`) is enforced before any run starts.

## Stack rules (binding)

- FastAPI with Jinja2 templates and HTMX. Tailwind, HTMX and three.js load from a CDN only. No npm, React or JS build tools.
- Free-tier cloud only. No Supabase, Neon, Vercel or similar defaults.
- Every capability is exposed twice: a REST API under `/api/v1` and an MCP server at `/mcp`. Agents pay per call over x402 (USDC). User-initiated checkout is supported through `app/payments/checkout.py`, which keeps the payment provider behind one interface.
- Built with Claude models and Claude agent swarms only.
- Project constraints live in the DATA PRODUCTS project docs `claude/constraints.md` and `claude/idea-ledger.md`. Apply every constraint exactly as written.

## Launch gate

Run the `security-audit` skill (`.claude/skills/security-audit/`) against the full repo before every launch and every public deploy. No launch ships with an open high or critical finding.

## Skills in this repo

- `.claude/skills/security-audit/` — Cloudflare security-audit skill (MIT, license kept in the folder).
- `.claude/skills/product-brainstorming/` — Anthropic knowledge-work-plugins (Apache-2.0, license kept in the folder).
- `.claude/skills/evaluating-startup-ideas/` and `.claude/skills/idea-validation/` — Refound AI lenny-skills (MIT, license kept in each folder).

## Layout

- `app/main.py` — app factory, x402 middleware, MCP mount, web routes
- `app/api/routes.py` — REST endpoints
- `app/mcp_server.py` — MCP tools, paid ones wrapped with x402
- `app/payments/` — x402 rail and the abstract checkout provider
- `app/templates/` — Jinja2 + HTMX + Tailwind (CDN)
- `tests/` — smoke tests, including the 402 response on paid routes
