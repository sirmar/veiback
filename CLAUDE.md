# Claude instructions

## Language
- Communicate with the user in Swedish
- All code, files, comments and documentation must be in English

## Monorepo structure
- `resume.yaml` — shared CV data, lives at the repo root
- `webpage/` — personal website (Astro), deployed to veiback.se
- `cv/` — PDF CV generator (Python + Puppeteer)
- Both subprojects use `DEV_CONTEXT=..` so the build context is the repo root

## resume.yaml
- Bilingual per field: `description: {sv: ..., en: ...}`
- Single source of truth for both subprojects — edit only this file
- Keep it clean CV data only; no site-specific content
