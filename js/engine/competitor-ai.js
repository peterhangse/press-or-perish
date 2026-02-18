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
 * Generate competitor score for a given day
 * @param {number} day - Current day (1-5)
 * @returns {number} Competitor's points for today
 */
export function generateCompetitorScore(day) {
  // Base ranges by day
  const ranges = {
    1: { min: 6, max: 9 },   // easy start
    2: { min: 7, max: 10 },
    3: { min: 8, max: 11 },  // mid difficulty
    4: { min: 8, max: 12 },
    5: { min: 9, max: 12 },  // strong finish
  };

  const range = ranges[day] || ranges[3];
  return randomInt(range.min, range.max);
}

/**
 * Get competitor headline text (flavor)
 * @param {number} score - Competitor's score today
 * @returns {string} A generic competing headline
 */
export function getCompetitorHeadline(score) {
  if (score >= 11) return pickRandom(STRONG_HEADLINES);
  if (score >= 8)  return pickRandom(AVERAGE_HEADLINES);
  return pickRandom(WEAK_HEADLINES);
}

/**
 * Get the competitor newspaper name
 */
export function getCompetitorName() {
  return 'Regionbladet';
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
