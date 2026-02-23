/**
 * TRANSITION SCREEN — Day header with fade-in animations
 */

import * as SFX from '../engine/sfx-engine.js';
import { getDeficitColor } from './components.js';

const DAY_NAMES = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY'];
const DAY_DATES = [
  'November 11, 1974',
  'November 12, 1974',
  'November 13, 1974',
  'November 14, 1974',
  'November 15, 1974',
];

/**
 * Show day transition
 * @param {number} day - Day number (0 for tutorial, 1-5 for game)
 * @param {number} deficit - Current deficit
 * @param {Function} onDone - Called after transition completes
 * @param {Object} [extraOpts] - Extra options like customTitle, customSubtitle, dates, bossName
 */
export function show(day, deficit, onDone, extraOpts = {}) {
  const container = document.getElementById('screen-transition');
  container.innerHTML = '';

  // Custom title/subtitle for town transitions
  if (extraOpts.customTitle) {
    const customTitleEl = document.createElement('div');
    customTitleEl.className = 'transition-day';
    customTitleEl.textContent = extraOpts.customTitle;
    container.appendChild(customTitleEl);

    if (extraOpts.customSubtitle) {
      const customSubEl = document.createElement('div');
      customSubEl.className = 'transition-mood';
      customSubEl.style.marginTop = '12px';
      customSubEl.textContent = extraOpts.customSubtitle;
      container.appendChild(customSubEl);
    }

    const hint = document.createElement('div');
    hint.className = 'transition-hint';
    hint.textContent = 'Click to continue';
    container.appendChild(hint);

    SFX.play('ambientTick');
    let done = false;
    const finish = () => {
      if (done) return;
      done = true;
      container.removeEventListener('click', finish);
      if (onDone) onDone();
    };
    container.addEventListener('click', finish);
    setTimeout(finish, 5000);
    return;
  }

  // Day number
  const dayNum = document.createElement('div');
  dayNum.className = 'transition-day';
  dayNum.textContent = day === 0 ? 'YOUR FIRST DAY' : `DAY ${day}`;
  container.appendChild(dayNum);

  // Day name
  const dayName = document.createElement('div');
  dayName.className = 'transition-day-name';
  dayName.textContent = day === 0 ? 'MONDAY' : (DAY_NAMES[day - 1] || '');
  container.appendChild(dayName);

  // Date
  const date = document.createElement('div');
  date.className = 'transition-date';
  date.textContent = day === 0 ? 'November 10, 1974' : (DAY_DATES[day - 1] || '');
  container.appendChild(date);

  // Deficit display (hidden on day 1)
  if (day > 1) {
    const deficitEl = document.createElement('div');
    deficitEl.className = 'transition-deficit';

    const defLabel = document.createElement('span');
    defLabel.className = 'transition-deficit-label';
    defLabel.textContent = 'Deficit: ';

    const defValue = document.createElement('span');
    defValue.className = 'transition-deficit-value';
    defValue.textContent = deficit;
    defValue.style.color = getDeficitColor(deficit);

    deficitEl.appendChild(defLabel);
    deficitEl.appendChild(defValue);
    container.appendChild(deficitEl);
  }

  // Mood text
  const mood = document.createElement('div');
  mood.className = 'transition-mood';
  mood.textContent = getMoodText(day, deficit);
  container.appendChild(mood);

  // Click to skip hint
  const hint = document.createElement('div');
  hint.className = 'transition-hint';
  hint.textContent = 'Click to continue';
  container.appendChild(hint);

  // Auto-advance after 3 seconds, or click to skip
  SFX.play('ambientTick');
  let done = false;
  const finish = () => {
    if (done) return;
    done = true;
    container.removeEventListener('click', finish);
    if (onDone) onDone();
  };
  container.addEventListener('click', finish);
  setTimeout(finish, 3000);
}

/**
 * Get mood text based on day and deficit
 */
function getMoodText(day, deficit) {
  if (day === 0) return 'Time to show them what you\'ve got.';
  if (day === 1) return 'A fresh start.';
  if (deficit <= -12) return 'This could be your last day.';
  if (deficit <= -8) return 'The pressure is crushing.';
  if (deficit <= -5) return 'The pressure builds. The competition leads.';
  if (deficit >= 0) return 'You\'re ahead. Keep it up.';
  return 'Another day. Another chance.';
}
