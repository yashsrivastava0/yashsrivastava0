# Projects and Public Presence Audit — Evidence, Ranking, Gaps, and Next-Step Research

**Status:** Research and recommendation package only. No repositories, profile settings, websites, LinkedIn fields, or deployments are changed by this document.  
**Research date:** 2026-10-06  
**Account:** `yashsrivastava0`  
**Goal:** Build an evidence-backed hierarchy of public work for an AI-engineering job search, with explicit treatment of ownership, team work, demos, licenses, contradictions, and recruiter-facing risk.

---

## 1. Executive findings

The strongest professional story is now:

1. **OryxenAI** — flagship owned AI product.
2. **QuotaMesh** — AI infrastructure and systems engineering.
3. **AI Receptionist** — current voice-AI/team project; high technical value, but private and not owned solely by the user.
4. **MediFindX0** — applied multimodal AI with a currently resolving Hugging Face Space.
5. **BlogerVoger** — useful full-stack/product breadth after demo/license verification.
6. **YASHODA** — visually strong full-stack work, but its live demo currently contains commerce-like scale/service claims that should be treated as a credibility blocker unless those claims are real and supportable.
7. **Ai-Portfolio** — important as the destination website and visual identity source, usually not as a pin because the profile already links to the portfolio.

The biggest profile opportunity is not “add more effects.” It is to **concentrate attention on the three systems that best prove current AI engineering** and make the public facts consistent across GitHub, portfolio, LinkedIn, and résumé.

The biggest risks found are:

- an empty repository currently occupying the first pin;
- a public `oauth` repository previously observed with a root `.env` filename, which warrants a separate credential-hygiene review without exposing its contents;
- unresolved company/date/education/certification inconsistencies;
- the old portfolio carrying aggressive experience and performance claims that should not be copied to GitHub without strong evidence;
- YASHODA’s live demo presenting business-like metrics such as member count/rating/dispatch/returns that appear as real claims to a visitor even though the project is being used as a portfolio/demo project;
- a temptation to present a private team AI Receptionist as an owned/open-source project, which should be avoided.

---

## 2. Evidence and confidence rules

### Labels used

| Label | Meaning |
|---|---|
| **Verified public** | Observed through the live public page, GitHub metadata, or connected GitHub repository content during this pass. |
| **Repository claim** | Stated by a repository README. It may be accurate, but should be checked against current code/demo before being repeated externally. |
| **User-supplied team evidence** | Present in supplied private/team project material; not public evidence. |
| **Resume-supported** | Present in résumé/career material; should be reconciled with public channels where relevant. |
| **Needs confirmation** | Contradictory, inaccessible, stale, or not independently verified. |
| **Blocker before feature** | A credibility/security/licensing issue that should be resolved before a project becomes a flagship. |

### What this audit is not

This is not:

- a full code audit;
- a penetration test;
- a secret scan;
- a license legal opinion;
- proof that every README feature works;
- proof of deployment quality;
- permission to publish private team material.

---

## 3. Repository-count discrepancy

The connected GitHub inventory currently exposes **24 repositories with public visibility** under the account. A signed-out profile rendering observed during this research pass displayed **23 repositories**.

Do not silently normalize this difference. Before implementation, recheck:

- signed-out profile;
- repository tab;
- visibility of each candidate;
- whether a recently changed repo is indexed/rendered differently.

The public README should not contain a numeric “I have N repositories” claim.

---

## 4. Priority ranking

### 4.1 Heuristic evidence score

This is a portfolio-selection heuristic, not an objective measure of engineering quality.

Scoring dimensions, each 0–5:

- **Role relevance** — fit for AI Engineer / agentic / voice / backend roles
- **Systems depth** — architecture, state, failure handling, boundaries
- **Public evidence** — accessible code/docs/demo
- **Documentation** — clarity, setup, limits, tests
- **Recruiter readiness** — can a reviewer understand it quickly and trust the presentation?

| Project | Relevance | Systems | Public evidence | Docs | Recruiter readiness | Total /25 | Recommended role |
|---|---:|---:|---:|---:|---:|---:|---|
| **OryxenAI** | 5 | 5 | 5 | 5 | 5 | **25** | flagship #1 |
| **QuotaMesh** | 5 | 5 | 5 | 5 | 4 | **24** | flagship #2 |
| **AI Receptionist** | 5 | 5 | 1 | 5 | 3 | **19** | narrative #3; private team work |
| **MediFindX0** | 4 | 3 | 4 | 4 | 3 | **18** | applied AI breadth |
| **BlogerVoger** | 2 | 3 | 3 | 4 | 3 | **15** | full-stack breadth |
| **YASHODA** | 1 | 3 | 4 | 4 | 2 | **14** | visual/product breadth after cleanup |
| **Ai-Portfolio** | 3 | 3 | 3 | 4 | 4 | **17** | primary website, not necessary as pin |

Why AI Receptionist scores lower on public evidence: the supplied repository is private/team-owned. Its technical signal is high, but a recruiter cannot independently inspect it from the public profile unless the team later authorizes a public case study or repository.

---

## 5. Recommended public story

### Owned systems

1. **OryxenAI** — product + agent workflow + backend/state + delivery.
2. **QuotaMesh** — routing + policy + failure handling + local AI infrastructure.

### Team / current build

3. **AI Receptionist** — voice AI, full-duplex audio, tools, calendar, safety backstops, multi-tenant configuration.

### Supporting breadth

4. **MediFindX0** — applied multimodal AI.
5. **BlogerVoger** — full-stack publishing product.
6. **YASHODA** — UI/product engineering only after its demo is clearly presented as a demo.

### Collaboration signal

7. **Public open-source contributions** — add only when there is a meaningful public contribution record.

This hierarchy is stronger than presenting every repository with equal weight.

---

## 6. Deep review — OryxenAI

**Repository:** https://github.com/yashsrivastava0/OryxenAI  
**Demo:** https://app.oryxenai.me/  
**Observed language:** Python  
**Priority:** **#1**

### Audience-facing description

The current README presents OryxenAI as:

> an AI-assisted portfolio workspace with memory, review points, and a private Studio.

It frames the product around turning fragmented background material into approved context, approved content, and a validated page version rather than around a generic “AI website generator.”

### Strong evidence

The README currently documents:

- Explorer Agent → Content Architect → Studio progression;
- explicit user approvals between stages;
- persistent artifacts such as briefs, content plans, page versions, and validation records;
- Preact/TypeScript/Vite frontend;
- Python/FastAPI/Pydantic backend;
- PostgreSQL/JSONB/async SQLAlchemy/Alembic persistence;
- durable background job behavior;
- owner-scoped sessions and versioning;
- testing across Pytest, Vitest, Playwright, Ruff, and mypy;
- Docker, GitHub Actions, and Render configuration;
- private preview isolation/security boundaries;
- a clear current limitation: public portfolio publishing/export is not implemented.

### Demo check

The app resolved during this research pass and showed the authenticated/private workspace flow plus clearly labeled fictional samples.

This is good recruiter evidence because the live page is consistent with the README’s “private Studio” boundary rather than pretending to be a fully open publishing network.

### README strengths

- strong problem framing;
- product and engineering both visible;
- meaningful diagrams;
- current limitations disclosed;
- architecture is described in terms of responsibility rather than a badge wall;
- “what is available today” is separated from future capability.

### README gaps / next checks

Before making it the profile’s main external proof:

1. confirm what a signed-out recruiter can inspect without admission;
2. make sure the opening 20–30 seconds of the demo are useful even if signup is restricted;
3. verify repository About description, topics, homepage, and license;
4. verify that screenshots/hero assets still match the current product;
5. check that no internal/private example data appears in screenshots;
6. avoid exposing internal run metrics or customer/employer material.

### Visual recommendation

Keep the current custom hero style and add 1–2 real, current product screenshots if they are safe. Do not replace the README with generic shields.

### Pin candidacy

**Definite #1** after final verification.

### Recruiter one-liner

> AI-assisted portfolio workspace that turns approved user context into reviewable content and validated private portfolio versions.

---

## 7. Deep review — QuotaMesh

**Repository:** https://github.com/yashsrivastava0/QuotaMesh  
**Hosted demo:** none identified; project provides local/demo behavior  
**Priority:** **#2**  
**Current stage:** repository describes it as **alpha**

### Audience-facing description

The README now describes a local AI API capacity gateway that accepts OpenAI-compatible traffic and routes it across authorized, user-configured provider access.

### Strong evidence

Current README material includes:

- authenticated localhost Chat Completions gateway;
- deterministic target ordering and fallback;
- shared cooldown state;
- plan/expiry/paid-use controls;
- FREE / TRIAL / PAID capacity grouping;
- named project profiles;
- local durable usage/history;
- explicit rule that prompts/responses are not saved in metadata-only history;
- streaming commitment semantics;
- handling for 429s, billing/auth failures, network failures, and model access;
- paid caps;
- local/demo mode;
- tests, docs, roadmap, contributing information.

The README explicitly says QuotaMesh does **not** create provider capacity, bypass limits, or make paid calls free. That boundary should stay visible.

### Why this project matters

QuotaMesh is an excellent complement to OryxenAI because it proves engineering judgment around:

- policy;
- failure states;
- deterministic routing;
- shared state;
- streaming edge cases;
- cost controls;
- local security boundaries.

### Gaps / next checks

1. verify quick-start in a clean environment;
2. verify loopback-only/security behavior matches the README;
3. verify supported providers/models and phase status;
4. verify license file;
5. ensure the product specification PDF has no internal/private material before linking it prominently;
6. consider one architecture screenshot or terminal/demo capture that explains routing without requiring a reviewer to install the tool first.

### Pin candidacy

**Definite #2.**

### Recruiter one-liner

> Alpha local AI API gateway for routing authorized OpenAI-compatible traffic with deterministic fallback, shared cooldowns, and explicit paid-use controls.

---

## 8. Special review — AI Receptionist (private team project)

**Repository owner in supplied evidence:** `VIDHIGUPTA17`  
**Repository:** private in the supplied page  
**User relationship:** supplied evidence shows `yashsrivastava0` contributing to the repository  
**Priority:** **#3 in the professional narrative, not currently a public pin**

### What the supplied project material supports

The README describes **Pine & Peak — AI Voice Receptionist**, a real-time HVAC intake/scheduling agent using:

- Python 3.11+
- FastAPI
- Google Gemini Live
- WebSockets
- full-duplex audio streaming
- tool calling
- Google Calendar scheduling
- deterministic safety/emergency backstops
- prompt-injection filtering
- multi-tenant YAML configuration
- browser microphone/speaker test client

The README lists seven business tools for:

- service-area checks;
- customer lookup;
- intake fact recording;
- appointment searches;
- booking;
- callbacks;
- staff transfers.

It also describes an idempotency mechanism around booking and a deterministic lockout when emergency conditions are detected.

The current roadmap says browser/Gemini Live is Phase 1; telephony integration is planned for Phase 2; distributed persistence/integrations are later.

### Why it is high-value evidence

This project proves a different capability from the first two:

| Project | Primary signal |
|---|---|
| OryxenAI | product + agent workflow + durable application |
| QuotaMesh | AI infrastructure + routing + failure semantics |
| AI Receptionist | real-time voice + tools + safety + scheduling |

Together they form a coherent “production AI systems” story.

### Public-presence treatment

**Recommended wording:**

> **AI Voice Receptionist — team project**  
> Real-time HVAC intake and scheduling agent using Gemini Live, FastAPI, tool calling, deterministic safety backstops, and calendar workflows.

Do not publish:

- private repo link;
- private business policies;
- credentials;
- customer records;
- internal architecture that the team does not approve;
- private commit/branch details;
- claims of sole ownership.

### Pin candidacy

**Not now** because the supplied repository is private.

GitHub’s profile reference permits pinning a public repository you own or have contributed to recently. If the team later makes this repository public and contribution eligibility is satisfied, it becomes a strong pin candidate.

### Best future option

With team/business approval, create a **sanitized public case study** or project page describing:

- problem;
- role;
- high-level architecture;
- safety design;
- tool flow;
- test strategy;
- what was implemented vs planned.

That would provide recruiter evidence without exposing the private repository.

---

## 9. Deep review — MediFindX0

**Repository:** https://github.com/yashsrivastava0/MediFindX0  
**Demo:** https://huggingface.co/spaces/PromptYASH/Medifindx  
**Observed demo status during research:** Hugging Face page resolved and displayed “Running on Zero.”  
**Priority:** supporting AI project

### Current README story

The README presents MediFindX as an educational medicine/symptom information assistant with:

- text input;
- image input;
- voice input;
- pharmacy URL input;
- grounded sources including RxNorm and openFDA;
- report generation;
- map;
- inline follow-up chat;
- PDF export.

It includes an educational-use disclaimer.

### Strengths

- applied AI;
- multimodal inputs;
- public demo;
- source-grounding concept;
- tests;
- clear quick start.

### Credibility / safety gaps

The README currently includes language such as “AI recommends medicines with rationale” in symptom mode. For a recruiter profile, do not amplify this. The public profile should describe it as an **educational health-information assistant**, not as a diagnostic system, prescribing system, doctor, or clinical decision tool.

The older résumé/portfolio material mentions a **nine-agent** architecture, while the inspected public README does not establish that number as a meaningful current architecture fact. Do not use “9-agent” on GitHub until code/current docs substantiate it.

Also verify:

- current model names/limits;
- each input mode;
- report behavior;
- demo uptime;
- license;
- whether old portfolio descriptions still match.

### Pin candidacy

Good #4 candidate if the demo remains usable and the health framing is tightened.

### Recruiter one-liner

> Educational multimodal health-information assistant using grounded public sources across text, image, and voice workflows.

---

## 10. Deep review — BlogerVoger

**Repository:** https://github.com/yashsrivastava0/BlogerVoger  
**Homepage in project metadata:** `https://bloger-voger.vercel.app`  
**Crawler result during this pass:** page content was not retrievable; treat deployment as **not verified**, not necessarily broken.  
**Priority:** full-stack breadth

### Current README story

The README calls it a modern full-stack publishing platform and explicitly notes that it began as a 2024 academic assignment and has since been modernized.

Documented stack includes:

- React 18
- Vite
- Tailwind
- Framer Motion
- Node.js / Express
- JWT / bcrypt
- MongoDB / Mongoose
- Cloudinary
- React Quill

Features include authoring, search/filtering, profiles/admin, comments/likes, and local client persistence.

### Strengths

- honest project-origin note;
- broad end-user feature set;
- full-stack structure;
- recognizable publishing problem;
- current README is much clearer than an unstructured student repo.

### Gaps

1. verify live deployment manually;
2. verify the README’s backend/database claims against current code after redesign;
3. clarify when local persistence is used vs MongoDB;
4. verify a root `LICENSE` exists because the README says “MIT — see LICENSE”;
5. make sure `.env.example` contains placeholders only;
6. use current screenshots rather than generic stock imagery;
7. keep it lower than AI projects on an AI-engineer profile.

### Pin candidacy

Conditional #5.

---

## 11. Deep review — YASHODA

**Repository:** https://github.com/yashsrivastava0/YASHODA  
**Demo:** https://v0-yashoda.vercel.app/  
**Demo status:** resolved successfully during this research pass.  
**Priority:** frontend/product breadth after credibility cleanup

### Current README story

A “considered marketplace” across fashion, electronics, home decor, and skincare, implemented with:

- Next.js 16
- React 19
- TypeScript
- MongoDB
- JWT/bcrypt auth
- cart flows
- admin/customer routes
- Vercel deployment
- demo catalog fallback

The README describes a calm editorial interface and includes security/performance notes.

### Major credibility issue found in live demo

The live homepage currently displays business-like claims including:

- “50K+ members”
- “4.9/5 average customer rating”
- “24h dispatch”
- “30 day easy returns”

If these are fictional/sample/demo values, a recruiter or engineering manager has no way to know that from the headline presentation. That can undermine trust in the rest of the portfolio.

**Recommendation before featuring YASHODA prominently:** make any simulated metrics and commerce promises obviously demonstrative, or remove them. Do not leave portfolio mock data looking like real company traction.

### License/presentation issue

The README says:

> Private project. All rights reserved.

The repository itself is public. Public visibility does not automatically grant an open-source license, so this is not legally impossible; however, the presentation is confusing.

Clarify the intended public status:

- public source showcase, all rights reserved;
- open-source project with an actual license;
- or private/commercial code that should not be public.

Do not call YASHODA open source unless a suitable license actually grants those rights.

### Pin candidacy

Not a top-five recommendation until the demo claims and public/license intent are cleaned up.

---

## 12. Deep review — Ai-Portfolio

**Repository:** https://github.com/yashsrivastava0/Ai-Portfolio  
**Repository homepage / suggested portfolio:** https://yashdev.ai.studio/  
**Crawler result:** repository is public; the `yashdev.ai.studio` page itself returned empty crawler content during this pass, so manual browser verification is still required.  
**Priority:** website destination and design source, not necessarily a pin

### Current README story

The repo describes an “Autonomous Editorial Portfolio & Companion Engine” with:

- React 19
- TypeScript
- Tailwind CSS 4
- Vite
- Express
- server-side Gemini proxy
- custom popstate router
- procedural SVG sidekick
- section-aware gestures
- inactivity state
- cursor proximity behavior
- native speech synthesis
- telemetry / scroll-depth behavior

### Visual value

This repository contains the most useful source material for GitHub-profile art direction:

- warm editorial eggshell;
- deep ink;
- cyan active accent;
- amber state accent;
- crimson high-priority accent;
- structured Swiss/editorial layout;
- “zero-pill” discipline;
- animated companion behavior.

### Recommendation

Use the portfolio’s **visual logic**, not its full interactive complexity, in the GitHub profile.

GitHub should borrow:

- palette;
- strong typography;
- line/grid discipline;
- custom original SVG language;
- one restrained motion cue.

GitHub should **not** try to recreate:

- cursor-aware companion;
- inactivity behavior;
- speech synthesis;
- runtime AI chat;
- scroll telemetry.

Those features belong on the website.

### Canonical-link recommendation

Per the requested direction, use `yashdev.ai.studio` as the **suggested primary** portfolio URL, but complete a manual browser check before the actual GitHub field is changed.

The old Vercel portfolio remains useful for comparison but appears to carry older positioning and aggressive experience/project claims. It should not remain the canonical link once the newer site is confirmed ready.

### Pin candidacy

Usually **no**. The website field already links to the portfolio, and a pin slot is more valuable for a technical system.

---

## 13. Inventory of 24 public repositories

This inventory reflects the connected GitHub visibility results during the research pass. Do not infer quality solely from size or recency.

### Flagship / detailed-review group

| Repository | Recommended treatment |
|---|---|
| `OryxenAI` | flagship #1 |
| `QuotaMesh` | flagship #2 |
| `MediFindX0` | applied AI / possible pin |
| `BlogerVoger` | full-stack breadth / conditional pin |
| `YASHODA` | product/UI breadth after demo credibility cleanup |
| `Ai-Portfolio` | website source / design system; generally not a pin |

### Lower-priority / needs-review index

| Repository | Current treatment recommendation |
|---|---|
| `Blogger` | older/parallel blogging project; compare against BlogerVoger before surfacing |
| `Gaming-library` | inspect nested implementation and current relevance before any claim |
| `Portfolio` | older portfolio-like repository; avoid duplicating Ai-Portfolio |
| `Web-Scraping-Project` | review code, data-source terms, and current legality/terms compliance before featuring |
| `AI-Yash-Portfolio` | currently empty; do not feature or pin |
| `yash-backend` | currently minimal/empty-looking; do not feature without a distinct purpose |
| `assi` | small app; inspect purpose and current behavior |
| `oauth` | public hygiene review required because a root `.env` filename was previously observed |
| `Intern-UI` | inspect nested project and whether it demonstrates current-level work |
| `Bazinga` | older clone-style project; inspect logs/scripts and current demo before use |
| `login-page` | small/older UI project; not flagship material |
| `Tokenzi` | minimal/README-only or near-empty in prior inspection; review before any use |
| `harmonic-` | empty/minimal in current metadata; do not feature |
| `insyd-notifications` | potentially substantive, but inspect `proof.txt`, purpose, and current status before use |
| `C-T-MUX-agent` | empty/minimal in current metadata; do not infer purpose |
| `algox` | potentially substantive full-stack structure; inspect current README/demo before ranking |
| `prodigy-info-tech` | internship/assignment-style work; lower-priority unless a specific project is exceptional |
| `password` | small Go project; do not describe as a secure password generator without reviewing randomness/security |

The profile README should not contain this full inventory. It exists to stop old experiments from competing with the strongest current work.

---

## 14. Public security and hygiene findings

### 14.1 `oauth` — root `.env` filename observed

A public repository was previously observed with a root `.env` filename. This does **not** prove that a real credential is inside, and this research pass intentionally does not expose or quote any value.

A separate authorized security pass should:

1. inspect the file safely;
2. determine whether any value is live/secret;
3. if a secret was exposed, revoke/rotate it **before** thinking about history cleanup;
4. replace committed runtime secrets with example placeholders;
5. add runtime `.env` to `.gitignore`;
6. inspect commit history only after rotation;
7. avoid pasting any secret into issues, chat, README, or logs.

GitHub guidance:

- https://docs.github.com/en/code-security/tutorials/remediate-leaked-secrets/remediating-a-leaked-secret
- https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository

### 14.2 Other hygiene checks

Before drawing recruiter attention to a repo:

- verify all `.env.example` files contain placeholders only;
- inspect `Bazinga` logs and `generate_commits.sh` for public usefulness;
- inspect `insyd-notifications/proof.txt` for private or irrelevant content;
- make sure README license claims match an actual license file / owner intent;
- check dependency and CI status on flagships;
- remove development artifacts only after understanding them; do not blindly delete;
- never turn private work public merely to improve a portfolio.

---

## 15. Demo/status matrix

| Project | Public artifact | Research-pass result | Profile treatment |
|---|---|---|---|
| OryxenAI | `app.oryxenai.me` | resolved; authenticated/private workspace and samples visible | feature |
| QuotaMesh | local demo / repo | no hosted demo identified | feature as local developer tool |
| AI Receptionist | private team repo | supplied private evidence only | describe at high level; no public link |
| MediFindX0 | Hugging Face Space | resolved; “Running on Zero” page visible | good supporting demo |
| BlogerVoger | Vercel | crawler returned no content | manual verification required |
| YASHODA | Vercel | resolved | fix/label demo claims before flagship use |
| Ai-Portfolio | `yashdev.ai.studio` | crawler returned empty content | manually verify before canonical switch |
| Old portfolio | Vercel | resolved | comparison only; appears stale vs intended new site |

A crawler failure is **not** proof that a site is down. The browser-control implementation pass should manually open each unresolved URL.

---

## 16. Portfolio-site comparison

### Suggested primary

`https://yashdev.ai.studio/`

Reason:

- user explicitly selected it as the suggested primary;
- `Ai-Portfolio` is the newer portfolio repository;
- its design language better matches the desired editorial + advanced identity.

### Existing GitHub website

`https://v0-yash-srivastava-portfolio-vl.vercel.app/`

The old site was retrievable and contains:

- “AI & Agentic LLM Engineer” positioning;
- older experience presentation;
- 9-agent MediFindX claims;
- ParserAI and YashAI;
- several strong quantified impact claims;
- a broader skill/tool list.

### Recommendation

Do not copy old-site claims into the new GitHub README automatically.

Before retiring it as the primary GitHub link:

1. verify `yashdev.ai.studio` manually;
2. ensure project links work;
3. resolve employment dates and education;
4. compare certification lists;
5. remove or substantiate old quantified impact claims;
6. make sure the new site reflects OryxenAI, QuotaMesh, and current voice-AI work in the correct priority.

---

## 17. LinkedIn alignment checklist

The current public LinkedIn search result is directionally aligned with the target story: AI/Agentic LLM engineering and Xpression are visible. It also currently surfaces BBD Institute of Technology and Management as education and several certifications.

Do not treat this as a license to overwrite LinkedIn. Use it to identify conflicts.

### Must align later

- headline / role wording;
- current company spelling;
- current job title;
- JUTEQ dates;
- education institution/university relationship;
- canonical portfolio;
- OryxenAI name/summary;
- QuotaMesh status;
- AI Receptionist team/private framing;
- certifications;
- featured links.

### Certifications review

The older audit classified some certifications as portfolio-only. The current public LinkedIn search snapshot now surfaces certifications including:

- RAG-focused Udemy material;
- AWS AI Practitioner;
- LLM Engineering;
- OpenAI API fine-tuning material.

This does **not** resolve the discrepancy automatically. Confirm exact certificate:

- title;
- issuer;
- date;
- credential URL/ID if used publicly;
- whether it belongs on résumé, LinkedIn, portfolio, or nowhere.

Do not copy a certification merely because it appears on one stale channel.

---

## 18. Contradiction and relation map

| Topic | Evidence A | Evidence B | Treatment |
|---|---|---|---|
| Company spelling | GitHub: `EXPERSSION` | LinkedIn/other material: Xpression | verify official brand, then normalize |
| JUTEQ dates | résumé: Jul–Oct 2025 | newer portfolio audit: Jul–Oct 2024 | **needs confirmation** |
| Education | résumé/new portfolio: AKTU relationship | LinkedIn: BBD Institute of Technology and Management | express institution + university accurately or omit |
| Portfolio URL | GitHub: old Vercel | user-selected suggested primary: `yashdev.ai.studio` | verify new site, then prefer it |
| OryxenAI scope | portfolio-generation product | README says private Studio; public publish/export not implemented | use README boundary |
| QuotaMesh maturity | strong system features | README says alpha | keep alpha |
| AI Receptionist ownership | strong contribution evidence | repository is private and team-owned | say “team project,” not “my open-source repo” |
| MediFindX architecture | old material says nine agents | public README does not establish that count | omit count until verified |
| MediFindX health behavior | README includes medicine recommendation wording | public profile should avoid clinical/diagnostic framing | use educational-information wording |
| YASHODA scale claims | live demo shows 50K+/4.9/5/etc. | portfolio/demo context does not establish real business | label/remove sample claims before featuring |
| Certifications | different channel inventories | current LinkedIn now surfaces several certs | reconcile item by item |
| Contact | résumé includes direct details | public profile does not need them | keep private by default |

---

## 19. Advanced public-presence strategy

The profile should establish a **three-layer evidence ladder**.

### Layer 1 — owned, inspectable systems

- OryxenAI
- QuotaMesh

This proves “I can build and own a system.”

### Layer 2 — team production-style collaboration

- AI Receptionist

This proves “I can work in a team on current, real-time AI engineering,” but only at the level the team permits publicly.

### Layer 3 — public ecosystem collaboration

- future merged open-source contributions

This proves “I can work with maintainers and code I do not control.”

This is more credible for hiring than six personal demos with similar stacks.

---

## 20. Open-source contribution roadmap

This roadmap is a recommendation, not a current claim.

### Stage 1 — contribution discovery

Pick 3–5 active repositories that overlap with actual work:

- FastAPI/Pydantic ecosystem;
- agent orchestration / LangGraph;
- MCP SDK/tooling;
- voice/audio tooling;
- provider SDKs;
- AI eval/observability;
- small AI developer tools with active maintainers.

### Stage 2 — choose high-probability work

Prefer:

- reproducible bugs;
- missing tests;
- docs that accompany code behavior;
- type/schema bugs;
- error handling;
- async/concurrency edge cases;
- small developer-experience improvements.

Avoid starting with a giant feature proposal.

### Stage 3 — build public evidence

For each meaningful merged PR, record:

- issue/problem;
- what changed;
- tests;
- maintainer feedback;
- PR link.

### Stage 4 — profile integration

Once there is a strong contribution, add it to:

- profile README “Open Source & Collaboration”;
- pins if the repository is eligible and relevant;
- LinkedIn Featured only if useful.

Do not manufacture contribution activity or use commit scripts to simulate consistency.

---

## 21. Repository README standard for featured work

Every featured repo should answer these quickly:

1. **What problem does this solve?**
2. **Who is it for?**
3. **What is implemented now?**
4. **What is planned/not implemented?**
5. **How does it work at a high level?**
6. **How can I run it?**
7. **How can I test it?**
8. **Is there a real demo?**
9. **What data/keys/services are required?**
10. **What license applies?**

Recommended opening sequence:

```text
Name
One-line problem statement
Live demo / quick start / docs
1 screenshot or architecture visual
What it does
How it works
Current boundaries
Quick start
Tests
Architecture / deeper docs
License
```

Do not force every repository into identical visual branding. Keep project identity while maintaining equivalent information quality.

---

## 22. Visual assets by project

### OryxenAI

Use:

- current hero;
- one current product screenshot;
- one workflow/architecture diagram.

Avoid:

- overdecorating a README that is already detailed.

### QuotaMesh

Use:

- one capacity/routing diagram;
- one dashboard/terminal demo image;
- optional short GIF showing deterministic fallback.

### AI Receptionist

Only with team approval:

- sanitized architecture diagram;
- no customer data;
- no internal policy pages;
- no real phone numbers;
- no credentials;
- no private repo paths that reveal protected context.

### MediFindX0

Use:

- current app screenshot;
- grounding/data-source diagram;
- educational disclaimer visible.

### BlogerVoger

Use:

- real current UI screenshots;
- no stock mockups that imply functionality not in the code.

### YASHODA

Use:

- UI screenshots only after sample/fictional metrics are clearly labeled.

---

## 23. What should not be promoted

Do not build the professional story around:

- empty repos;
- login pages;
- assignment repos;
- clone projects;
- raw commit counts;
- star counts with little context;
- visitor counters;
- “top language” percentages;
- fabricated streaks;
- generated commit scripts;
- unsupported business metrics;
- private-team code presented as personal ownership.

The hiring signal should come from **complexity handled clearly**, not from quantity.

---

## 24. Recommended pin decision gate

A repository gets pinned only if all are true:

- public and pin-eligible;
- relevant to target AI/backend roles;
- README understandable in under two minutes;
- status/limitations honest;
- no known secret-hygiene issue;
- demo either works or is clearly absent/local;
- license intent clear;
- screenshots contain no private data;
- project is materially distinct from the other pins.

If a candidate fails two or more gates, leave the slot empty rather than filling it for visual symmetry.

---

## 25. Browser-control research handoff

When the future browser-control implementation pass begins, verify in this order:

### Profile

- profile README repo exists / does not exist;
- current fields;
- current pin order;
- signed-out profile rendering;
- repository-count discrepancy.

### Top projects

- OryxenAI app signed-out experience;
- QuotaMesh README/quick-start;
- MediFindX Hugging Face demo;
- BlogerVoger deployment;
- YASHODA demo labeling;
- Ai-Portfolio / `yashdev.ai.studio`.

### Facts

- Xpression spelling;
- current title;
- JUTEQ dates;
- education;
- certifications.

### Safety

- root `.env` concern;
- license files;
- private/team AI Receptionist boundaries.

Only after those checks should a separate authorized pass change GitHub.

---

## 26. Final recommendation

For hiring in Europe and Asia, the profile should stop looking like a collection of unrelated repositories and start reading like an **AI systems portfolio**.

The desired narrative is:

> **Yash builds production-oriented AI systems.**  
> OryxenAI shows product and agent orchestration.  
> QuotaMesh shows infrastructure, routing, and reliability.  
> AI Receptionist shows real-time voice, tools, safety, and team delivery.  
> Public open-source contributions show collaboration outside code he owns.

Everything else should support that narrative, not compete with it.

---

## 27. Research references

### GitHub official

- https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme
- https://docs.github.com/en/account-and-profile/tutorials/using-your-github-profile-to-enhance-your-resume
- https://docs.github.com/en/account-and-profile/reference/profile-reference
- https://docs.github.com/en/account-and-profile/concepts/personal-profile
- https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes
- https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories
- https://docs.github.com/en/code-security/tutorials/remediate-leaked-secrets/remediating-a-leaked-secret
- https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository

### Profile patterns / dynamic assets

- https://github.com/abhisheknaiidu/awesome-github-profile-readme
- https://github.com/Platane/snk
- https://github.com/stats-organization/github-stats-extended
- https://github.com/stats-organization/github-readme-stats-action
- https://github.com/DenverCoder1/readme-typing-svg
- https://github.com/BerkaySevinc/easy-github-profile
- https://github.com/anuraghazra/github-readme-stats

### Public project evidence

- https://github.com/yashsrivastava0/OryxenAI
- https://app.oryxenai.me/
- https://github.com/yashsrivastava0/QuotaMesh
- https://github.com/yashsrivastava0/MediFindX0
- https://huggingface.co/spaces/PromptYASH/Medifindx
- https://github.com/yashsrivastava0/BlogerVoger
- https://github.com/yashsrivastava0/YASHODA
- https://v0-yashoda.vercel.app/
- https://github.com/yashsrivastava0/Ai-Portfolio
- https://yashdev.ai.studio/
- https://v0-yash-srivastava-portfolio-vl.vercel.app/

The private/team AI Receptionist analysis in this document comes from the user-supplied repository evidence and is intentionally not linked publicly.
