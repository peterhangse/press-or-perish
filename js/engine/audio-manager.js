/**
 * AUDIO MANAGER — Title screen music with fade in/out and crossfade loop
 */

const FADE_DURATION = 5;    // seconds for fade in/out
const DEFAULT_VOLUME = 0.3; // 30% — background level

let audio = null;
let maxVolume = DEFAULT_VOLUME;
let muted = false;
let fadeInterval = null;

/**
 * Initialize the audio element
 */
function init() {
  if (audio) return;
  audio = new Audio('audio/soundtrack.mp3');
  audio.loop = true;
  audio.volume = 0;

  // Restore mute preference
  muted = localStorage.getItem('pop_muted') === 'true';
}

/**
 * Start playing with fade-in
 */
function play() {
  init();
  if (muted) {
    audio.volume = 0;
    audio.play().catch(() => {});
    return;
  }
  audio.volume = 0;
  audio.play().catch(() => {});
  fadeIn();
}

/**
 * Stop with fade-out, then pause
 */
function stop() {
  if (!audio) return;
  fadeOut(() => {
    audio.pause();
    audio.currentTime = 0;
  });
}

/**
 * Fade in over FADE_DURATION seconds
 */
function fadeIn() {
  clearFade();
  const step = maxVolume / (FADE_DURATION * 20); // 20 ticks/sec
  fadeInterval = setInterval(() => {
    if (!audio) { clearFade(); return; }
    if (audio.volume + step >= maxVolume) {
      audio.volume = muted ? 0 : maxVolume;
      clearFade();
    } else {
      audio.volume = muted ? 0 : Math.min(audio.volume + step, maxVolume);
    }
  }, 50);
}

/**
 * Fade out over FADE_DURATION seconds, then call onDone
 */
function fadeOut(onDone) {
  if (!audio) { if (onDone) onDone(); return; }
  clearFade();
  const startVol = audio.volume;
  if (startVol <= 0) { if (onDone) onDone(); return; }
  const step = startVol / (FADE_DURATION * 20);
  fadeInterval = setInterval(() => {
    if (!audio) { clearFade(); if (onDone) onDone(); return; }
    if (audio.volume - step <= 0) {
      audio.volume = 0;
      clearFade();
      if (onDone) onDone();
    } else {
      audio.volume = Math.max(audio.volume - step, 0);
    }
  }, 50);
}

function clearFade() {
  if (fadeInterval) {
    clearInterval(fadeInterval);
    fadeInterval = null;
  }
}

/**
 * Toggle mute on/off. Returns new muted state.
 */
function toggleMute() {
  muted = !muted;
  localStorage.setItem('pop_muted', muted);
  if (audio) {
    if (muted) {
      audio.volume = 0;
    } else {
      audio.volume = maxVolume;
    }
  }
  return muted;
}

function isMuted() {
  return muted;
}

export { play, stop, toggleMute, isMuted };
