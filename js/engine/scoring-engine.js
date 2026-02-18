/**
 * SCORING ENGINE — Points, deficit, and end-of-day math
 * Pure functions. No DOM. Portable to Godot.
 *
 * Formula: Total = base_value + (tier * 2)
 * Range: 2 (lowest base, tier 0) to 14 (base 8, tier 3)
 * Deficit: player_score - competitor_score, cumulative
 * Threshold: -10 = PERISHED
 */

/**
 * Calculate points earned for a story interview
 * @param {number} baseValue - Story base value (2-8)
 * @param {number} tier - Tier reached (0-3)
 * @returns {number} Total points
 */
export function calculatePoints(baseValue, tier) {
  return baseValue + (tier * 2);
}

/**
 * Calculate deficit change for the day
 * @param {number} playerScore - Player's points today
 * @param {number} competitorScore - Competitor's points today
 * @returns {number} Deficit delta (negative = falling behind)
 */
export function calculateDeficitDelta(playerScore, competitorScore) {
  return playerScore - competitorScore;
}

/**
 * Apply deficit change and return new total
 * @param {number} currentDeficit - Current cumulative deficit
 * @param {number} delta - Today's deficit change
 * @returns {number} New deficit total
 */
export function applyDeficit(currentDeficit, delta) {
  return currentDeficit + delta;
}

/**
 * Get deficit severity for UI display
 * @param {number} deficit - Current deficit
 * @returns {string} 'safe' | 'warning' | 'danger'
 */
export function getDeficitSeverity(deficit) {
  if (deficit > -3) return 'safe';
  if (deficit > -7) return 'warning';
  return 'danger';
}

/**
 * Get deficit bar fill percentage (0-100)
 * @param {number} deficit - Current deficit (0 to -10)
 * @returns {number} Fill percentage
 */
export function getDeficitFillPercent(deficit) {
  return Math.min(100, Math.max(0, (Math.abs(deficit) / 10) * 100));
}

/**
 * Get distance-to-perish message
 * @param {number} deficit
 * @returns {string}
 */
export function getPerishDistance(deficit) {
  const dist = 10 + deficit; // deficit is negative or zero
  if (dist <= 0) return 'PERISHED';
  if (dist <= 3) return `${dist} from perishing!`;
  if (dist <= 5) return `${dist} from perishing`;
  return `${dist} from perishing`;
}
