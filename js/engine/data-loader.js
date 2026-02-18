/**
 * DATA LOADER — Fetches JSON data files
 */

let storiesCache = null;
let npcsCache = null;
let bossCache = null;

/**
 * Load all game data
 */
export async function loadAllData() {
  const [stories, npcs, boss] = await Promise.all([
    loadStories(),
    loadNPCs(),
    loadBossDialogue(),
  ]);
  return { stories, npcs, boss };
}

/**
 * Load stories data
 */
export async function loadStories() {
  if (storiesCache) return storiesCache;
  const res = await fetch('data/stories.json');
  storiesCache = await res.json();
  return storiesCache;
}

/**
 * Load NPC data
 */
export async function loadNPCs() {
  if (npcsCache) return npcsCache;
  const res = await fetch('data/npcs.json');
  npcsCache = await res.json();
  return npcsCache;
}

/**
 * Load boss dialogue data
 */
export async function loadBossDialogue() {
  if (bossCache) return bossCache;
  const res = await fetch('data/boss-dialogue.json');
  bossCache = await res.json();
  return bossCache;
}

/**
 * Get a story by ID
 */
export function getStory(stories, id) {
  return stories.find(s => s.id === id);
}

/**
 * Get an NPC by ID
 */
export function getNPC(npcs, id) {
  return npcs.find(n => n.id === id);
}
