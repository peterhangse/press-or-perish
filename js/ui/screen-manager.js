/**
 * SCREEN MANAGER — Controls screen transitions
 * Hard cuts (no fade), flash overlay for impact
 */

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

  // Toggle HUD bar
  if (SCREENS_WITH_UI.includes(screenId)) {
    hudBar.classList.add('visible');
  } else {
    hudBar.classList.remove('visible');
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
  flashOverlay.classList.remove('flash');
  void flashOverlay.offsetWidth;
  flashOverlay.classList.add('flash');
}
