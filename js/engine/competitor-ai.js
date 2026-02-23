/**
 * COMPETITOR AI — Generates daily competitor scores
 * Pure functions. No DOM. Portable to Godot.
 *
 * The competitor averages 8-10 points/day.
 * Slight variance creates tension. They can have good & bad days.
 *
 * Day 1-2: competitor is slightly weaker (warming up)
 * Day 3:   average performance
 * Day 4-5: competitor gets stronger
 */

/**
 * Default ranges (Småstad) — used as fallback
 */
const DEFAULT_RANGES = {
  1: { min: 6, max: 9 },
  2: { min: 7, max: 10 },
  3: { min: 8, max: 11 },
  4: { min: 8, max: 12 },
  5: { min: 9, max: 12 },
};

/**
 * Generate competitor score for a given day
 * @param {number} day - Current day (1-5)
 * @param {Object} [townConfig] - Town config with competitorScoreRanges
 * @returns {number} Competitor's points for today
 */
export function generateCompetitorScore(day, townConfig) {
  const ranges = townConfig?.competitorScoreRanges || DEFAULT_RANGES;
  const range = ranges[day] || ranges[3] || DEFAULT_RANGES[3];
  return randomInt(range.min, range.max);
}

/**
 * Get competitor headline text (flavor)
 * @param {number} score - Competitor's score today
 * @param {Object} [townConfig] - Town config with competitorHeadlines
 * @returns {string} A generic competing headline
 */
export function getCompetitorHeadline(score, townConfig) {
  const headlines = townConfig?.competitorHeadlines;
  const strong = headlines?.strong || STRONG_HEADLINES;
  const average = headlines?.average || AVERAGE_HEADLINES;
  const weak = headlines?.weak || WEAK_HEADLINES;
  if (score >= 11) return pickRandom(strong);
  if (score >= 8)  return pickRandom(average);
  return pickRandom(weak);
}

/**
 * Get the competitor newspaper name
 * @param {Object} [townConfig] - Town config with competitorName
 * @returns {string} Competitor name
 */
export function getCompetitorName(townConfig) {
  return townConfig?.competitorName || 'Regionbladet';
}

// — Flavor text —
const STRONG_HEADLINES = [
  'Exposes corruption in municipal leadership',
  'Exclusive interview with the county governor',
  'Investigation: Millions missing from budget',
  'Witnesses break silence on factory disaster',
  'New revelations shake local politics',
];

const AVERAGE_HEADLINES = [
  'City council debates school closure',
  'Report: Road network in disrepair',
  'Business owners worry ahead of winter',
  'New principal takes over after controversy',
  'Landowner in dispute with municipality',
];

const WEAK_HEADLINES = [
  'Award for local sports club',
  'Autumn market draws visitors',
  'Library extends opening hours',
  'Traffic light repaired after complaints',
  'New park bench unveiled at the square',
];

function randomInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

function pickRandom(arr) {
  return arr[Math.floor(Math.random() * arr.length)];
}
