/**
 * KEYBOARD — play the whole game without a mouse
 *
 * Enter / Space  finish the line being typed, otherwise press the screen's main button
 * 1–8            pick a lead on the desk, or a question in the interview
 * Escape         close an open panel (settings, highscores, achievements)
 *
 * Focused buttons and inputs keep their native behaviour.
 */

import { completeTypewriter } from './interview-screen.js';

function activeScreen() {
  return document.querySelector('.screen.active');
}

function isVisible(el) {
  return !!el && el.offsetParent !== null && getComputedStyle(el).visibility !== 'hidden';
}

function firstVisible(selector, root = document) {
  return [...root.querySelectorAll(selector)].find(isVisible) || null;
}

/** An open overlay/modal takes keyboard priority over the screen behind it */
function openOverlay() {
  return firstVisible('.settings-overlay, .highscore-overlay, .name-prompt-overlay')
    || document.querySelector('.achievements-backdrop.open');
}

function pressPrimary() {
  // Title screen: reveal the menu
  const title = document.getElementById('start-title');
  if (isVisible(title) && !title.classList.contains('settled')) { title.click(); return true; }

  // Boss note on the tutorial desk
  const backdrop = firstVisible('.flyin-backdrop');
  if (backdrop) { backdrop.click(); return true; }

  const screen = activeScreen();
  if (!screen) return false;

  // Click-to-continue screens
  if (screen.id === 'screen-transition') { screen.click(); return true; }

  const primary = [...screen.querySelectorAll('[data-primary="true"]')]
    .filter(el => isVisible(el) && !el.disabled).pop();
  if (primary) { primary.click(); return true; }

  // Fallback: the last visible enabled paper button on this screen
  const btn = [...screen.querySelectorAll('button.btn-paper, .onboarding-btn, button.start-btn')]
    .filter(el => isVisible(el) && !el.disabled).pop();
  if (btn) { btn.click(); return true; }
  return false;
}

function pickNumber(n) {
  const screen = activeScreen();
  if (!screen) return false;
  if (screen.id === 'screen-interview') {
    const qs = [...screen.querySelectorAll('.question-btn')].filter(isVisible);
    const q = qs[n - 1];
    if (q && !q.disabled) { q.click(); return true; }
    return false;
  }
  if (screen.id === 'screen-desk' && !firstVisible('.flyin-backdrop')) {
    const cards = [...screen.querySelectorAll('.lead-card')].filter(isVisible);
    const card = cards[n - 1];
    if (card) { card.click(); card.focus(); return true; }
  }
  return false;
}

function closeOverlay(overlay) {
  const close = [...overlay.querySelectorAll('button')].find(b => /close|×|✕/i.test(b.textContent) || b.classList.contains('close'));
  if (close) { close.click(); return true; }
  overlay.click();
  return true;
}

export function init() {
  document.addEventListener('keydown', (e) => {
    if (e.defaultPrevented || e.altKey || e.ctrlKey || e.metaKey) return;
    const target = e.target;
    const tag = target?.tagName;
    if (tag === 'INPUT' || tag === 'TEXTAREA' || tag === 'SELECT') return;

    const overlay = openOverlay();
    if (e.key === 'Escape') {
      if (overlay) { e.preventDefault(); closeOverlay(overlay); }
      return;
    }
    if (overlay) return; // let the overlay's own buttons handle the rest

    if (e.key === 'Enter' || e.key === ' ') {
      // A focused button/card already does the right thing natively
      if (tag === 'BUTTON' || target?.getAttribute?.('role') === 'button') {
        if (completeTypewriter()) e.preventDefault();
        return;
      }
      if (completeTypewriter() || pressPrimary()) e.preventDefault();
      return;
    }

    if (/^[1-8]$/.test(e.key)) {
      if (pickNumber(Number(e.key))) e.preventDefault();
    }
  });
}
