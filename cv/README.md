# cv

Generates PDF CVs from `resume.yaml` using Puppeteer (HTML/CSS → PDF).

## Usage

```sh
dev run -- --lang sv --template website
dev run -- --lang en --template print
```

Output is written to `output/cv_<lang>_<template>.pdf`.

## Templates

Templates are Jinja2 HTML files in `src/`. Each template consists of a `<name>.html` and an optional `<name>.css`.

| Name    | Description                       |
|---------|-----------------------------------|
| website | Inspired by veiback.se aesthetics |
| print   | Optimized for print/PDF           |

## Data

`resume.yaml` lives at the repo root.
It is bilingual — each field has `sv` and `en` variants where applicable.
