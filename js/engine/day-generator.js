/**
 * DAY GENERATOR — Generates the 8 leads for each day
 * Pure functions. No DOM. Portable to Godot.
 *
 * Day 1-2: mostly easy leads (base 2-4)
 * Day 3:   mix of easy + medium (base 3-6)
 * Day 4-5: hard leads dominate (base 5-8); 'expert' and 'elite' stories
 *          (Kuststad's toughest) join the hard pool on these days
 *
 * 8 leads per day, 3 source types mixed
 */

/**
 * Generate 3 leads for Day Zero (tutorial) — 1 per source type, easy only
 * @param {Array} allStories - Full stories array (already filtered by town)
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
 * @param {Array} allStories - Full stories array (already filtered by town)
 * @param {Array} usedIds - Already-used story IDs this run
 * @param {string} [carryOverId] - A lead passed on yesterday that is still open; always dealt again
 * @param {number} [count=8] - Leads on the desk (towns.json `leadsPerDay`: Småstad 4, Industristad 6, Kuststad 8)
 * @returns {Array} story objects for today's desk
 */
export function generateDayLeads(day, allStories, usedIds, carryOverId = null, count = 8) {
  const carryOver = carryOverId
    ? allStories.find(s => s.id === carryOverId && !usedIds.includes(s.id))
    : null;
  const available = allStories.filter(s => !usedIds.includes(s.id) && s !== carryOver);

  // Difficulty pools
  const topTier = day >= 4 ? ['hard', 'expert', 'elite'] : ['hard'];
  const easy   = available.filter(s => s.difficulty === 'easy');
  const medium = available.filter(s => s.difficulty === 'medium');
  const hard   = available.filter(s => topTier.includes(s.difficulty));

  // Difficulty mix for an 8-lead desk, scaled down for smaller desks
  const MIX = {
    1: [6, 2, 0],
    2: [5, 2, 1],
    3: [2, 4, 2],
    4: [1, 2, 5],
    5: [0, 2, 6],
  };
  const [e, m, h] = scaleMix(MIX[day] || [3, 3, 2], count);
  const pool = buildPool(easy, e, medium, m, hard, h);

  // Ensure exactly `count` leads, fill gaps from any pool (random, not file order)
  const fillers = shuffle(available.filter(s => !pool.includes(s)));
  while (pool.length < count && fillers.length) pool.push(fillers.pop());

  const leads = shuffle(pool).slice(0, carryOver ? count - 1 : count);
  if (carryOver) leads.splice(Math.floor(Math.random() * (leads.length + 1)), 0, carryOver);
  return leads;
}

/**
 * Scale an 8-lead difficulty mix to `count` leads (largest remainder, keeps the total exact)
 * e.g. [6,2,0] → 4 leads: [3,1,0]; [1,2,5] → 6 leads: [1,1,4]
 */
export function scaleMix(mix, count) {
  const total = mix.reduce((a, b) => a + b, 0);
  const raw = mix.map(n => (n * count) / total);
  const out = raw.map(Math.floor);
  let left = count - out.reduce((a, b) => a + b, 0);
  const order = raw.map((r, i) => [r - Math.floor(r), i]).sort((a, b) => b[0] - a[0] || b[1] - a[1]);
  for (const [, i] of order) { if (left <= 0) break; out[i]++; left--; }
  return out;
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
