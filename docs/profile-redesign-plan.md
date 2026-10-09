# Profile design and implementation

Research and implementation: **8 October 2026**.

The profile introduces Yash as an AI engineer who builds agentic systems and
the backends behind them. It supports his search for remote roles with US
and European teams from India. The character artwork establishes the visual
identity; a smaller first-name signature leaves the work as the main focus.
Voice AI appears as a project area, not as his specialization.

The attached blueprint and audit are background context. Their recommendations
are not restrictions. The current user request controls the design, wording,
project selection, and use of anime characters.

## Reader flow

1. **Role and character artwork.** A small custom vector signature for Yash
   beside Goku Ultra Instinct and Satoru Gojo. The introduction repeats the identity in native Markdown so
   it stays accessible and readable independently of the image.
2. **Specific work.** OryxenAI, QuotaMesh, and AI Receptionist. Each gets a short
   description of what it does, relevant engineering details, and a useful next
   step. The team project is explicitly labeled as in development.
3. **Engineering context.** A compact stack and an expandable paragraph about
   Xpression, JUTEQ, and IIT Mandi.
4. **Actual activity.** A dated 12-week contribution chart and links to GitHub's
   current history and public PR search.
5. **Personality.** Tanjiro in the same ink, silver, and cyan palette. This panel
   is visible by default, followed by one short line about anime and side projects.
6. **Contact.** Portfolio, LinkedIn, and the existing public email.

## Visual design

### Typography

The hero name, project names, and Tanjiro panel use **Syne**, an expressive
geometric typeface. The hero uses only “Yash,” in mixed case at weight 700,
with a nominal size of 62px on desktop and 48px on mobile. It is a small
signature rather than a two-line masthead. A restrained silver gradient gives
the lettering depth. The surname is absent from visible profile text; existing
usernames and contact URLs remain valid.

Letters are converted to vector paths. The finished SVGs do not request fonts
from Google or rely on the viewer having a particular typeface installed.
Native Markdown text uses GitHub's own typography. Small graphic labels use
system sans-serif fonts.

The original font and its SIL Open Font License are retained under
`assets/profile/fonts/`. The source is
[Google Fonts' Syne directory](https://github.com/google/fonts/tree/main/ofl/syne).

### Character artwork

Two text-free art plates supply the opening and closing panels. The revised
opening pairs Goku Ultra Instinct with Satoru Gojo, whose blindfold and grin
keep him distinct from Goku. Tanjiro remains in the closing panel. Both use
dark ink, silver-blue rim lighting, restrained water/aura detail, and generous
space for type. The typography is composited as vector content rather than
baked into generated image text.

Desktop and mobile use separate compositions. On mobile, the character occupies
an upper portrait area with both Goku and Gojo visible, and the small signature
sits over a dark lower gradient. Project
names remain readable instead of scaling down a wide desktop strip.

“One more quick fix. Famous last words.” adds a little coding sarcasm to the
hero. It is a caption, not an attributed character quote. It uses ordinary text
with no typing animation and stays subordinate to the engineering identity.

The character art is generated fan art, not official artwork or an endorsement.

### Motion

| Asset | Motion | Purpose |
| --- | --- | --- |
| Name | Slow highlight across the outlined letters | Add depth while keeping every letter stable and readable |
| Goku and Gojo panel | Low-opacity aura and a few slow particles | Give the artwork some atmosphere |
| Tanjiro panel | Thin moving water stroke | Match the character's artwork and the silver-blue theme |
| OryxenAI | Orbiting schematic points | Suggest agent coordination |
| QuotaMesh | A packet along a branching route | Suggest routing and fallback |
| AI Receptionist | A small audio waveform | Identify real-time voice work |

These are decorative graphics, not live status indicators or application demos.
The body text, metrics, and layout do not move. No typing widget, battle GIF,
flashing badge, autoplay video, or third-party animation service is needed.

All animated assets have explicit static counterparts. README `<picture>`
branches select those files when the viewer requests reduced motion, before
choosing the appropriate size and theme. This avoids relying entirely on media
queries inside an SVG image, which did not reliably follow page-level emulation
in the local browser. Internal reduced-motion CSS also supports standalone SVG
viewing.

### Asset dimensions

| Asset | Desktop | Mobile |
| --- | --- | --- |
| Hero | 1000 x 320 | 440 x 350 |
| Project panels | 1000 x 126 | 440 x 98 |
| Activity chart | 900 x 192 | 400 x 224 |
| Tanjiro panel | 1000 x 245 | 440 x 260 |

Project panels and activity have light and dark variants. The character panels
are intentional dark artwork in either theme. Cyan is darker on light surfaces
so labels and lines retain contrast.

Every character SVG embeds its raster artwork as a data URI. No external image
request is needed inside the SVG. The files contain no JavaScript or
`foreignObject`. They remain complete if the README is copied with its assets.

## Content choices

### OryxenAI

Describe the workflow plainly: bring background and project notes, review copy,
and refine a private portfolio. Approval steps, saved state, workers, and browser
checks are concrete engineering details. Keep the private workspace boundary;
do not claim a public publishing/export feature.

Source: [current public repository](https://github.com/yashsrivastava0/OryxenAI).

### QuotaMesh

Describe a local endpoint for authorized API access, with user-selected routing
and paid-use rules, fallback, shared cooldowns, and local usage history. Its
current public README describes a v0.1 MVP, so the old alpha label was replaced.
Do not imply that the gateway creates free provider capacity.

Source: [current public repository](https://github.com/yashsrivastava0/QuotaMesh).

### AI Receptionist

This replaces MediFindX in the visible profile at the user's request. The user
confirms that he is contributing and building with a team. The supplied context
contains a specific description of a voice receptionist for HVAC intake and
scheduling using Gemini Live, FastAPI, real-time audio, tools, Google Calendar,
and safety checks. That supports a short, high-level introduction.

The README calls it a **team project, in development**. It does not imply sole
ownership, public source availability, completed telephony integration, customer
traction, or production deployment. There is no private repository URL, customer
information, internal configuration, or business policy in the profile. The
contact link provides a useful next step without inventing a public demo.

The original MediFindX assets and context documents are retained but are no
longer referenced by the visible README.

### Wording

Use direct language about projects and work. Avoid invented slogans, broad
self-ranking claims, inflated metrics, decorative long dashes, HTML spacing
entities, and the earlier “side quest” framing. Preserve the actual AI/LLM role;
removing generic prose does not mean removing technical content.

The headline and introduction focus on agentic systems, context, recovery,
and Python backends. Voice wording stays inside the AI Receptionist project.

Experience remains a short expandable paragraph instead of a résumé timeline.
Future upstream work is expressed as a plan. Add exact merged-PR links when they
exist, rather than implying contributions already made.

## Research behind the design

The live public profile was inspected from fetched GitHub HTML. Its original
README matched this checkout's starting README. The older attachment's claim
that there was no profile README is no longer current. This session has a local
Chromium browser for rendering checks, not control of the user's signed-in
browser.

| Live source inspected | Design decision |
| --- | --- |
| [GitAscii](https://github.com/Igorcbraz/GitAscii) and its [published example](https://github.com/Igorcbraz/GitAscii/blob/main/public/example.svg) | Use self-contained, repository-owned SVGs, a strong typographic hierarchy, and theme-aware pictures. Build original panels instead of running its editor/publishing stack. |
| [Mauro's profile generator](https://github.com/maurodesouza/profile-readme-generator) and [profile](https://github.com/maurodesouza/maurodesouza) | Use modular sections, a personal introduction, useful links, and a small stack. |
| [Awesome profile READMEs](https://github.com/abhisheknaiidu/awesome-github-profile-readme) | Keep one coherent visual identity instead of stacking unrelated components. |
| [Anime profile search](https://github.com/search?q=anime+profile+readme&type=repositories) | Character artwork can establish personality; keep project evidence and native text easy to scan. |
| [Tierney's profile](https://github.com/bnb/bnb) and [swyx's profile](https://github.com/sw-yx/sw-yx) | Prefer specific work and ordinary language over a long skills résumé. |
| [GitHub profile README documentation](https://github.com/github/docs/blob/main/content/account-and-profile/how-tos/profile-customization/managing-your-profile-readme.md) | The live profile uses the public `username/username` repository and a root README. |
| [GitHub job-search guidance](https://github.com/github/docs/blob/main/content/account-and-profile/tutorials/using-your-github-profile-to-enhance-your-resume.md) | Make role, relevant projects, location, and contact easy to find. |
| [README Stats](https://github.com/anuraghazra/github-readme-stats) | Its current README points to a maintained successor and warns about the public endpoint. Use a dated repository-owned chart. |
| [Contribution snake](https://github.com/Platane/snk) and [Activity Graph](https://github.com/ashutosh00710/github-readme-activity-graph) | Scheduled asset generation is useful. One actual activity chart is sufficient alongside the new character and project motion. |
| GPRM feature list supplied by the user | Select useful components; omit counters, trophies, donations, and unrelated memes. Its marketing text is context, not a verified service specification. |

No reference generator implementation was copied. Six local stack icons come
from [Simple Icons](https://github.com/simple-icons/simple-icons), whose source
is CC0. Brand marks remain their owners' marks.

## Authoring and refresh commands

Viewing the README requires no install or application build. The activity
updater and its tests use only Python's standard library:

```sh
cd /workspace/Profilehub
python3 -m unittest discover -s tests -v
python3 scripts/update_activity.py --username yashsrivastava0
```

To rebuild visual assets after editing the authoring script, install the optional
design dependency and run the renderer. FontTools 4.61.1 is already available in
this machine; the renderer was executed and repeatability checked.

```sh
python3 -m pip install -r requirements-design.txt
python3 scripts/render_profile.py
```

The renderer writes animated and static variants together. Fonts and text-free
artwork in `assets/profile/fonts/` and `assets/profile/source/` are its inputs.
Generated artwork originals are also preserved outside the checkout.

The daily workflow tests the activity pipeline, fetches the signed-out GitHub
calendar, validates complete dates and count formats, then updates only the five
activity output files. It uses GitHub's ordinary Actions token. A failed fetch or
unfamiliar response cannot silently produce zero activity or replace the last
published chart. Its schedule is 06:23 UTC, or **11:53 am IST**; GitHub schedules
are best-effort.

Contribution counts are not commit totals or engineering-quality scores. The
chart contains an observation date, a labeled partial final week, and exact daily
counts in `activity.json`. Anonymized private counts can appear if enabled on the
account. Links to current GitHub history remain available.

## Publication

This task edits the local **Profilehub** checkout. The live profile is served
from **`yashsrivastava0/yashsrivastava0`**.

To publish, copy the reviewed root README, `assets/profile/`, the scripts, tests,
and `.github/workflows/profile-activity.yml` into that profile repository.
Copying only the README breaks asset links. Enable Actions and run the activity
workflow once. If branch protection blocks a bot push, refresh locally and use
that repository's normal review process. No PAT or new secret is required for
public calendar data.

The design does not alter GitHub bio, pins, LinkedIn, or external deployments.
AI Receptionist remains a narrative feature rather than a public repository pin.

## Validation

The validation report records local tests, asset integrity, theme/mobile
selection, animation behavior, and static fallback behavior. Browser previews
use GitHub Markdown CSS and CommonMark. They demonstrate this implementation's
layout, not that the changed profile is already published.
