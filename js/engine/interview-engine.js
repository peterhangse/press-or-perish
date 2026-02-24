/**
 * INTERVIEW ENGINE — Lookup table reader
 * ~30 lines of pure logic. No DOM. Portable to Godot.
 *
 * Every Q1→Q2 combination maps to a hardcoded result:
 *   { tier, response, expression }
 *
 * Total points = base_value + (tier * 2)
 */

/**
 * Get Q1 options for a story
 * @param {Object} story - Story data from stories.json
 * @returns {Array} Q1 archetype choices
 */
export function getQ1Options(story) {
  return story.interview.q1_options;
}

/**
 * Get Q2 options based on Q1 choice
 * @param {Object} story - Story data
 * @param {string} q1Archetype - The Q1 archetype chosen ('friendly'|'direct'|'pressure'|'silence')
 * @returns {Array} Q2 follow-up choices
 */
export function getQ2Options(story, q1Archetype) {
  const branch = story.interview.branches[q1Archetype];
  if (!branch) return [];
  return branch.q2_options;
}

/**
 * Compute Q1 bonus based on branch quality.
 * If the chosen archetype's branch has ANY outcome with tier >= 2,
 * the approach was good and earns +2. Otherwise 0.
 */
export function computeQ1Bonus(story, q1Archetype) {
  const branch = story.interview.branches[q1Archetype];
  if (!branch || !branch.outcomes) return 0;
  const maxTier = Math.max(...branch.outcomes.map(o => o.tier));
  return maxTier >= 2 ? 2 : 0;
}

/**
 * Resolve the full interview outcome
 * @param {Object} story - Story data
 * @param {string} q1Archetype - The Q1 archetype chosen
 * @param {number} q2Index - Index of Q2 option chosen (0-2)
 * @returns {Object} { tier, points, q1Bonus, q2Bonus, response, expression, feedback }
 */
export function resolveInterview(story, q1Archetype, q2Index) {
  const branch = story.interview.branches[q1Archetype];
  const outcome = branch.outcomes[q2Index];

  const tier = outcome.tier;
  const q1Bonus = computeQ1Bonus(story, q1Archetype);
  const q2Bonus = Math.max(0, (tier * 2) - q1Bonus);
  const points = story.base_value + q1Bonus + q2Bonus;

  return {
    tier,
    points,
    q1Bonus,
    q2Bonus,
    response: outcome.response,
    expression: outcome.expression,
    feedback: outcome.feedback || '',
    note: outcome.note || '',
    q1Response: branch.q1_response,
  };
}

/**
 * Get headline options for publishing
 * @param {Object} story - Story data
 * @param {number} tier - Tier reached (0-3)
 * @returns {Array} Headline choices [{text, tone}]
 */
export function getHeadlines(story, tier) {
  // Support both formats:
  // - Tiered object: { tier_0: [...], tier_1: [...], tier_2: [...], tier_3: [...] }
  // - Flat array: [{text, tone}, {text, tone}, {text, tone}]
  if (Array.isArray(story.headlines)) {
    return story.headlines;
  }
  return story.headlines[`tier_${tier}`] || story.headlines.tier_0;
}
