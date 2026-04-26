import { readFileSync } from 'node:fs';
import { join } from 'node:path';
import yaml from 'js-yaml';
import type { BilingualString, Content, Locale, Resume } from './types';

function loadYaml<T>(filename: string): T {
  const filePath = join(process.cwd(), 'src/data', filename);
  const raw = readFileSync(filePath, 'utf-8');
  return yaml.load(raw) as T;
}

function loadYamlFromRoot<T>(filename: string): T {
  const filePath = join(process.cwd(), '..', filename);
  const raw = readFileSync(filePath, 'utf-8');
  return yaml.load(raw) as T;
}

export function loadContent(locale: Locale): Content {
  return loadYaml<Content>(`content.${locale}.yaml`);
}

export function loadResume(): Resume {
  return loadYamlFromRoot<Resume>('resume.yaml');
}

export function getString(val: BilingualString | string, locale: Locale): string {
  if (typeof val === 'string') return val;
  return val[locale] ?? val.sv ?? '';
}
