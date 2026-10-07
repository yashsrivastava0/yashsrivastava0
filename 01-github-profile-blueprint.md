# GitHub Profile Blueprint — Recruiter-First, AI-Engineer, Distinctive

**Status:** Research and recommendation package only. No GitHub, repository, LinkedIn, portfolio, or deployment changes are authorized by this document.  
**Research date:** 2026-10-06  
**Target profile:** `yashsrivastava0`  
**Primary audience:** AI/ML engineering recruiters, engineering managers, founders, and senior engineers in Europe and Asia; secondary audience: open-source maintainers and technical collaborators.

---

## 1. Executive recommendation

The profile should communicate one idea immediately:

> **AI Engineer building production-oriented agentic systems, voice AI, and reliable AI infrastructure.**

The best profile for this target is **not** the most animated GitHub profile. It is the profile that gives a recruiter a strong answer to “Who is this engineer, and what has he actually built?” in roughly ten seconds, then gives an engineer enough evidence to inspect the work in one or two minutes.

GitHub’s own job-search guidance recommends a concise professional profile, a profile README, and **3–5 pinned projects** chosen for relevance and breadth. It explicitly notes that hiring managers may spend only a couple of minutes looking at projects, so the selected repositories should be easy to understand and explore. It also recommends including both projects you own and projects you have contributed to where possible.

**Recommended design principle:** **professional signal first, memorable identity second, decoration third.**

For this profile, that means:

1. **OryxenAI first** — strongest owned AI product and the best proof of product + backend + agentic engineering.
2. **QuotaMesh second** — strongest systems/infrastructure proof.
3. **AI Receptionist third in narrative priority** — strong current voice-AI/team-work evidence, but it is private/team-owned, so it should not be presented as an owned or open-source repository.
4. **One genuine public open-source contribution** should eventually occupy a prominent position once there is a meaningful merged contribution that can be linked.
5. **MediFindX0 / BlogerVoger** can provide additional breadth; YASHODA should be treated cautiously until its demo marketing claims are made clearly demonstrative rather than real-business claims.
6. Use **one original visual system** and **at most one optional animated element**. Do not stack multiple third-party widgets.

The existing draft was already directionally strong in prioritizing concise positioning, a small project set, restrained motion, and accessibility. The main upgrades from this research pass are:

- make the current **AI Receptionist** a top-three narrative project;
- make **open-source collaboration** a dedicated profile signal rather than a future afterthought;
- replace the old `github-readme-stats` recommendation with the maintained **GitHub Stats Extended / GitHub Action** path if a stats card is used at all;
- sharpen the visual identity into an original **silver-flow + editorial ink** system that can evoke the calm intensity of Ultra Instinct and the motion discipline of anime sword/brush aesthetics without copying protected characters or artwork;
- keep interactive/speaking experiences on the portfolio or project demo, because a GitHub README is not an application runtime.

---

## 2. Evidence model

Use these labels while implementing the profile later:

| Label | Meaning |
|---|---|
| **Verified public** | Observed in the current public GitHub, repository, demo, LinkedIn, or official project documentation during this research pass. |
| **Repository claim** | Described by a project README or repository metadata; should be rechecked before being repeated as a public profile claim. |
| **Resume-supported** | Supported by the user’s résumé or supplied career materials but not necessarily independently public. |
| **User-prioritized** | A priority or preference explicitly supplied for this profile project. |
| **Needs confirmation** | Conflicting, stale, inaccessible, or not yet substantiated. |
| **Do not publish by default** | Direct contact details, credentials/secrets, employer-internal details, private customer information, or unsupported metrics. |

A repository README is useful evidence of how the project describes itself, but it is not independent proof that every feature, benchmark, deployment, user count, or performance claim is currently true.

---

## 3. Current-profile audit

### 3.1 High-signal findings

The current public GitHub profile has a **professional identity gap at the top of the page**: no visible profile README was observed, so the profile begins with GitHub’s standard profile surface and pinned repositories instead of a concise AI-engineer narrative.

The inspected public profile currently shows:

- Display name: **Yash Srivastava**
- Username: **`yashsrivastava0`**
- Company field: **`EXPERSSION`**
- Location: **India**
- Website: the older Vercel portfolio URL
- LinkedIn and X links
- Existing pins:
  1. `AI-Yash-Portfolio`
  2. `BlogerVoger`
  3. `OryxenAI`
  4. `QuotaMesh`
- `AI-Yash-Portfolio` is currently empty and is therefore a weak first impression.
- No public `yashsrivastava0/yashsrivastava0` profile repository was found in the inspected public repository set.

### 3.2 Repository-count discrepancy to preserve

There is a current evidence discrepancy that should **not** be silently resolved:

- the connected GitHub repository inventory exposed **24 repositories with public visibility**;
- the signed-out profile rendering observed during this research pass displayed **23 repositories**.

Possible causes include indexing, profile rendering, filtering, or a recent visibility/state change. The implementation agent should recheck the live profile immediately before any update and record the count it sees. The count itself should not be written into the README.

### 3.3 Current pin problem

The current order does not tell the strongest story:

- an empty repository appears first;
- the strongest AI project, OryxenAI, is third;
- QuotaMesh is fourth;
- the profile does not surface the current voice-AI project or a distinct open-source contribution story.

**Recommended correction later:** remove the empty project from the featured set and make the first two pins unmistakably AI/product engineering.

---

## 4. Recruiter-facing positioning

### 4.1 Positioning hierarchy

The profile should position Yash primarily as an **AI Engineer**, not as a general “developer who also uses AI.”

Recommended hierarchy:

1. **AI Engineer**
2. **Agentic / multi-agent systems**
3. **Voice AI / real-time agents**
4. **RAG, context, memory, tool use**
5. **Backend and systems engineering**
6. **Production delivery: Python, FastAPI, PostgreSQL, Docker, AWS**
7. Full-stack/UI work only as supporting breadth

This avoids an over-broad “everything engineer” profile while still showing that the work reaches production surfaces.

### 4.2 Recommended headline options

Use one, not several stacked titles.

**Default:**

> **AI Engineer · Agentic Systems · Voice AI · Production AI**

**More systems-oriented:**

> **AI Engineer building agentic systems, voice AI, and reliable AI infrastructure**

**More product-oriented:**

> **AI Engineer building practical AI products from orchestration to production**

Do not use “expert,” “visionary,” “world-class,” “10x,” or similar self-ranking language.

### 4.3 Recommended one-sentence introduction

> I build production-oriented AI systems across agents, voice, retrieval, context, tools, and dependable backend infrastructure.

A second sentence may add product orientation:

> My work focuses on turning model capability into systems that can be reviewed, tested, recovered, and operated.

This is stronger than a long list of frameworks because it describes engineering behavior rather than only tool familiarity.

### 4.4 Europe / Asia job-search signal

If the user wants this publicly visible, a short status line can be useful:

> **Open to AI Engineering opportunities across Europe, Asia, and remote teams.**

Only publish this if location, relocation, time-zone, and work-authorization implications are acceptable. Do **not** imply visa sponsorship eligibility or work authorization that has not been confirmed.

---

## 5. Information architecture for the profile README

The README should have two reading layers.

### Layer A — the 10-second recruiter scan

Visible before a long scroll:

1. Name
2. AI Engineer headline
3. One-sentence explanation
4. Portfolio / LinkedIn links
5. Three strongest systems
6. Optional “open to” line

### Layer B — the 90-second technical scan

Below that:

7. Selected systems with 1–2 lines each
8. Open-source / collaboration section
9. Technical focus grouped by capability
10. Compact experience snapshot
11. Optional repo-owned stats or contribution animation
12. Closing / connect

### Recommended section order

```text
Yash Srivastava
AI Engineer · Agentic Systems · Voice AI · Production AI

One-sentence positioning
Portfolio · LinkedIn

Selected Systems
1. OryxenAI
2. QuotaMesh
3. AI Receptionist — team project / private

Open Source & Collaboration
- merged public contributions, each with exact PR/repo link

Technical Focus
- AI systems
- backend / data
- engineering / delivery

Experience Snapshot
- concise role + company, only after facts are reconciled

Optional GitHub Activity Visual
- one static/repo-owned stats card OR one snake animation

Connect
```

Do not place a large animation, typing effect, badge wall, or character art before the identity and selected work.

---

## 6. Project hierarchy and profile treatment

### 6.1 OryxenAI — priority 1

**Role in profile:** flagship owned AI product.

Recommended framing:

> **OryxenAI** — an AI-assisted portfolio workspace that turns approved context into reviewable content and validated private portfolio versions.

Why it is strong recruiter evidence:

- product-level problem definition;
- staged agent workflow;
- explicit human approval boundaries;
- persistent state and versioning;
- frontend + backend + database architecture;
- durable background work;
- testing and delivery infrastructure;
- explicit current product limits rather than pretending everything is complete.

Avoid calling it a public portfolio-publishing platform while public publishing/export is not implemented.

### 6.2 QuotaMesh — priority 2

**Role in profile:** AI infrastructure / systems proof.

Recommended framing:

> **QuotaMesh** — an alpha local AI API gateway for routing authorized OpenAI-compatible traffic across configured capacity with deterministic fallback, shared cooldowns, and explicit paid-use controls.

Why it complements OryxenAI:

- OryxenAI proves product and orchestration depth;
- QuotaMesh proves routing, state, failure handling, boundaries, and API/system thinking.

Keep **alpha** visible. Do not frame it as a “free AI API,” quota bypass, hosted gateway, or service that manufactures provider capacity.

### 6.3 AI Receptionist — priority 3 in narrative

**Role in profile:** current voice-AI + real-time + team collaboration proof.

The supplied project material describes a real-time HVAC voice receptionist using Gemini Live and FastAPI, with browser audio streaming, tool execution, calendar scheduling, deterministic emergency guardrails, multi-tenant configuration, and a planned telephony path.

Recommended profile framing:

> **AI Voice Receptionist — team project** — real-time HVAC intake and scheduling agent using Gemini Live, FastAPI, tool calling, deterministic safety backstops, and calendar workflows.

Important boundaries:

- It is a **private team repository** in the supplied evidence.
- Do not imply sole ownership.
- Do not call it open source.
- Do not publish private repository URLs or internal files.
- If a public case study is later desired, obtain team/business approval first and create a sanitized description that contains no customer, credential, policy, or internal-operational information.
- If it later becomes a public repository and GitHub recognizes the user’s recent contribution, it can become a pin candidate.

### 6.4 Fourth / fifth positions

Preferred order after the top three narrative items:

- **MediFindX0** — strong applied/multimodal AI signal; live Hugging Face Space currently resolves. Keep it educational and avoid medical-decision claims.
- **BlogerVoger** — useful full-stack/product breadth; verify deployment and license before featuring as live/open-source.
- **YASHODA** — visually strong product breadth but should not be a flagship until demo marketing metrics are clearly identified as sample/demo data or otherwise substantiated.
- **Ai-Portfolio** — use as the website destination, not normally a pin, because pinning the portfolio repository duplicates the website link.

---

## 7. Recommended pin strategy

GitHub’s official job-search guidance recommends **3–5 highlighted projects** and specifically suggests a mixture of projects you own and projects you contributed to where possible.

### Target pin set — after verification

| Order | Candidate | Why |
|---:|---|---|
| 1 | **OryxenAI** | strongest owned AI product; breadth + depth |
| 2 | **QuotaMesh** | AI infrastructure / reliability / systems |
| 3 | **Public open-source contribution** | collaboration evidence; use a repository with a meaningful recent contribution |
| 4 | **MediFindX0** | applied multimodal AI + live demo |
| 5 | **BlogerVoger** | full-stack/product breadth if demo/license are clean |

**AI Receptionist is third in the README narrative, but not currently a pin recommendation because the supplied repository is private.**

If the AI Receptionist later becomes public and pin-eligible, it can replace the fourth/fifth slot depending on the final hiring target.

### What to remove from the current featured set

`AI-Yash-Portfolio` should not be a pin while it is empty. An empty first pin is stronger negative evidence than having fewer pins.

---

## 8. Open-source contribution strategy

GitHub’s own job-search guidance says open-source projects can demonstrate collaboration. The goal should therefore be **credible contribution evidence**, not a decorative “open source enthusiast” badge.

### What counts as high-signal

Prefer contributions where the public record shows at least one of:

- a merged bug fix;
- a test or reliability improvement;
- documentation tied to a real technical change;
- a performance or developer-experience improvement;
- a small feature accepted by maintainers;
- a useful issue investigation followed by code or tests;
- meaningful review/discussion work on a project relevant to AI engineering.

### Good ecosystems to target

These are **contribution targets, not current claims**:

- FastAPI / Starlette / Pydantic ecosystem
- LangGraph / agent orchestration tools
- MCP tooling and SDKs
- provider SDKs used in real work
- voice/audio infrastructure libraries
- observability / eval tooling for AI systems
- smaller, active AI developer-tool repositories where a focused PR is realistically reviewable

### How to display contributions

Add a small section only after real contributions exist:

```text
Open Source & Collaboration

• project/repo — fixed X / added Y / improved Z — PR #123
• project/repo — tests/documentation for X — PR #456
```

The repository name, contribution, and exact PR link matter more than contribution-count graphics.

Do not label ordinary personal repositories as “open source” if they do not actually have a license that grants open-source rights.

---

## 9. Visual strategy: professional anime energy without fan-art risk

The user’s preference for **Goku Ultra Instinct** and **Demon Slayer** can be translated into design qualities rather than copied characters.

### Design qualities to borrow

From “Ultra Instinct” as an aesthetic idea:

- calm confidence rather than aggression;
- silver/white energy;
- controlled motion;
- high contrast;
- focused central composition;
- “power held in reserve” rather than visual noise.

From Demon-Slayer-like visual language:

- decisive brush/ink motion;
- diagonal energy;
- rhythm and negative space;
- a single vivid accent against neutral surfaces;
- elegant line work.

### Do not copy

Avoid:

- Goku’s face, hair silhouette, costume, exact aura composition, or Dragon Ball marks;
- Demon Slayer characters, Nichirin designs copied from the series, logos, uniform patterns, breathing-style graphics, or recognizable fan art;
- third-party anime GIFs;
- scraped wallpapers;
- unofficial character art in the header.

### Recommended original visual concept: **Calm Power / Silver Flow**

Use the current editorial portfolio palette as the base:

- warm paper / eggshell
- deep ink / charcoal
- one silver-white energy band
- electric cyan as the primary live accent
- a very small crimson accent for emphasis

The key visual can be an **original abstract “O / X / flow” sigil** or a broad brush-like energy stroke crossing a structured grid. It can suggest an aura or sword-motion line without representing any existing character or weapon.

### Three visual options to compare

| Option | Description | Recruiter safety | Memorability | Recommendation |
|---|---|---:|---:|---|
| **A. Editorial Core** | typography + original geometric/ink mark, no motion | 5/5 | 3.5/5 | safest |
| **B. Silver-Flow Editorial** | editorial core + original silver/cyan energy stroke + subtle animation/fallback | 4.5/5 | 5/5 | **best fit** |
| **C. Full Anime Header** | large character-like art, GIFs, effects | 2/5 | 5/5 | do not use |

Do **not** lock the final artwork during the research phase. Prototype A and B, then compare in GitHub light/dark mode and on mobile.

---

## 10. Motion and effect options

### 10.1 Best option: one repo-owned visual

A custom banner should be maintained inside the profile repository, with:

- light and dark variants;
- descriptive alt text;
- text content duplicated in normal Markdown rather than only inside the image;
- a static fallback;
- no remote runtime dependency.

GitHub supports `<picture>` with `prefers-color-scheme`, so the README can serve a light and dark asset.

### 10.2 Contribution snake

`Platane/snk` remains a reasonable optional effect. It can generate an SVG/GIF from the contribution graph using GitHub Actions and supports light/dark variants.

**Recommendation:** if used, place it **near the bottom**, not in the hero. Generate the asset into a repository-controlled branch/path so the README does not depend on a separate hosted rendering endpoint.

Use a static fallback and useful alt text.

### 10.3 GitHub stats cards

The older `anuraghazra/github-readme-stats` project now directs users to the actively maintained **GitHub Stats Extended** successor or the associated GitHub Action.

If a stats card is used:

- use **`stats-organization/github-readme-stats-action`**;
- generate a static SVG into the profile repository;
- keep at most one compact card;
- do not use rank letters as a professional claim;
- do not rely on the old public `github-readme-stats.vercel.app` service;
- remember that public data, private contributions, and cache behavior can differ.

A valid design choice is to **omit stats cards entirely** because GitHub already shows the native contribution graph and repository activity.

### 10.4 Typing SVG

`DenverCoder1/readme-typing-svg` is popular and maintained, but it adds another external rendering service unless self-hosted.

For this profile, it is not recommended as the main hero because:

- the headline should be readable instantly;
- animated typing delays information;
- external rendering introduces uptime/caching risk;
- it is a common pattern and therefore less distinctive.

If tested, use it only as a minor accent and self-host or generate a local alternative.

### 10.5 Effects to avoid

Do not stack:

- typing header;
- trophy grid;
- streak card;
- language card;
- contribution snake;
- visitor counter;
- animated character;
- multiple GIF dividers.

That makes the page look template-generated rather than senior/production-oriented.

---

## 11. “Speaking” and interactivity: what GitHub can and cannot do

A GitHub profile README is **not a website runtime**. Do not plan around embedded JavaScript, a live speech agent, Web Speech API, cursor tracking, or an interactive AI companion inside the README.

The richer portfolio repository already demonstrates a procedural companion and speech behavior. Keep those experiences on the portfolio/site.

GitHub can instead use:

- a static screenshot or lightweight preview image;
- a short GIF showing a real workflow;
- a link to the live portfolio;
- a link to a public voice-AI demo if one exists and is safe to expose;
- a `▶ Voice AI demo` link rather than pretending the README itself can talk.

This division is beneficial: **GitHub proves engineering; the portfolio demonstrates experience design.**

---

## 12. Profile field recommendations

### Name

Keep:

> **Yash Srivastava**

### Bio

Recommended default:

> **AI Engineer building agentic systems, voice AI, and reliable AI infrastructure.**

Alternative:

> **AI Engineer focused on agent workflows, voice systems, RAG, and production backends.**

### Company

Current public GitHub shows `EXPERSSION`, while other public material uses **Xpression**.

**Action later:** verify the company’s official spelling, then correct the typo. Do not publish an employer-specific internal role description in the company field.

### Location

`India` is sufficient if the user wants location public. Do not add a precise city solely for optimization.

### Website

**Suggested primary:** `https://yashdev.ai.studio/`

The current GitHub website field points to:

`https://v0-yash-srivastava-portfolio-vl.vercel.app/`

During this research pass, the old Vercel page was retrievable and contained older positioning and several strong performance claims. The `yashdev.ai.studio` site was not retrievable by the crawler in this pass, although repository metadata and user direction identify it as the intended modern portfolio.

**Before replacing the field:** manually verify `yashdev.ai.studio` in the browser, its HTTPS/canonical behavior, content, project links, and mobile view. Then use it as the primary GitHub website if correct.

### LinkedIn

Keep the current public LinkedIn link after cross-channel facts are reconciled.

### X

Keep only if the account is active and intentionally professional. It is optional and lower priority than GitHub, portfolio, and LinkedIn.

### Public email / phone

Do not add by default. GitHub, portfolio, and LinkedIn provide enough contact paths.

---

## 13. Technical-focus section

Use grouped text, not a badge per dependency.

Recommended structure:

**AI systems**
- Agentic workflows and orchestration
- Voice AI and real-time agents
- RAG, context, memory, tool use, MCP
- Structured outputs, evaluation, guardrails

**Backend and data**
- Python
- FastAPI
- PostgreSQL
- async workers / durable jobs where demonstrated

**Engineering and delivery**
- Docker
- GitHub Actions / CI
- AWS
- testing and browser verification where demonstrated

**Supporting product stack**
- TypeScript / modern frontend work only where it strengthens the selected project story

Do not include every model provider, framework, UI library, or dependency.

---

## 14. Accessibility and rendering requirements

The profile must remain useful with images disabled.

Required:

- all identity and project descriptions in real Markdown text;
- descriptive alt text;
- logical heading order;
- descriptive links, not “click here”;
- adequate light/dark contrast;
- no flashing or rapid animation;
- static fallback for motion;
- no essential information inside decorative assets;
- mobile/narrow-view check;
- signed-out browser check;
- no custom Unicode “fancy font” text;
- no secrets, tokens, private URLs, or direct customer data in SVG/GIF source or workflow logs.

For light/dark art, use GitHub’s supported `<picture>` pattern rather than assuming one background works everywhere.

---

## 15. Recruiter-readability rules

A recruiter should be able to answer these from the first screen:

1. What role does this person do?
2. What kind of AI systems does he build?
3. What are the top two things he owns?
4. Is there current production-oriented work?
5. Where is the portfolio / LinkedIn?
6. Is there evidence of collaboration/open source?

An engineer clicking a flagship repository should then be able to answer:

1. What problem does it solve?
2. What is actually implemented?
3. How does it work?
4. How do I run/test it?
5. What are the boundaries / known limitations?
6. Is the license clear?
7. Is a demo available and honest?
8. Are tests/CI visible?

---

## 16. Cross-channel consistency checklist

Before implementation, reconcile:

| Topic | Current issue | Recommendation |
|---|---|---|
| Company | GitHub shows `EXPERSSION`; other public material shows Xpression | verify official spelling, then use one spelling |
| JUTEQ dates | conflicting year in supplied materials | keep date out of GitHub README until confirmed |
| Education | AKTU vs BBD institution wording | describe university/institute relationship accurately or omit education from GitHub |
| Portfolio | old Vercel URL vs `yashdev.ai.studio` | prefer `yashdev.ai.studio` after browser verification |
| Certifications | older materials and current public profile do not perfectly align | confirm issuer/title/date for each before copying |
| OryxenAI | public publishing boundary | say private Studio / private preview unless status changes |
| QuotaMesh | alpha status | preserve alpha label |
| AI Receptionist | private/team project | label team contribution; no ownership/open-source implication |
| MediFindX | health product | educational information only; avoid clinical/diagnostic language |
| YASHODA | demo contains commerce-like traction/service claims | label/remove sample claims before featuring prominently |
| Contact | résumé may contain direct email/phone | keep private by default |

---

## 17. Suggested implementation sequence for Browser Control AI

This is a plan only; it does not authorize actions.

### Phase 0 — fact and safety gate

1. Recheck public profile fields.
2. Resolve company spelling.
3. Resolve JUTEQ date.
4. Resolve education wording.
5. Verify `yashdev.ai.studio`.
6. Review any public `.env` or possible secret exposure separately before drawing recruiter attention to those repositories.
7. Verify project licenses and live demos.

### Phase 1 — create profile foundation

1. Create/verify the special public `yashsrivastava0` profile repository.
2. Add a text-first profile README.
3. Update profile bio and canonical website.
4. Reorder pins around OryxenAI and QuotaMesh.
5. Remove empty `AI-Yash-Portfolio` from pins.

### Phase 2 — visual layer

1. Prototype Editorial Core.
2. Prototype Silver-Flow Editorial.
3. Check both in GitHub light and dark modes.
4. Test mobile/narrow width.
5. Add only one motion element if it improves rather than delays comprehension.

### Phase 3 — project proof

1. Improve metadata/screenshots for selected flagships.
2. Verify OryxenAI recruiter-access experience.
3. Keep QuotaMesh’s alpha/local boundary visible.
4. Add a public, permission-safe voice-AI case study only if the team approves.
5. Feature a meaningful public open-source contribution once available.

### Phase 4 — alignment

Update LinkedIn/portfolio only after the facts are resolved and only in a separately authorized pass.

---

## 18. Decision matrix

| Decision | Recommendation | Confidence |
|---|---|---|
| Profile README | Create one | High |
| Top project | OryxenAI | High |
| Second project | QuotaMesh | High |
| Third narrative project | AI Receptionist, labeled team/private | High |
| Pin AI Receptionist now | No, private | High |
| Open-source section | Yes, after real contributions exist | High |
| Primary portfolio | `yashdev.ai.studio` after manual verification | High, user-directed |
| Empty AI-Yash-Portfolio pin | Remove later | High |
| Full anime character banner | No | High |
| Original anime-inspired energy motif | Yes | High |
| Snake animation | Optional, low on page | Medium |
| Old GitHub Readme Stats public endpoint | Do not use | High |
| GitHub Stats Extended Action | Preferred if a stats card is used | High |
| Typing SVG hero | Avoid | Medium-high |
| Visitor counter / trophy wall | Avoid | High |
| Speaking/interactive README | Not technically appropriate | High |
| Direct email/phone | Omit by default | High |

---

## 19. Research notes and sources

Research prioritized official GitHub documentation and primary project repositories; community patterns and recruiter-oriented commentary were used only as secondary evidence.

### GitHub official

- [Managing your profile README](https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme)
- [Using your GitHub profile to enhance your resume](https://docs.github.com/en/account-and-profile/tutorials/using-your-github-profile-to-enhance-your-resume)
- [Profile reference](https://docs.github.com/en/account-and-profile/reference/profile-reference)
- [Personal profile / profile README concepts](https://docs.github.com/en/account-and-profile/concepts/personal-profile)
- [Quickstart for writing on GitHub](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/quickstart-for-writing-on-github)
- [About READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)
- [Best practices for repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories)

### README patterns and motion

- [Awesome GitHub Profile README showcase](https://github.com/abhisheknaiidu/awesome-github-profile-readme)
- [`Platane/snk`](https://github.com/Platane/snk)
- [`DenverCoder1/readme-typing-svg`](https://github.com/DenverCoder1/readme-typing-svg)
- [`BerkaySevinc/easy-github-profile`](https://github.com/BerkaySevinc/easy-github-profile) — useful 2026 example of action-generated local SVG assets; use as a pattern reference, not a template to copy.

### Stats

- [GitHub Stats Extended](https://github.com/stats-organization/github-stats-extended)
- [GitHub Readme Stats Action](https://github.com/stats-organization/github-readme-stats-action)
- [Legacy `github-readme-stats`](https://github.com/anuraghazra/github-readme-stats) — the project currently directs users to its maintained successor; do not build a new profile around the legacy public endpoint.

### Secondary practitioner signal

- [How to show shipped projects on a GitHub profile README — Make Taksh, 2026-09-25](https://maketaksh.com/guides/github-profile-readme)

### Project/public-presence links checked

- [GitHub profile](https://github.com/yashsrivastava0)
- [OryxenAI repository](https://github.com/yashsrivastava0/OryxenAI)
- [OryxenAI app](https://app.oryxenai.me/)
- [QuotaMesh repository](https://github.com/yashsrivastava0/QuotaMesh)
- [MediFindX0 repository](https://github.com/yashsrivastava0/MediFindX0)
- [MediFindX Hugging Face Space](https://huggingface.co/spaces/PromptYASH/Medifindx)
- [BlogerVoger repository](https://github.com/yashsrivastava0/BlogerVoger)
- [YASHODA repository](https://github.com/yashsrivastava0/YASHODA)
- [YASHODA demo](https://v0-yashoda.vercel.app/)
- [Ai-Portfolio repository](https://github.com/yashsrivastava0/Ai-Portfolio)
- Suggested primary portfolio: `https://yashdev.ai.studio/`
- Existing profile portfolio: `https://v0-yash-srivastava-portfolio-vl.vercel.app/`

---

## 20. Final blueprint

The strongest profile is a **calm, high-evidence AI-engineering profile** with an original, subtle “silver-flow” signature.

The page should feel like this:

> **AI Engineer** first.  
> **OryxenAI + QuotaMesh + Voice AI** second.  
> **Open-source collaboration** third.  
> **Distinctive visual identity** around them, not in front of them.

The anime influence should be felt through **discipline, energy, contrast, and motion**, not through copied anime characters. The technical sophistication should be felt through **project evidence, system boundaries, tests, demos, and honest status labels**, not through a wall of badges or dynamic counters.
