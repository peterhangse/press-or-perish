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
 */
export function render(leads, day, bossNote, callback) {
  currentLeads = leads;
  selectedIndex = null;
  onInvestigate = callback;

  const container = document.getElementById('screen-desk');
  container.innerHTML = '';

  // Top bar with window
  const topBar = document.createElement('div');
  topBar.className = 'desk-top-bar';

  const window_ = document.createElement('div');
  window_.className = 'desk-window';
  const sky = document.createElement('div');
  sky.className = 'desk-window-sky morning';
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

    // Random visual flair — each card gets a unique look
    applyCardFlair(card, lead, i);

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
function applyCardFlair(card, lead, index) {
  // Seeded pseudo-random based on story id for consistency
  const seed = (lead.id || '').split('').reduce((a, c) => a + c.charCodeAt(0), 0) + index;
  const h1 = (seed * 7 + 13) % 100;
  const h2 = (seed * 11 + 7) % 100;
  const h3 = (seed * 17 + 3) % 100;

  // ~12% chance of coffee ring stain — randomized position
  if ((seed * 7) % 100 < 12) {
    card.classList.add('flair-coffee');
    card.style.setProperty('--coffee-x', `${15 + h1 * 0.65}%`);
    card.style.setProperty('--coffee-y', `${20 + h2 * 0.55}%`);
    card.style.setProperty('--coffee-size', `${14 + (h3 % 10)}px`);
  }

  // Letters: ~20% chance of faint postal stamp — randomized angle + position
  if (lead.source_type === 'letter' && (seed * 11) % 100 < 20) {
    card.classList.add('flair-stamp');
    card.style.setProperty('--stamp-rot', `${-28 + (h1 % 36)}deg`);
    card.style.setProperty('--stamp-x', `${35 + (h2 % 35)}%`);
    card.style.setProperty('--stamp-y', `${30 + (h3 % 35)}%`);
  }

  // Documents: ~15% chance of paper clip — randomized horizontal position
  if (lead.source_type === 'document' && (seed * 17) % 100 < 15) {
    card.classList.add('flair-clip');
    card.style.setProperty('--clip-x', `${10 + (h1 % 55)}%`);
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
