/**
 * SETTINGS — Player preferences (volume, text speed, text size, motion)
 * No DOM. Persisted in localStorage under 'pop_settings' (versioned).
 */

const KEY = 'pop_settings';
const VERSION = 1;

export const TEXT_SPEEDS = {
  normal:  { label: 'Normal',  msPerWord: 130 },
  fast:    { label: 'Fast',    msPerWord: 45 },
  instant: { label: 'Instant', msPerWord: 0 },
};

const DEFAULTS = {
  v: VERSION,
  musicVolume: 1,     // 0..1, multiplies each track's base volume
  sfxVolume: 1,       // 0..1, master gain for synthesized SFX
  textSpeed: 'normal',
  largeText: null,    // null = automatic (on for small screens), true/false = forced
  reduceMotion: null, // null = follow the OS setting, true/false = forced
};

let current = load();
const listeners = [];

function load() {
  try {
    const raw = localStorage.getItem(KEY);
    if (!raw) return { ...DEFAULTS };
    const data = JSON.parse(raw);
    if (!data || typeof data !== 'object') return { ...DEFAULTS };
    // Future migrations go here (data.v < VERSION)
    return { ...DEFAULTS, ...data, v: VERSION };
  } catch {
    return { ...DEFAULTS };
  }
}

function persist() {
  try {
    localStorage.setItem(KEY, JSON.stringify(current));
  } catch {
    // Private mode / full storage — settings simply won't persist
  }
}

export function get(key) {
  return current[key];
}

export function getAll() {
  return { ...current };
}

export function set(key, value) {
  if (!(key in DEFAULTS)) return;
  current[key] = value;
  persist();
  listeners.forEach(fn => fn(key, value, getAll()));
}

export function onChange(fn) {
  listeners.push(fn);
}

/** Milliseconds per word for the typewriter, from the text speed setting. */
export function msPerWord() {
  return (TEXT_SPEEDS[current.textSpeed] || TEXT_SPEEDS.normal).msPerWord;
}
