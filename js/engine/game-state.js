/**
 * GAME STATE — Single source of truth for runtime state
 * Pure data, no DOM. Portable to Godot.
 */

const DEFAULT_STATE = {
  // Run state
  phase: 'start', // start | onboarding | transition | desk | interview | publish | sleep | results | gameover
  day: 0,         // 1-5 during game
  deficit: 0,     // cumulative deficit, -10 = perished

  // Today
  todayLeads: [],       // 8 story IDs offered today
  selectedLead: null,   // story ID player picked
  interviewPhase: 0,    // 0 = not started, 1 = Q1 picked, 2 = Q2 picked (done)
  q1Choice: null,       // archetype string chosen for Q1
  q2Choice: null,       // Q2 option index chosen
  tierReached: 0,       // 0-3 result tier
  pointsEarned: 0,      // points for today
  headlineChosen: null,  // headline index (0-2)
  competitorScore: 0,    // AI competitor points today

  // History
  dayHistory: [],  // [{day, storyId, tier, points, competitorScore, deficit, headline}]
  usedStoryIds: [], // prevent repeats
  usedBossQuotes: [], // prevent repeat boss quotes within a week
  usedBossNotes: [],  // prevent repeat boss desk notes within a week

  // Meta
  runNumber: 0,
  bestScore: 0,
  playerName: '',
};

/**
 * Create a fresh game state
 */
export function createState() {
  return structuredClone(DEFAULT_STATE);
}

/**
 * Reset for a new day within the same run
 */
export function resetDay(state) {
  state.todayLeads = [];
  state.selectedLead = null;
  state.interviewPhase = 0;
  state.q1Choice = null;
  state.q2Choice = null;
  state.tierReached = 0;
  state.pointsEarned = 0;
  state.headlineChosen = null;
  state.competitorScore = 0;
}

/**
 * Record end-of-day in history
 */
export function recordDay(state) {
  state.dayHistory.push({
    day: state.day,
    storyId: state.selectedLead,
    tier: state.tierReached,
    points: state.pointsEarned,
    competitorScore: state.competitorScore,
    deficit: state.deficit,
    headline: state.headlineChosen,
  });
}

/**
 * Check if the game is over
 */
export function isPerished(state) {
  return state.deficit <= -10;
}

/**
 * Check if the player survived the full week
 */
export function hasSurvived(state) {
  return state.day >= 5 && !isPerished(state);
}
