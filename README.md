# veiback

Personal website and CV generator for [veiback.se](https://veiback.se).

## Structure

| Path | Description |
|------|-------------|
| `resume.yaml` | Single source of truth for CV data (bilingual: `sv`/`en`) |
| `webpage/` | Personal website built with Astro |
| `cv/` | PDF CV generator (Python + Puppeteer) |

## Development

```sh
# Webpage
cd webpage && dev watch

# CV
cd cv && dev run --lang sv --template classic
```

## Deploy

```sh
cd webpage
dev build
bash scripts/deploy.sh
```
