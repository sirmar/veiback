# cv

Generates PDF CVs from `resume.yaml` using Pandoc.

## Usage

```sh
dev run -- --lang sv --template classic
dev run -- --lang en --template classic
```

Output is written to `output/cv_<lang>_<template>.pdf`.

## Templates

| Name      | Description                       |
|-----------|-----------------------------------|
| classic   | Clean, minimal LaTeX layout       |
| website   | Inspired by veiback.se aesthetics |

## Data

`resume.yaml` is a symlink to `../webpage/src/data/resume.yaml`.
It is bilingual — each field has `sv` and `en` variants where applicable.
