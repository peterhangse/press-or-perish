/**
 * SCREEN MANAGER — Controls screen transitions
 * Hard cuts (no fade), flash overlay for impact
 */

import * as SFX from '../engine/sfx-engine.js';

const screens = {};
let currentScreen = null;
let hudBar = null;
let flashOverlay = null;

// Screens that show HUD bar (deficit meter, week strip, clock)
const SCREENS_WITH_UI = ['desk', 'interview', 'publish', 'results'];

/**
 * Initialize screen manager
 */
export function init() {
  document.querySelectorAll('.screen').forEach(el => {
    const id = el.id.replace('screen-', '');
    screens[id] = el;
  });
  hudBar = document.getElementById('hud-bar');
  flashOverlay = document.getElementById('flash-overlay');
}

/**
 * Switch to a screen with hard cut
 * @param {string} screenId - Screen name (e.g. 'desk', 'interview')
 * @param {boolean} flash - Whether to flash on transition
 */
export function switchTo(screenId, flash = false) {
  // Hide all screens
  Object.values(screens).forEach(el => el.classList.remove('active'));

  // Show target
  const target = screens[screenId];
  if (!target) {
    console.error(`Screen not found: ${screenId}`);
    return;
  }
  target.classList.add('active');
  currentScreen = screenId;

  // Sync ALL backgrounds (body, wrapper, HUD) so no color mismatch anywhere
  const bgMap = {
    start: '#2a1f12', onboarding: '#2a1f12',
    desk: '#2a1f12', interview: '#2a1f12', publish: '#2a1f12', results: '#2a1f12',
    transition: '#0a0a14', gameover: '#0a0a14'
  };
  const bg = bgMap[screenId] || '#2a1f12';
  document.documentElement.style.background = bg;
  document.body.style.background = bg;
  const wrapper = document.getElementById('game-wrapper');
  if (wrapper) {
    wrapper.style.background = bg;
    wrapper.style.boxShadow = `0 0 0 200vmax ${bg}`;
  }

  // Toggle HUD bar
  if (SCREENS_WITH_UI.includes(screenId)) {
    hudBar.classList.add('visible');
    hudBar.style.background = '';
  } else {
    hudBar.classList.remove('visible');
    hudBar.style.background = bg;
  }

  // Flash effect
  if (flash && flashOverlay) {
    flashOverlay.classList.remove('flash');
    // Force reflow
    void flashOverlay.offsetWidth;
    flashOverlay.classList.add('flash');
  }
}

/**
 * Get current screen ID
 */
export function getCurrent() {
  return currentScreen;
}

/**
 * Flash the overlay (for emphasis moments)
 */
export function flash() {
  if (!flashOverlay) return;
  SFX.play('ambientTick');
  flashOverlay.classList.remove('flash');
  void flashOverlay.offsetWidth;
  flashOverlay.classList.add('flash');
}
