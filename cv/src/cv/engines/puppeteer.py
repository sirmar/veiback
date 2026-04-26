import asyncio
import base64
import os
import tempfile
from pathlib import Path
from typing import Any

import jinja2


def render(
  data: dict[str, Any], lang: str, template: str, templates_dir: Path, output_path: Path
) -> None:
  template_path = templates_dir / f'{template}.html'
  if not template_path.exists():
    raise ValueError(f'Template not found: {template_path}')

  env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(str(templates_dir)),
    autoescape=jinja2.select_autoescape(['html']),
  )
  env.filters['format_date'] = _format_date(lang)

  css_path = templates_dir / f'{template}.css'
  css = css_path.read_text(encoding='utf-8') if css_path.exists() else ''

  profile_image = _load_profile_image(templates_dir)

  tmpl = env.get_template(f'{template}.html')
  html = tmpl.render(**data, lang=lang, css=css, profile_image=profile_image)

  with tempfile.NamedTemporaryFile(
    mode='w', suffix='.html', delete=False, encoding='utf-8'
  ) as f:
    f.write(html)
    html_path = Path(f.name)

  try:
    asyncio.run(_pdf(html_path, output_path))
  finally:
    html_path.unlink()


def _format_date(lang: str):
  _months_sv = [
    'jan',
    'feb',
    'mar',
    'apr',
    'maj',
    'jun',
    'jul',
    'aug',
    'sep',
    'okt',
    'nov',
    'dec',
  ]
  _months_en = [
    'Jan',
    'Feb',
    'Mar',
    'Apr',
    'May',
    'Jun',
    'Jul',
    'Aug',
    'Sep',
    'Oct',
    'Nov',
    'Dec',
  ]

  def _filter(value: str | None) -> str:
    if value is None:
      return 'Nu' if lang == 'sv' else 'Present'
    parts = str(value).split('-')
    if len(parts) == 2:
      month = int(parts[1]) - 1
      months = _months_sv if lang == 'sv' else _months_en
      return f'{months[month]} {parts[0]}'
    return str(value)

  return _filter


def _load_profile_image(templates_dir: Path) -> str:
  candidates = [
    templates_dir.parent / 'profilbild.jpg',
    templates_dir / 'profilbild.jpg',
  ]
  for path in candidates:
    if path.exists():
      data = base64.b64encode(path.read_bytes()).decode('ascii')
      return f'data:image/jpeg;base64,{data}'
  return ''


async def _pdf(html_path: Path, output_path: Path) -> None:
  try:
    from pyppeteer import launch  # type: ignore[import-untyped]
  except ImportError as e:
    raise RuntimeError(
      'pyppeteer is required for the puppeteer engine. '
      'Add it to your dependencies: uv add pyppeteer'
    ) from e

  executable = os.environ.get('PUPPETEER_EXECUTABLE_PATH')
  launch_args: dict = {'args': ['--no-sandbox', '--disable-dev-shm-usage']}
  if executable:
    launch_args['executablePath'] = executable

  browser = await launch(**launch_args)
  try:
    page = await browser.newPage()
    await page.goto(f'file://{html_path}', {'waitUntil': 'networkidle0'})
    await page.pdf(
      {
        'path': str(output_path),
        'format': 'A4',
        'printBackground': True,
        'margin': {'top': '0', 'right': '0', 'bottom': '0', 'left': '0'},
      }
    )
  finally:
    await browser.close()
