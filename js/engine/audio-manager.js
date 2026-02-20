/**
 * AUDIO MANAGER — Multi-track audio: title, game (looped), perish/survive
 */

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
    el.loop = true;
    el.volume = 0;
    tracks[name] = { el, maxVolume: vol, fadeInterval: null };
  }
  return tracks[name];
}

// Restore mute preference on load
muted = localStorage.getItem('pop_muted') === 'true';

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
  const step = track.maxVolume / (FADE_DURATION * 20);
  track.fadeInterval = setInterval(() => {
    if (muted) { track.el.volume = 0; clearTrackFade(track); return; }
    if (track.el.volume + step >= track.maxVolume) {
      track.el.volume = track.maxVolume;
      clearTrackFade(track);
    } else {
      track.el.volume = Math.min(track.el.volume + step, track.maxVolume);
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
  localStorage.setItem('pop_muted', muted);
  // Apply to all tracks
  Object.values(tracks).forEach(track => {
    if (muted) {
      track.el.volume = 0;
    } else if (activeTrack) {
      const active = tracks[activeTrack];
      if (active === track) {
        track.el.volume = track.maxVolume;
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
