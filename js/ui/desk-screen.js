/**
 * DESK SCREEN — Morning lead selection (8 leads, pick 1)
 */

import * as ScreenManager from './screen-manager.js';
import * as SFX from '../engine/sfx-engine.js';

let currentLeads = [];
let selectedIndex = null;
let onInvestigate = null;

/**
 * Render the desk with today's leads
 * @param {Array} leads - 8 story objects for today
 * @param {number} day - Current day number
 * @param {Object} bossNote - { text, name } boss note for today
 * @param {Function} callback - Called with selected story when player investigates
 * @param {Object} [townConfig] - Optional town config for visual theming
 */
export function render(leads, day, bossNote, callback, townConfig) {
  currentLeads = leads;
  selectedIndex = null;
  onInvestigate = callback;

  const container = document.getElementById('screen-desk');
  container.innerHTML = '';

  // Apply town-specific CSS class
  container.classList.remove('town-smastad', 'town-industristad');
  if (townConfig?.cssClass) {
    container.classList.add(townConfig.cssClass);
  }

  // Top bar with window
  const topBar = document.createElement('div');
  topBar.className = 'desk-top-bar';

  const window_ = document.createElement('div');
  window_.className = 'desk-window';
  const sky = document.createElement('div');
  sky.className = 'desk-window-sky morning';

  // Add smoke elements for Industristad
  if (townConfig?.id === 'industristad') {
    for (let i = 0; i < 6; i++) {
      const smoke = document.createElement('div');
      smoke.className = 'chimney-smoke';
      sky.appendChild(smoke);
    }
  }

  window_.appendChild(sky);
  topBar.appendChild(window_);

  // Boss note (always create the pinned note element for Day Zero fly target)
  let pinnedNote = null;
  if (bossNote) {
    pinnedNote = document.createElement('div');
    pinnedNote.className = 'boss-note';
    if (day === 0) pinnedNote.style.visibility = 'hidden'; // hidden initially on Day Zero
    const noteName = document.createElement('div');
    noteName.className = 'boss-note-name';
    noteName.textContent = bossNote.name || 'Gunnar';
    const noteText = document.createElement('div');
    noteText.textContent = bossNote.text;
    pinnedNote.appendChild(noteName);
    pinnedNote.appendChild(noteText);
    topBar.appendChild(pinnedNote);
  }

  container.appendChild(topBar);

  // Lead cards grid
  const grid = document.createElement('div');
  grid.className = 'desk-leads';

  leads.forEach((lead, i) => {
    const card = document.createElement('div');
    card.className = 'lead-card';
    card.dataset.index = i;

    // Paper aging — each card gets a noticeably different paper tone
    const paperColors = townConfig?.id === 'industristad'
      ? [
          '#dddce0', // cool grey
          '#d8d8dc', // steel grey
          '#e0dfe2', // light grey
          '#d4d4da', // industrial grey
          '#dcdbe0', // blue-grey
          '#d6d6dc', // newsprint
          '#e2e1e4', // crisp grey
          '#d2d2d8', // aged grey
        ]
      : [
          '#e8dfc8', // standard cream
          '#e2d8b8', // yellowed
          '#ede4d0', // bright white-ish
          '#ddd4b4', // well-aged yellow
          '#e5dcc4', // warm cream
          '#e0d5b0', // old newsprint
          '#eae1cb', // fresh paper
          '#d8cfad', // very aged
        ];
    const paperIdx = ((lead.id || '').charCodeAt(0) + i * 7) % paperColors.length;
    card.style.setProperty('--paper-tone', paperColors[paperIdx]);

    // Random visual flair — each card gets a unique look
    applyCardFlair(card, lead, i, townConfig);

    // Source badge — colored tag
    const badge = document.createElement('div');
    badge.className = `lead-badge ${lead.source_type}`;
    badge.textContent = getSourceLabel(lead.source_type);

    // Headline — big and bold
    const headline = document.createElement('div');
    headline.className = 'lead-headline';
    headline.textContent = lead.title;

    // Lead description
    const leadText = document.createElement('div');
    leadText.className = 'lead-text';
    leadText.textContent = lead.lead_text || '';

    // Source: name + title
    const npcLine = document.createElement('div');
    npcLine.className = 'lead-npc';
    if (lead.npc_name) {
      const npcTitle = lead.npc_title ? `, ${lead.npc_title}` : '';
      npcLine.textContent = `Source: ${lead.npc_name}${npcTitle}`;
    }

    card.appendChild(badge);
    card.appendChild(headline);
    card.appendChild(leadText);
    card.appendChild(npcLine);

    card.addEventListener('click', () => selectLead(i));
    grid.appendChild(card);
  });

  container.appendChild(grid);

  // Bottom action bar
  const actionBar = document.createElement('div');
  actionBar.className = 'desk-action-bar';

  const selectedLabel = document.createElement('div');
  selectedLabel.className = 'desk-selected-label';
  selectedLabel.textContent = 'SELECT A LEAD TO INVESTIGATE';

  const investigateBtn = document.createElement('button');
  investigateBtn.className = 'desk-investigate-btn';
  investigateBtn.textContent = 'INVESTIGATE';
  investigateBtn.disabled = true;
  investigateBtn.addEventListener('click', () => {
    if (selectedIndex !== null && onInvestigate) {
      SFX.play('stamp');
      // Rubber stamp flash — Papers Please style
      showStamp(container, 'ASSIGNED');
      // Slight delay for stamp feel before transitioning
      setTimeout(() => {
        onInvestigate(currentLeads[selectedIndex]);
      }, 350);
    }
  });

  actionBar.appendChild(selectedLabel);
  actionBar.appendChild(investigateBtn);
  container.appendChild(actionBar);

  // Day Zero: fly-in boss note modal
  if (day === 0 && bossNote) {
    showFlyInNote(container, bossNote, pinnedNote);
  }
}

/**
 * Show a centered boss note that flies in, then on click animates to the pinned position
 */
function showFlyInNote(container, bossNote, pinnedNote) {
  // Dimmed backdrop
  const backdrop = document.createElement('div');
  backdrop.className = 'flyin-backdrop';

  // Centered modal note
  const modal = document.createElement('div');
  modal.className = 'flyin-note';

  const name = document.createElement('div');
  name.className = 'boss-note-name';
  name.style.fontSize = '11px';
  name.style.marginBottom = '6px';
  name.textContent = bossNote.name || 'Gunnar';

  const text = document.createElement('div');
  text.style.cssText = 'font-family: var(--font-body); font-size: 11px; color: var(--ink); line-height: 1.5;';
  text.textContent = bossNote.text;

  const hint = document.createElement('div');
  hint.style.cssText = 'font-family: var(--font-body); font-size: 8px; color: var(--ink-faded); margin-top: 8px; text-align: center;';
  hint.textContent = 'Click to continue';

  modal.appendChild(name);
  modal.appendChild(text);
  modal.appendChild(hint);
  backdrop.appendChild(modal);
  container.appendChild(backdrop);

  // Force reflow then trigger entrance animation
  void modal.offsetWidth;
  modal.classList.add('visible');

  // On click: animate note to pinned position, then remove modal
  backdrop.addEventListener('click', () => {
    SFX.play('click');
    modal.classList.remove('visible');
    modal.classList.add('fly-to-corner');

    modal.addEventListener('transitionend', () => {
      backdrop.remove();
      // Reveal the pinned note
      if (pinnedNote) {
        pinnedNote.style.visibility = 'visible';
        pinnedNote.classList.add('fade-in');
      }
    }, { once: true });
  });
}

/**
 * Handle lead selection — expand card to show detail
 */
function selectLead(index) {
  // If clicking the already selected card, deselect
  if (selectedIndex === index) {
    SFX.play('deselect');
    selectedIndex = null;
    document.querySelectorAll('.lead-card').forEach(card => {
      card.classList.remove('selected');
    });
    // Update bottom bar
    const label = document.querySelector('.desk-selected-label');
    const btn = document.querySelector('.desk-investigate-btn');
    if (label) label.textContent = 'SELECT A LEAD TO INVESTIGATE';
    if (btn) btn.disabled = true;
    return;
  }

  selectedIndex = index;
  SFX.play('select');

  // Update card selection visuals
  document.querySelectorAll('.lead-card').forEach((card, i) => {
    card.classList.toggle('selected', i === index);
  });

  // Update bottom bar
  const label = document.querySelector('.desk-selected-label');
  const btn = document.querySelector('.desk-investigate-btn');
  if (label) label.textContent = `ASSIGNED: ${currentLeads[index].title}`;
  if (btn) btn.disabled = false;
}

/**
 * Apply subtle visual flair to a lead card — randomized positions via CSS vars
 */
function applyCardFlair(card, lead, index, townConfig) {
  const isIndustrial = townConfig?.id === 'industristad';

  // Seeded pseudo-random based on story id for consistency
  const seed = (lead.id || '').split('').reduce((a, c) => a + c.charCodeAt(0), 0) + index;
  const h1 = (seed * 7 + 13) % 100;
  const h2 = (seed * 11 + 7) % 100;
  const h3 = (seed * 17 + 3) % 100;

  if (isIndustrial) {
    // Industristad: ~30% chance of grease/ink smudge
    if ((seed * 7) % 100 < 30) {
      card.classList.add('flair-grease');
      const size = 40 + (h3 % 30);
      const corner = (seed * 3) % 4;
      const offset = -(size * 0.3);
      const jX = (h1 % 10) - 5;
      const jY = (h2 % 10) - 5;
      let cx, cy;
      if (corner === 0)      { cx = offset + jX; cy = offset + jY; }
      else if (corner === 1) { cx = `calc(100% - ${size + offset - jX}px)`; cy = offset + jY; }
      else if (corner === 2) { cx = offset + jX; cy = `calc(100% - ${size + offset - jY}px)`; }
      else                   { cx = `calc(100% - ${size + offset - jX}px)`; cy = `calc(100% - ${size + offset - jY}px)`; }
      card.style.setProperty('--grease-size', `${size}px`);
      card.style.setProperty('--grease-x', typeof cx === 'number' ? `${cx}px` : cx);
      card.style.setProperty('--grease-y', typeof cy === 'number' ? `${cy}px` : cy);
      card.style.setProperty('--grease-rot', `${-20 + (h1 % 40)}deg`);
    }
  } else {
    // Småstad: ~25% chance of coffee stain
    if ((seed * 7) % 100 < 25) {
      card.classList.add('flair-coffee');
      const corner = (seed * 3) % 4;
      const size = 70 + (h3 % 30);
      const offset = -(size * 0.4);
      const jitterX = (h1 % 10) - 5;
      const jitterY = (h2 % 10) - 5;
      let cx, cy;
      if (corner === 0)      { cx = offset + jitterX; cy = offset + jitterY; }
      else if (corner === 1) { cx = `calc(100% - ${size + offset - jitterX}px)`; cy = offset + jitterY; }
      else if (corner === 2) { cx = offset + jitterX; cy = `calc(100% - ${size + offset - jitterY}px)`; }
      else                   { cx = `calc(100% - ${size + offset - jitterX}px)`; cy = `calc(100% - ${size + offset - jitterY}px)`; }
      card.style.setProperty('--coffee-size', `${size}px`);
      card.style.setProperty('--coffee-x', typeof cx === 'number' ? `${cx}px` : cx);
      card.style.setProperty('--coffee-y', typeof cy === 'number' ? `${cy}px` : cy);
    }
  }

  // Stamps — documents get "MOTTAGET" (Småstad) or "HEMLIGT" (both, via CSS)
  if (lead.source_type === 'letter' && (seed * 11) % 100 < 35) {
    card.classList.add('flair-stamp');
    card.style.setProperty('--stamp-rot', `${-28 + (h1 % 36)}deg`);
    card.style.setProperty('--stamp-x', `${35 + (h2 % 35)}%`);
    card.style.setProperty('--stamp-y', `${30 + (h3 % 35)}%`);
  }
}

/**
 * Get localized source type label
 */
function getSourceLabel(type) {
  switch (type) {
    case 'letter':   return 'Letter';
    case 'document': return 'Document';
    case 'street':   return 'Street Tip';
    default:         return 'Tip';
  }
}

/**
 * Show a rubber stamp flash — Papers Please style
 */
function showStamp(container, text) {
  const stamp = document.createElement('div');
  stamp.className = 'stamp-flash';
  stamp.textContent = text;
  container.appendChild(stamp);
  stamp.addEventListener('animationend', () => stamp.remove());
}
