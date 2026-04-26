import type { Locale } from './types';

const ui = {
  sv: {
    nav: {
      services: 'Tjänster',
      about: 'Om mig',
      experience: 'Erfarenhet',
      clients: 'Kunder',
      contact: 'Kontakt',
    },
    sections: {
      services: 'Vad jag erbjuder',
      about: 'Om mig',
      experience: 'Erfarenhet',
      clients: 'Kunder & uppdragsgivare',
      contact: 'Hör av dig',
    },
    experience: {
      present: 'nu',
      via: 'via',
      at: 'hos',
    },
    contact: {
      cta: 'Hör av dig',
      intro: 'Har du ett uppdrag eller vill du bara byta några ord? Skicka ett mejl eller ring.',
      email: 'E-post',
      phone: 'Telefon',
      linkedin: 'LinkedIn',
      github: 'GitHub',
      cv: 'Ladda ner CV',
      cvWeb: 'CV',
      cvPrint: 'CV (utskrift)',
    },
    about: {
      yearsUnit: 'års',
      experience: 'erfarenhet',
    },
  },
  en: {
    nav: {
      services: 'Services',
      about: 'About',
      experience: 'Experience',
      clients: 'Clients',
      contact: 'Contact',
    },
    sections: {
      services: 'What I offer',
      about: 'About me',
      experience: 'Experience',
      clients: 'Clients & engagements',
      contact: 'Get in touch',
    },
    experience: {
      present: 'present',
      via: 'via',
      at: 'at',
    },
    contact: {
      cta: 'Get in touch',
      intro: 'Have an assignment or just want to talk? Send an email or give me a call.',
      email: 'Email',
      phone: 'Phone',
      linkedin: 'LinkedIn',
      github: 'GitHub',
      cv: 'Download CV',
      cvWeb: 'CV',
      cvPrint: 'CV (print)',
    },
    about: {
      yearsUnit: 'yr',
      experience: 'experience',
    },
  },
};

export function t(locale: Locale, key: string): string {
  const keys = key.split('.');
  let current: unknown = ui[locale];
  for (const k of keys) {
    current = (current as Record<string, unknown>)?.[k];
  }
  return (current as string) ?? key;
}
