/**
 * ACHIEVEMENTS UI — Panel, button, unlock animation
 * Press or Perish
 */

import * as Achievements from '../engine/achievements.js';
import * as SFX from '../engine/sfx-engine.js';

// ── Icon mapping (emoji pixel stand-ins) ──
const ICONS = {
  // Milestones
  first_byline:           '📰',
  no_skill:               '📄',
  breakthrough:           '💡',
  beat_the_clock:         '⏱',
  survived:               '🗓',
  press_master:           '🖊',
  margin_of_error:        '🎯',
  overqualified:          '🎓',
  front_page_material:    '📣',
  // Interview Mastery
  soft_touch:             '🤝',
  silent_treatment:       '🤫',
  full_arsenal:           '🧰',
  pattern_master:         '🔥',
  hidden_gem:             '💎',
  bulldozer:              '🚜',
  just_the_facts:         '📋',
  one_trick_pony:         '🐴',
  // Survival
  clean_sweep:            '🧹',
  comeback_king:          '👑',
  perfect_week:           '⭐',
  high_scorer:            '🏆',
  veteran:                '🎖',
  not_dead_yet:           '💀',
  photo_finish:           '📷',
  tuesday_is_the_new_friday: '💥',
  // Stories
  journalism_at_its_best: '😢',
  its_my_fault:           '💔',
  s_is_doing_it_again:    '📕',
  i_recorded_it:          '🎙',
  twenty_minutes:         '⏰',
  three_years_of_silence: '🕯',
  print_that_if_you_dare: '🐺',
  eighty_five_vs_twenty_seven: '🍽',
  fourteen_and_crying:    '🍫',
  stop_the_presses:       '📞',
  follow_the_money:       '💰',
  pumpkin_pulitzer:       '🎃',
  // Rookie Mistakes
  get_back_to_your_desk:  '🪑',
  ive_never_met_you:      '👻',
  you_sound_like_the_police: '👮',
  we_are_done_here:       '🚪',
  five_zeroes:            '0️⃣',
  wrong_crowd:            '😬',
  speedrun:               '⚡',
  silence_is_awkward:     '😶',
};

let panelOpen = false;
let unlockQueue = [];
let showingUnlock = false;

/**
 * Add the medal button to #game-wrapper (called from boot())
 */
export function addAchievementButton() {
  const wrapper = document.getElementById('game-wrapper');
  if (!wrapper) return;

  const btn = document.createElement('button');
  btn.id = 'achievements-btn';
  btn.className = 'achievements-btn';
  btn.style.display = 'none'; // hidden until game starts (like mute)
  updateButtonLabel(btn);

  btn.addEventListener('click', () => {
    SFX.play('click');
    togglePanel();
  });

  wrapper.appendChild(btn);

  // Also create panel + backdrop (hidden by default)
  const backdrop = document.createElement('div');
  backdrop.id = 'achievements-backdrop';
  backdrop.className = 'achievements-backdrop';
  backdrop.addEventListener('click', () => closePanel());
  wrapper.appendChild(backdrop);

  const panel = document.createElement('div');
  panel.id = 'achievements-panel';
  panel.className = 'achievements-panel';
  wrapper.appendChild(panel);
}

/**
 * Show the achievement button (call after start screen click)
 */
export function showButton() {
  const btn = document.getElementById('achievements-btn');
  if (btn) btn.style.display = '';
}

/**
 * Update button label with current count
 */
function updateButtonLabel(btn) {
  btn = btn || document.getElementById('achievements-btn');
  if (!btn) return;

  btn.innerHTML = `<span class="achievements-medal">🎖</span>`;
}

/**
 * Toggle the achievements panel
 */
function togglePanel() {
  if (panelOpen) {
    closePanel();
  } else {
    openPanel();
  }
}

/**
 * Open the panel
 */
function openPanel() {
  const panel = document.getElementById('achievements-panel');
  const backdrop = document.getElementById('achievements-backdrop');
  if (!panel) return;

  renderPanel(panel);
  panel.classList.add('open');
  if (backdrop) backdrop.classList.add('open');
  panelOpen = true;
}

/**
 * Close the panel
 */
function closePanel() {
  const panel = document.getElementById('achievements-panel');
  const backdrop = document.getElementById('achievements-backdrop');
  if (panel) panel.classList.remove('open');
  if (backdrop) backdrop.classList.remove('open');
  panelOpen = false;
}

/**
 * Render the full panel content
 */
function renderPanel(panel) {
  panel.innerHTML = '';

  const unlocked = Achievements.loadUnlocked();
  const total = Achievements.getTotal();
  const all = Achievements.getAll();

  // Tab header with close button
  const tab = document.createElement('div');
  tab.className = 'achievements-tab';

  const closeBtn = document.createElement('button');
  closeBtn.className = 'ach-close-btn';
  closeBtn.textContent = '✕';
  closeBtn.addEventListener('click', () => { SFX.play('click'); closePanel(); });
  tab.appendChild(closeBtn);

  const title = document.createElement('span');
  title.className = 'achievements-tab-title';
  title.textContent = 'ACHIEVEMENTS';
  tab.appendChild(title);

  const count = document.createElement('span');
  count.className = 'achievements-tab-count';
  count.textContent = `${unlocked.size}/${total}`;
  tab.appendChild(count);

  panel.appendChild(tab);

  // Build by category
  for (const cat of Achievements.CATEGORIES) {
    const catAchievements = all.filter(a => a.category === cat.id);
    if (catAchievements.length === 0) continue;

    const header = document.createElement('div');
    header.className = 'ach-category-header';
    header.textContent = cat.name;
    panel.appendChild(header);

    for (const ach of catAchievements) {
      const isUnlocked = unlocked.has(ach.id);
      const card = document.createElement('div');
      card.className = `ach-card ${isUnlocked ? 'unlocked' : 'locked'}`;

      // Icon
      const iconContainer = document.createElement('div');
      iconContainer.className = 'ach-icon-container';
      const icon = document.createElement('span');
      icon.className = 'ach-icon';
      icon.textContent = ICONS[ach.id] || '?';
      iconContainer.appendChild(icon);

      // Info
      const info = document.createElement('div');
      info.className = 'ach-info';

      const name = document.createElement('div');
      name.className = 'ach-name';
      name.textContent = ach.name;

      const desc = document.createElement('div');
      desc.className = 'ach-desc';
      desc.textContent = isUnlocked ? ach.description : '???';

      info.appendChild(name);
      info.appendChild(desc);

      card.appendChild(iconContainer);
      card.appendChild(info);
      panel.appendChild(card);
    }
  }
}

/**
 * Show unlock animation for one or more achievements.
 * Queues them if multiple trigger at once.
 *
 * @param {Array<Object>} achievements - Array of newly unlocked achievement objects
 */
export function showUnlocks(achievements) {
  for (const ach of achievements) {
    unlockQueue.push(ach);
  }
  if (!showingUnlock) processUnlockQueue();
}

/**
 * Process the unlock animation queue
 */
function processUnlockQueue() {
  if (unlockQueue.length === 0) {
    showingUnlock = false;
    // Update button count after all shown
    updateButtonLabel();
    return;
  }

  showingUnlock = true;
  const ach = unlockQueue.shift();

  const wrapper = document.getElementById('game-wrapper');
  if (!wrapper) { processUnlockQueue(); return; }

  // Play stamp SFX
  SFX.play('stamp');

  // Create overlay
  const overlay = document.createElement('div');
  overlay.className = 'achievement-unlock-overlay';

  const card = document.createElement('div');
  card.className = `achievement-unlock-card ${ach.category === 'rookie' ? 'rookie' : ''}`;

  // Icon
  const iconEl = document.createElement('div');
  iconEl.className = 'unlock-icon';
  iconEl.textContent = ICONS[ach.id] || '?';

  // Text
  const textEl = document.createElement('div');

  const label = document.createElement('div');
  label.className = 'unlock-label';
  label.textContent = ach.category === 'rookie' ? '⚠ Rookie Mistake' : '★ Achievement Unlocked';

  const nameEl = document.createElement('div');
  nameEl.className = 'unlock-name';
  nameEl.textContent = ach.name;

  const descEl = document.createElement('div');
  descEl.className = 'unlock-desc';
  descEl.textContent = ach.description;

  textEl.appendChild(label);
  textEl.appendChild(nameEl);
  textEl.appendChild(descEl);

  card.appendChild(iconEl);
  card.appendChild(textEl);
  overlay.appendChild(card);
  wrapper.appendChild(overlay);

  // Hold for 2s, then fade out
  setTimeout(() => {
    card.classList.add('fade-out');
    setTimeout(() => {
      overlay.remove();
      // Stagger next unlock by 400ms
      setTimeout(() => processUnlockQueue(), 400);
    }, 500);
  }, 2000);
}
