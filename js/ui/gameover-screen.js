/**
 * GAME OVER SCREEN — Perished (fired) or Survived endings
 */

import * as SFX from '../engine/sfx-engine.js';

/**
 * Show game over: PERISHED (fired)
 * @param {Object} opts
 * @param {number} opts.finalDeficit - Final deficit value
 * @param {number} opts.daysCompleted - Days completed before firing
 * @param {Array} opts.dayHistory - Full day history
 * @param {Function} opts.onRestart - Restart callback
 */
export function showPerished(opts) {
  const container = document.getElementById('screen-gameover');
  container.innerHTML = '';
  container.classList.remove('gameover-survive');

  // Title
  const title = document.createElement('div');
  title.className = 'gameover-title';
  title.textContent = 'PERISHED';
  container.appendChild(title);
  SFX.play('slam');

  // Subtitle
  const sub = document.createElement('div');
  sub.className = 'gameover-subtitle';
  sub.textContent = `Småstads Tidning can no longer afford to keep you. Gunnar gave you a chance, ${opts.playerName || 'kid'}. You failed.`;
  container.appendChild(sub);

  // Cold epilogue
  const epilogue = document.createElement('div');
  epilogue.className = 'gameover-epilogue';
  epilogue.textContent = getPerishedEpilogue(opts.daysCompleted, opts.playerName || 'kid');
  container.appendChild(epilogue);

  // Stats
  const stats = document.createElement('div');
  stats.className = 'gameover-stats';

  addStat(stats, opts.daysCompleted, 'DAYS');
  addStat(stats, opts.finalDeficit, 'DEFICIT');
  const totalPoints = opts.dayHistory.reduce((sum, d) => sum + d.points, 0);
  addStat(stats, totalPoints, 'POINTS');
  container.appendChild(stats);

  // Restart
  const btn = document.createElement('button');
  btn.className = 'btn-paper gameover-restart';
  btn.textContent = 'Try Again';
  btn.addEventListener('click', () => {
    SFX.play('click');
    opts.onRestart && opts.onRestart();
  });
  container.appendChild(btn);
}

/**
 * Show game over: SURVIVED (made it through the week)
 * @param {Object} opts
 * @param {number} opts.finalDeficit - Final deficit value
 * @param {Array} opts.dayHistory - Full day history
 * @param {Function} opts.onRestart - Restart callback
 */
export function showSurvived(opts) {
  const container = document.getElementById('screen-gameover');
  container.innerHTML = '';
  container.classList.add('gameover-survive');

  // Title
  const title = document.createElement('div');
  title.className = 'gameover-title';
  title.textContent = 'SURVIVED';
  container.appendChild(title);
  SFX.play('slam');

  // Message (cold, not triumphant)
  const msg = document.createElement('div');
  msg.className = 'survive-message';
  msg.textContent = getSurvivedMessage(opts.finalDeficit);
  container.appendChild(msg);

  // Epilogue
  const epilogue = document.createElement('div');
  epilogue.className = 'gameover-epilogue';
  epilogue.textContent = `Gunnar nods briefly. "You can stay, ${opts.playerName || 'kid'}. For now." Regionbladet moves on. Småstads Tidning lives another day. That's enough.`;
  container.appendChild(epilogue);

  // Stats
  const stats = document.createElement('div');
  stats.className = 'gameover-stats';

  addStat(stats, 5, 'DAYS');
  addStat(stats, opts.finalDeficit, 'DEFICIT');
  const totalPoints = opts.dayHistory.reduce((sum, d) => sum + d.points, 0);
  addStat(stats, totalPoints, 'POINTS');
  const avgPoints = Math.round(totalPoints / 5);
  addStat(stats, avgPoints, 'AVG');
  container.appendChild(stats);

  // Restart
  const btn = document.createElement('button');
  btn.className = 'btn-paper gameover-restart';
  btn.textContent = 'Play Again';
  btn.addEventListener('click', () => {
    SFX.play('click');
    opts.onRestart && opts.onRestart();
  });
  container.appendChild(btn);
}

/**
 * Add a stat box
 */
function addStat(container, value, label) {
  const stat = document.createElement('div');
  stat.className = 'gameover-stat';

  const valEl = document.createElement('div');
  valEl.className = 'gameover-stat-value';
  valEl.textContent = value;

  const labelEl = document.createElement('div');
  labelEl.className = 'gameover-stat-label';
  labelEl.textContent = label;

  stat.appendChild(valEl);
  stat.appendChild(labelEl);
  container.appendChild(stat);
}

/**
 * Cold epilogue text for perished ending
 */
function getPerishedEpilogue(days, name) {
  if (days <= 1) {
    return `You pack up the same day, ${name}. The town has already forgotten your name. The bus back to Stockholm leaves at five.`;
  }
  if (days <= 3) {
    return `You leave the key on the desk. The phone booth outside the office smells of rain and decay. No one calls for ${name}.`;
  }
  return `Almost, ${name}. But almost doesn't cut it in this business. You take the train home in the dark. Småstad shrinks in the rearview.`;
}

/**
 * Survived message based on final deficit
 */
function getSurvivedMessage(deficit) {
  if (deficit >= 0) {
    return 'You beat Regionbladet. Not by much, but enough. Småstad has a paper that dares.';
  }
  if (deficit >= -5) {
    return 'Tough days, but you made it. Gunnar raises an eyebrow — the closest he gets to a compliment.';
  }
  if (deficit >= -10) {
    return 'You survived. Barely. Regionbladet still leads, but the paper lives. It\'ll have to do.';
  }
  return 'By the thinnest of margins, you survived the week. Gunnar says nothing. That silence speaks for itself.';
}
