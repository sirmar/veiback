# Requirements — Veibäck Effektiv Utveckling AB

## Technical

- **Framework:** Astro (static output, scalable to SSR/backend later)
- **Responsive:** Desktop and mobile
- **Static site:** No backend now, but structure should make it easy to add later
- **Data:** YAML files parsed and rendered by Astro
  - `resume.yaml` — pure CV data (also used for other purposes beyond the site)
  - `content.sv.yaml` / `content.en.yaml` — sales/soft content per language
- **Photo:** `public/profilbild.jpg`

## Design

- Modern style
- Subtle animations and motion effects
- Single-page with multiple sections (easy to refactor into multi-page later)

### Colour palette

| Role           | Hex       |
|----------------|-----------|
| Background     | `#0f1117` |
| Surface        | `#1c1f26` |
| Text primary   | `#e8eaed` |
| Text muted     | `#8b949e` |
| Accent         | `#4a9e6b` |
| Accent hover   | `#5db87e` |

Accent green is inspired by the forest tones in the profile photo — muted, slightly blue-green, not neon or olive.

### Motion & interaction

- Elements fade in + slide up on scroll (IntersectionObserver)
- Hero elements stagger in on load
- Subtle animated background orbs (blurred, low opacity, slow drift)
- Service cards lift slightly on hover with accent border

### UI patterns

- Skill tags displayed as pills (dark green background, accent border and text)
- Frosted-glass nav bar (backdrop-filter blur)
- Section labels in small caps accent colour above headings

## Sections (order)

1. Hero — name, tagline, profile photo
2. Services — three packages
3. About
4. Experience — CV timeline
5. Clients — logos/names
6. Contact

## Languages

- Swedish (`/sv/`) and English (`/en/`)
- Astro i18n routing

## Content

- Company: Veibäck Effektiv Utveckling AB
- Person: Marcus Veibäck
- Tone: Personal, direct, forward-looking — not formal CV style
- Availability for assignments not communicated
- No client quotes yet (can be added later)
- C/C++ de-emphasised (long ago, focus on high-level languages now)
