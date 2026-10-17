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
  dayResolved: null,     // { tier, points, q1Bonus, q2Bonus, perish, q1Archetype, q2Index } once Q2 is answered
  deficitBefore: 0,      // deficit at the start of today (for the results screen)
  scoop: null,           // { storyId, title } — a lead you passed on that the competitor ran today
  carryOverLeadId: null, // a lead you passed on yesterday that is still open today
  perishCause: null,     // text explaining an instant firing

  // History
  dayHistory: [],  // [{day, storyId, tier, points, competitorScore, deficit, headline}]
  usedStoryIds: [], // prevent repeats
  usedBossQuotes: [], // prevent repeat boss quotes within a week
  usedBossNotes: [],  // prevent repeat boss desk notes within a week
  npcMemory: {},      // { npcId: { title, tier, expression } } — sources remember earlier meetings this run

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
  state.dayResolved = null;
  state.deficitBefore = state.deficit;
  state.scoop = null;
  state.perishCause = null;
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
  state.carryOverLeadId = null;
  resetDay(state);
}

// — Save / Load (localStorage) —

const SAVE_KEY = 'pop_save';
const SAVE_VERSION = 3;

/**
 * Persist current run state to localStorage.
 * Called at every commitment point of a day (day start, leads dealt, lead
 * picked, opening question, answer resolved) so a reload can never undo a
 * decision or re-deal the desk. Skips Day Zero.
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
    npcMemory: state.npcMemory,
    carryOverLeadId: state.carryOverLeadId,
    // Progress within the current day
    todayLeads: state.todayLeads,
    selectedLead: state.selectedLead,
    q1Choice: state.q1Choice,
    dayResolved: state.dayResolved,
    competitorScore: state.competitorScore,
    deficitBefore: state.deficitBefore,
    scoop: state.scoop,
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
    if (!data || ![1, 2, SAVE_VERSION].includes(data.saveVersion)) return null;
    // v1 → v2: add town fields with defaults
    if (data.saveVersion === 1) {
      data.currentTown = data.currentTown || 'smastad';
      data.townIndex = data.townIndex || 0;
      data.townHistory = data.townHistory || [];
      data.saveVersion = 2;
    }
    // v2 → v3: in-day progress fields (a v2 save was always written at day start)
    if (data.saveVersion === 2) {
      data.npcMemory = {};
      data.carryOverLeadId = null;
      data.todayLeads = [];
      data.selectedLead = null;
      data.q1Choice = null;
      data.dayResolved = null;
      data.competitorScore = 0;
      data.deficitBefore = data.deficit;
      data.scoop = null;
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
  try { localStorage.removeItem(SAVE_KEY); } catch { /* ignore */ }
}

/**
 * Check if a saved game exists.
 */
export function hasSave() {
  try { return !!localStorage.getItem(SAVE_KEY); } catch { return false; }
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
  state.npcMemory = saveData.npcMemory || {};
  state.carryOverLeadId = saveData.carryOverLeadId || null;
  state.todayLeads = saveData.todayLeads || [];
  state.selectedLead = saveData.selectedLead || null;
  state.q1Choice = saveData.q1Choice || null;
  state.dayResolved = saveData.dayResolved || null;
  state.competitorScore = saveData.competitorScore || 0;
  state.deficitBefore = saveData.deficitBefore ?? saveData.deficit;
  state.scoop = saveData.scoop || null;
}

/**
 * Remember how a meeting with a source went, so they recognise the reporter later in the run.
 */
export function rememberNpc(state, npcId, storyTitle, tier, expression) {
  if (!npcId) return;
  state.npcMemory[npcId] = { title: storyTitle, tier, expression };
}

/**
 * Line shown in the interview when the source has met the reporter before (or null).
 */
export function npcMemoryLine(state, npcId) {
  const m = state.npcMemory?.[npcId];
  if (!m) return null;
  if (m.tier >= 2) return `Remembers you from "${m.title}" — you listened last time.`;
  if (['hostile', 'defiant'].includes(m.expression)) return `Remembers you from "${m.title}" — and hasn't forgotten how that went.`;
  return `Recognises you from "${m.title}".`;
}
