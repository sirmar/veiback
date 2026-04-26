from pathlib import Path
from typing import Any

from cv.engines import puppeteer


TEMPLATES_DIR = Path(__file__).parents[2]
OUTPUT_DIR = Path(__file__).parents[2] / 'output'


def render(data: dict[str, Any], lang: str, template: str) -> Path:
  OUTPUT_DIR.mkdir(exist_ok=True)
  output_path = OUTPUT_DIR / f'cv_{lang}_{template}.pdf'
  puppeteer.render(data, lang, template, TEMPLATES_DIR, output_path)
  return output_path
