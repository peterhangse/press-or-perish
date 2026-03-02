/**
 * MAIN — Entry point, game loop, screen wiring
 * Press or Perish · Roguelike Journalism Game
 */

import * as GameState from './engine/game-state.js';
import * as DayGenerator from './engine/day-generator.js';
import * as ScoringEngine from './engine/scoring-engine.js';
import * as CompetitorAI from './engine/competitor-ai.js';
import * as DataLoader from './engine/data-loader.js';
import * as ScreenManager from './ui/screen-manager.js';
import * as Components from './ui/components.js';
import * as Onboarding from './ui/onboarding.js';
import * as DeskScreen from './ui/desk-screen.js';
import * as InterviewScreen from './ui/interview-screen.js';
import * as PublishScreen from './ui/publish-screen.js';
import * as ResultsScreen from './ui/results-screen.js';
import * as TransitionScreen from './ui/transition-screen.js';
import * as GameOverScreen from './ui/gameover-screen.js';
import * as AudioManager from './engine/audio-manager.js';
import * as SFX from './engine/sfx-engine.js';
import * as Achievements from './engine/achievements.js';
import * as AchievementsUI from './ui/achievements-ui.js';

// — Game data cache —
let gameData = null;
let state = null;
let activeTownConfig = null; // current town config from towns.json

/**
 * Get the active town config, setting it from state if needed
 */
function getTownConfig() {
  if (!activeTownConfig && gameData?.towns && state) {
    activeTownConfig = DataLoader.getTownConfig(gameData.towns, state.currentTown);
  }
  return activeTownConfig;
}

/**
 * Get the boss dialogue for the current town
 */
function getBossDialogue() {
  const townId = state?.currentTown || 'smastad';
  return gameData.boss?.[townId] || gameData.boss?.['smastad'] || gameData.boss;
}

/**
 * Get stories filtered for the current town
 */
function getTownStories() {
  return DataLoader.getStoriesByTown(gameData.stories, state?.currentTown || 'smastad');
}

// — Init —
async function boot() {
  // Scale canvas to fit browser — listen on visualViewport too for mobile
  scaleCanvas();
  window.addEventListener('resize', scaleCanvas);
  if (window.visualViewport) {
    window.visualViewport.addEventListener('resize', scaleCanvas);
  }

  // Initialize screen manager
  ScreenManager.init();

  // Load all game data
  try {
    gameData = await DataLoader.loadAllData();
    console.log(`Loaded ${gameData.stories.length} stories, ${gameData.npcs.length} NPCs, ${gameData.towns.length} towns`);
  } catch (e) {
    console.error('Failed to load game data:', e);
    return;
  }

  // Build persistent UI
  Components.buildWeekStrip();

  // Wire start screen
  document.getElementById('btn-new-run').addEventListener('click', () => { SFX.play('click'); startNewRun(); });
  document.getElementById('btn-tutorial').addEventListener('click', () => { SFX.play('click'); startTutorial(); });

  // Wire continue button (resume saved game)
  document.getElementById('btn-continue').addEventListener('click', () => { SFX.play('click'); resumeSavedGame(); });
  refreshContinueButton();

  // Add persistent mute button on the game-wrapper (visible across all screens)
  addMuteButton();
  const muteBtn = document.getElementById('mute-btn');
  if (muteBtn) muteBtn.style.display = 'none';

  // Add achievements button (visible across all screens)
  AchievementsUI.addAchievementButton();

  // Add dev skip buttons
  addDevButtons();

  // Title logo-button: click to start music + reveal menu
  const titleEl = document.getElementById('start-title');
  const revealEl = document.getElementById('start-reveal');
  titleEl.addEventListener('click', () => {
    if (titleEl.classList.contains('settled')) return;
    // Warm up SFX AudioContext on first gesture
    SFX.warmUp();
    SFX.play('click');
    // Start title music
    AudioManager.play('title');
    // Settle title and reveal menu
    titleEl.classList.add('settled');
    setTimeout(() => {
      revealEl.classList.add('visible');
      if (muteBtn) muteBtn.style.display = '';
      AchievementsUI.showButton();
      // Show dev buttons
      const devBtn = document.getElementById('dev-skip-btn');
      if (devBtn) devBtn.style.display = '';
    }, 400);
  });

  // Wire onboarding complete event
  document.addEventListener('onboarding-complete', (e) => {
    const name = e.detail?.playerName || '';
    if (name) {
      state.playerName = name;
      localStorage.setItem('pop_player_name', name);
    }
    startDayZero();
  });

  // Show best score if exists
  const best = localStorage.getItem('pop_best_score');
  if (best) {
    document.getElementById('start-bestscore').textContent = `Best: ${best} pts`;
  }

  // Wire highscore button
  document.getElementById('btn-highscores').addEventListener('click', () => {
    SFX.play('click');
    showHighscoreBoard();
  });

  // Show start screen
  ScreenManager.switchTo('start');
}

/**
 * Scale the 640×360 canvas to fit the browser
 * Uses visualViewport when available (handles mobile keyboard, address bar)
 */
function scaleCanvas() {
  const wrapper = document.getElementById('game-wrapper');
  const hudH = 34;
  const vw = window.visualViewport ? window.visualViewport.width : window.innerWidth;
  const vh = window.visualViewport ? window.visualViewport.height : window.innerHeight;
  const sx = vw / 640;
  const sy = vh / (360 + hudH);
  const s = Math.min(sx, sy);
  wrapper.style.transform = `translate(-50%, -50%) scale(${s})`;
}

/**
 * Start a new run (skip onboarding + day zero)
 */
function startNewRun() {
  // Clear any existing save — fresh run
  GameState.clearSave();
  refreshContinueButton();

  state = GameState.createState();
  state.runNumber = (parseInt(localStorage.getItem('pop_run_count') || '0')) + 1;
  localStorage.setItem('pop_run_count', state.runNumber);

  // Set town config for first town
  activeTownConfig = DataLoader.getTownConfig(gameData.towns, state.currentTown);

  // Switch to game soundtrack (looped)
  AudioManager.play('game');

  // Ask for name before starting
  showNamePrompt((name) => {
    state.playerName = name;
    localStorage.setItem('pop_player_name', name);
    startDay(1);
  });
}

/**
 * Start tutorial (onboarding + day zero)
 */
function startTutorial() {
  state = GameState.createState();
  state.runNumber = (parseInt(localStorage.getItem('pop_run_count') || '0')) + 1;
  localStorage.setItem('pop_run_count', state.runNumber);

  // Set town config for first town
  activeTownConfig = DataLoader.getTownConfig(gameData.towns, state.currentTown);

  // Switch to game soundtrack (looped)
  AudioManager.play('game');

  Onboarding.start();
}

/**
 * Day Zero — Tutorial day (runs once after onboarding)
 * 3 easy leads (1 per source type), restricted Q1 options,
 * competitor shock ending, does NOT affect real deficit.
 */
function startDayZero() {
  state.day = 0;
  GameState.resetDay(state);

  Components.updateWeekStrip(0, []);
  Components.updateDeficitMeter(0);
  Components.updateClock('desk');

  ScreenManager.switchTo('transition', true);
  TransitionScreen.show(0, 0, () => {
    showDayZeroDesk();
  }, { townConfig: getTownConfig() });
}

/** Day Zero desk — 3 easy leads, 1 per source type */
function showDayZeroDesk() {
  const townStories = getTownStories();
  const leads = DayGenerator.generateDayZeroLeads(townStories);
  state.todayLeads = leads.map(l => l.id);

  const tc = getTownConfig();
  const bossName = tc?.bossName || 'Gunnar';
  const isIndustrial = tc?.id === 'industristad';
  const isCoastal = tc?.id === 'kuststad';

  const bossNote = isIndustrial
    ? { text: `First day at the Industristad Paper, ${pn()}. The mill owners are already watching. Pick a story — but be careful who you trust in this town.`, name: bossName }
    : isCoastal
    ? { text: `First day at the Kuststad Paper, ${pn()}. The shipping company owns half this town and Sjöfartstidningen prints whatever they're told. Pick a story — but watch the tides.`, name: bossName }
    : { text: `It's your first day at work, ${pn()}. We expect nothing today. See this as a test for tomorrow... Pick a story.`, name: bossName };

  ScreenManager.switchTo('desk', true);
  Components.updateClock('desk');
  DeskScreen.render(leads, 0, bossNote, (selectedStory) => {
    startDayZeroInterview(selectedStory);
  }, getTownConfig());
}

/** Day Zero interview — first interview has 2 of 4 Q1 options grayed out */
function startDayZeroInterview(story) {
  state.selectedLead = story.id;
  state.usedStoryIds.push(story.id);

  const npc = DataLoader.getNPC(gameData.npcs, story.npc_id) || {
    id: story.npc_id,
    name: story.npc_name || 'Unknown',
    title: story.npc_title || '',
    initial_demeanor: 'Guarded',
  };

  ScreenManager.switchTo('interview', true);
  Components.updateClock('interview');

  // Gray out the last 2 Q1 archetypes (pressure & silence) for the tutorial
  InterviewScreen.start(story, npc, (result) => {
    state.tierReached = result.tier;
    state.pointsEarned = result.points;
    state.q1Choice = result.q1Archetype;
    state.q2Choice = result.q2Index;
    state.baseValue = story.base_value || 0;
    showDayZeroPublish(story, result);
  }, { disabledArchetypes: ['pressure', 'silence'], townConfig: getTownConfig() });
}

/** Day Zero publish — same as normal but leads to competitor shock */
function showDayZeroPublish(story, interviewResult) {
  // Competitor gets a massive score for the shock effect
  state.competitorScore = 14;

  // Headline scoring disabled — auto-pick first headline
  state.headlineChosen = 0;
  state.headlineBonus = 0;

  // Skip sleep screen — go straight to results
  showDayZeroResults(story, interviewResult);
}

/** Day Zero results — competitor shock, then start real Day 1 */
function showDayZeroResults(story, interviewResult) {
  ScreenManager.switchTo('results', true);
  Components.updateClock('results');

  const tc = getTownConfig();
  const isIndustrial = tc?.id === 'industristad';
  const isCoastal = tc?.id === 'kuststad';
  const playerHeadlineText = interviewResult.headlines[state.headlineChosen]?.text || story.title;

  const competitorHeadline = isIndustrial
    ? 'FACTORY WHISTLEBLOWER REVEALS DECADE OF SAFETY VIOLATIONS'
    : isCoastal
    ? 'COAST GUARD WHISTLEBLOWER REVEALS YEARS OF HARBOR SMUGGLING'
    : 'COUNTY CORRUPTION RING EXPOSED — THREE OFFICIALS ARRESTED';

  const dayZeroNote = isIndustrial
    ? 'Same rules as Småstad — but the stakes are higher. Your story has a base value, and your interview technique determines the rest.'
    : isCoastal
    ? 'Same rules as before — but the harbor has deeper secrets. Your story has a base value, and your interview technique determines the rest.'
    : 'This is your score. The story itself has a base value — but how you handle the interview decides the rest. Choose your approach wisely.';

  const bossQuoteText = isIndustrial
    ? `The deficit works the same way, ${pn()}. Stay above -10 or the Industristad Paper folds. Fabriksbladet won\'t go easy on you.`
    : isCoastal
    ? `The deficit works the same way, ${pn()}. Stay above -10 or the Kuststad Paper folds. Sjöfartstidningen has the shipping company\'s money behind them.`
    : `See that number? That\'s the deficit, ${pn()}. Stay above -10 or the paper closes. Every day is a fight.`;

  const competitorShockText = isIndustrial
    ? `${tc.competitorName} ran an industry exposé on their front page. They have sources inside the mill. You need to build your own.`
    : isCoastal
    ? `${tc.competitorName} ran a harbor exposé on their front page. They have sources inside the coast guard. You'll need to find your own.`
    : `${tc?.competitorName || 'Regionbladet'} ran a massive scoop. This is the competition you\'re up against — every single day.`;

  ResultsScreen.render({
    playerHeadline: playerHeadlineText,
    playerScore: state.pointsEarned,
    competitorScore: state.competitorScore,
    competitorHeadline,
    deficitBefore: 0,
    deficitAfter: 0,  // Day Zero doesn't affect real deficit
    baseValue: story.base_value,
    tierBonus: (interviewResult.q1Bonus || 0) + (interviewResult.q2Bonus || 0),
    q1Bonus: interviewResult.q1Bonus || 0,
    q2Bonus: interviewResult.q2Bonus || 0,
    headlineBonus: state.headlineBonus || 0,
    tier: state.tierReached,
    day: 0,
    isDayZero: true,
    dayZeroNote1: dayZeroNote,
    bossQuote: bossQuoteText,
    competitorShock: competitorShockText,
    paperName: tc?.newspaperName || 'Småstad Paper',
    bossName: tc?.bossName || 'Gunnar',
    competitorName: tc?.competitorName || 'Regionbladet',
    townName: tc?.name || 'Småstad',
    onContinue: () => {
      // Reset state cleanly — Day Zero doesn't count toward score
      state.deficit = 0;
      // Keep the day-zero story in usedStoryIds so it won't appear again
      const dayZeroStoryId = state.selectedLead;
      state.usedStoryIds = dayZeroStoryId ? [dayZeroStoryId] : [];
      state.dayHistory = [];
      startDay(1);
    },
  });
}

/**
 * Start a new day
 */
function startDay(dayNum) {
  state.day = dayNum;
  GameState.resetDay(state);

  // Auto-save at the start of each real day (skip Day Zero)
  if (dayNum >= 1) {
    GameState.saveToLocalStorage(state);
  }

  // Update persistent UI
  Components.updateWeekStrip(state.day, state.dayHistory);
  Components.updateDeficitMeter(state.deficit);
  Components.updateClock('desk');

  // Show day transition
  ScreenManager.switchTo('transition', true);
  TransitionScreen.show(state.day, state.deficit, () => {
    // After transition, show desk
    showDesk();
  }, { townConfig: getTownConfig() });
}

/**
 * Show the morning desk with leads
 */
function showDesk() {
  // Generate today's leads (filtered by current town)
  const townStories = getTownStories();
  const leads = DayGenerator.generateDayLeads(state.day, townStories, state.usedStoryIds);
  state.todayLeads = leads.map(l => l.id);

  // Get boss note for today
  const bossNote = getBossNote(state.day, state.deficit);

  // Render desk
  ScreenManager.switchTo('desk', true);
  Components.updateClock('desk');
  DeskScreen.render(leads, state.day, bossNote, (selectedStory) => {
    startInterview(selectedStory);
  }, getTownConfig());
}

/**
 * Start an interview with the selected story's NPC
 */
function startInterview(story) {
  state.selectedLead = story.id;
  state.usedStoryIds.push(story.id);

  // Find NPC for this story
  const npc = DataLoader.getNPC(gameData.npcs, story.npc_id) || {
    id: story.npc_id,
    name: story.npc_name || 'Unknown',
    title: story.npc_title || '',
    initial_demeanor: 'Guarded',
  };

  // Switch to interview
  ScreenManager.switchTo('interview', true);
  Components.updateClock('interview');

  InterviewScreen.start(story, npc, (result) => {
    // Interview complete — store results
    state.tierReached = result.tier;
    state.pointsEarned = result.points;
    state.q1Choice = result.q1Archetype;
    state.q2Choice = result.q2Index;
    state.baseValue = story.base_value;

    // Move to publish
    showPublish(story, result);
  }, { townConfig: getTownConfig() });
}

/**
 * Show the publish/headline screen
 */
function showPublish(story, interviewResult) {
  // Generate competitor score
  state.competitorScore = CompetitorAI.generateCompetitorScore(state.day, getTownConfig());

  // Headline scoring disabled — auto-pick first headline
  state.headlineChosen = 0;
  state.headlineBonus = 0;

  // Calculate deficit
  const delta = ScoringEngine.calculateDeficitDelta(state.pointsEarned, state.competitorScore);
  const deficitBefore = state.deficit;
  state.deficit = ScoringEngine.applyDeficit(state.deficit, delta);

  // Record in history
  GameState.recordDay(state);

  // Check daily achievements
  checkAndShowAchievements('day_end');

  // Skip sleep screen — go straight to results
  showResults(story, interviewResult, deficitBefore);
}

/**
 * Show end-of-day results
 */
function showResults(story, interviewResult, deficitBefore) {
  ScreenManager.switchTo('results', true);
  Components.updateClock('results');
  Components.updateDeficitMeter(deficitBefore);
  Components.updateWeekStrip(state.day, state.dayHistory);

  const playerHeadlineText = interviewResult.headlines[state.headlineChosen]?.text || story.title;
  const tc = getTownConfig();
  const competitorHeadline = CompetitorAI.getCompetitorHeadline(state.competitorScore, tc);

  ResultsScreen.render({
    playerHeadline: playerHeadlineText,
    playerScore: state.pointsEarned,
    competitorScore: state.competitorScore,
    competitorHeadline,
    deficitBefore,
    deficitAfter: state.deficit,
    baseValue: story.base_value,
    tierBonus: (interviewResult.q1Bonus || 0) + (interviewResult.q2Bonus || 0),
    q1Bonus: interviewResult.q1Bonus || 0,
    q2Bonus: interviewResult.q2Bonus || 0,
    headlineBonus: state.headlineBonus || 0,
    tier: state.tierReached,
    day: state.day,
    bossQuote: getStoryBossQuote(story, state.tierReached) || getBossQuote(state.deficit, state.day),
    paperName: tc?.newspaperName || 'Småstad Paper',
    bossName: tc?.bossName || 'Gunnar',
    competitorName: tc?.competitorName || 'Regionbladet',
    townName: tc?.name || 'Småstad',
    onPhase2: () => {
      Components.updateDeficitMeter(state.deficit);
    },
    onContinue: () => {
      // Check game over
      if (GameState.isPerished(state)) {
        showGameOver();
      } else if (state.day >= 5) {
        // Check if there's a next town to advance to
        const nextTown = DataLoader.getNextTown(gameData.towns, state.currentTown);
        if (nextTown) {
          showTownAdvance(nextTown);
        } else {
          showEnding();
        }
      } else {
        startDay(state.day + 1);
      }
    },
  });
}

/**
 * Show game over — perished
 */
function showGameOver() {
  // Clear save — run is over
  GameState.clearSave();

  // Switch to perish soundtrack
  AudioManager.play('perish');

  ScreenManager.switchTo('gameover', true);
  ScreenManager.flash();

  // Save to highscore board (cumulative across all towns)
  const runStats = getRunStats();
  saveHighscore(runStats.totalPoints, runStats.totalDays, runStats.avgPoints, false);

  // Check game-over achievements
  checkAndShowAchievements('game_over');

  const perishRunStats = getRunStats();
  GameOverScreen.showPerished({
    finalDeficit: state.deficit,
    daysCompleted: state.day,
    dayHistory: state.dayHistory,
    townHistory: state.townHistory,
    currentTownId: state.currentTown,
    runStats: perishRunStats,
    playerName: pn(),
    paperName: getTownConfig()?.newspaperName || 'Småstad Paper',
    bossName: getTownConfig()?.bossName || 'Gunnar',
    competitorName: getTownConfig()?.competitorName || 'Regionbladet',
    townName: getTownConfig()?.name || 'Småstad',
    onRestart: () => {
      returnToStart();
    },
  });
}

/**
 * Show ending — survived the week
 */
function showEnding() {
  // Clear save — run is over
  GameState.clearSave();

  // Switch to perish/survive soundtrack
  AudioManager.play('perish');

  ScreenManager.switchTo('gameover');

  // Save best score (cumulative across all towns)
  const runStats = getRunStats();
  const best = parseInt(localStorage.getItem('pop_best_score') || '0');
  if (runStats.totalPoints > best) {
    localStorage.setItem('pop_best_score', runStats.totalPoints);
  }

  // Save to highscore board
  saveHighscore(runStats.totalPoints, runStats.totalDays, runStats.avgPoints, true);

  // Check game-over achievements
  checkAndShowAchievements('game_over');

  GameOverScreen.showSurvived({
    finalDeficit: state.deficit,
    dayHistory: state.dayHistory,
    townHistory: state.townHistory,
    currentTownId: state.currentTown,
    runStats: runStats,
    playerName: pn(),
    paperName: getTownConfig()?.newspaperName || 'Småstad Paper',
    bossName: getTownConfig()?.bossName || 'Gunnar',
    competitorName: getTownConfig()?.competitorName || 'Regionbladet',
    townName: getTownConfig()?.name || 'Småstad',
    onRestart: () => {
      returnToStart();
    },
  });
}

/**
 * Check achievements and show unlock animations
 * @param {string} trigger - 'day_end' or 'game_over'
 */
function checkAndShowAchievements(trigger) {
  if (!state || state.day === 0) return; // skip day zero

  const totalPoints = state.dayHistory.reduce((sum, d) => sum + d.points, 0);
  const ctx = {
    trigger,
    day: state.day,
    storyId: state.selectedLead,
    q1Archetype: state.q1Choice,
    q2Index: state.q2Choice,
    tier: state.tierReached,
    points: state.pointsEarned,
    baseValue: state.baseValue || 0,
    competitorScore: state.competitorScore,
    deficit: state.deficit,
    dayHistory: state.dayHistory,
    survived: trigger === 'game_over' && GameState.hasSurvived(state),
    totalPoints,
  };

  const newlyUnlocked = Achievements.checkAchievements(trigger, ctx);
  if (newlyUnlocked.length > 0) {
    AchievementsUI.showUnlocks(newlyUnlocked);
  }
}

/**
 * Pick a random item from an array (or return the string as-is).
 * Avoids repeats within the same week by checking usedList.
 */
function pickUnused(pool, usedList) {
  if (typeof pool === 'string') return pool;
  if (!Array.isArray(pool) || pool.length === 0) return '';
  const available = pool.filter(q => !usedList.includes(q));
  const source = available.length > 0 ? available : pool; // fallback: allow repeats if all used
  const pick = source[Math.floor(Math.random() * source.length)];
  usedList.push(pick);
  return pick;
}

/**
 * Get boss note for the desk based on day and deficit
 */
function getBossNote(day, deficit) {
  const bossDialogue = getBossDialogue();
  const notes = bossDialogue?.desk_notes;
  if (!notes) return null;

  const bossName = getTownConfig()?.bossName || 'Gunnar';

  // Check deficit-specific notes first
  if (deficit <= -10 && notes.danger) {
    return { text: injectName(pickUnused(notes.danger, state.usedBossNotes)), name: bossName };
  }
  if (deficit <= -5 && notes.warning) {
    return { text: injectName(pickUnused(notes.warning, state.usedBossNotes)), name: bossName };
  }

  // Day-specific notes
  const dayPool = notes[`day_${day}`];
  if (dayPool) {
    return { text: injectName(pickUnused(dayPool, state.usedBossNotes)), name: bossName };
  }

  return { text: injectName(pickUnused(notes.default || 'Deliver.', state.usedBossNotes)), name: bossName };
}

/**
 * Get story-specific boss quote if the story has boss_result_quotes.
 * Tier 0-1 = positive (soft coverage), Tier 2-3 = negative (exposed the hunters).
 */
function getStoryBossQuote(story, tier) {
  const overrides = story.boss_result_quotes;
  if (!overrides) return null;
  const pool = tier >= 2 ? overrides.negative : overrides.positive;
  if (!pool || pool.length === 0) return null;
  return injectName(pool[Math.floor(Math.random() * pool.length)]);
}

/**
 * Get boss quote for results based on deficit
 */
function getBossQuote(deficit, day) {
  const bossDialogue = getBossDialogue();
  const quotes = bossDialogue?.result_quotes;
  if (!quotes) return '';

  let pool;
  if (deficit <= -12)     pool = quotes.critical;
  else if (deficit <= -8) pool = quotes.bad;
  else if (deficit <= -3) pool = quotes.warning;
  else if (deficit >= 5)  pool = quotes.great;
  else if (deficit >= 2)  pool = quotes.good;
  else                    pool = quotes.neutral;

  if (!pool) return injectName('Tomorrow again.');
  return injectName(pickUnused(pool, state.usedBossQuotes));
}

/**
 * Player name shorthand — returns the name or 'kid' as fallback
 */
function pn() {
  return state?.playerName || localStorage.getItem('pop_player_name') || 'kid';
}

/**
 * Inject player name into a text string (replaces {name} or 'kid')
 */
function injectName(text) {
  const name = pn();
  // Replace {name} placeholders if any
  let result = text.replace(/\{name\}/g, name);
  return result;
}

/**
 * Compute cumulative run stats across all towns (townHistory + current)
 */
function getRunStats() {
  // Gather all day histories from completed towns + current
  const allDays = [
    ...(state.townHistory || []).flatMap(t => t.dayHistory || []),
    ...state.dayHistory,
  ];
  const totalPoints = allDays.reduce((sum, d) => sum + d.points, 0);
  const totalDays = allDays.length;
  const avgPoints = totalDays > 0 ? Math.round((totalPoints / totalDays) * 10) / 10 : 0;
  return { totalPoints, totalDays, avgPoints };
}

/**
 * Save a completed run to the highscore board
 */
function saveHighscore(totalPoints, totalDays, avgPoints, survived) {
  const entries = JSON.parse(localStorage.getItem('pop_highscores') || '[]');
  entries.push({
    name: pn(),
    points: totalPoints,
    days: totalDays,
    avg: avgPoints,
    survived,
    date: new Date().toISOString(),
  });
  // Keep max 50 entries
  if (entries.length > 50) entries.splice(0, entries.length - 50);
  localStorage.setItem('pop_highscores', JSON.stringify(entries));
}

/**
 * Show the highscore board modal
 */
function showHighscoreBoard() {
  const startScreen = document.getElementById('screen-start');
  const existing = startScreen.querySelector('.highscore-overlay');
  if (existing) existing.remove();

  const entries = JSON.parse(localStorage.getItem('pop_highscores') || '[]');
  // Sort by points descending
  entries.sort((a, b) => b.points - a.points);

  const overlay = document.createElement('div');
  overlay.className = 'highscore-overlay';

  const card = document.createElement('div');
  card.className = 'highscore-card';

  const title = document.createElement('div');
  title.className = 'highscore-title';
  title.textContent = 'PRESS ARCHIVE';
  card.appendChild(title);

  if (entries.length === 0) {
    const empty = document.createElement('div');
    empty.className = 'highscore-empty';
    empty.textContent = 'No completed runs yet.';
    card.appendChild(empty);
  } else {
    const table = document.createElement('div');
    table.className = 'highscore-table';

    // Header row
    const header = document.createElement('div');
    header.className = 'highscore-row highscore-header';
    header.innerHTML = '<span>#</span><span>Reporter</span><span>Points</span><span>Days</span><span>Avg</span><span>Date</span>';
    table.appendChild(header);

    entries.forEach((entry, i) => {
      const row = document.createElement('div');
      row.className = `highscore-row ${entry.survived ? 'survived' : 'perished'}`;

      const rank = document.createElement('span');
      rank.textContent = i + 1;

      const name = document.createElement('span');
      name.className = 'highscore-name';
      name.textContent = entry.name;

      const pts = document.createElement('span');
      pts.textContent = entry.points;

      const days = document.createElement('span');
      days.textContent = entry.days;

      const avg = document.createElement('span');
      avg.textContent = entry.avg != null ? entry.avg : (entry.days > 0 ? Math.round((entry.points / entry.days) * 10) / 10 : 0);

      const date = document.createElement('span');
      date.className = 'highscore-date';
      const d = new Date(entry.date);
      date.textContent = `${d.getFullYear()}-${String(d.getMonth()+1).padStart(2,'0')}-${String(d.getDate()).padStart(2,'0')} ${String(d.getHours()).padStart(2,'0')}:${String(d.getMinutes()).padStart(2,'0')}`;

      row.appendChild(rank);
      row.appendChild(name);
      row.appendChild(pts);
      row.appendChild(days);
      row.appendChild(avg);
      row.appendChild(date);
      table.appendChild(row);
    });

    card.appendChild(table);
  }

  const closeBtn = document.createElement('button');
  closeBtn.className = 'btn-paper highscore-close';
  closeBtn.textContent = 'Close';
  closeBtn.addEventListener('click', () => {
    SFX.play('click');
    overlay.remove();
  });
  card.appendChild(closeBtn);

  overlay.appendChild(card);
  overlay.addEventListener('click', (e) => {
    if (e.target === overlay) overlay.remove();
  });
  startScreen.appendChild(overlay);
}

/**
 * Show a quick name prompt for New Game (no tutorial)
 */
function showNamePrompt(callback) {
  const startScreen = document.getElementById('screen-start');
  // Create modal overlay
  const overlay = document.createElement('div');
  overlay.className = 'name-prompt-overlay';
  
  const card = document.createElement('div');
  card.className = 'name-prompt-card';
  
  const label = document.createElement('div');
  label.className = 'name-prompt-label';
  label.textContent = 'YOUR NAME, REPORTER';
  
  const input = document.createElement('input');
  input.type = 'text';
  input.className = 'name-prompt-input';
  input.maxLength = 24;
  const savedName = localStorage.getItem('pop_player_name') || '';
  if (savedName) input.value = savedName;
  input.placeholder = 'Type your name...';
  
  const btn = document.createElement('button');
  btn.className = 'btn-paper name-prompt-btn';
  btn.textContent = 'LET\'S GO';
  btn.disabled = !savedName;
  btn.style.opacity = savedName ? '' : '0.35';
  
  input.addEventListener('input', () => {
    const hasName = input.value.trim().length > 0;
    btn.disabled = !hasName;
    btn.style.opacity = hasName ? '' : '0.35';
  });
  
  function submit() {
    const name = input.value.trim();
    if (!name) return;
    SFX.play('stamp');
    overlay.remove();
    callback(name);
  }
  
  btn.addEventListener('click', submit);
  input.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') submit();
  });
  
  card.appendChild(label);
  card.appendChild(input);
  card.appendChild(btn);
  overlay.appendChild(card);
  startScreen.appendChild(overlay);
  
  setTimeout(() => input.focus(), 100);
}

/**
 * Resume a saved game from localStorage
 */
function resumeSavedGame() {
  const saveData = GameState.loadFromLocalStorage();
  if (!saveData) return;

  state = GameState.createState();
  GameState.restoreFromSave(state, saveData);

  // Set town config from saved town
  activeTownConfig = DataLoader.getTownConfig(gameData.towns, state.currentTown);

  // Switch to game soundtrack (looped)
  AudioManager.play('game');

  // Jump straight to the saved day
  startDay(saveData.day);
}

/**
 * Show or hide the Continue button based on whether a save exists.
 * When save exists, demote New Game to secondary styling.
 */
function refreshContinueButton() {
  const btnContinue = document.getElementById('btn-continue');
  const btnNewRun = document.getElementById('btn-new-run');
  const saveInfo = document.getElementById('start-save-info');
  const saveData = GameState.loadFromLocalStorage();

  if (saveData) {
    btnContinue.style.display = '';
    btnNewRun.classList.add('start-btn-secondary');
    // Show save info with town name
    const dayNames = ['', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'];
    const dayLabel = dayNames[saveData.day] || `Day ${saveData.day}`;
    const townLabel = saveData.currentTown ? ` · ${saveData.currentTown.charAt(0).toUpperCase() + saveData.currentTown.slice(1)}` : '';
    saveInfo.textContent = `${dayLabel} · Deficit: ${saveData.deficit}${townLabel}`;
    saveInfo.style.display = '';
  } else {
    btnContinue.style.display = 'none';
    btnNewRun.classList.remove('start-btn-secondary');
    saveInfo.style.display = 'none';
  }
}

/**
 * Show town advance screen when player completes a town and there's a next one
 */
function showTownAdvance(nextTown) {
  // Save the current run is over for this town
  GameState.clearSave();

  // Check game-over achievements
  checkAndShowAchievements('game_over');

  // Advance game state to next town
  GameState.advanceToNextTown(state, nextTown.id);
  activeTownConfig = DataLoader.getTownConfig(gameData.towns, state.currentTown);

  // Save state at new town start
  GameState.saveToLocalStorage(state);
  refreshContinueButton();

  // Show full onboarding cutscene for the new town
  Onboarding.startTownAdvance(activeTownConfig, pn(), () => {
    // If this town has a Day Zero, run it before Day 1
    if (activeTownConfig.dayZeroDate) {
      startDayZero();
    } else {
      startDay(1);
    }
  });
}

/**
 * Return to start screen with title music
 */
function returnToStart() {
  AudioManager.play('title');
  ScreenManager.switchTo('start');
  // Re-settle the title so the menu is visible
  const titleEl = document.getElementById('start-title');
  const revealEl = document.getElementById('start-reveal');
  if (titleEl) titleEl.classList.add('settled');
  if (revealEl) revealEl.classList.add('visible');
  // Update continue button state
  refreshContinueButton();
}

/**
 * Add dev-mode skip button (below mute) for jumping to a specific town
 */
function addDevButtons() {
  const wrapper = document.getElementById('game-wrapper');
  const btn = document.createElement('button');
  btn.id = 'dev-skip-btn';
  btn.className = 'dev-btn';
  btn.textContent = '⚙ Skip to town';
  btn.style.display = 'none'; // hidden until title click
  btn.addEventListener('click', () => {
    SFX.play('click');
    // Cycle through available dev towns
    const devTowns = ['industristad', 'kuststad'];
    const current = btn.dataset.devTown || 'industristad';
    startDevTown(current);
  });
  // Right-click to cycle target town
  btn.addEventListener('contextmenu', (e) => {
    e.preventDefault();
    const devTowns = ['industristad', 'kuststad'];
    const current = btn.dataset.devTown || 'industristad';
    const idx = devTowns.indexOf(current);
    const next = devTowns[(idx + 1) % devTowns.length];
    btn.dataset.devTown = next;
    btn.textContent = `⚙ ${next.charAt(0).toUpperCase() + next.slice(1)}`;
    SFX.play('click');
  });
  btn.dataset.devTown = 'industristad';
  btn.textContent = '⚙ Industristad';
  wrapper.appendChild(btn);
}

/**
 * Dev: start a run directly in a specific town, skipping earlier towns
 */
function startDevTown(townId) {
  GameState.clearSave();
  refreshContinueButton();

  state = GameState.createState();
  state.runNumber = (parseInt(localStorage.getItem('pop_run_count') || '0')) + 1;
  localStorage.setItem('pop_run_count', state.runNumber);

  // Jump state to the requested town
  const townIdx = gameData.towns.findIndex(t => t.id === townId);
  if (townIdx > 0) {
    // Fake surviving previous towns
    for (let i = 0; i < townIdx; i++) {
      const prevTown = gameData.towns[i];
      state.townHistory.push({ townId: prevTown.id, deficit: 0, dayHistory: [], survived: true });
    }
    state.currentTown = townId;
    state.townIndex = townIdx;
  }
  activeTownConfig = DataLoader.getTownConfig(gameData.towns, state.currentTown);

  AudioManager.play('game');
  showNamePrompt((name) => {
    state.playerName = name;
    localStorage.setItem('pop_player_name', name);
    // Run the town's onboarding cutscene, then Day Zero or Day 1
    Onboarding.startTownAdvance(activeTownConfig, name, () => {
      if (activeTownConfig.dayZeroDate) {
        startDayZero();
      } else {
        startDay(1);
      }
    });
  });
}

/**
 * Add persistent mute button on game-wrapper (visible across all screens)
 */
function addMuteButton() {
  const wrapper = document.getElementById('game-wrapper');
  const btn = document.createElement('button');
  btn.id = 'mute-btn';
  btn.className = 'mute-btn';
  const label = () => AudioManager.isMuted() ? '<span class="mute-note">\u266a</span> off' : '<span class="mute-note">\u266a</span> on';
  btn.innerHTML = label();
  btn.addEventListener('click', () => {
    const muted = AudioManager.toggleMute();
    btn.innerHTML = muted ? '<span class="mute-note">\u266a</span> off' : '<span class="mute-note">\u266a</span> on';
    btn.classList.toggle('muted', muted);
  });
  if (AudioManager.isMuted()) btn.classList.add('muted');
  wrapper.appendChild(btn);
}

// — BOOT —
boot();
