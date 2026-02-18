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
 * Resolve the full interview outcome
 * @param {Object} story - Story data
 * @param {string} q1Archetype - The Q1 archetype chosen
 * @param {number} q2Index - Index of Q2 option chosen (0-2)
 * @returns {Object} { tier, points, response, expression, feedback }
 */
export function resolveInterview(story, q1Archetype, q2Index) {
  const branch = story.interview.branches[q1Archetype];
  const outcome = branch.outcomes[q2Index];

  const tier = outcome.tier;
  const points = story.base_value + (tier * 2);

  return {
    tier,
    points,
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
  // Each story has headlines keyed by tier
  return story.headlines[`tier_${tier}`] || story.headlines.tier_0;
}
