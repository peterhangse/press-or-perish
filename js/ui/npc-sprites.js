/**
 * NPC SPRITES — CSS pixel art portraits for all interviewable characters
 * 
 * Each sprite is an array of pixel definitions: { x, y, w, h, cls, style? }
 *   x/y = position in pixels (scale-2 = 8px per unit, so multiply by 8)
 *   w/h = size in pixels
 *   cls = CSS color class (s-mid, h-brown, c-worker-blue, etc.)
 *   style = optional inline style override
 * 
 * Portrait container: 120×160px. Using 8px/pixel (scale-2 equivalent).
 * Grid: ~15×20 pixel units.
 */

// ── PIXEL HELPERS ──
// All coordinates in "pixel" units (multiply by PX at render time)
const PX = 8;

function hashStr(s) {
  let h = 0;
  for (let i = 0; i < s.length; i++) h = ((h << 5) - h + s.charCodeAt(i)) | 0;
  return Math.abs(h);
}

// ════════════════════════════════════════
// SPRITE DEFINITIONS — 28 NPCs
// Container: 15×20 grid, 8px/unit = 120×160px
// ════════════════════════════════════════

const SPRITES = {

  // ── KARL LINDSTRÖM — Sawmill worker, 34, guarded ──
  karl_lindstrom: {
    bg: 'background:linear-gradient(180deg,#1a2010 0%,#141808 60%,#1a1208 100%)',
    pixels: [
      // Hair — dark brown, swept, 70s sideburns
      { x: 4, y: 0, w: 7, h: 1, cls: 'h-dark-brown' },
      { x: 3, y: 1, w: 9, h: 1, cls: 'h-dark-brown' },
      { x: 2, y: 2, w: 1, h: 2, cls: 'h-dark-brown' },   // left sideburn
      { x: 12, y: 2, w: 1, h: 2, cls: 'h-dark-brown' },   // right sideburn
      // Head
      { x: 3, y: 2, w: 9, h: 6, cls: 's-mid' },
      // Stubble
      { x: 3, y: 7, w: 9, h: 1, style: 'background:#8a6040' },
      // Eyes — worried
      { x: 4, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 5, y: 4, w: 1, h: 1, cls: 'e-dark' },
      { x: 9, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 10, y: 4, w: 1, h: 1, cls: 'e-dark' },
      // Worried brows
      { x: 4, y: 3, w: 3, h: 1, cls: 'h-dark-brown', style: 'transform:rotate(6deg)' },
      { x: 9, y: 3, w: 3, h: 1, cls: 'h-dark-brown', style: 'transform:rotate(-6deg)' },
      // Nose
      { x: 6, y: 5, w: 3, h: 1, cls: 's-worn' },
      // Mouth — tight
      { x: 5, y: 7, w: 5, h: 1, style: 'background:#7a4a30;height:4px' },
      // Neck
      { x: 6, y: 8, w: 3, h: 2, cls: 's-mid' },
      // Body — worker's jacket
      { x: 2, y: 10, w: 11, h: 8, cls: 'c-worker-blue' },
      // Collar
      { x: 5, y: 10, w: 5, h: 2, cls: 'x-collar' },
      // Arms
      { x: 1, y: 11, w: 2, h: 7, cls: 'c-worker-blue' },
      { x: 12, y: 11, w: 2, h: 6, cls: 'c-worker-blue' },
      // Bandaged hand
      { x: 12, y: 16, w: 2, h: 2, cls: 'x-bandage' },
      // Shadow
      { x: 2, y: 17, w: 11, h: 1, cls: 'x-shadow' },
    ],
  },

  // ── BIRGITTA EKBERG — Mother of missing Anna, distressed ──
  birgitta_ekberg: {
    bg: 'background:linear-gradient(180deg,#1e1a14 0%,#181410 60%,#120e0a 100%)',
    pixels: [
      // Hair — blonde, shoulder length, messy
      { x: 3, y: 0, w: 9, h: 1, cls: 'h-blonde' },
      { x: 2, y: 1, w: 11, h: 1, cls: 'h-blonde' },
      { x: 2, y: 2, w: 1, h: 5, cls: 'h-blonde' },
      { x: 12, y: 2, w: 1, h: 5, cls: 'h-blonde' },
      // Head
      { x: 3, y: 2, w: 9, h: 6, cls: 's-pale' },
      // Eyes — red-rimmed from crying
      { x: 4, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 5, y: 4, w: 1, h: 1, cls: 'e-blue' },
      { x: 9, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 10, y: 4, w: 1, h: 1, cls: 'e-blue' },
      // Dark circles
      { x: 4, y: 5, w: 2, h: 1, style: 'background:rgba(120,70,60,0.4)' },
      { x: 9, y: 5, w: 2, h: 1, style: 'background:rgba(120,70,60,0.4)' },
      // Brows — raised, distressed
      { x: 4, y: 3, w: 3, h: 1, cls: 'h-blonde', style: 'transform:rotate(8deg)' },
      { x: 9, y: 3, w: 3, h: 1, cls: 'h-blonde', style: 'transform:rotate(-8deg)' },
      // Nose
      { x: 6, y: 5, w: 3, h: 1, cls: 's-pale' },
      // Mouth — trembling
      { x: 5, y: 7, w: 5, h: 1, style: 'background:#9a6058' },
      // Blush from crying
      { x: 3, y: 5, w: 2, h: 2, cls: 'x-blush' },
      { x: 10, y: 5, w: 2, h: 2, cls: 'x-blush' },
      // Neck
      { x: 6, y: 8, w: 3, h: 2, cls: 's-pale' },
      // Body — cardigan, clutching handbag
      { x: 2, y: 10, w: 11, h: 8, cls: 'c-cardigan-wine' },
      { x: 5, y: 10, w: 5, h: 2, cls: 'x-collar' },
      // Arms — holding something
      { x: 1, y: 11, w: 2, h: 7, cls: 'c-cardigan-wine' },
      { x: 12, y: 11, w: 2, h: 7, cls: 'c-cardigan-wine' },
      // Handbag
      { x: 12, y: 15, w: 3, h: 3, style: 'background:#5a3a18' },
      // Shadow
      { x: 2, y: 17, w: 11, h: 1, cls: 'x-shadow' },
    ],
  },

  // ── ERIK PERSSON — Farmer, tired ──
  erik_persson: {
    bg: 'background:linear-gradient(180deg,#1a2010 0%,#161a08 60%,#1a1208 100%)',
    pixels: [
      // Cap
      { x: 3, y: 0, w: 9, h: 2, style: 'background:#3a4030' },
      { x: 2, y: 1, w: 11, h: 1, style: 'background:#3a4030' },
      // Hair under cap — grey
      { x: 2, y: 2, w: 1, h: 2, cls: 'h-grey' },
      { x: 12, y: 2, w: 1, h: 2, cls: 'h-grey' },
      // Head — weathered
      { x: 3, y: 2, w: 9, h: 6, cls: 's-worn' },
      // Eyes — tired, downcast
      { x: 4, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 5, y: 4, w: 1, h: 1, cls: 'e-dark' },
      { x: 9, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 10, y: 4, w: 1, h: 1, cls: 'e-dark' },
      // Bags under eyes
      { x: 4, y: 5, w: 2, h: 1, style: 'background:rgba(100,70,50,0.4)' },
      { x: 9, y: 5, w: 2, h: 1, style: 'background:rgba(100,70,50,0.4)' },
      // Flat brows
      { x: 4, y: 3, w: 3, h: 1, cls: 'h-grey' },
      { x: 9, y: 3, w: 3, h: 1, cls: 'h-grey' },
      // Nose — broad
      { x: 6, y: 5, w: 3, h: 2, cls: 's-worn' },
      // Mouth — down
      { x: 5, y: 7, w: 5, h: 1, style: 'background:#7a4a38' },
      // Neck
      { x: 6, y: 8, w: 3, h: 2, cls: 's-worn' },
      // Body — plaid shirt
      { x: 2, y: 10, w: 11, h: 8, cls: 'c-shirt-check' },
      { x: 5, y: 10, w: 5, h: 2, cls: 'x-collar' },
      // Arms
      { x: 1, y: 11, w: 2, h: 7, cls: 'c-shirt-check' },
      { x: 12, y: 11, w: 2, h: 7, cls: 'c-shirt-check' },
      // Cap in hand
      { x: 0, y: 15, w: 3, h: 2, style: 'background:#3a4030' },
      // Shadow
      { x: 2, y: 17, w: 11, h: 1, cls: 'x-shadow' },
    ],
  },

  // ── GUNNAR EK — Editor-in-chief, glasses, intense ──
  gunnar_ek: {
    bg: 'background:linear-gradient(180deg,#1a1810 0%,#14120a 60%,#1a1208 100%)',
    pixels: [
      // Hair — thinning, grey
      { x: 4, y: 0, w: 7, h: 1, cls: 'h-grey' },
      { x: 3, y: 1, w: 9, h: 1, cls: 'h-grey' },
      // Head
      { x: 3, y: 2, w: 9, h: 6, cls: 's-worn' },
      // Glasses
      { x: 3, y: 3, w: 4, h: 2, style: 'background:transparent;border:1px solid #2a1a08' },
      { x: 8, y: 3, w: 4, h: 2, style: 'background:transparent;border:1px solid #2a1a08' },
      { x: 7, y: 4, w: 1, h: 1, style: 'background:#2a1a08;width:4px;height:4px' },
      // Eyes behind glasses
      { x: 4, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 5, y: 4, w: 1, h: 1, cls: 'e-dark' },
      { x: 9, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 10, y: 4, w: 1, h: 1, cls: 'e-dark' },
      // Heavy brows
      { x: 3, y: 3, w: 4, h: 1, cls: 'h-grey' },
      { x: 8, y: 3, w: 4, h: 1, cls: 'h-grey' },
      // Nose
      { x: 6, y: 5, w: 3, h: 1, cls: 's-worn' },
      // Mouth — grimace
      { x: 5, y: 7, w: 5, h: 1, style: 'background:#7a4a30' },
      // Neck
      { x: 6, y: 8, w: 3, h: 2, cls: 's-worn' },
      // Body — shirt with rolled sleeves
      { x: 2, y: 10, w: 11, h: 8, cls: 'c-shirt-white' },
      { x: 5, y: 10, w: 5, h: 1, style: 'background:#8a7a5a' }, // tie
      { x: 6, y: 11, w: 3, h: 5, style: 'background:#8a7a5a' }, // tie
      // Arms
      { x: 1, y: 11, w: 2, h: 7, cls: 'c-shirt-white' },
      { x: 12, y: 11, w: 2, h: 7, cls: 'c-shirt-white' },
      // Shadow
      { x: 2, y: 17, w: 11, h: 1, cls: 'x-shadow' },
    ],
  },

  // ── INGA JOHANSSON — Retired nurse, knits, avoids eye contact ──
  inga_johansson: {
    bg: 'background:linear-gradient(180deg,#1e1a14 0%,#181410 60%,#120e0a 100%)',
    pixels: [
      // Hair — silver bun
      { x: 4, y: 0, w: 7, h: 1, cls: 'h-silver' },
      { x: 3, y: 1, w: 9, h: 1, cls: 'h-silver' },
      { x: 6, y: 0, w: 3, h: 1, cls: 'h-silver', style: 'border-radius:50%' }, // bun
      { x: 2, y: 2, w: 1, h: 3, cls: 'h-grey' },
      { x: 12, y: 2, w: 1, h: 3, cls: 'h-grey' },
      // Head
      { x: 3, y: 2, w: 9, h: 6, cls: 's-worn' },
      // Wrinkles
      { x: 2, y: 5, w: 1, h: 2, style: 'background:rgba(80,50,30,0.3)' },
      { x: 12, y: 5, w: 1, h: 2, style: 'background:rgba(80,50,30,0.3)' },
      // Eyes — averted, looking down-left
      { x: 4, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 4, y: 4, w: 1, h: 1, cls: 'e-green' },
      { x: 9, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 9, y: 4, w: 1, h: 1, cls: 'e-green' },
      // Soft brows
      { x: 4, y: 3, w: 3, h: 1, cls: 'h-silver' },
      { x: 9, y: 3, w: 3, h: 1, cls: 'h-silver' },
      // Nose
      { x: 6, y: 5, w: 3, h: 1, cls: 's-worn' },
      // Mouth — pursed
      { x: 5, y: 7, w: 5, h: 1, style: 'background:#9a6a58' },
      // Neck
      { x: 6, y: 8, w: 3, h: 2, cls: 's-worn' },
      // Body — cardigan
      { x: 2, y: 10, w: 11, h: 8, cls: 'c-cardigan-wine' },
      { x: 5, y: 10, w: 5, h: 3, cls: 'x-collar' },
      // Arms — knitting
      { x: 1, y: 11, w: 2, h: 7, cls: 'c-cardigan-wine' },
      { x: 12, y: 11, w: 2, h: 7, cls: 'c-cardigan-wine' },
      // Knitting in hands
      { x: 0, y: 16, w: 3, h: 1, style: 'background:#8a2030' },
      { x: 13, y: 15, w: 2, h: 2, style: 'background:#8a2030' },
      // Shadow
      { x: 2, y: 17, w: 11, h: 1, cls: 'x-shadow' },
    ],
  },

  // ── LARS BJÖRK — Council chairman, big smile, politician ──
  lars_bjork: {
    bg: 'background:linear-gradient(180deg,#1a1c28 0%,#121420 60%,#0e1018 100%)',
    pixels: [
      // Hair — thinning, combed, grey temples
      { x: 4, y: 0, w: 7, h: 1, cls: 'h-grey' },
      { x: 3, y: 1, w: 9, h: 1, cls: 'h-brown' },
      { x: 2, y: 2, w: 1, h: 2, cls: 'h-grey' },
      { x: 12, y: 2, w: 1, h: 2, cls: 'h-grey' },
      // Head — pale, indoor
      { x: 3, y: 2, w: 9, h: 6, cls: 's-pale' },
      // Jowls
      { x: 2, y: 6, w: 1, h: 2, cls: 's-pale' },
      { x: 12, y: 6, w: 1, h: 2, cls: 's-pale' },
      // Eyes — friendly but calculating
      { x: 4, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 5, y: 4, w: 1, h: 1, cls: 'e-blue' },
      { x: 9, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 10, y: 4, w: 1, h: 1, cls: 'e-blue' },
      // Brows — flat, controlled
      { x: 4, y: 3, w: 3, h: 1, cls: 'h-grey' },
      { x: 9, y: 3, w: 3, h: 1, cls: 'h-grey' },
      // Nose
      { x: 6, y: 5, w: 3, h: 2, cls: 's-pale' },
      // Mouth — big smile
      { x: 4, y: 7, w: 7, h: 1, style: 'background:#9a6058;border-radius:0 0 4px 4px' },
      // Neck
      { x: 6, y: 8, w: 3, h: 2, cls: 's-pale' },
      // Body — navy suit
      { x: 2, y: 10, w: 11, h: 8, cls: 'c-suit-navy' },
      // Tie
      { x: 6, y: 10, w: 3, h: 5, cls: 'x-tie-red' },
      // Lapels
      { x: 5, y: 10, w: 2, h: 3, cls: 'x-collar' },
      { x: 8, y: 10, w: 2, h: 3, cls: 'x-collar' },
      // Arms
      { x: 1, y: 11, w: 2, h: 7, cls: 'c-suit-navy' },
      { x: 12, y: 11, w: 2, h: 7, cls: 'c-suit-navy' },
      // Shadow
      { x: 2, y: 17, w: 11, h: 1, cls: 'x-shadow' },
    ],
  },

  // ── SVEN-ERIK BERG — Union rep, IF Metall, leaning forward ──
  sven_erik_berg: {
    bg: 'background:linear-gradient(180deg,#1a1810 0%,#14120a 60%,#0e0c06 100%)',
    pixels: [
      // Hair — dark, short
      { x: 4, y: 0, w: 7, h: 1, cls: 'h-dark-brown' },
      { x: 3, y: 1, w: 9, h: 1, cls: 'h-dark-brown' },
      { x: 2, y: 2, w: 1, h: 2, cls: 'h-dark-brown' },
      { x: 12, y: 2, w: 1, h: 2, cls: 'h-dark-brown' },
      // Head
      { x: 3, y: 2, w: 9, h: 6, cls: 's-mid' },
      // Eyes — direct, intense
      { x: 4, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 5, y: 4, w: 1, h: 1, cls: 'e-dark' },
      { x: 9, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 10, y: 4, w: 1, h: 1, cls: 'e-dark' },
      // Heavy brows — purposeful
      { x: 4, y: 3, w: 3, h: 1, cls: 'h-dark-brown' },
      { x: 9, y: 3, w: 3, h: 1, cls: 'h-dark-brown' },
      // Mustache
      { x: 5, y: 6, w: 5, h: 1, cls: 'x-mustache' },
      // Nose
      { x: 6, y: 5, w: 3, h: 1, cls: 's-mid' },
      // Mouth
      { x: 5, y: 7, w: 5, h: 1, style: 'background:#7a4a38' },
      // Neck
      { x: 6, y: 8, w: 3, h: 2, cls: 's-mid' },
      // Body — worker grey
      { x: 2, y: 10, w: 11, h: 8, cls: 'c-worker-grey' },
      { x: 5, y: 10, w: 5, h: 2, cls: 'x-collar' },
      // Arms — leaning forward, elbows on table
      { x: 0, y: 11, w: 3, h: 6, cls: 'c-worker-grey', style: 'transform:rotate(8deg)' },
      { x: 12, y: 11, w: 3, h: 6, cls: 'c-worker-grey', style: 'transform:rotate(-8deg)' },
      // Shadow
      { x: 2, y: 17, w: 11, h: 1, cls: 'x-shadow' },
    ],
  },

  // ── MARGARETA LUND — Teacher, polite smile but tense ──
  margareta_lund: {
    bg: 'background:linear-gradient(180deg,#1e1a18 0%,#181412 60%,#12100e 100%)',
    pixels: [
      // Hair — brown, neat
      { x: 3, y: 0, w: 9, h: 1, cls: 'h-brown' },
      { x: 2, y: 1, w: 11, h: 1, cls: 'h-brown' },
      { x: 2, y: 2, w: 1, h: 4, cls: 'h-brown' },
      { x: 12, y: 2, w: 1, h: 4, cls: 'h-brown' },
      // Head
      { x: 3, y: 2, w: 9, h: 6, cls: 's-light' },
      // Eyes
      { x: 4, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 5, y: 4, w: 1, h: 1, cls: 'e-dark' },
      { x: 9, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 10, y: 4, w: 1, h: 1, cls: 'e-dark' },
      // Brows
      { x: 4, y: 3, w: 3, h: 1, cls: 'h-brown' },
      { x: 9, y: 3, w: 3, h: 1, cls: 'h-brown' },
      // Nose
      { x: 6, y: 5, w: 3, h: 1, cls: 's-light' },
      // Mouth — polite smile
      { x: 5, y: 7, w: 5, h: 1, style: 'background:#9a6a58;border-radius:0 0 2px 2px' },
      // Neck
      { x: 6, y: 8, w: 3, h: 2, cls: 's-light' },
      // Body — blouse
      { x: 2, y: 10, w: 11, h: 8, cls: 'c-blouse-grey' },
      { x: 5, y: 10, w: 5, h: 2, cls: 'x-collar' },
      // Brooch
      { x: 7, y: 12, w: 1, h: 1, cls: 'x-badge', style: 'border-radius:50%' },
      // Arms
      { x: 1, y: 11, w: 2, h: 7, cls: 'c-blouse-grey' },
      { x: 12, y: 11, w: 2, h: 7, cls: 'c-blouse-grey' },
      // Shadow
      { x: 2, y: 17, w: 11, h: 1, cls: 'x-shadow' },
    ],
  },

  // ── GÖSTA NILSSON — Retired police officer, pipe ──
  gosta_nilsson: {
    bg: 'background:linear-gradient(180deg,#14181e 0%,#0e1218 60%,#0a0e12 100%)',
    pixels: [
      // Hair — receding, grey
      { x: 5, y: 0, w: 5, h: 1, cls: 'h-grey' },
      { x: 3, y: 1, w: 9, h: 1, cls: 'h-grey' },
      { x: 2, y: 2, w: 1, h: 2, cls: 'h-grey' },
      { x: 12, y: 2, w: 1, h: 2, cls: 'h-grey' },
      // Head — square
      { x: 3, y: 2, w: 9, h: 6, cls: 's-mid' },
      // Eyes — calm, assessing
      { x: 4, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 5, y: 4, w: 1, h: 1, cls: 'e-dark' },
      { x: 9, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 10, y: 4, w: 1, h: 1, cls: 'e-dark' },
      // Brows
      { x: 4, y: 3, w: 3, h: 1, cls: 'h-grey' },
      { x: 9, y: 3, w: 3, h: 1, cls: 'h-grey' },
      // Mustache — thick grey
      { x: 5, y: 6, w: 5, h: 1, style: 'background:#7a7068' },
      // Nose
      { x: 6, y: 5, w: 3, h: 1, cls: 's-mid' },
      // Mouth with pipe
      { x: 5, y: 7, w: 3, h: 1, style: 'background:#7a4a38' },
      { x: 11, y: 6, w: 3, h: 1, style: 'background:#5a3a18' }, // pipe
      { x: 13, y: 5, w: 1, h: 1, style: 'background:#5a3a18' }, // pipe bowl
      // Neck
      { x: 6, y: 8, w: 3, h: 2, cls: 's-mid' },
      // Body — checked shirt
      { x: 2, y: 10, w: 11, h: 8, cls: 'c-shirt-check' },
      { x: 5, y: 10, w: 5, h: 2, cls: 'x-collar' },
      // Arms
      { x: 1, y: 11, w: 2, h: 7, cls: 'c-shirt-check' },
      { x: 12, y: 11, w: 2, h: 7, cls: 'c-shirt-check' },
      // Shadow
      { x: 2, y: 17, w: 11, h: 1, cls: 'x-shadow' },
    ],
  },

  // ── HELENA STRAND — Hospital aide, nervous, whispering ──
  helena_strand: {
    bg: 'background:linear-gradient(180deg,#181c1e 0%,#121618 60%,#0e1012 100%)',
    pixels: [
      // Hair — dark, pulled back
      { x: 3, y: 0, w: 9, h: 1, cls: 'h-dark-brown' },
      { x: 3, y: 1, w: 9, h: 1, cls: 'h-dark-brown' },
      // Head
      { x: 3, y: 2, w: 9, h: 6, cls: 's-light' },
      // Eyes — looking around
      { x: 4, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 4, y: 4, w: 1, h: 1, cls: 'e-dark' }, // looking left
      { x: 9, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 9, y: 4, w: 1, h: 1, cls: 'e-dark' },
      // Raised brows — nervous
      { x: 4, y: 3, w: 3, h: 1, cls: 'h-dark-brown', style: 'transform:rotate(4deg)' },
      { x: 9, y: 3, w: 3, h: 1, cls: 'h-dark-brown', style: 'transform:rotate(-4deg)' },
      // Nose
      { x: 6, y: 5, w: 3, h: 1, cls: 's-light' },
      // Mouth — small, tense
      { x: 6, y: 7, w: 3, h: 1, style: 'background:#9a6a58' },
      // Neck
      { x: 6, y: 8, w: 3, h: 2, cls: 's-light' },
      // Body — white nurse uniform
      { x: 2, y: 10, w: 11, h: 8, style: 'background:#c8c0b0' },
      { x: 5, y: 10, w: 5, h: 1, style: 'background:#d8d0c0' },
      // Arms
      { x: 1, y: 11, w: 2, h: 7, style: 'background:#c8c0b0' },
      { x: 12, y: 11, w: 2, h: 7, style: 'background:#c8c0b0' },
      // Shadow
      { x: 2, y: 17, w: 11, h: 1, cls: 'x-shadow' },
    ],
  },

  // ── ANDERS VIK — Family man, determined with sorrow ──
  anders_vik: {
    bg: 'background:linear-gradient(180deg,#1a1810 0%,#141208 60%,#1a1208 100%)',
    pixels: [
      // Hair — brown, neat
      { x: 4, y: 0, w: 7, h: 1, cls: 'h-brown' },
      { x: 3, y: 1, w: 9, h: 1, cls: 'h-brown' },
      // Head
      { x: 3, y: 2, w: 9, h: 6, cls: 's-mid' },
      // Eyes — determined but sad
      { x: 4, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 5, y: 4, w: 1, h: 1, cls: 'e-dark' },
      { x: 9, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 10, y: 4, w: 1, h: 1, cls: 'e-dark' },
      // Brows — inner up (sad)
      { x: 4, y: 3, w: 3, h: 1, cls: 'h-brown', style: 'transform:rotate(5deg)' },
      { x: 9, y: 3, w: 3, h: 1, cls: 'h-brown', style: 'transform:rotate(-5deg)' },
      // Nose
      { x: 6, y: 5, w: 3, h: 1, cls: 's-mid' },
      // Mouth — set
      { x: 5, y: 7, w: 5, h: 1, style: 'background:#7a4a38' },
      // Neck
      { x: 6, y: 8, w: 3, h: 2, cls: 's-mid' },
      // Body — sweater
      { x: 2, y: 10, w: 11, h: 8, style: 'background:#3a3828' },
      { x: 5, y: 10, w: 5, h: 2, cls: 'x-collar' },
      // Arms
      { x: 1, y: 11, w: 2, h: 7, style: 'background:#3a3828' },
      { x: 12, y: 11, w: 2, h: 7, style: 'background:#3a3828' },
      // Shadow
      { x: 2, y: 17, w: 11, h: 1, cls: 'x-shadow' },
    ],
  },

  // ── KERSTIN ALVÉN — Former journalist, calm, analytical ──
  kerstin_alven: {
    bg: 'background:linear-gradient(180deg,#18161a 0%,#12101a 60%,#0e0c12 100%)',
    pixels: [
      // Hair — short grey, professional
      { x: 3, y: 0, w: 9, h: 1, cls: 'h-grey' },
      { x: 3, y: 1, w: 9, h: 1, cls: 'h-grey' },
      { x: 2, y: 2, w: 1, h: 3, cls: 'h-grey' },
      { x: 12, y: 2, w: 1, h: 3, cls: 'h-grey' },
      // Head
      { x: 3, y: 2, w: 9, h: 6, cls: 's-pale' },
      // Glasses
      { x: 3, y: 3, w: 4, h: 2, style: 'background:transparent;border:1px solid #2a1a08' },
      { x: 8, y: 3, w: 4, h: 2, style: 'background:transparent;border:1px solid #2a1a08' },
      // Eyes
      { x: 4, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 5, y: 4, w: 1, h: 1, cls: 'e-green' },
      { x: 9, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 10, y: 4, w: 1, h: 1, cls: 'e-green' },
      // Brows — level
      { x: 4, y: 3, w: 3, h: 1, cls: 'h-grey' },
      { x: 9, y: 3, w: 3, h: 1, cls: 'h-grey' },
      // Nose
      { x: 6, y: 5, w: 3, h: 1, cls: 's-pale' },
      // Mouth — neutral, knowing
      { x: 5, y: 7, w: 5, h: 1, style: 'background:#8a5a50' },
      // Neck
      { x: 6, y: 8, w: 3, h: 2, cls: 's-pale' },
      // Body — blazer
      { x: 2, y: 10, w: 11, h: 8, cls: 'c-suit-dark' },
      { x: 5, y: 10, w: 5, h: 2, cls: 'x-collar' },
      // Arms
      { x: 1, y: 11, w: 2, h: 7, cls: 'c-suit-dark' },
      { x: 12, y: 11, w: 2, h: 7, cls: 'c-suit-dark' },
      // Notepad in hand
      { x: 13, y: 15, w: 2, h: 3, style: 'background:#d4c9a8' },
      // Shadow
      { x: 2, y: 17, w: 11, h: 1, cls: 'x-shadow' },
    ],
  },

  // ── ARVID MAGNUSSON — Driver, anxious ──
  arvid_magnusson: {
    bg: 'background:linear-gradient(180deg,#1a1a10 0%,#14140a 60%,#0e0e06 100%)',
    pixels: [
      // Cap — driver's cap
      { x: 3, y: 0, w: 9, h: 2, style: 'background:#2a2a28' },
      { x: 2, y: 1, w: 11, h: 1, style: 'background:#2a2a28' },
      // Head
      { x: 3, y: 2, w: 9, h: 6, cls: 's-mid' },
      // Eyes — looking around
      { x: 4, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 4, y: 4, w: 1, h: 1, cls: 'e-dark' },
      { x: 9, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 10, y: 4, w: 1, h: 1, cls: 'e-dark' },
      // Brows — raised
      { x: 4, y: 3, w: 3, h: 1, cls: 'h-dark-brown', style: 'transform:rotate(3deg)' },
      { x: 9, y: 3, w: 3, h: 1, cls: 'h-dark-brown', style: 'transform:rotate(-3deg)' },
      // Sweat
      { x: 2, y: 4, w: 1, h: 1, cls: 'x-sweat' },
      // Nose
      { x: 6, y: 5, w: 3, h: 1, cls: 's-mid' },
      // Mouth
      { x: 5, y: 7, w: 5, h: 1, style: 'background:#7a4a38' },
      // Neck
      { x: 6, y: 8, w: 3, h: 2, cls: 's-mid' },
      // Body — jacket
      { x: 2, y: 10, w: 11, h: 8, cls: 'c-worker-grey' },
      { x: 5, y: 10, w: 5, h: 2, cls: 'x-collar' },
      // Arms
      { x: 1, y: 11, w: 2, h: 7, cls: 'c-worker-grey' },
      { x: 12, y: 11, w: 2, h: 7, cls: 'c-worker-grey' },
      // Shadow
      { x: 2, y: 17, w: 11, h: 1, cls: 'x-shadow' },
    ],
  },

  // ── ARNE WIKSTRÖM — Shopkeeper, businesslike ──
  arne_wikstrom: {
    bg: 'background:linear-gradient(180deg,#1a1810 0%,#161408 60%,#100e06 100%)',
    pixels: [
      // Hair — neat, dark, balding top
      { x: 5, y: 0, w: 5, h: 1, cls: 'h-dark-brown' },
      { x: 3, y: 1, w: 9, h: 1, cls: 'h-dark-brown' },
      { x: 2, y: 2, w: 1, h: 2, cls: 'h-dark-brown' },
      { x: 12, y: 2, w: 1, h: 2, cls: 'h-dark-brown' },
      // Head
      { x: 3, y: 2, w: 9, h: 6, cls: 's-light' },
      // Eyes — direct, sharp
      { x: 4, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 5, y: 4, w: 1, h: 1, cls: 'e-dark' },
      { x: 9, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 10, y: 4, w: 1, h: 1, cls: 'e-dark' },
      // Brows — level
      { x: 4, y: 3, w: 3, h: 1, cls: 'h-dark-brown' },
      { x: 9, y: 3, w: 3, h: 1, cls: 'h-dark-brown' },
      // Nose
      { x: 6, y: 5, w: 3, h: 1, cls: 's-light' },
      // Mouth — thin
      { x: 5, y: 7, w: 5, h: 1, style: 'background:#8a5a4a' },
      // Neck
      { x: 6, y: 8, w: 3, h: 2, cls: 's-light' },
      // Body — apron over shirt
      { x: 2, y: 10, w: 11, h: 8, cls: 'c-shirt-white' },
      { x: 3, y: 12, w: 9, h: 6, style: 'background:#4a4a3a' }, // apron
      // Arms
      { x: 1, y: 11, w: 2, h: 7, cls: 'c-shirt-white' },
      { x: 12, y: 11, w: 2, h: 7, cls: 'c-shirt-white' },
      // Shadow
      { x: 2, y: 17, w: 11, h: 1, cls: 'x-shadow' },
    ],
  },

  // ── RUNE SJÖBERG — Construction worker, straight to the point ──
  rune_sjoberg: {
    bg: 'background:linear-gradient(180deg,#1a1a10 0%,#14140a 60%,#1a1208 100%)',
    pixels: [
      // Hard hat
      { x: 2, y: 0, w: 11, h: 2, style: 'background:#c8a820' },
      // Head — square, strong
      { x: 3, y: 2, w: 9, h: 6, cls: 's-mid' },
      // Eyes — straight
      { x: 4, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 5, y: 4, w: 1, h: 1, cls: 'e-dark' },
      { x: 9, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 10, y: 4, w: 1, h: 1, cls: 'e-dark' },
      // Heavy brows
      { x: 4, y: 3, w: 3, h: 1, cls: 'h-dark-brown' },
      { x: 9, y: 3, w: 3, h: 1, cls: 'h-dark-brown' },
      // Nose
      { x: 6, y: 5, w: 3, h: 1, cls: 's-mid' },
      // Mouth
      { x: 5, y: 7, w: 5, h: 1, style: 'background:#7a4a38' },
      // Stubble
      { x: 3, y: 7, w: 9, h: 1, style: 'background:rgba(40,26,10,0.3)' },
      // Neck
      { x: 6, y: 8, w: 3, h: 2, cls: 's-mid' },
      // Body — high-vis vest
      { x: 2, y: 10, w: 11, h: 8, style: 'background:#b89830' },
      { x: 2, y: 13, w: 11, h: 1, style: 'background:#e8d860' }, // reflective strip
      // Arms
      { x: 1, y: 11, w: 2, h: 7, style: 'background:#b89830' },
      { x: 12, y: 11, w: 2, h: 7, style: 'background:#b89830' },
      // Shadow
      { x: 2, y: 17, w: 11, h: 1, cls: 'x-shadow' },
    ],
  },

  // ── BENGT-ÅKE FRID — Archivist, pedantic, tentative ──
  bengt_ake_frid: {
    bg: 'background:linear-gradient(180deg,#161418 0%,#101012 60%,#0a0a0e 100%)',
    pixels: [
      // Hair — thin, combed
      { x: 4, y: 0, w: 7, h: 1, cls: 'h-brown' },
      { x: 3, y: 1, w: 9, h: 1, cls: 'h-brown' },
      // Head — narrow
      { x: 3, y: 2, w: 9, h: 6, cls: 's-pale' },
      // Glasses — round
      { x: 3, y: 3, w: 4, h: 3, style: 'background:transparent;border:1px solid #2a1a08;border-radius:50%' },
      { x: 8, y: 3, w: 4, h: 3, style: 'background:transparent;border:1px solid #2a1a08;border-radius:50%' },
      // Eyes — focused
      { x: 4, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 5, y: 4, w: 1, h: 1, cls: 'e-dark' },
      { x: 9, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 10, y: 4, w: 1, h: 1, cls: 'e-dark' },
      // Thin brows
      { x: 4, y: 3, w: 3, h: 1, cls: 'h-brown', style: 'height:4px' },
      { x: 9, y: 3, w: 3, h: 1, cls: 'h-brown', style: 'height:4px' },
      // Nose — pointed
      { x: 7, y: 5, w: 1, h: 2, cls: 's-pale' },
      // Mouth — small, pursed
      { x: 6, y: 7, w: 3, h: 1, style: 'background:#8a5a50' },
      // Neck
      { x: 6, y: 8, w: 3, h: 2, cls: 's-pale' },
      // Body — vest over shirt
      { x: 2, y: 10, w: 11, h: 8, style: 'background:#3a3830' },
      { x: 5, y: 10, w: 5, h: 2, cls: 'c-shirt-white' },
      // Arms
      { x: 1, y: 11, w: 2, h: 7, style: 'background:#3a3830' },
      { x: 12, y: 11, w: 2, h: 7, style: 'background:#3a3830' },
      // Papers in hand
      { x: 13, y: 14, w: 2, h: 4, style: 'background:#d4c9a8;transform:rotate(-3deg)' },
      // Shadow
      { x: 2, y: 17, w: 11, h: 1, cls: 'x-shadow' },
    ],
  },

  // ── TOMMY BERG — Carpenter, tight-lipped ──
  tommy_berg: {
    bg: 'background:linear-gradient(180deg,#1a1a10 0%,#161408 60%,#100e06 100%)',
    pixels: [
      // Hair — short, dark
      { x: 4, y: 0, w: 7, h: 1, cls: 'h-dark-brown' },
      { x: 3, y: 1, w: 9, h: 1, cls: 'h-dark-brown' },
      // Head — blocky
      { x: 3, y: 2, w: 9, h: 6, cls: 's-mid' },
      // Eyes
      { x: 4, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 5, y: 4, w: 1, h: 1, cls: 'e-dark' },
      { x: 9, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 10, y: 4, w: 1, h: 1, cls: 'e-dark' },
      // Flat brows
      { x: 4, y: 3, w: 3, h: 1, cls: 'h-dark-brown' },
      { x: 9, y: 3, w: 3, h: 1, cls: 'h-dark-brown' },
      // Nose
      { x: 6, y: 5, w: 3, h: 1, cls: 's-mid' },
      // Mouth — tight line
      { x: 5, y: 7, w: 5, h: 1, style: 'background:#6a3a28;height:4px' },
      // Neck
      { x: 6, y: 8, w: 3, h: 2, cls: 's-mid' },
      // Body — flannel
      { x: 2, y: 10, w: 11, h: 8, cls: 'c-shirt-check' },
      { x: 5, y: 10, w: 5, h: 2, cls: 'x-collar' },
      // Arms — thick
      { x: 0, y: 11, w: 3, h: 7, cls: 'c-shirt-check' },
      { x: 12, y: 11, w: 3, h: 7, cls: 'c-shirt-check' },
      // Shadow
      { x: 2, y: 17, w: 11, h: 1, cls: 'x-shadow' },
    ],
  },

  // ── BERIT HOLM — Nurse, warm but stressed ──
  berit_holm: {
    bg: 'background:linear-gradient(180deg,#181c1e 0%,#121618 60%,#0e1012 100%)',
    pixels: [
      // Hair — brown, pinned up
      { x: 3, y: 0, w: 9, h: 1, cls: 'h-brown' },
      { x: 3, y: 1, w: 9, h: 1, cls: 'h-brown' },
      // Head
      { x: 3, y: 2, w: 9, h: 6, cls: 's-light' },
      // Eyes — warm
      { x: 4, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 5, y: 4, w: 1, h: 1, cls: 'e-dark' },
      { x: 9, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 10, y: 4, w: 1, h: 1, cls: 'e-dark' },
      // Soft brows
      { x: 4, y: 3, w: 3, h: 1, cls: 'h-brown', style: 'transform:rotate(3deg)' },
      { x: 9, y: 3, w: 3, h: 1, cls: 'h-brown', style: 'transform:rotate(-3deg)' },
      // Nose
      { x: 6, y: 5, w: 3, h: 1, cls: 's-light' },
      // Mouth — warm smile
      { x: 5, y: 7, w: 5, h: 1, style: 'background:#9a6a58;border-radius:0 0 2px 2px' },
      // Neck
      { x: 6, y: 8, w: 3, h: 2, cls: 's-light' },
      // Body — nurse uniform white
      { x: 2, y: 10, w: 11, h: 8, style: 'background:#d0c8b8' },
      { x: 5, y: 10, w: 5, h: 1, style: 'background:#d8d0c0' },
      // Nurse cap hint
      { x: 5, y: 0, w: 5, h: 1, style: 'background:#d8d0c0' },
      // Arms
      { x: 1, y: 11, w: 2, h: 7, style: 'background:#d0c8b8' },
      { x: 12, y: 11, w: 2, h: 7, style: 'background:#d0c8b8' },
      // Shadow
      { x: 2, y: 17, w: 11, h: 1, cls: 'x-shadow' },
    ],
  },

  // ── BO LUNDGREN — Dock worker, suspicious ──
  bo_lundgren: {
    bg: 'background:linear-gradient(180deg,#141a1e 0%,#0e1418 60%,#0a0e12 100%)',
    pixels: [
      // Hair — dark, buzz cut
      { x: 4, y: 0, w: 7, h: 1, cls: 'h-black' },
      { x: 3, y: 1, w: 9, h: 1, cls: 'h-black' },
      // Head — wide, thick neck
      { x: 2, y: 2, w: 11, h: 6, cls: 's-mid' },
      // Eyes — narrow, suspicious
      { x: 4, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 5, y: 4, w: 1, h: 1, cls: 'e-dark' },
      { x: 9, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 10, y: 4, w: 1, h: 1, cls: 'e-dark' },
      // Low heavy brows
      { x: 3, y: 3, w: 4, h: 1, cls: 'h-black' },
      { x: 8, y: 3, w: 4, h: 1, cls: 'h-black' },
      // Nose
      { x: 6, y: 5, w: 3, h: 2, cls: 's-mid' },
      // Mouth — down
      { x: 5, y: 7, w: 5, h: 1, style: 'background:#6a3a28' },
      // Thick neck
      { x: 5, y: 8, w: 5, h: 2, cls: 's-mid' },
      // Body — tank top / dock clothes
      { x: 1, y: 10, w: 13, h: 8, cls: 'c-worker-grey' },
      // Arms — thick
      { x: 0, y: 11, w: 2, h: 7, cls: 'c-worker-grey' },
      { x: 13, y: 11, w: 2, h: 7, cls: 'c-worker-grey' },
      // Shadow
      { x: 1, y: 17, w: 13, h: 1, cls: 'x-shadow' },
    ],
  },

  // ── MAJ-BRITT OLSSON — Housekeeper, quiet, wringing hands ──
  maj_britt_olsson: {
    bg: 'background:linear-gradient(180deg,#1e1a14 0%,#181410 60%,#120e0a 100%)',
    pixels: [
      // Hair — grey, pulled tight
      { x: 3, y: 0, w: 9, h: 1, cls: 'h-grey' },
      { x: 3, y: 1, w: 9, h: 1, cls: 'h-grey' },
      { x: 2, y: 2, w: 1, h: 3, cls: 'h-grey' },
      { x: 12, y: 2, w: 1, h: 3, cls: 'h-grey' },
      // Head
      { x: 3, y: 2, w: 9, h: 6, cls: 's-worn' },
      // Eyes — down, avoiding
      { x: 4, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 5, y: 5, w: 1, h: 1, cls: 'e-dark' }, // looking down
      { x: 9, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 10, y: 5, w: 1, h: 1, cls: 'e-dark' },
      // Brows
      { x: 4, y: 3, w: 3, h: 1, cls: 'h-grey' },
      { x: 9, y: 3, w: 3, h: 1, cls: 'h-grey' },
      // Wrinkles
      { x: 2, y: 5, w: 1, h: 2, style: 'background:rgba(80,50,30,0.3)' },
      { x: 12, y: 5, w: 1, h: 2, style: 'background:rgba(80,50,30,0.3)' },
      // Nose
      { x: 6, y: 5, w: 3, h: 1, cls: 's-worn' },
      // Mouth — tight
      { x: 6, y: 7, w: 3, h: 1, style: 'background:#8a5a50' },
      // Neck
      { x: 6, y: 8, w: 3, h: 2, cls: 's-worn' },
      // Body — plain dress
      { x: 2, y: 10, w: 11, h: 8, style: 'background:#4a4040' },
      { x: 5, y: 10, w: 5, h: 2, cls: 'x-collar' },
      // Arms — hands wringing
      { x: 1, y: 11, w: 2, h: 6, style: 'background:#4a4040' },
      { x: 12, y: 11, w: 2, h: 6, style: 'background:#4a4040' },
      { x: 5, y: 16, w: 5, h: 2, cls: 's-worn' }, // hands wringing in front
      // Shadow
      { x: 2, y: 17, w: 11, h: 1, cls: 'x-shadow' },
    ],
  },

  // ── RUNE KARLSSON — Mechanic, relaxed but sharp ──
  rune_karlsson: {
    bg: 'background:linear-gradient(180deg,#1a1810 0%,#14120a 60%,#0e0c06 100%)',
    pixels: [
      // Hair — dark brown
      { x: 4, y: 0, w: 7, h: 1, cls: 'h-dark-brown' },
      { x: 3, y: 1, w: 9, h: 1, cls: 'h-dark-brown' },
      // Head
      { x: 3, y: 2, w: 9, h: 6, cls: 's-mid' },
      // Eyes — sharp, relaxed
      { x: 4, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 5, y: 4, w: 1, h: 1, cls: 'e-dark' },
      { x: 9, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 10, y: 4, w: 1, h: 1, cls: 'e-dark' },
      // Brows — one slightly raised
      { x: 4, y: 3, w: 3, h: 1, cls: 'h-dark-brown' },
      { x: 9, y: 3, w: 3, h: 1, cls: 'h-dark-brown', style: 'transform:rotate(-3deg)' },
      // Nose
      { x: 6, y: 5, w: 3, h: 1, cls: 's-mid' },
      // Mouth — slight smirk
      { x: 5, y: 7, w: 5, h: 1, style: 'background:#8a5a50' },
      // Stubble
      { x: 3, y: 7, w: 9, h: 1, style: 'background:rgba(40,26,10,0.2)' },
      // Neck
      { x: 6, y: 8, w: 3, h: 2, cls: 's-mid' },
      // Body — overalls
      { x: 2, y: 10, w: 11, h: 8, cls: 'c-worker-blue' },
      { x: 5, y: 10, w: 5, h: 2, style: 'background:#5a5a4a' }, // overall bib
      // Grease stain detail
      { x: 10, y: 13, w: 2, h: 1, style: 'background:rgba(40,30,10,0.4)' },
      // Arms
      { x: 1, y: 11, w: 2, h: 7, cls: 'c-worker-blue' },
      { x: 12, y: 11, w: 2, h: 7, cls: 'c-worker-blue' },
      // Wrench in hand
      { x: 13, y: 15, w: 2, h: 3, style: 'background:#8a8a80' },
      // Shadow
      { x: 2, y: 17, w: 11, h: 1, cls: 'x-shadow' },
    ],
  },

  // ── ASTRID NYBERG — Retiree, friendly, offers coffee ──
  astrid_nyberg: {
    bg: 'background:linear-gradient(180deg,#1e1a14 0%,#181410 60%,#120e0a 100%)',
    pixels: [
      // Hair — white, curly
      { x: 3, y: 0, w: 9, h: 2, cls: 'h-silver' },
      { x: 2, y: 1, w: 11, h: 1, cls: 'h-silver' },
      { x: 2, y: 2, w: 1, h: 3, cls: 'h-silver' },
      { x: 12, y: 2, w: 1, h: 3, cls: 'h-silver' },
      // Head
      { x: 3, y: 2, w: 9, h: 6, cls: 's-worn' },
      // Eyes — warm, crinkled
      { x: 4, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 5, y: 4, w: 1, h: 1, cls: 'e-blue' },
      { x: 9, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 10, y: 4, w: 1, h: 1, cls: 'e-blue' },
      // Crinkles around eyes
      { x: 3, y: 4, w: 1, h: 1, style: 'background:rgba(80,50,30,0.3)' },
      { x: 11, y: 4, w: 1, h: 1, style: 'background:rgba(80,50,30,0.3)' },
      // Brows
      { x: 4, y: 3, w: 3, h: 1, cls: 'h-silver' },
      { x: 9, y: 3, w: 3, h: 1, cls: 'h-silver' },
      // Nose
      { x: 6, y: 5, w: 3, h: 1, cls: 's-worn' },
      // Mouth — warm smile
      { x: 4, y: 7, w: 7, h: 1, style: 'background:#9a6a58;border-radius:0 0 3px 3px' },
      // Neck
      { x: 6, y: 8, w: 3, h: 2, cls: 's-worn' },
      // Body — floral blouse (simulated with cardigan)
      { x: 2, y: 10, w: 11, h: 8, cls: 'c-cardigan-wine' },
      { x: 5, y: 10, w: 5, h: 2, cls: 'x-collar' },
      // Arms
      { x: 1, y: 11, w: 2, h: 7, cls: 'c-cardigan-wine' },
      { x: 12, y: 11, w: 2, h: 7, cls: 'c-cardigan-wine' },
      // Coffee cup in hand
      { x: 13, y: 14, w: 2, h: 3, style: 'background:#d4c9a8' },
      { x: 13, y: 13, w: 1, h: 1, style: 'background:rgba(180,160,120,0.5)' }, // steam
      // Shadow
      { x: 2, y: 17, w: 11, h: 1, cls: 'x-shadow' },
    ],
  },

  // ── PER-ERIK JOHANSSON — Farmer, pipe, quiet ──
  per_erik_johansson: {
    bg: 'background:linear-gradient(180deg,#1a2010 0%,#161a08 60%,#1a1208 100%)',
    pixels: [
      // Cap
      { x: 3, y: 0, w: 9, h: 2, style: 'background:#3a4030' },
      { x: 2, y: 1, w: 11, h: 1, style: 'background:#3a4030' },
      // Head — weathered
      { x: 3, y: 2, w: 9, h: 6, cls: 's-worn' },
      // Eyes — steady
      { x: 4, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 5, y: 4, w: 1, h: 1, cls: 'e-dark' },
      { x: 9, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 10, y: 4, w: 1, h: 1, cls: 'e-dark' },
      // Brows
      { x: 4, y: 3, w: 3, h: 1, cls: 'h-grey' },
      { x: 9, y: 3, w: 3, h: 1, cls: 'h-grey' },
      // Nose
      { x: 6, y: 5, w: 3, h: 2, cls: 's-worn' },
      // Pipe in mouth
      { x: 5, y: 7, w: 3, h: 1, style: 'background:#7a4a38' },
      { x: 11, y: 6, w: 2, h: 1, style: 'background:#5a3a18' },
      { x: 12, y: 5, w: 1, h: 1, style: 'background:#5a3a18' },
      // Neck
      { x: 6, y: 8, w: 3, h: 2, cls: 's-worn' },
      // Body — work shirt
      { x: 2, y: 10, w: 11, h: 8, cls: 'c-shirt-check' },
      { x: 5, y: 10, w: 5, h: 2, cls: 'x-collar' },
      // Arms
      { x: 1, y: 11, w: 2, h: 7, cls: 'c-shirt-check' },
      { x: 12, y: 11, w: 2, h: 7, cls: 'c-shirt-check' },
      // Shadow
      { x: 2, y: 17, w: 11, h: 1, cls: 'x-shadow' },
    ],
  },

  // ── TOMAS FALK — Municipal secretary, checking watch ──
  tomas_falk: {
    bg: 'background:linear-gradient(180deg,#1a1c28 0%,#121420 60%,#0e1018 100%)',
    pixels: [
      // Hair — neat, dark
      { x: 4, y: 0, w: 7, h: 1, cls: 'h-dark-brown' },
      { x: 3, y: 1, w: 9, h: 1, cls: 'h-dark-brown' },
      // Head
      { x: 3, y: 2, w: 9, h: 6, cls: 's-pale' },
      // Eyes — looking at watch direction
      { x: 4, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 4, y: 4, w: 1, h: 1, cls: 'e-dark' },
      { x: 9, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 9, y: 4, w: 1, h: 1, cls: 'e-dark' },
      // Brows — impatient
      { x: 4, y: 3, w: 3, h: 1, cls: 'h-dark-brown' },
      { x: 9, y: 3, w: 3, h: 1, cls: 'h-dark-brown' },
      // Nose
      { x: 6, y: 5, w: 3, h: 1, cls: 's-pale' },
      // Mouth — thin
      { x: 5, y: 7, w: 5, h: 1, style: 'background:#8a5a50' },
      // Neck
      { x: 6, y: 8, w: 3, h: 2, cls: 's-pale' },
      // Body — suit
      { x: 2, y: 10, w: 11, h: 8, cls: 'c-suit-dark' },
      { x: 6, y: 10, w: 3, h: 5, cls: 'x-tie-grey' },
      { x: 5, y: 10, w: 2, h: 2, cls: 'x-collar' },
      { x: 8, y: 10, w: 2, h: 2, cls: 'x-collar' },
      // Arms — one raised checking watch
      { x: 1, y: 11, w: 2, h: 7, cls: 'c-suit-dark' },
      { x: 12, y: 11, w: 2, h: 5, cls: 'c-suit-dark' },
      // Watch on raised wrist
      { x: 12, y: 11, w: 2, h: 1, cls: 'x-badge' },
      // Shadow
      { x: 2, y: 17, w: 11, h: 1, cls: 'x-shadow' },
    ],
  },

  // ── MARGARETA HOLM — Caretaker, practical ──
  margareta_holm: {
    bg: 'background:linear-gradient(180deg,#1a1a14 0%,#141410 60%,#1a1208 100%)',
    pixels: [
      // Hair — brown, tied back
      { x: 3, y: 0, w: 9, h: 1, cls: 'h-brown' },
      { x: 3, y: 1, w: 9, h: 1, cls: 'h-brown' },
      // Head
      { x: 3, y: 2, w: 9, h: 6, cls: 's-mid' },
      // Eyes — direct
      { x: 4, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 5, y: 4, w: 1, h: 1, cls: 'e-dark' },
      { x: 9, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 10, y: 4, w: 1, h: 1, cls: 'e-dark' },
      // Brows
      { x: 4, y: 3, w: 3, h: 1, cls: 'h-brown' },
      { x: 9, y: 3, w: 3, h: 1, cls: 'h-brown' },
      // Nose
      { x: 6, y: 5, w: 3, h: 1, cls: 's-mid' },
      // Mouth — set, practical
      { x: 5, y: 7, w: 5, h: 1, style: 'background:#8a5a4a' },
      // Neck
      { x: 6, y: 8, w: 3, h: 2, cls: 's-mid' },
      // Body — work smock
      { x: 2, y: 10, w: 11, h: 8, style: 'background:#4a5a4a' },
      { x: 5, y: 10, w: 5, h: 2, cls: 'x-collar' },
      // Arms
      { x: 1, y: 11, w: 2, h: 7, style: 'background:#4a5a4a' },
      { x: 12, y: 11, w: 2, h: 7, style: 'background:#4a5a4a' },
      // Keys on belt
      { x: 10, y: 14, w: 2, h: 2, cls: 'x-badge' },
      // Shadow
      { x: 2, y: 17, w: 11, h: 1, cls: 'x-shadow' },
    ],
  },

  // ── MAJ-BRITT HANSSON — Cashier, anxious, whispering ──
  maj_britt_hansson: {
    bg: 'background:linear-gradient(180deg,#1a1810 0%,#14120a 60%,#0e0c06 100%)',
    pixels: [
      // Hair — blonde, short
      { x: 3, y: 0, w: 9, h: 1, cls: 'h-blonde' },
      { x: 3, y: 1, w: 9, h: 1, cls: 'h-blonde' },
      { x: 2, y: 2, w: 1, h: 2, cls: 'h-blonde' },
      { x: 12, y: 2, w: 1, h: 2, cls: 'h-blonde' },
      // Head
      { x: 3, y: 2, w: 9, h: 6, cls: 's-light' },
      // Eyes — wide, nervous
      { x: 4, y: 3, w: 2, h: 2, cls: 'e-white' },
      { x: 5, y: 4, w: 1, h: 1, cls: 'e-blue' },
      { x: 9, y: 3, w: 2, h: 2, cls: 'e-white' },
      { x: 10, y: 4, w: 1, h: 1, cls: 'e-blue' },
      // Raised brows
      { x: 4, y: 2, w: 3, h: 1, cls: 'h-blonde', style: 'transform:rotate(5deg)' },
      { x: 9, y: 2, w: 3, h: 1, cls: 'h-blonde', style: 'transform:rotate(-5deg)' },
      // Nose
      { x: 6, y: 5, w: 3, h: 1, cls: 's-light' },
      // Mouth — small, pressed
      { x: 6, y: 7, w: 3, h: 1, style: 'background:#9a6a58' },
      // Neck
      { x: 6, y: 8, w: 3, h: 2, cls: 's-light' },
      // Body — store uniform blouse
      { x: 2, y: 10, w: 11, h: 8, style: 'background:#5a5858' },
      { x: 5, y: 10, w: 5, h: 2, cls: 'x-collar' },
      // Name tag
      { x: 9, y: 12, w: 2, h: 1, cls: 'x-badge' },
      // Arms
      { x: 1, y: 11, w: 2, h: 7, style: 'background:#5a5858' },
      { x: 12, y: 11, w: 2, h: 7, style: 'background:#5a5858' },
      // Shadow
      { x: 2, y: 17, w: 11, h: 1, cls: 'x-shadow' },
    ],
  },

  // ── BIRGITTA LUND — Librarian, helpful, systematic ──
  birgitta_lund: {
    bg: 'background:linear-gradient(180deg,#161418 0%,#101012 60%,#0a0a0e 100%)',
    pixels: [
      // Hair — brown, neat bun
      { x: 3, y: 0, w: 9, h: 1, cls: 'h-brown' },
      { x: 3, y: 1, w: 9, h: 1, cls: 'h-brown' },
      { x: 6, y: 0, w: 3, h: 1, cls: 'h-brown', style: 'border-radius:50%' }, // bun
      // Head
      { x: 3, y: 2, w: 9, h: 6, cls: 's-pale' },
      // Glasses
      { x: 3, y: 3, w: 4, h: 2, style: 'background:transparent;border:1px solid #2a1a08' },
      { x: 8, y: 3, w: 4, h: 2, style: 'background:transparent;border:1px solid #2a1a08' },
      // Eyes
      { x: 4, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 5, y: 4, w: 1, h: 1, cls: 'e-dark' },
      { x: 9, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 10, y: 4, w: 1, h: 1, cls: 'e-dark' },
      // Brows
      { x: 4, y: 3, w: 3, h: 1, cls: 'h-brown' },
      { x: 9, y: 3, w: 3, h: 1, cls: 'h-brown' },
      // Nose
      { x: 6, y: 5, w: 3, h: 1, cls: 's-pale' },
      // Mouth — helpful smile
      { x: 5, y: 7, w: 5, h: 1, style: 'background:#9a6a58;border-radius:0 0 2px 2px' },
      // Neck
      { x: 6, y: 8, w: 3, h: 2, cls: 's-pale' },
      // Body — cardigan
      { x: 2, y: 10, w: 11, h: 8, cls: 'c-cardigan-wine' },
      { x: 5, y: 10, w: 5, h: 2, cls: 'x-collar' },
      // Arms
      { x: 1, y: 11, w: 2, h: 7, cls: 'c-cardigan-wine' },
      { x: 12, y: 11, w: 2, h: 7, cls: 'c-cardigan-wine' },
      // Book in hand
      { x: 13, y: 13, w: 2, h: 4, style: 'background:#3a2a18' },
      // Shadow
      { x: 2, y: 17, w: 11, h: 1, cls: 'x-shadow' },
    ],
  },

  // ── OLLE MAGNUSSON — Postman, knows everything ──
  olle_magnusson: {
    bg: 'background:linear-gradient(180deg,#1a1a14 0%,#141410 60%,#1a1208 100%)',
    pixels: [
      // Postman cap
      { x: 3, y: 0, w: 9, h: 2, cls: 'c-uniform-blue' },
      { x: 2, y: 1, w: 11, h: 1, cls: 'c-uniform-blue' },
      // Badge on cap
      { x: 6, y: 0, w: 3, h: 1, cls: 'x-badge' },
      // Head
      { x: 3, y: 2, w: 9, h: 6, cls: 's-mid' },
      // Eyes — knowing
      { x: 4, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 5, y: 4, w: 1, h: 1, cls: 'e-dark' },
      { x: 9, y: 4, w: 2, h: 1, cls: 'e-white' },
      { x: 10, y: 4, w: 1, h: 1, cls: 'e-dark' },
      // Slight smile lines
      { x: 3, y: 5, w: 1, h: 1, style: 'background:rgba(80,50,30,0.3)' },
      { x: 11, y: 5, w: 1, h: 1, style: 'background:rgba(80,50,30,0.3)' },
      // Brows
      { x: 4, y: 3, w: 3, h: 1, cls: 'h-brown' },
      { x: 9, y: 3, w: 3, h: 1, cls: 'h-brown' },
      // Nose
      { x: 6, y: 5, w: 3, h: 1, cls: 's-mid' },
      // Mouth — hint of a smile
      { x: 5, y: 7, w: 5, h: 1, style: 'background:#8a5a50;border-radius:0 0 2px 2px' },
      // Neck
      { x: 6, y: 8, w: 3, h: 2, cls: 's-mid' },
      // Body — postal uniform
      { x: 2, y: 10, w: 11, h: 8, cls: 'c-uniform-blue' },
      // Postal badge
      { x: 4, y: 12, w: 2, h: 2, cls: 'x-badge' },
      // Arms
      { x: 1, y: 11, w: 2, h: 7, cls: 'c-uniform-blue' },
      { x: 12, y: 11, w: 2, h: 7, cls: 'c-uniform-blue' },
      // Mail bag
      { x: 12, y: 14, w: 3, h: 4, style: 'background:#5a4a28' },
      // Shadow
      { x: 2, y: 17, w: 11, h: 1, cls: 'x-shadow' },
    ],
  },
};

// ════════════════════════════════════════
// RENDER FUNCTIONS
// ════════════════════════════════════════

/**
 * Render an NPC sprite into a container element
 * @param {string} npcId - NPC ID to look up
 * @param {HTMLElement} container - DOM element to render into
 */
export function renderSprite(npcId, container) {
  const sprite = SPRITES[npcId];
  if (!sprite) {
    renderFallback(npcId, container);
    return;
  }

  container.innerHTML = '';
  container.classList.add('sprite-container');

  // Background
  const bg = document.createElement('div');
  bg.style.cssText = `position:absolute;inset:0;${sprite.bg || 'background:linear-gradient(180deg,#1a1a14 0%,#141410 60%,#1a1208 100%)'}`;
  container.appendChild(bg);

  // Sprite body wrapper — for idle sway animation
  const body = document.createElement('div');
  body.className = 'sprite-body';
  // Random offset so NPCs don't sway in sync
  body.style.animationDelay = `${(hashStr(npcId) % 3000)}ms`;

  // Pixels
  sprite.pixels.forEach(p => {
    const el = document.createElement('div');
    el.className = `p ${p.cls || ''}`;
    el.style.cssText = `left:${p.x * PX}px;top:${p.y * PX}px;width:${p.w * PX}px;height:${p.h * PX}px;${p.style || ''}`;

    // Tag eye pixels for blink animation
    if (p.cls && (p.cls.includes('e-white') || p.cls.includes('e-dark'))) {
      el.classList.add('sprite-eye');
      // Random blink offset
      el.style.animationDelay = `${(hashStr(npcId) % 2500) + 1000}ms`;
    }

    body.appendChild(el);
  });

  container.appendChild(body);
}

/**
 * Fallback procedural portrait for NPCs without hand-crafted sprites
 */
function renderFallback(npcId, container) {
  container.innerHTML = '';
  container.classList.add('sprite-container');

  const bg = document.createElement('div');
  bg.style.cssText = 'position:absolute;inset:0;background:linear-gradient(180deg,#1a1a14,#141410,#1a1208);';
  container.appendChild(bg);

  const hash = hashStr(npcId);
  const skins = ['#d4a574', '#c8956a', '#b87a50', '#dbb898'];
  const hairs = ['#2a1a0a', '#5a3a18', '#7a7068', '#aaa09a', '#c8a040', '#1a1208'];
  const clothes = ['#2a3a5a', '#3a4040', '#1e2830', '#5a2030', '#5a5850', '#283a58'];

  const skin = skins[hash % skins.length];
  const hair = hairs[(hash >> 2) % hairs.length];
  const cloth = clothes[(hash >> 4) % clothes.length];

  const pixels = [
    { x: 4, y: 0, w: 7, h: 1, style: `background:${hair}` },
    { x: 3, y: 1, w: 9, h: 1, style: `background:${hair}` },
    { x: 3, y: 2, w: 9, h: 6, style: `background:${skin}` },
    { x: 4, y: 4, w: 2, h: 1, style: 'background:#e8e0d0' },
    { x: 5, y: 4, w: 1, h: 1, style: 'background:#1a1208' },
    { x: 9, y: 4, w: 2, h: 1, style: 'background:#e8e0d0' },
    { x: 10, y: 4, w: 1, h: 1, style: 'background:#1a1208' },
    { x: 5, y: 7, w: 5, h: 1, style: 'background:#7a4a30' },
    { x: 6, y: 8, w: 3, h: 2, style: `background:${skin}` },
    { x: 2, y: 10, w: 11, h: 8, style: `background:${cloth}` },
    { x: 5, y: 10, w: 5, h: 2, style: 'background:#c8c0b0' },
    { x: 1, y: 11, w: 2, h: 7, style: `background:${cloth}` },
    { x: 12, y: 11, w: 2, h: 7, style: `background:${cloth}` },
    { x: 2, y: 17, w: 11, h: 1, style: 'background:rgba(0,0,0,0.25)' },
  ];

  pixels.forEach(p => {
    const el = document.createElement('div');
    el.className = 'p';
    el.style.cssText = `left:${p.x * PX}px;top:${p.y * PX}px;width:${p.w * PX}px;height:${p.h * PX}px;${p.style || ''}`;
    container.appendChild(el);
  });
}
