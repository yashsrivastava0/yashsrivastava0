# Profile validation

Validated locally on **8 October 2026**.

## Passed

- **11 activity tests:** count formats, absent or changed calendar markup,
  duplicate and missing dates, partial weeks, year boundaries, zero activity,
  weekly totals, repeatable writes, SVG XML, and retention of the last snapshot
  when a network request fails.
- **Live activity fetch:** the signed-out GitHub calendar produced a complete
  20 July to 8 October 2026 snapshot with **1,882 contributions** and **56 active
  days**. Daily counts and weekly totals agree. The last week is labeled partial.
- **12 Chromium layouts:** dark and light at 375px, 768px, and 1024px, each with
  ordinary motion and reduced motion. All 12 visible images load, no horizontal
  page overflow, correct size/theme/motion variants, and a working experience
  disclosure. Tanjiro is visible without opening a disclosure. AI Receptionist
  is present with its team/in-development status; MediFindX is absent.
- **Animation behavior:** the hero highlight, Tanjiro water, agent orbit, route
  packet, and receptionist waveform run in normal mode. In a timed image check,
  the embedded hero changed between frames with motion enabled. Its explicit
  static variant changed **zero pixels** with reduced motion. Standalone SVG
  media queries also stop the animation.
- **Assets:** all **42** README image/source references resolve; all **46** SVGs
  parse. Character artwork is embedded in the SVGs. No JavaScript, external image
  URLs inside SVGs, or `foreignObject` content is present. Static variants contain
  no keyframes. The four source/earlier PNGs pass image integrity checks.
- **Typography:** Syne is outlined into SVG paths; the source font and SIL Open
  Font License are retained. The renderer runs using FontTools 4.61.1. Repeating
  generation produces identical character-panel files.
- **Workflow:** YAML parses, checkout's pinned commit matches its upstream
  v4.2.2 tag, and the local test/activity commands pass. Activity generation
  continues to need only Python's standard library.
- **Content and repository review:** no long dashes, spacing entities, or
  MediFindX references remain in the visible README. Only “Yash” is used as the
  display name, at a smaller size. The header focuses on agents and backends;
  voice wording is confined to AI Receptionist. Goku and Gojo share the hero,
  with both faces visible on desktop and mobile. Original research documents,
  `yash.md`, older assets, and `.gitignore` are preserved. `git diff --check` passes.

## Scope

These are local previews using GitHub Markdown CSS and CommonMark. Screenshots,
layout checks, and motion checks are in `/workspace/profilehub-preview/`.
They verify the implementation, not publication to the live profile.

The daily GitHub Action has not run from these local changes. After publication,
it needs Actions enabled and permission to update generated files. Its dated
snapshot remains useful if a refresh fails or GitHub delays the schedule.

AI Receptionist's short description uses the user's current confirmation of team
involvement and the supplied project context. It is a high-level description of
work in development, not a verified public deployment. No private repository,
customer information, or internal configuration is published in the README.

External project deployments were not runtime-tested in this design pass.
The profile repository remains `yashsrivastava0/yashsrivastava0`; this checkout is
Profilehub. See [publication instructions](profile-redesign-plan.md#publication).
