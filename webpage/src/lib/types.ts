export type Locale = 'sv' | 'en';

export interface BilingualString {
  sv: string;
  en: string;
}

export interface Service {
  title: string;
  description: string;
  keywords: string[];
}

export interface Content {
  company: {
    name: string;
    tagline: string;
    description: string;
  };
  services: Service[];
  dualities: { a: string; b: string }[];
  clients: { name: string }[];
  about: {
    heading: string;
    body: string;
  };
}

export interface Role {
  title: string;
  start: string;
  end: string | null;
}

export interface ExperienceEntry {
  employer: string;
  employment_type: 'employee' | 'consultancy' | 'self';
  client?: string;
  location: string;
  roles: Role[];
  description: BilingualString;
  skills: string[];
}

export interface Education {
  institution: string;
  start: number;
  end: number;
  degree: BilingualString;
  notes?: BilingualString;
}

export interface Course {
  title: string;
  provider: string;
  year: number;
}

export interface LanguageEntry {
  language: BilingualString;
  level: BilingualString;
}

export interface VolunteerEntry {
  role: BilingualString;
  organization: string | null;
  start: number;
  end: number | null;
}

export interface Resume {
  personal: {
    name: string;
    address: string;
    phone: string;
    email: string;
    linkedin: string;
    github: string;
    website: string;
  };
  profile: BilingualString;
  experience: ExperienceEntry[];
  education: Education[];
  courses: Course[];
  languages: LanguageEntry[];
  volunteer: VolunteerEntry[];
  misc: BilingualString[];
}
