/**
 * RESULTS SCREEN — End-of-day comparison: Your paper vs. Regionbladet
 */

import * as CompetitorAI from '../engine/competitor-ai.js';
import * as SFX from '../engine/sfx-engine.js';

/**
 * Show end-of-day results
 * @param {Object} opts
 * @param {string} opts.playerHeadline - Player's chosen headline
 * @param {number} opts.playerScore - Player's total points today
 * @param {number} opts.competitorScore - Competitor's score today
 * @param {string} opts.competitorHeadline - Competitor's headline
 * @param {number} opts.deficitBefore - Deficit before today
 * @param {number} opts.deficitAfter - Deficit after today
 * @param {number} opts.baseValue - Story base value
 * @param {number} opts.tierBonus - Tier bonus (tier*2)
 * @param {number} opts.day - Current day
 * @param {string} opts.bossQuote - Boss reaction quote
 * @param {Function} opts.onContinue - Callback when player continues
 */
export function render(opts) {
  const container = document.getElementById('screen-results');
  container.innerHTML = '';

  const wrapper = document.createElement('div');
  wrapper.className = 'results-container';

  // ═══ PHASE 1: Your story scoring + "Go to sleep" ═══
  const phase1 = document.createElement('div');
  phase1.className = 'results-phase results-phase-1';

  const title1 = document.createElement('div');
  title1.className = 'results-title';
  title1.textContent = opts.isDayZero ? 'STORY FILED' : `DAY ${opts.day} — STORY FILED`;
  phase1.appendChild(title1);

  // Scoring breakdown (your story only)
  const breakdown = document.createElement('div');
  breakdown.className = 'results-breakdown';
  addNewsValueRow(breakdown, opts.baseValue);
  addInterviewBonusRow(breakdown, 'Approach', opts.q1Bonus || 0);
  addInterviewBonusRow(breakdown, 'Follow-up', opts.q2Bonus || 0);
  // Headline scoring disabled — uncomment to re-enable
  // addInterviewBonusRow(breakdown, 'Headline', opts.headlineBonus || 0);
  addBreakdownRow(breakdown, 'Your total', `${opts.playerScore}`, 'positive', true);
  phase1.appendChild(breakdown);

  // Day Zero teaching note on Phase 1
  if (opts.isDayZero && opts.dayZeroNote1) {
    const note1 = document.createElement('div');
    note1.className = 'results-boss-sticky results-boss-note-inline visible';
    const note1Text = document.createElement('div');
    note1Text.className = 'results-boss-sticky-text';
    note1Text.textContent = opts.dayZeroNote1;
    const note1Name = document.createElement('div');
    note1Name.className = 'results-boss-sticky-name';
    note1Name.textContent = `— ${opts.bossName || 'Gunnar'}`;
    note1.appendChild(note1Text);
    note1.appendChild(note1Name);
    phase1.appendChild(note1);
  }

  // Go to sleep button
  const sleepBtn = document.createElement('button');
  sleepBtn.className = 'btn-paper results-sleep-btn';
  sleepBtn.textContent = 'Go to sleep';
  sleepBtn.addEventListener('click', () => {
    SFX.play('click');
    sleepBtn.remove();
    showPhase2(wrapper, opts);
  });
  phase1.appendChild(sleepBtn);

  wrapper.appendChild(phase1);
  container.appendChild(wrapper);
}

/**
 * Phase 2: Headlines slide in, then comparison, deficit, boss quote
 */
function showPhase2(wrapper, opts) {
  // Update title
  const title = wrapper.querySelector('.results-title');
  if (title) title.textContent = opts.isDayZero ? 'TRIAL DAY — RESULTS' : `DAY ${opts.day} — RESULTS`;

  // Side-by-side comparison container
  const comparison = document.createElement('div');
  comparison.className = 'results-comparison';

  // Player's paper — slides in first
  const yours = buildPaperCard(
    'YOUR PAPER',
    opts.paperName || 'Småstads Tidning',
    opts.playerHeadline,
    opts.playerScore,
    true
  );
  yours.classList.add('results-slide-in-left');
  comparison.appendChild(yours);
  SFX.play('reveal');

  // Competitor's paper — slides in second (delayed)
  const theirs = buildPaperCard(
    'THE COMPETITION',
    opts.competitorName || CompetitorAI.getCompetitorName(),
    opts.competitorHeadline,
    opts.competitorScore,
    false
  );
  theirs.classList.add('results-slide-in-right');
  comparison.appendChild(theirs);
  setTimeout(() => SFX.play('reveal'), 600);

  // Insert comparison after the breakdown
  const breakdown = wrapper.querySelector('.results-breakdown');
  breakdown.parentNode.insertBefore(comparison, breakdown);

  // Phase 2 bottom section — appears after headlines
  const phase2Bottom = document.createElement('div');
  phase2Bottom.className = 'results-phase results-phase-2';
  phase2Bottom.style.opacity = '0';

  // Competitor row in breakdown
  const compBreakdown = document.createElement('div');
  compBreakdown.className = 'results-breakdown';
  addBreakdownRow(compBreakdown, opts.competitorName || CompetitorAI.getCompetitorName(), `${opts.competitorScore}`, '');
  const delta = opts.playerScore - opts.competitorScore;
  addBreakdownRow(compBreakdown, 'Today\'s change', `${delta > 0 ? '+' : ''}${delta}`, delta > 0 ? 'positive' : delta < 0 ? 'negative' : '', true);
  phase2Bottom.appendChild(compBreakdown);
  setTimeout(() => SFX.play(delta >= 0 ? 'relief' : 'tension'), 1200);

  // Deficit update
  const deficitRow = document.createElement('div');
  deficitRow.className = 'results-deficit';

  const defLabel = document.createElement('span');
  defLabel.className = 'results-deficit-label';
  defLabel.textContent = 'Deficit: ';

  const defBefore = document.createElement('span');
  defBefore.className = 'results-deficit-value';
  defBefore.textContent = opts.deficitBefore;
  defBefore.style.color = opts.deficitBefore < 0 ? 'var(--deficit-red)' : opts.deficitBefore > 0 ? 'var(--deficit-safe)' : '';

  const arrow = document.createElement('span');
  arrow.className = 'results-deficit-arrow';
  arrow.textContent = ' → ';

  const defAfter = document.createElement('span');
  defAfter.className = 'results-deficit-value';
  defAfter.textContent = opts.deficitAfter;
  defAfter.style.color = opts.deficitAfter < 0 ? 'var(--deficit-red)' : opts.deficitAfter > 0 ? 'var(--deficit-safe)' : '';

  deficitRow.appendChild(defLabel);
  deficitRow.appendChild(defBefore);
  deficitRow.appendChild(arrow);
  deficitRow.appendChild(defAfter);
  phase2Bottom.appendChild(deficitRow);

  // Boss quote — yellow sticky note that flies in from the right
  if (opts.bossQuote) {
    const sticky = document.createElement('div');
    sticky.className = 'results-boss-sticky';

    const stickyName = document.createElement('div');
    stickyName.className = 'results-boss-sticky-name';
    stickyName.textContent = `— ${opts.bossName || 'Gunnar'}`;

    const stickyText = document.createElement('div');
    stickyText.className = 'results-boss-sticky-text';
    stickyText.textContent = opts.bossQuote;

    sticky.appendChild(stickyText);
    sticky.appendChild(stickyName);
    wrapper.appendChild(sticky);

    // Fly in after phase 2 settles (1.8s after phase 2 appears)
    setTimeout(() => {
      sticky.classList.add('visible');
      SFX.play('note');
    }, 1200 + 600);
  }

  // Competitor shock message (Day Zero only)
  if (opts.competitorShock) {
    const shock = document.createElement('div');
    shock.className = 'results-shock';
    shock.textContent = opts.competitorShock;
    phase2Bottom.appendChild(shock);
  }

  // Continue button
  const btn = document.createElement('button');
  btn.className = 'btn-paper results-continue';
  if (opts.isDayZero) {
    btn.textContent = 'Begin for real →';
  } else {
    btn.textContent = opts.day < 5 ? 'Next day →' : 'Final results';
  }
  btn.addEventListener('click', () => {
    SFX.play('click');
    if (opts.onContinue) opts.onContinue();
  });
  phase2Bottom.appendChild(btn);

  wrapper.appendChild(phase2Bottom);

  // Staggered reveal: your paper (0ms) → competitor (600ms) → bottom section (1200ms)
  setTimeout(() => {
    phase2Bottom.style.transition = 'opacity 0.5s ease';
    phase2Bottom.style.opacity = '1';
  }, 1200);
}

/**
 * Build a newspaper card for comparison
 */
function buildPaperCard(label, paperName, headline, score, isYours) {
  const card = document.createElement('div');
  card.className = `results-paper ${isYours ? 'yours' : ''}`;

  const nameEl = document.createElement('div');
  nameEl.className = 'results-paper-name';
  nameEl.textContent = label;

  const paperEl = document.createElement('div');
  paperEl.className = isYours ? 'results-masthead-yours' : 'results-masthead-theirs';
  paperEl.textContent = paperName;

  const headlineEl = document.createElement('div');
  headlineEl.className = 'results-paper-headline';
  headlineEl.textContent = headline;

  const scoreEl = document.createElement('div');
  scoreEl.className = 'results-paper-score';
  scoreEl.textContent = score;

  const scoreLabel = document.createElement('div');
  scoreLabel.className = 'results-paper-label';
  scoreLabel.textContent = 'POINTS';

  card.appendChild(nameEl);
  card.appendChild(paperEl);
  card.appendChild(headlineEl);
  card.appendChild(scoreEl);
  card.appendChild(scoreLabel);
  return card;
}

/**
 * Add a row to the scoring breakdown
 */
function addBreakdownRow(container, label, value, colorClass, isTotal = false) {
  const row = document.createElement('div');
  row.className = `breakdown-row ${isTotal ? 'total' : ''}`;

  const labelEl = document.createElement('span');
  labelEl.textContent = label;

  const valEl = document.createElement('span');
  valEl.className = `breakdown-value ${colorClass}`;
  valEl.textContent = value;

  row.appendChild(labelEl);
  row.appendChild(valEl);
  container.appendChild(row);
}

/**
 * Add the news value row with dots — 4 slots (each dot = 2 points), matching interview style
 */
function addNewsValueRow(container, baseValue) {
  const MAX_DOTS = 4;           // 4 dots × 2 pts = 8 max
  const filled = Math.floor(baseValue / 2);
  const row = document.createElement('div');
  row.className = 'breakdown-row';

  const labelEl = document.createElement('span');
  labelEl.textContent = 'News value';

  const rightSide = document.createElement('span');
  rightSide.style.cssText = 'display:flex; align-items:center; gap:6px;';

  const dots = document.createElement('span');
  dots.style.cssText = 'display:flex; gap:3px; align-items:center;';
  for (let i = 0; i < MAX_DOTS; i++) {
    const dot = document.createElement('span');
    dot.style.cssText = 'width:6px; height:6px; border-radius:50%; border:1px solid; display:inline-block;';
    if (i < filled) {
      dot.style.background = 'var(--paper-aged)';
      dot.style.borderColor = 'var(--paper-aged)';
    } else {
      dot.style.background = 'transparent';
      dot.style.borderColor = 'var(--ink-faded)';
    }
    dots.appendChild(dot);
  }

  const valEl = document.createElement('span');
  valEl.className = 'breakdown-value positive';
  valEl.textContent = `+${baseValue}`;

  rightSide.appendChild(dots);
  rightSide.appendChild(valEl);

  row.appendChild(labelEl);
  row.appendChild(rightSide);
  container.appendChild(row);
}

/**
 * Add an interview bonus row (Q1 or Q2) showing +N or ✗
 */
function addInterviewBonusRow(container, label, bonus) {
  const row = document.createElement('div');
  row.className = 'breakdown-row';

  const labelEl = document.createElement('span');
  labelEl.textContent = label;

  const valEl = document.createElement('span');
  if (bonus > 0) {
    valEl.className = 'breakdown-value positive';
    valEl.textContent = `+${bonus}`;
  } else {
    valEl.className = 'breakdown-value fail';
    valEl.textContent = '✗';
  }

  row.appendChild(labelEl);
  row.appendChild(valEl);
  container.appendChild(row);
}
