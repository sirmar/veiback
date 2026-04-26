from pathlib import Path
from typing import Any

import yaml


def load(lang: str) -> dict[str, Any]:
  path = Path(__file__).parents[2] / 'resume.yaml'
  with open(path) as f:
    raw = yaml.safe_load(f)
  return _resolve(raw, lang)


def _resolve(node: Any, lang: str) -> Any:
  if isinstance(node, dict):
    if set(node.keys()) <= {'sv', 'en'}:
      value = node.get(lang, '')
      # Split multi-paragraph strings into lists so templates can add spacing
      if isinstance(value, str) and '\n' in value:
        paragraphs = [p.strip() for p in value.strip().split('\n') if p.strip()]
        return paragraphs if len(paragraphs) > 1 else paragraphs[0]
      return value
    return {k: _resolve(v, lang) for k, v in node.items()}
  if isinstance(node, list):
    return [_resolve(item, lang) for item in node]
  return node
