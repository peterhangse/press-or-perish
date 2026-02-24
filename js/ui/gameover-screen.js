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
  sub.textContent = `${opts.paperName || 'Småstads Tidning'} can no longer afford to keep you. ${opts.bossName || 'Gunnar'} gave you a chance, ${opts.playerName || 'kid'}. You failed.`;
  container.appendChild(sub);

  // Cold epilogue
  const epilogue = document.createElement('div');
  epilogue.className = 'gameover-epilogue';
  epilogue.textContent = getPerishedEpilogue(opts.daysCompleted, opts.playerName || 'kid', opts.townName || 'Småstad');
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
  epilogue.textContent = `${opts.bossName || 'Gunnar'} nods briefly. "You can stay, ${opts.playerName || 'kid'}. For now." ${opts.competitorName || 'Regionbladet'} moves on. ${opts.paperName || 'Småstads Tidning'} lives another day. That's enough.`;
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
function getPerishedEpilogue(days, name, townName) {
  townName = townName || 'Småstad';
  if (days <= 1) {
    return `One day, ${name}. That's all you lasted. The desk is cleared before lunch. ${townName} doesn't even notice you left.`;
  }
  if (days <= 3) {
    return `You leave the key on the desk and walk out into the rain. Nobody stops you. By tomorrow, someone else will sit in your chair.`;
  }
  return `Almost, ${name}. You could feel it turning — but not fast enough. The last bus out of ${townName} leaves at dusk. You're on it.`;
}

/**
 * Survived message based on final deficit
 */
function getSurvivedMessage(deficit) {
  if (deficit >= 0) {
    return 'You beat the competition. Not by much, but enough.';
  }
  if (deficit >= -5) {
    return 'Tough days, but you made it.';
  }
  if (deficit >= -10) {
    return 'You survived. Barely. The competition still leads, but the paper lives. It\'ll have to do.';
  }
  return 'By the thinnest of margins, you survived the week.';
}
