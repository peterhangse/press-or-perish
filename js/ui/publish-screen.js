/**
 * PUBLISH SCREEN — Headline selection + sleep phase
 */

import * as SFX from '../engine/sfx-engine.js';

let onPublish = null;

/**
 * Show the publish/headline selection screen
 * @param {Object} story - Current story
 * @param {Array} headlines - Headline options [{text, tone}]
 * @param {number} points - Points earned today
 * @param {number} day - Current day
 * @param {Function} callback - Called with { headlineIndex } when published
 */
export function render(story, headlines, points, day, callback) {
  onPublish = callback;

  const container = document.getElementById('screen-publish');
  container.innerHTML = '';

  const wrapper = document.createElement('div');
  wrapper.className = 'publish-container';

  // Newspaper preview
  const paper = document.createElement('div');
  paper.className = 'newspaper-preview';

  const masthead = document.createElement('div');
  masthead.className = 'newspaper-masthead';
  masthead.textContent = 'Småstads Tidning';

  const date = document.createElement('div');
  date.className = 'newspaper-date';
  date.textContent = getDayDate(day);

  paper.appendChild(masthead);
  paper.appendChild(date);

  // Headline choices
  const choices = document.createElement('div');
  choices.className = 'headline-choices';

  let selectedIndex = null;

  headlines.forEach((h, i) => {
    const option = document.createElement('div');
    option.className = 'headline-option';
    option.dataset.index = i;

    const text = document.createElement('div');
    text.className = 'headline-text';
    text.textContent = h.text;

    const tone = document.createElement('div');
    tone.className = 'headline-tone';
    tone.textContent = h.tone || '';

    option.appendChild(text);
    option.appendChild(tone);

    option.addEventListener('click', () => {
      SFX.play('select');
      selectedIndex = i;
      document.querySelectorAll('.headline-option').forEach((o, j) => {
        o.classList.toggle('selected', j === i);
      });
      publishBtn.classList.add('ready');
    });

    choices.appendChild(option);
  });

  paper.appendChild(choices);
  wrapper.appendChild(paper);

  // Publish button
  const publishBtn = document.createElement('button');
  publishBtn.className = 'publish-btn';
  publishBtn.id = 'publish-btn';
  publishBtn.textContent = 'PRESS';
  publishBtn.addEventListener('click', () => {
    if (selectedIndex !== null && onPublish) {
      SFX.play('stamp');
      onPublish({ headlineIndex: selectedIndex });
    }
  });
  wrapper.appendChild(publishBtn);

  container.appendChild(wrapper);
}

/**
 * Show the sleep phase (after publishing, before results)
 * @param {number} day - Current day
 * @param {number} points - Player's points
 * @param {number} competitorPoints - Competitor's points
 * @param {number} deficitDelta - Today's deficit change
 * @param {Function} callback - Called when player continues
 */
export function showSleep(day, points, competitorPoints, deficitDelta, callback) {
  const container = document.getElementById('screen-publish');
  container.innerHTML = '';

  const sleep = document.createElement('div');
  sleep.className = 'sleep-container';

  const text = document.createElement('div');
  sleep.className = 'sleep-container';

  // Day complete text
  const dayText = document.createElement('div');
  dayText.className = 'sleep-text';
  dayText.textContent = getSleepText(day, deficitDelta);

  // Deficit change display
  const change = document.createElement('div');
  change.className = `sleep-deficit-change ${deficitDelta > 0 ? 'positive' : deficitDelta < 0 ? 'negative' : 'neutral'}`;
  change.textContent = `${deficitDelta > 0 ? '+' : ''}${deficitDelta}`;
  SFX.play(deficitDelta >= 0 ? 'relief' : 'tension');

  const changeLabel = document.createElement('div');
  changeLabel.style.cssText = 'font-family: var(--font-body); font-size: 9px; color: var(--paper-dark);';
  changeLabel.textContent = deficitDelta >= 0 ? 'You gained ground' : 'You fell behind';

  // Continue
  const btn = document.createElement('button');
  btn.className = 'btn-paper sleep-continue';
  if (day === 0) {
    btn.textContent = 'Sleep → See results';
  } else {
    btn.textContent = day < 5 ? 'Sleep → Next day' : 'See weekly results';
  }
  btn.addEventListener('click', () => {
    SFX.play('click');
    if (callback) callback();
  });

  sleep.appendChild(dayText);
  sleep.appendChild(change);
  sleep.appendChild(changeLabel);
  sleep.appendChild(btn);
  container.appendChild(sleep);
}

/**
 * Get the date string for a day
 */
function getDayDate(day) {
  const dates = [
    'Sunday, November 10, 1974',   // Day 0 (tutorial)
    'Monday, November 11, 1974',
    'Tuesday, November 12, 1974',
    'Wednesday, November 13, 1974',
    'Thursday, November 14, 1974',
    'Friday, November 15, 1974',
  ];
  return dates[day] || dates[1];
}

/**
 * Get sleep flavor text based on day and deficit
 */
function getSleepText(day, deficitDelta) {
  if (day === 0) {
    return 'Your first day at the paper. The competition doesn\'t sleep.';
  }
  if (day === 1) {
    return deficitDelta >= 0
      ? 'First day done. You fall asleep feeling a glimmer of hope.'
      : 'First day and already behind. The bed feels hard tonight.';
  }
  if (day === 5) {
    return 'The week is over. You lie staring at the ceiling.';
  }
  if (deficitDelta >= 2) {
    return 'A good day. You fall asleep quickly.';
  }
  if (deficitDelta <= -3) {
    return 'You lie awake for hours. Gunnar\'s words echo.';
  }
  return 'Another day. The alarm is set for 6:00 AM.';
}
