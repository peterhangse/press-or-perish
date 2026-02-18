/**
 * COMPONENTS — Updates persistent UI elements
 * Deficit meter, week strip, game clock
 */

import { getDeficitSeverity, getDeficitFillPercent, getPerishDistance } from '../engine/scoring-engine.js';

const DAY_NAMES = ['MON', 'TUE', 'WED', 'THU', 'FRI'];
const CLOCK_PHASES = {
  desk:      { time: '08:00', phase: 'Morning' },
  interview: { time: '12:00', phase: 'Midday' },
  publish:   { time: '16:00', phase: 'Afternoon' },
  sleep:     { time: '22:00', phase: 'Evening' },
  results:   { time: '23:00', phase: 'Night' },
};

/**
 * Build the week strip for 5 days
 */
export function buildWeekStrip() {
  const strip = document.getElementById('week-strip');
  strip.innerHTML = '';
  for (let i = 1; i <= 5; i++) {
    const day = document.createElement('div');
    day.className = 'week-day';
    day.dataset.day = i;
    day.textContent = i;
    strip.appendChild(day);
  }
}

/**
 * Update week strip to reflect current day and history
 * @param {number} currentDay - Current day (1-5)
 * @param {Array} dayHistory - Array of completed day records
 */
export function updateWeekStrip(currentDay, dayHistory) {
  const days = document.querySelectorAll('.week-day');
  days.forEach(dayEl => {
    const d = parseInt(dayEl.dataset.day);
    dayEl.classList.remove('current', 'completed', 'good', 'bad', 'ok');

    if (d === currentDay) {
      dayEl.classList.add('current');
    } else if (d < currentDay) {
      dayEl.classList.add('completed');
      const record = dayHistory.find(h => h.day === d);
      if (record) {
        const delta = record.points - record.competitorScore;
        if (delta > 0) dayEl.classList.add('good');
        else if (delta < 0) dayEl.classList.add('bad');
        else dayEl.classList.add('ok');
      }
    }
  });
}

/**
 * Update deficit meter display
 * @param {number} deficit - Current deficit value
 */
export function updateDeficitMeter(deficit) {
  const fill = document.getElementById('deficit-fill');
  const value = document.getElementById('deficit-value');
  const warning = document.getElementById('deficit-warning');

  const severity = getDeficitSeverity(deficit);
  const fillPct = getDeficitFillPercent(deficit);
  const perishMsg = getPerishDistance(deficit);

  fill.style.width = `${fillPct}%`;
  fill.classList.remove('warn', 'danger');
  if (severity === 'warning') fill.classList.add('warn');
  if (severity === 'danger') fill.classList.add('danger');

  value.textContent = deficit;
  warning.textContent = perishMsg;
}

/**
 * Update game clock for current phase
 * @param {string} phase - Game phase name
 */
export function updateClock(phase) {
  const clockData = CLOCK_PHASES[phase] || CLOCK_PHASES.desk;
  document.getElementById('clock-time').textContent = clockData.time;
  document.getElementById('clock-phase').textContent = clockData.phase;
}

/**
 * Update the desk window sky based on time of day
 * @param {string} phase - Current phase
 */
export function updateWindowSky(phase) {
  const sky = document.querySelector('.desk-window-sky');
  if (!sky) return;
  sky.classList.remove('morning', 'afternoon', 'evening');
  if (phase === 'desk') sky.classList.add('morning');
  else if (phase === 'interview' || phase === 'publish') sky.classList.add('afternoon');
  else sky.classList.add('evening');
}
