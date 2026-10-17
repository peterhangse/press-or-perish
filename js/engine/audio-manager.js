/**
 * AUDIO MANAGER — Multi-track audio: title, game (looped), perish/survive
 */

import * as Settings from './settings.js';

const FADE_DURATION = 3;       // seconds for fade in/out
const TITLE_VOLUME = 0.3;     // title screen music
const GAME_VOLUME = 0.25;     // in-game background loop
const PERISH_VOLUME = 0.35;   // perish/survive screen

// Track registry
const tracks = {};
let muted = false;
let activeTrack = null;       // currently playing track name

/**
 * Create or get a track by name
 */
function getTrack(name) {
  if (!tracks[name]) {
    const src = {
      title:  'audio/soundtrack.mp3',
      game:   'audio/Soundtrack_Ingame.mp3?v=2',
      perish: 'audio/Soundtrack_perishscreen.mp3',
    }[name];
    const vol = {
      title:  TITLE_VOLUME,
      game:   GAME_VOLUME,
      perish: PERISH_VOLUME,
    }[name] || 0.3;

    const el = new Audio(src);
    el.volume = 0;

    // Perish track: loop back at 0:18 instead of playing full file
    if (name === 'perish') {
      el.loop = false;
      el.addEventListener('timeupdate', () => {
        if (el.currentTime >= 18) {
          el.currentTime = 0;
          el.play().catch(() => {});
        }
      });
    } else {
      el.loop = true;
    }

    tracks[name] = { el, maxVolume: vol, fadeInterval: null };
  }
  return tracks[name];
}

// Restore mute preference on load
try { muted = localStorage.getItem('pop_muted') === 'true'; } catch { muted = false; }

/** Target volume for a track: its base level scaled by the music volume setting. */
function targetVolume(track) {
  const scale = Settings.get('musicVolume');
  return track.maxVolume * (typeof scale === 'number' ? scale : 1);
}

/** Apply the current music volume setting to the playing track. */
function applyMusicVolume() {
  if (!activeTrack || muted) return;
  const track = tracks[activeTrack];
  if (!track) return;
  clearTrackFade(track);
  track.el.volume = targetVolume(track);
}
Settings.onChange((key) => { if (key === 'musicVolume') applyMusicVolume(); });

// Pause music while the tab is hidden, resume when it comes back
let pausedByVisibility = false;
if (typeof document !== 'undefined') {
  document.addEventListener('visibilitychange', () => {
    const track = activeTrack && tracks[activeTrack];
    if (!track) return;
    if (document.hidden) {
      if (!track.el.paused) { track.el.pause(); pausedByVisibility = true; }
    } else if (pausedByVisibility) {
      pausedByVisibility = false;
      track.el.play().catch(() => {});
    }
  });
}

/**
 * Play a named track with fade-in. Fades out any currently active track first.
 * @param {string} name - 'title' | 'game' | 'perish'
 */
function play(name = 'title') {
  if (activeTrack === name) return; // already playing

  // Fade out previous track
  if (activeTrack) {
    const prev = activeTrack;
    fadeOutTrack(prev, () => {
      const t = tracks[prev];
      if (t) { t.el.pause(); t.el.currentTime = 0; }
    });
  }

  activeTrack = name;
  const track = getTrack(name);
  track.el.volume = 0;

  const promise = track.el.play();
  if (promise) {
    promise.then(() => {
      if (!muted) fadeInTrack(name);
    }).catch(() => {
      // Autoplay blocked — will retry on user interaction
    });
  }
}

/**
 * Retry play after user interaction
 */
function retryPlay() {
  if (activeTrack) {
    const track = tracks[activeTrack];
    if (track && track.el.paused) {
      track.el.play().then(() => {
        if (!muted) fadeInTrack(activeTrack);
      }).catch(() => {});
    }
  }
}

/**
 * Stop current track with fade-out
 */
function stop() {
  if (!activeTrack) return;
  const name = activeTrack;
  activeTrack = null;
  fadeOutTrack(name, () => {
    const t = tracks[name];
    if (t) { t.el.pause(); t.el.currentTime = 0; }
  });
}

/**
 * Fade in a specific track
 */
function fadeInTrack(name) {
  const track = tracks[name];
  if (!track) return;
  clearTrackFade(track);
  const target = targetVolume(track);
  const step = Math.max(target, 0.001) / (FADE_DURATION * 20);
  track.fadeInterval = setInterval(() => {
    if (muted) { track.el.volume = 0; clearTrackFade(track); return; }
    if (track.el.volume + step >= target) {
      track.el.volume = target;
      clearTrackFade(track);
    } else {
      track.el.volume = Math.min(track.el.volume + step, target);
    }
  }, 50);
}

/**
 * Fade out a specific track, then call onDone
 */
function fadeOutTrack(name, onDone) {
  const track = tracks[name];
  if (!track) { if (onDone) onDone(); return; }
  clearTrackFade(track);
  const startVol = track.el.volume;
  if (startVol <= 0) { if (onDone) onDone(); return; }
  const step = startVol / (FADE_DURATION * 20);
  track.fadeInterval = setInterval(() => {
    if (track.el.volume - step <= 0) {
      track.el.volume = 0;
      clearTrackFade(track);
      if (onDone) onDone();
    } else {
      track.el.volume = Math.max(track.el.volume - step, 0);
    }
  }, 50);
}

function clearTrackFade(track) {
  if (track.fadeInterval) {
    clearInterval(track.fadeInterval);
    track.fadeInterval = null;
  }
}

/**
 * Toggle mute on/off. Returns new muted state.
 */
function toggleMute() {
  muted = !muted;
  try { localStorage.setItem('pop_muted', muted); } catch { /* ignore */ }
  // Apply to all tracks
  Object.values(tracks).forEach(track => {
    if (muted) {
      track.el.volume = 0;
    } else if (activeTrack) {
      const active = tracks[activeTrack];
      if (active === track) {
        track.el.volume = targetVolume(track);
      }
    }
  });
  return muted;
}

function isMuted() {
  return muted;
}

/**
 * Get the name of the currently playing track
 */
function getActiveTrack() {
  return activeTrack;
}

export { play, stop, retryPlay, toggleMute, isMuted, getActiveTrack };
