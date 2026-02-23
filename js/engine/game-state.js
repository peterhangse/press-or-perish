/**
 * GAME STATE — Single source of truth for runtime state
 * Pure data, no DOM. Portable to Godot.
 */

const DEFAULT_STATE = {
  // Run state
  phase: 'start', // start | onboarding | transition | desk | interview | publish | sleep | results | gameover
  day: 0,         // 1-5 during game
  deficit: 0,     // cumulative deficit, -10 = perished

  // Town progression
  currentTown: 'smastad',  // town ID string
  townIndex: 0,            // 0-based linear progression order
  townHistory: [],         // [{townId, deficit, dayHistory, survived}] — completed towns

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
  baseValue: 0,          // story base news value

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
  state.baseValue = 0;
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
    q1Archetype: state.q1Choice,
    q2Index: state.q2Choice,
    baseValue: state.baseValue || 0,
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

/**
 * Archive current town results and reset for a new town.
 * Call when the player survives a week and advances.
 */
export function advanceToNextTown(state, nextTownId) {
  // Archive current town
  state.townHistory.push({
    townId: state.currentTown,
    deficit: state.deficit,
    dayHistory: [...state.dayHistory],
    survived: true,
  });

  // Reset for new town
  state.currentTown = nextTownId;
  state.townIndex += 1;
  state.day = 0;
  state.deficit = 0;
  state.dayHistory = [];
  state.usedStoryIds = [];
  state.usedBossQuotes = [];
  state.usedBossNotes = [];
  resetDay(state);
}

// — Save / Load (localStorage) —

const SAVE_KEY = 'pop_save';
const SAVE_VERSION = 2;

/**
 * Persist current run state to localStorage.
 * Call at the start of each day (1–5). Skips Day Zero.
 */
export function saveToLocalStorage(state) {
  if (state.day < 1) return; // don't save tutorial
  const payload = {
    saveVersion: SAVE_VERSION,
    savedAt: new Date().toISOString(),
    day: state.day,
    deficit: state.deficit,
    playerName: state.playerName,
    runNumber: state.runNumber,
    dayHistory: state.dayHistory,
    usedStoryIds: state.usedStoryIds,
    usedBossQuotes: state.usedBossQuotes,
    usedBossNotes: state.usedBossNotes,
    currentTown: state.currentTown,
    townIndex: state.townIndex,
    townHistory: state.townHistory,
  };
  try {
    localStorage.setItem(SAVE_KEY, JSON.stringify(payload));
  } catch (e) {
    console.warn('Failed to save game:', e);
  }
}

/**
 * Load saved run from localStorage.
 * Returns the parsed save object, or null if none / invalid.
 */
export function loadFromLocalStorage() {
  try {
    const raw = localStorage.getItem(SAVE_KEY);
    if (!raw) return null;
    const data = JSON.parse(raw);
    // Accept current version or v1 (pre-town) saves
    if (!data || (data.saveVersion !== SAVE_VERSION && data.saveVersion !== 1)) return null;
    // Migrate v1 saves: add town fields with defaults
    if (data.saveVersion === 1) {
      data.currentTown = data.currentTown || 'smastad';
      data.townIndex = data.townIndex || 0;
      data.townHistory = data.townHistory || [];
      data.saveVersion = SAVE_VERSION;
    }
    return data;
  } catch (e) {
    console.warn('Failed to load save:', e);
    return null;
  }
}

/**
 * Remove saved game from localStorage.
 */
export function clearSave() {
  localStorage.removeItem(SAVE_KEY);
}

/**
 * Check if a saved game exists.
 */
export function hasSave() {
  return !!localStorage.getItem(SAVE_KEY);
}

/**
 * Restore a saved game into the live state object.
 */
export function restoreFromSave(state, saveData) {
  state.day = saveData.day;
  state.deficit = saveData.deficit;
  state.playerName = saveData.playerName;
  state.runNumber = saveData.runNumber;
  state.dayHistory = saveData.dayHistory || [];
  state.usedStoryIds = saveData.usedStoryIds || [];
  state.usedBossQuotes = saveData.usedBossQuotes || [];
  state.usedBossNotes = saveData.usedBossNotes || [];
  state.currentTown = saveData.currentTown || 'smastad';
  state.townIndex = saveData.townIndex || 0;
  state.townHistory = saveData.townHistory || [];
}
