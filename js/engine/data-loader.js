/**
 * DATA LOADER — Fetches JSON data files
 */

let storiesCache = null;
let npcsCache = null;
let bossCache = null;
let townsCache = null;

/**
 * Load all game data
 */
export async function loadAllData() {
  const [stories, npcs, boss, towns] = await Promise.all([
    loadStories(),
    loadNPCs(),
    loadBossDialogue(),
    loadTowns(),
  ]);
  return { stories, npcs, boss, towns };
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
 * Load towns data
 */
export async function loadTowns() {
  if (townsCache) return townsCache;
  const res = await fetch('data/towns.json');
  townsCache = await res.json();
  return townsCache;
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

/**
 * Get a town config by ID
 */
export function getTownConfig(towns, townId) {
  return towns.find(t => t.id === townId);
}

/**
 * Get the next town in progression order, or null if at the last town
 */
export function getNextTown(towns, currentTownId) {
  const current = towns.find(t => t.id === currentTownId);
  if (!current) return null;
  const next = towns.find(t => t.order === current.order + 1);
  return next || null;
}

/**
 * Filter stories by town
 */
export function getStoriesByTown(stories, townId) {
  return stories.filter(s => s.town === townId);
}
