/**
 * TRANSITION SCREEN — Day header with fade-in animations
 */

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
 */
export function show(day, deficit, onDone) {
  const container = document.getElementById('screen-transition');
  container.innerHTML = '';

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
    const severity = deficit > -5 ? 'safe' : deficit > -10 ? 'warning' : 'danger';
    defValue.className = `transition-deficit-value ${severity}`;
    defValue.textContent = deficit;

    deficitEl.appendChild(defLabel);
    deficitEl.appendChild(defValue);
    container.appendChild(deficitEl);
  }

  // Mood text
  const mood = document.createElement('div');
  mood.className = 'transition-mood';
  mood.textContent = getMoodText(day, deficit);
  container.appendChild(mood);

  // Auto-advance after 3 seconds
  setTimeout(() => {
    if (onDone) onDone();
  }, 3000);
}

/**
 * Get mood text based on day and deficit
 */
function getMoodText(day, deficit) {
  if (day === 0) return 'Time to show them what you\'ve got.';
  if (day === 1) return 'A fresh start.';
  if (deficit <= -12) return 'This could be your last day.';
  if (deficit <= -8) return 'Gunnar\'s stare burns the back of your neck.';
  if (deficit <= -5) return 'The pressure builds. The competition leads.';
  if (deficit >= 0) return 'You\'re ahead. Keep it up.';
  return 'Another day. Another chance.';
}
