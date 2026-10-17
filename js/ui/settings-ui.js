/**
 * SETTINGS UI — gear button + settings panel (volume, text speed, text size, motion)
 */

import * as Settings from '../engine/settings.js';
import * as SFX from '../engine/sfx-engine.js';

let lastFocus = null;

/** Apply display-related settings to the page (called on boot, on change and on resize). */
export function applyDisplaySettings(scale) {
  const root = document.documentElement;
  const large = Settings.get('largeText');
  // Automatic: larger text when the game is drawn small (phones, small windows)
  const autoLarge = typeof scale === 'number' ? scale < 1.3 : root.classList.contains('auto-large');
  if (typeof scale === 'number') root.classList.toggle('auto-large', autoLarge);
  root.classList.toggle('large-text', large === true || (large === null && autoLarge));

  const motion = Settings.get('reduceMotion');
  root.classList.toggle('reduce-motion', motion === true);
  root.classList.toggle('motion-on', motion === false);
}

export function addSettingsButton() {
  const wrapper = document.getElementById('game-wrapper');
  if (!wrapper) return;
  const btn = document.createElement('button');
  btn.id = 'settings-btn';
  btn.className = 'settings-btn';
  btn.setAttribute('aria-label', 'Settings');
  btn.title = 'Settings';
  btn.textContent = '⚙';
  btn.style.display = 'none'; // shown with the other corner buttons after the title click
  btn.addEventListener('click', () => { SFX.play('click'); open(); });
  wrapper.appendChild(btn);

  Settings.onChange(() => applyDisplaySettings());
  applyDisplaySettings();
}

export function showButton() {
  const btn = document.getElementById('settings-btn');
  if (btn) btn.style.display = '';
}

function segmented(label, key, options) {
  const row = document.createElement('div');
  row.className = 'settings-row';
  const name = document.createElement('div');
  name.className = 'settings-label';
  name.textContent = label;
  row.appendChild(name);

  const group = document.createElement('div');
  group.className = 'settings-segmented';
  group.setAttribute('role', 'radiogroup');
  group.setAttribute('aria-label', label);
  const render = () => {
    group.querySelectorAll('button').forEach(b => {
      const on = JSON.stringify(Settings.get(key)) === b.dataset.value;
      b.classList.toggle('on', on);
      b.setAttribute('aria-checked', on ? 'true' : 'false');
    });
  };
  options.forEach(([text, value]) => {
    const b = document.createElement('button');
    b.type = 'button';
    b.setAttribute('role', 'radio');
    b.dataset.value = JSON.stringify(value);
    b.textContent = text;
    b.addEventListener('click', () => { Settings.set(key, value); SFX.play('click'); render(); });
    group.appendChild(b);
  });
  render();
  row.appendChild(group);
  return row;
}

function slider(label, key) {
  const row = document.createElement('label');
  row.className = 'settings-row';
  const name = document.createElement('div');
  name.className = 'settings-label';
  name.textContent = label;
  const input = document.createElement('input');
  input.type = 'range';
  input.min = '0';
  input.max = '100';
  input.step = '5';
  input.value = String(Math.round((Settings.get(key) ?? 1) * 100));
  input.className = 'settings-range';
  const out = document.createElement('span');
  out.className = 'settings-value';
  out.textContent = `${input.value}%`;
  input.addEventListener('input', () => {
    Settings.set(key, Number(input.value) / 100);
    out.textContent = `${input.value}%`;
  });
  input.addEventListener('change', () => { if (key === 'sfxVolume') SFX.play('click'); });
  row.appendChild(name);
  row.appendChild(input);
  row.appendChild(out);
  return row;
}

export function open() {
  close();
  lastFocus = document.activeElement;
  const wrapper = document.getElementById('game-wrapper');
  const overlay = document.createElement('div');
  overlay.className = 'settings-overlay';
  overlay.addEventListener('click', (e) => { if (e.target === overlay) close(); });

  const card = document.createElement('div');
  card.className = 'settings-card';
  card.setAttribute('role', 'dialog');
  card.setAttribute('aria-modal', 'true');
  card.setAttribute('aria-label', 'Settings');

  const title = document.createElement('div');
  title.className = 'settings-title';
  title.textContent = 'SETTINGS';
  card.appendChild(title);

  card.appendChild(slider('Music', 'musicVolume'));
  card.appendChild(slider('Sound effects', 'sfxVolume'));
  card.appendChild(segmented('Text speed', 'textSpeed', [['Normal', 'normal'], ['Fast', 'fast'], ['Instant', 'instant']]));
  card.appendChild(segmented('Larger text', 'largeText', [['Auto', null], ['On', true], ['Off', false]]));
  card.appendChild(segmented('Reduce motion', 'reduceMotion', [['System', null], ['On', true], ['Off', false]]));

  const tip = document.createElement('div');
  tip.className = 'settings-tip';
  tip.textContent = 'Keys: Enter/Space continue or skip text · 1–8 pick a lead or question · Esc close';
  card.appendChild(tip);

  const closeBtn = document.createElement('button');
  closeBtn.className = 'btn-paper settings-close';
  closeBtn.textContent = 'Close';
  closeBtn.addEventListener('click', () => { SFX.play('click'); close(); });
  card.appendChild(closeBtn);

  overlay.appendChild(card);
  wrapper.appendChild(overlay);
  closeBtn.focus();
}

export function close() {
  document.querySelectorAll('.settings-overlay').forEach(el => el.remove());
  if (lastFocus && document.contains(lastFocus)) lastFocus.focus();
  lastFocus = null;
}
