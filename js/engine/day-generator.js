/**
 * DAY GENERATOR — Generates the 8 leads for each day
 * Pure functions. No DOM. Portable to Godot.
 *
 * Day 1-2: mostly easy leads (base 2-4)
 * Day 3:   mix of easy + medium (base 3-6)
 * Day 4-5: hard leads dominate (base 5-8)
 *
 * 8 leads per day, 3 source types mixed
 */

/**
 * Generate 3 leads for Day Zero (tutorial) — 1 per source type, easy only
 * @param {Array} allStories - Full stories array from stories.json
 * @returns {Array} 3 story objects (1 letter, 1 document, 1 street)
 */
export function generateDayZeroLeads(allStories) {
  const easy = allStories.filter(s => s.difficulty === 'easy');
  const letter = shuffle(easy.filter(s => s.source_type === 'letter'));
  const doc    = shuffle(easy.filter(s => s.source_type === 'document'));
  const street = shuffle(easy.filter(s => s.source_type === 'street'));

  const leads = [];
  if (letter.length) leads.push(letter[0]);
  if (doc.length)    leads.push(doc[0]);
  if (street.length) leads.push(street[0]);

  return shuffle(leads);
}

/**
 * Generate 8 leads for a given day
 * @param {number} day - Current day (1-5)
 * @param {Array} allStories - Full stories array from stories.json
 * @param {Array} usedIds - Already-used story IDs this run
 * @returns {Array} 8 story objects for today's desk
 */
export function generateDayLeads(day, allStories, usedIds) {
  const available = allStories.filter(s => !usedIds.includes(s.id));

  // Difficulty pools
  const easy   = available.filter(s => s.difficulty === 'easy');
  const medium = available.filter(s => s.difficulty === 'medium');
  const hard   = available.filter(s => s.difficulty === 'hard');

  let pool;
  switch (day) {
    case 1:
      pool = buildPool(easy, 6, medium, 2, hard, 0);
      break;
    case 2:
      pool = buildPool(easy, 5, medium, 2, hard, 1);
      break;
    case 3:
      pool = buildPool(easy, 2, medium, 4, hard, 2);
      break;
    case 4:
      pool = buildPool(easy, 1, medium, 2, hard, 5);
      break;
    case 5:
      pool = buildPool(easy, 0, medium, 2, hard, 6);
      break;
    default:
      pool = buildPool(easy, 3, medium, 3, hard, 2);
  }

  // Ensure exactly 8 leads, fill gaps from any pool
  while (pool.length < 8) {
    const filler = available.find(s => !pool.includes(s));
    if (filler) pool.push(filler);
    else break;
  }

  return shuffle(pool).slice(0, 8);
}

/**
 * Build a lead pool from difficulty tiers
 */
function buildPool(easy, eCount, medium, mCount, hard, hCount) {
  return [
    ...pickRandom(easy, eCount),
    ...pickRandom(medium, mCount),
    ...pickRandom(hard, hCount),
  ];
}

/**
 * Pick N random items from an array
 */
function pickRandom(arr, n) {
  const shuffled = shuffle([...arr]);
  return shuffled.slice(0, Math.min(n, shuffled.length));
}

/**
 * Fisher-Yates shuffle
 */
function shuffle(arr) {
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}
