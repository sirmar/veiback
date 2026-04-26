# Plan: HTML/CSS template approach

## Context

The LaTeX/Pandoc approach works but is slow to iterate on and token-heavy to debug.
The next step is to add HTML/CSS-based templates rendered to PDF via Puppeteer (headless
Chrome). This gives full CSS control, easy font loading, and a much faster design loop.

## Architecture

```
cv/
  src/
    cv/
      data.py          # unchanged — loads and resolves resume.yaml
      main.py          # add --engine flag: pandoc (default) | puppeteer
      render.py        # dispatch to correct engine
      engines/
        pandoc.py      # current logic, extracted here
        puppeteer.py   # new: render HTML template → PDF via Puppeteer
  templates/
    classic.tex        # existing LaTeX template
    website.html       # new: dark/green aesthetic inspired by veiback.se
    website.css        # styles for website template
  Dockerfile           # add Node + Puppeteer to prod stage (or separate stage)
```

## Usage

```sh
dev run -- --lang sv --template website --engine puppeteer
dev run -- --lang sv --template classic --engine pandoc
```

## Template format

Each HTML template is a Jinja2 file receiving the resolved `resume.yaml` data as context.
Python renders Jinja2 → HTML string, then passes it to Puppeteer via Node or
`pyppeteer` (Python Puppeteer binding).

Example template structure:

```html
<!DOCTYPE html>
<html lang="{{ lang }}">
<head>
  <meta charset="UTF-8">
  <link rel="stylesheet" href="website.css">
</head>
<body>
  <header>
    <h1>{{ personal.name }}</h1>
    <p>{{ personal.email }} · {{ personal.phone }}</p>
  </header>
  <section id="profile">
    {% for para in profile %}
    <p>{{ para }}</p>
    {% endfor %}
  </section>
  ...
</body>
</html>
```

## Dependencies to add

- `jinja2` — HTML templating (pure Python, already familiar from Flask/Django)
- `pyppeteer` or Node `puppeteer` — headless Chrome PDF rendering

Recommendation: use `pyppeteer` (Python wrapper) to avoid introducing a Node toolchain.
Fallback: call `node` via subprocess with a minimal puppeteer script if pyppeteer
proves unmaintained.

## Dockerfile changes

Add to `prod` stage (or a separate `puppeteer` stage):

```dockerfile
RUN apt-get install -y chromium
ENV PUPPETEER_EXECUTABLE_PATH=/usr/bin/chromium
```

pyppeteer downloads its own Chromium by default — override with the system one to
keep the image lean.

## Website template design

Mirrors the veiback.se aesthetic:

| Role           | Value      |
|----------------|------------|
| Background     | `#0f1117`  |
| Surface        | `#1c1f26`  |
| Text primary   | `#e8eaed`  |
| Text muted     | `#8b949e`  |
| Accent         | `#4a9e6b`  |
| Font           | Inter (Google Fonts or local) |

Section labels in small-caps accent colour, skill tags as pills,
clean timeline layout for experience.

## Verification

1. `dev build` — image builds with Chromium
2. `dev run -- --lang sv --template website --engine puppeteer`
3. Open `output/cv_sv_website.pdf` — verify layout, fonts, colours
4. `dev run -- --lang en --template website --engine puppeteer` — verify English variant
5. `dev lint` / `dev types` — still pass
