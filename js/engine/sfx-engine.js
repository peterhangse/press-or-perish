/**
 * SFX ENGINE — Web Audio API synthesized UI sounds
 * Press or Perish · 1970s Nordic newsroom aesthetic
 *
 * All sounds are synthesised in real-time (zero audio files).
 * A-minor harmonic base, ±5 % pitch randomisation, short attack.
 */

import { isMuted } from './audio-manager.js';

// ─── Shared context ──────────────────────────────────────────
let ctx = null;

function getCtx() {
  if (!ctx) ctx = new (window.AudioContext || window.webkitAudioContext)();
  if (ctx.state === 'suspended') ctx.resume();
  return ctx;
}

// ─── Helpers ─────────────────────────────────────────────────

/** Random pitch deviation (±5 %) */
function rnd(freq) {
  return freq * (0.95 + Math.random() * 0.1);
}

/** Create a gain node, connect to destination, return it. */
function gain(ac, vol) {
  const g = ac.createGain();
  g.gain.value = vol;
  g.connect(ac.destination);
  return g;
}

/** Quick white-noise buffer (1 frame, 44 100 samples). */
function noiseBuf(ac) {
  const buf = ac.createBuffer(1, ac.sampleRate, ac.sampleRate);
  const data = buf.getChannelData(0);
  for (let i = 0; i < data.length; i++) data[i] = Math.random() * 2 - 1;
  return buf;
}

// ─── Sound catalogue ────────────────────────────────────────

/**
 * TICK — lightest touch, per-word typewriter, ambient pings
 * 15 ms filtered noise burst
 */
function tick() {
  const ac = getCtx();
  const t = ac.currentTime;
  const g = gain(ac, 0.06);

  const noise = ac.createBufferSource();
  noise.buffer = noiseBuf(ac);
  const hp = ac.createBiquadFilter();
  hp.type = 'highpass';
  hp.frequency.value = rnd(4000);

  noise.connect(hp);
  hp.connect(g);

  g.gain.setValueAtTime(0.06, t);
  g.gain.exponentialRampToValueAtTime(0.001, t + 0.015);

  noise.start(t);
  noise.stop(t + 0.02);
}

/**
 * CLICK — button presses, menu interactions
 * 30 ms sine + slight pitch drop
 */
function click() {
  const ac = getCtx();
  const t = ac.currentTime;
  const g = gain(ac, 0.10);

  const osc = ac.createOscillator();
  osc.type = 'sine';
  osc.frequency.setValueAtTime(rnd(660), t);            // A5 area
  osc.frequency.exponentialRampToValueAtTime(rnd(440), t + 0.03);
  osc.connect(g);

  g.gain.setValueAtTime(0.10, t);
  g.gain.exponentialRampToValueAtTime(0.001, t + 0.035);

  osc.start(t);
  osc.stop(t + 0.04);
}

/**
 * SELECT — choosing a card/option (upward sweep)
 * 60 ms sine sweep from A4 → E5
 */
function select() {
  const ac = getCtx();
  const t = ac.currentTime;
  const g = gain(ac, 0.10);

  const osc = ac.createOscillator();
  osc.type = 'triangle';
  osc.frequency.setValueAtTime(rnd(440), t);            // A4
  osc.frequency.exponentialRampToValueAtTime(rnd(659), t + 0.06);  // E5
  osc.connect(g);

  g.gain.setValueAtTime(0.10, t);
  g.gain.exponentialRampToValueAtTime(0.001, t + 0.07);

  osc.start(t);
  osc.stop(t + 0.08);
}

/**
 * DESELECT — un-choosing (downward sweep)
 * 40 ms triangle sweep from E5 → A4
 */
function deselect() {
  const ac = getCtx();
  const t = ac.currentTime;
  const g = gain(ac, 0.08);

  const osc = ac.createOscillator();
  osc.type = 'triangle';
  osc.frequency.setValueAtTime(rnd(659), t);
  osc.frequency.exponentialRampToValueAtTime(rnd(440), t + 0.04);
  osc.connect(g);

  g.gain.setValueAtTime(0.08, t);
  g.gain.exponentialRampToValueAtTime(0.001, t + 0.05);

  osc.start(t);
  osc.stop(t + 0.06);
}

/**
 * STAMP — rubber stamp (ASSIGNED, FILED, PRESS)
 * 200 ms heavy impact: low sine hit + noise burst
 */
function stamp() {
  const ac = getCtx();
  const t = ac.currentTime;

  // Low thud
  const g1 = gain(ac, 0.18);
  const osc = ac.createOscillator();
  osc.type = 'sine';
  osc.frequency.setValueAtTime(rnd(110), t);             // A2
  osc.frequency.exponentialRampToValueAtTime(rnd(55), t + 0.2);
  osc.connect(g1);
  g1.gain.setValueAtTime(0.18, t);
  g1.gain.exponentialRampToValueAtTime(0.001, t + 0.25);
  osc.start(t);
  osc.stop(t + 0.3);

  // Ink-on-paper noise
  const g2 = gain(ac, 0.12);
  const noise = ac.createBufferSource();
  noise.buffer = noiseBuf(ac);
  const bp = ac.createBiquadFilter();
  bp.type = 'bandpass';
  bp.frequency.value = rnd(1200);
  bp.Q.value = 1.5;
  noise.connect(bp);
  bp.connect(g2);
  g2.gain.setValueAtTime(0.12, t);
  g2.gain.exponentialRampToValueAtTime(0.001, t + 0.15);
  noise.start(t);
  noise.stop(t + 0.2);
}

/**
 * NOTE — pen scratch / notesheet scribble
 * 80 ms filtered noise
 */
function note() {
  const ac = getCtx();
  const t = ac.currentTime;
  const g = gain(ac, 0.07);

  const noise = ac.createBufferSource();
  noise.buffer = noiseBuf(ac);
  const bp = ac.createBiquadFilter();
  bp.type = 'bandpass';
  bp.frequency.value = rnd(2500);
  bp.Q.value = 2;
  noise.connect(bp);
  bp.connect(g);

  g.gain.setValueAtTime(0.07, t);
  g.gain.exponentialRampToValueAtTime(0.001, t + 0.08);
  noise.start(t);
  noise.stop(t + 0.1);
}

/**
 * REVEAL — dramatic result unveil, newspaper card slide-in
 * 400 ms low tone → harmonic bloom
 */
function reveal() {
  const ac = getCtx();
  const t = ac.currentTime;

  const g = gain(ac, 0.12);
  const osc = ac.createOscillator();
  osc.type = 'sawtooth';
  osc.frequency.setValueAtTime(rnd(110), t);
  osc.frequency.exponentialRampToValueAtTime(rnd(220), t + 0.3);
  const lp = ac.createBiquadFilter();
  lp.type = 'lowpass';
  lp.frequency.setValueAtTime(400, t);
  lp.frequency.exponentialRampToValueAtTime(2000, t + 0.35);
  osc.connect(lp);
  lp.connect(g);

  g.gain.setValueAtTime(0.12, t);
  g.gain.linearRampToValueAtTime(0.12, t + 0.25);
  g.gain.exponentialRampToValueAtTime(0.001, t + 0.4);

  osc.start(t);
  osc.stop(t + 0.45);
}

/**
 * TENSION — dark low drone pulse, deficit danger
 * 300 ms sub-bass throb
 */
function tension() {
  const ac = getCtx();
  const t = ac.currentTime;

  const g = gain(ac, 0.14);
  const osc = ac.createOscillator();
  osc.type = 'sawtooth';
  osc.frequency.setValueAtTime(rnd(73.4), t);             // D2 – dark
  const lp = ac.createBiquadFilter();
  lp.type = 'lowpass';
  lp.frequency.value = 300;
  osc.connect(lp);
  lp.connect(g);

  g.gain.setValueAtTime(0.001, t);
  g.gain.linearRampToValueAtTime(0.14, t + 0.05);
  g.gain.linearRampToValueAtTime(0.14, t + 0.2);
  g.gain.exponentialRampToValueAtTime(0.001, t + 0.3);

  osc.start(t);
  osc.stop(t + 0.35);
}

/**
 * RELIEF — bright upward tone, positive outcome
 * 250 ms major-feel arpeggio (A4 → C#5 → E5)
 */
function relief() {
  const ac = getCtx();
  const t = ac.currentTime;
  const g = gain(ac, 0.10);

  const osc = ac.createOscillator();
  osc.type = 'triangle';
  // Quick major arpeggio
  osc.frequency.setValueAtTime(rnd(440), t);              // A4
  osc.frequency.setValueAtTime(rnd(554), t + 0.08);       // C#5
  osc.frequency.setValueAtTime(rnd(659), t + 0.16);       // E5

  osc.connect(g);
  g.gain.setValueAtTime(0.10, t);
  g.gain.linearRampToValueAtTime(0.10, t + 0.18);
  g.gain.exponentialRampToValueAtTime(0.001, t + 0.25);

  osc.start(t);
  osc.stop(t + 0.3);
}

/**
 * SLAM — big title impact (PERISHED, SURVIVED, title words)
 * 150 ms aggressive hit: square wave + noise
 */
function slam() {
  const ac = getCtx();
  const t = ac.currentTime;

  // Square wave punch
  const g1 = gain(ac, 0.20);
  const osc = ac.createOscillator();
  osc.type = 'square';
  osc.frequency.setValueAtTime(rnd(82.4), t);             // E2
  osc.frequency.exponentialRampToValueAtTime(rnd(41.2), t + 0.15);
  osc.connect(g1);
  g1.gain.setValueAtTime(0.20, t);
  g1.gain.exponentialRampToValueAtTime(0.001, t + 0.18);
  osc.start(t);
  osc.stop(t + 0.2);

  // Transient noise
  const g2 = gain(ac, 0.15);
  const noise = ac.createBufferSource();
  noise.buffer = noiseBuf(ac);
  noise.connect(g2);
  g2.gain.setValueAtTime(0.15, t);
  g2.gain.exponentialRampToValueAtTime(0.001, t + 0.06);
  noise.start(t);
  noise.stop(t + 0.08);
}

/**
 * AMBIENT_TICK — clock/timer/day-reveal ambient pulse
 * 20 ms very quiet ping
 */
function ambientTick() {
  const ac = getCtx();
  const t = ac.currentTime;
  const g = gain(ac, 0.04);

  const osc = ac.createOscillator();
  osc.type = 'sine';
  osc.frequency.setValueAtTime(rnd(1760), t);             // A6 — high, thin
  osc.connect(g);

  g.gain.setValueAtTime(0.04, t);
  g.gain.exponentialRampToValueAtTime(0.001, t + 0.02);

  osc.start(t);
  osc.stop(t + 0.03);
}

/**
 * REJECT — negative result, rejection stamp in onboarding
 * 100 ms downward buzz
 */
function reject() {
  const ac = getCtx();
  const t = ac.currentTime;
  const g = gain(ac, 0.10);

  const osc = ac.createOscillator();
  osc.type = 'sawtooth';
  osc.frequency.setValueAtTime(rnd(220), t);              // A3
  osc.frequency.exponentialRampToValueAtTime(rnd(110), t + 0.10);
  const lp = ac.createBiquadFilter();
  lp.type = 'lowpass';
  lp.frequency.value = 600;
  osc.connect(lp);
  lp.connect(g);

  g.gain.setValueAtTime(0.10, t);
  g.gain.exponentialRampToValueAtTime(0.001, t + 0.12);

  osc.start(t);
  osc.stop(t + 0.15);
}

// ─── Public API ──────────────────────────────────────────────

const catalogue = {
  tick,
  click,
  select,
  deselect,
  stamp,
  note,
  reveal,
  tension,
  relief,
  slam,
  ambientTick,
  reject,
};

/**
 * Play a named SFX. No-ops if muted or unknown name.
 * @param {string} name - key from catalogue
 */
export function play(name) {
  if (isMuted()) return;
  const fn = catalogue[name];
  if (fn) fn();
}

/**
 * Warm up the AudioContext (call on first user gesture).
 * Safe to call multiple times.
 */
export function warmUp() {
  getCtx();
}
