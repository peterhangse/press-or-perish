// Balance simulator — plays thousands of runs with the game's own engine modules.
// Usage: node tools/simulate_balance.mjs [runs=20000] [ranges.json]
//   ranges.json (optional): { "smastad": { "1": {"min":6,"max":9}, ... }, ... } to try new competitor ranges
// Prints survival per town and the average daily margin for a few player models.

import { readFileSync } from 'fs';
import { generateDayLeads } from '../js/engine/day-generator.js';
import { resolveInterview } from '../js/engine/interview-engine.js';
import { generateCompetitorScore, findScoop, findCarryOver, SCOOP_RULES } from '../js/engine/competitor-ai.js';

const root = new URL('..', import.meta.url);
const stories = JSON.parse(readFileSync(new URL('data/stories.json', root), 'utf8'));
const towns = JSON.parse(readFileSync(new URL('data/towns.json', root), 'utf8'));
const N = Number(process.argv[2] || 20000);
const override = process.argv[3] ? JSON.parse(readFileSync(process.argv[3], 'utf8')) : null;
const A = ['friendly', 'direct', 'pressure', 'silence'];
const TOWNS = ['smastad', 'industristad', 'kuststad'];
const byTown = Object.fromEntries(TOWNS.map(t => [t, stories.filter(s => s.town === t)]));
const cfg = Object.fromEntries(towns.map(t => [t.id, override?.[t.id] ? { ...t, competitorScoreRanges: override[t.id] } : t]));
const pick = arr => arr[Math.floor(Math.random() * arr.length)];

function bestPath(s) {
  let best = null;
  for (const a of A) for (let i = 0; i < 3; i++) {
    const r = resolveInterview(s, a, i);
    if (r.perish) continue;
    if (!best || r.points > best.points) best = { a, i, points: r.points };
  }
  return best;
}

// Player models: choose(leads) -> { story, a, i }
const MODELS = {
  random: L => ({ story: pick(L), a: pick(A), i: Math.floor(Math.random() * 3) }),
  medelspelare: L => {
    const story = Math.random() < 0.6 ? [...L].sort((x, y) => y.base_value - x.base_value || Math.random() - 0.5)[0] : pick(L);
    return { story, a: pick(A), i: Math.floor(Math.random() * 3) };
  },
  'medel + läser intervjun': L => {
    const story = Math.random() < 0.6 ? [...L].sort((x, y) => y.base_value - x.base_value || Math.random() - 0.5)[0] : pick(L);
    if (Math.random() < 0.5) { const b = bestPath(story); return { story, a: b.a, i: Math.floor(Math.random() * 3) }; }
    return { story, a: pick(A), i: Math.floor(Math.random() * 3) };
  },
  'alltid tystnad': L => ({ story: pick(L), a: 'silence', i: Math.floor(Math.random() * 3) }),
  'perfekt intervju': L => { const story = pick(L); const b = bestPath(story); return { story, a: b.a, i: b.i }; },
};

for (const [name, choose] of Object.entries(MODELS)) {
  const lostIn = Object.fromEntries(TOWNS.map(t => [t, 0]));
  let fired = 0, won = 0;
  const margins = Object.fromEntries(TOWNS.map(t => [t, [0, 0, 0, 0, 0].map(() => [])]));
  for (let run = 0; run < N; run++) {
    let dead = false;
    for (const t of TOWNS) {
      const used = []; let deficit = 0; let carry = null;
      for (let day = 1; day <= 5; day++) {
        const leads = generateDayLeads(day, byTown[t], used, carry, cfg[t].leadsPerDay || 8);
        const { story, a, i } = choose(leads);
        used.push(story.id);
        const r = resolveInterview(story, a, i);
        if (r.perish) { fired++; lostIn[t]++; dead = true; break; }
        const scoop = findScoop(leads, story);
        const comp = generateCompetitorScore(day, cfg[t]) + (scoop ? SCOOP_RULES.bonus : 0);
        carry = findCarryOver(leads, story, scoop?.id)?.id || null;
        margins[t][day - 1].push(r.points - comp);
        deficit += r.points - comp;
        if (deficit <= -10) { lostIn[t]++; dead = true; break; }
      }
      if (dead) break;
    }
    if (!dead) won++;
  }
  let alive = N; const surv = [];
  for (const t of TOWNS) { surv.push(`${t} ${alive ? Math.round(100 * (alive - lostIn[t]) / alive) : '-'}%`); alive -= lostIn[t]; }
  const avg = arr => arr.length ? (arr.reduce((s, x) => s + x, 0) / arr.length).toFixed(1) : '-';
  console.log(`${name.padEnd(24)} vinner ${(100 * won / N).toFixed(1)}% | överlever: ${surv.join(', ')} | sparkad i intervju ${(100 * fired / N).toFixed(1)}%`);
  console.log(`${''.padEnd(24)} marginal dag 1–5: ${TOWNS.map(t => `${t} [${margins[t].map(avg).join(' ')}]`).join('  ')}`);
}
