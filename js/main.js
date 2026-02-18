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

// — Game data cache —
let gameData = null;
let state = null;

// — Init —
async function boot() {
  // Scale canvas to fit browser
  scaleCanvas();
  window.addEventListener('resize', scaleCanvas);

  // Initialize screen manager
  ScreenManager.init();

  // Load all game data
  try {
    gameData = await DataLoader.loadAllData();
    console.log(`Loaded ${gameData.stories.length} stories, ${gameData.npcs.length} NPCs`);
  } catch (e) {
    console.error('Failed to load game data:', e);
    return;
  }

  // Build persistent UI
  Components.buildWeekStrip();

  // Wire start screen
  document.getElementById('btn-new-run').addEventListener('click', () => { AudioManager.stop(); startNewRun(); });
  document.getElementById('btn-tutorial').addEventListener('click', () => { AudioManager.stop(); startTutorial(); });

  // Add mute button (hidden until title is clicked)
  addMuteButton();
  const muteBtn = document.getElementById('mute-btn');
  if (muteBtn) muteBtn.style.display = 'none';

  // Title logo-button: click to start music + reveal menu
  const titleEl = document.getElementById('start-title');
  const revealEl = document.getElementById('start-reveal');
  titleEl.addEventListener('click', () => {
    if (titleEl.classList.contains('settled')) return;
    // Start music
    AudioManager.play();
    // Settle title and reveal menu
    titleEl.classList.add('settled');
    setTimeout(() => {
      revealEl.classList.add('visible');
      if (muteBtn) muteBtn.style.display = '';
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

  // Show start screen
  ScreenManager.switchTo('start');
}

/**
 * Scale the 640×360 canvas to fit the browser
 */
function scaleCanvas() {
  const wrapper = document.getElementById('game-wrapper');
  const hudH = 34;
  const scale = Math.min(
    window.innerWidth / 640,
    window.innerHeight / (360 + hudH)
  );
  wrapper.style.setProperty('--scale', scale);
}

/**
 * Start a new run (skip onboarding + day zero)
 */
function startNewRun() {
  state = GameState.createState();
  state.runNumber = (parseInt(localStorage.getItem('pop_run_count') || '0')) + 1;
  localStorage.setItem('pop_run_count', state.runNumber);

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
  });
}

/** Day Zero desk — 3 easy leads, 1 per source type */
function showDayZeroDesk() {
  const leads = DayGenerator.generateDayZeroLeads(gameData.stories);
  state.todayLeads = leads.map(l => l.id);

  const bossNote = { text: `It's your first day at work, ${pn()}. We expect nothing today. See this as a test for tomorrow... Pick a story.`, name: 'Gunnar' };

  ScreenManager.switchTo('desk', true);
  Components.updateClock('desk');
  DeskScreen.render(leads, 0, bossNote, (selectedStory) => {
    startDayZeroInterview(selectedStory);
  });
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
    showDayZeroPublish(story, result);
  }, { disabledArchetypes: ['pressure', 'silence'] });
}

/** Day Zero publish — same as normal but leads to competitor shock */
function showDayZeroPublish(story, interviewResult) {
  // Skip headline choice — auto-pick first headline
  state.headlineChosen = 0;

  // Competitor gets a massive score for the shock effect
  state.competitorScore = 14;

  const delta = ScoringEngine.calculateDeficitDelta(state.pointsEarned, state.competitorScore);

  ScreenManager.switchTo('publish', true);
  Components.updateClock('publish');

  PublishScreen.showSleep(0, state.pointsEarned, state.competitorScore, delta, () => {
    showDayZeroResults(story, interviewResult);
  });
}

/** Day Zero results — competitor shock, then start real Day 1 */
function showDayZeroResults(story, interviewResult) {
  ScreenManager.switchTo('results', true);
  Components.updateClock('results');

  const playerHeadlineText = interviewResult.headlines[state.headlineChosen]?.text || story.title;

  ResultsScreen.render({
    playerHeadline: playerHeadlineText,
    playerScore: state.pointsEarned,
    competitorScore: state.competitorScore,
    competitorHeadline: 'COUNTY CORRUPTION RING EXPOSED — THREE OFFICIALS ARRESTED',
    deficitBefore: 0,
    deficitAfter: 0,  // Day Zero doesn't affect real deficit
    baseValue: story.base_value,
    tierBonus: state.tierReached * 2,
    tier: state.tierReached,
    day: 0,
    isDayZero: true,
    bossQuote: `Welcome to the real world, ${pn()}. This is what we're up against.`,
    competitorShock: 'Regionbladet ran a massive scoop. This is the competition. Every day counts.',
    onContinue: () => {
      // Reset state cleanly — Day Zero doesn't count
      state.deficit = 0;
      state.usedStoryIds = [];
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

  // Update persistent UI
  Components.updateWeekStrip(state.day, state.dayHistory);
  Components.updateDeficitMeter(state.deficit);
  Components.updateClock('desk');

  // Show day transition
  ScreenManager.switchTo('transition', true);
  TransitionScreen.show(state.day, state.deficit, () => {
    // After transition, show desk
    showDesk();
  });
}

/**
 * Show the morning desk with leads
 */
function showDesk() {
  // Generate today's leads
  const leads = DayGenerator.generateDayLeads(state.day, gameData.stories, state.usedStoryIds);
  state.todayLeads = leads.map(l => l.id);

  // Get boss note for today
  const bossNote = getBossNote(state.day, state.deficit);

  // Render desk
  ScreenManager.switchTo('desk', true);
  Components.updateClock('desk');
  DeskScreen.render(leads, state.day, bossNote, (selectedStory) => {
    startInterview(selectedStory);
  });
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

    // Move to publish
    showPublish(story, result);
  });
}

/**
 * Show the publish/headline screen
 */
function showPublish(story, interviewResult) {
  // Skip headline choice — auto-pick first headline, go straight to sleep
  state.headlineChosen = 0;

  // Generate competitor score
  state.competitorScore = CompetitorAI.generateCompetitorScore(state.day);

  // Calculate deficit
  const delta = ScoringEngine.calculateDeficitDelta(state.pointsEarned, state.competitorScore);
  const deficitBefore = state.deficit;
  state.deficit = ScoringEngine.applyDeficit(state.deficit, delta);

  // Record in history
  GameState.recordDay(state);

  ScreenManager.switchTo('publish', true);
  Components.updateClock('publish');

  // Show sleep phase directly
  PublishScreen.showSleep(state.day, state.pointsEarned, state.competitorScore, delta, () => {
    showResults(story, interviewResult, deficitBefore);
  });
}

/**
 * Show end-of-day results
 */
function showResults(story, interviewResult, deficitBefore) {
  ScreenManager.switchTo('results', true);
  Components.updateClock('results');
  Components.updateDeficitMeter(state.deficit);
  Components.updateWeekStrip(state.day, state.dayHistory);

  const playerHeadlineText = interviewResult.headlines[state.headlineChosen]?.text || story.title;
  const competitorHeadline = CompetitorAI.getCompetitorHeadline(state.competitorScore);

  ResultsScreen.render({
    playerHeadline: playerHeadlineText,
    playerScore: state.pointsEarned,
    competitorScore: state.competitorScore,
    competitorHeadline,
    deficitBefore,
    deficitAfter: state.deficit,
    baseValue: story.base_value,
    tierBonus: state.tierReached * 2,
    tier: state.tierReached,
    day: state.day,
    bossQuote: getBossQuote(state.deficit, state.day),
    onContinue: () => {
      // Check game over
      if (GameState.isPerished(state)) {
        showGameOver();
      } else if (state.day >= 5) {
        showEnding();
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
  ScreenManager.switchTo('gameover', true);
  ScreenManager.flash();

  GameOverScreen.showPerished({
    finalDeficit: state.deficit,
    daysCompleted: state.day,
    dayHistory: state.dayHistory,
    playerName: pn(),
    onRestart: () => {
      ScreenManager.switchTo('start');
    },
  });
}

/**
 * Show ending — survived the week
 */
function showEnding() {
  ScreenManager.switchTo('gameover');

  // Save best score
  const totalPoints = state.dayHistory.reduce((sum, d) => sum + d.points, 0);
  const best = parseInt(localStorage.getItem('pop_best_score') || '0');
  if (totalPoints > best) {
    localStorage.setItem('pop_best_score', totalPoints);
  }

  GameOverScreen.showSurvived({
    finalDeficit: state.deficit,
    dayHistory: state.dayHistory,
    playerName: pn(),
    onRestart: () => {
      ScreenManager.switchTo('start');
    },
  });
}

/**
 * Get boss note for the desk based on day and deficit
 */
function getBossNote(day, deficit) {
  const notes = gameData.boss?.desk_notes;
  if (!notes) return null;

  // Check deficit-specific notes first
  if (deficit <= -10 && notes.danger) return { text: injectName(notes.danger), name: 'Gunnar' };
  if (deficit <= -5 && notes.warning) return { text: injectName(notes.warning), name: 'Gunnar' };

  // Day-specific notes
  const dayNote = notes[`day_${day}`];
  if (dayNote) return { text: injectName(dayNote), name: 'Gunnar' };

  return { text: injectName(notes.default || 'Deliver.'), name: 'Gunnar' };
}

/**
 * Get boss quote for results based on deficit
 */
function getBossQuote(deficit, day) {
  const quotes = gameData.boss?.result_quotes;
  if (!quotes) return '';

  if (deficit <= -12) return injectName(quotes.critical || `Not looking good, ${pn()}.`);
  if (deficit <= -8)  return injectName(quotes.bad || `Not enough, ${pn()}. Do better.`);
  if (deficit <= -3)  return injectName(quotes.warning || 'We\'re still behind.');
  if (deficit >= 2)   return injectName(quotes.good || 'Hmph. Not bad.');
  return injectName(quotes.neutral || 'Tomorrow again.');
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
 * Add mute button to start screen
 */
function addMuteButton() {
  const startScreen = document.getElementById('screen-start');
  const btn = document.createElement('button');
  btn.id = 'mute-btn';
  btn.textContent = AudioManager.isMuted() ? '🔇' : '🔊';
  btn.style.cssText = 'position:absolute;top:8px;left:8px;background:none;border:none;font-size:20px;cursor:pointer;z-index:10;opacity:0.7;padding:4px;';
  btn.addEventListener('click', () => {
    const muted = AudioManager.toggleMute();
    btn.textContent = muted ? '🔇' : '🔊';
  });
  startScreen.appendChild(btn);
}

// — BOOT —
boot();
