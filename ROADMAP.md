# PRESS OR PERISH — Roadmap

All features deferred from the MVD (Minimum Viable Demo) are preserved here, organized by milestone.

---

## ✅ MVD (v0.1) — Foundation
*Currently building*
- [x] 5-day game loop with 40 stories
- [x] Lookup-table interviews (4 Q1 × 3 Q2 = 12 paths/story)
- [x] Variable base news values (2-8) + fixed tier bonus (+2/tier)
- [x] Hidden gems (~6 deceptive leads)
- [x] Deficit meter (-15 = perished)
- [x] Competitor AI (70-80% optimal, misses hidden gems)
- [x] Onboarding sequence (rejections → Småstad → boss twist → title card)
- [x] Day Zero tutorial
- [x] Pixel art NPCs (5 core × 4 expressions, 35 simple × 2 expressions)
- [x] 3 source types on desk (letters, documents, street)
- [x] Deficit-reactive window backgrounds
- [x] Time-of-day lighting shifts
- [x] Sleep screen between publish and results
- [x] Boss dialogue keyed to deficit
- [x] Firebase Hosting deployment

---

## v1.1 — Replayability
*After MVD proven fun*
- [ ] **Randomization variables:** NPC names, detail swaps, amounts, dates rotate each run
- [ ] **Seeded PRNG:** Same seed = same run. Display seed on end screen for sharing.
- [ ] **Daily challenge mode:** Seed = today's date, one attempt only
- [ ] **High score tracking:** Per-run best score, saved to localStorage
- [ ] **5th Q1 archetype: Gentle Challenge** — politely questions official narrative, medium risk
- [ ] **4th Q2 option per Q1 path** — expands from 12 to 20 paths/story (800 total outcomes)

---

## v1.2 — Depth
*Layer complexity onto proven base*
- [ ] **Trust-conditional Q2 branching:** Q2 NPC responses vary by hidden trust level (HIGH/MEDIUM/LOW), not just Q1 choice
- [ ] **Between-tier partial scoring:** Hit 1 of 2 required topics = partial credit (5 pts instead of 6)
- [ ] **Topic category tracking:** Questions cover topic categories (Safety Record, Financial Motive, Coercion), tracked across Q1+Q2
- [ ] **Trust meter hybrid UI:** Subtle color shift on NPC nameplate (cold blue → warm amber). No numbers, no bar. Player learns to read the shift.
- [ ] **Trust as hidden variable:** 0-100 scale, each archetype has trust_delta per NPC personality type

---

## v2.0 — Meta-Progression
*The Slay the Spire model*
- [ ] **4 journalist characters** (horizontal variety, not power):
  - The Rookie (starter, no special ability)
  - The Charmer (higher starting NPC openness, aggressive damages more)
  - The Bulldog (aggressive questions less risky, trust-builders weaker)
  - The Networker (sees 1 extra detail per lead, interviews harder)
- [ ] **Unlock conditions:**
  - The Charmer: Reach Day 3 with The Rookie
  - The Bulldog: Survive a full run
  - The Networker: Win with 2 different characters
- [ ] **4 towns** (different story type distributions):
  - Småstad (starter): balanced mix
  - Industristad: labor disputes, factory accidents, union corruption
  - Kuststad: smuggling, missing persons, maritime accidents
  - Huvudstad District: high-stakes politics (hardest)
- [ ] **Town unlocks:** Win with all characters in current town → unlock next
- [ ] **Per-combination leaderboards:** 4 characters × 4 towns = 16 leaderboards
- [ ] **Character-specific onboarding:** Each character has unique Day Zero
- [ ] **Sound design:**
  - Typewriter clicks on notepad
  - Paper shuffle on desk
  - Dull thud on publish stamp
  - Red alert tone at danger zone
  - Silence between — Nordic noir emptiness
- [ ] **Cross-story threads:** Day 1 mill accident connects to Day 3 land deal (same developer)

---

## v3.0 — Complexity
*Endgame depth for mastered players*
- [ ] **NPC choice per lead:** Some leads offer 2-3 NPC interview targets (different angles, different difficulty)
  - MVP: 1 lead = 1 NPC (simple)
  - Kuststad: some leads offer alternate NPC
  - Huvudstad: most leads have 2-3 NPC options
- [ ] **Sidegrade items** (tradeoffs, not power):
  - "Press Pass": 3 Q1 options per interview BUT only 1 interview per day
  - "Anonymous Tip Line": See 1 extra lead detail BUT all interviews start colder
  - "Veteran's Notebook": See if you maxed info after interview BUT deficit threshold is -8 instead of -10
- [ ] **Item unlocks:** Specific achievements (max 5 stories total, win without aggressive, etc.)

---

## Design Principles (preserved from design sessions)
- **Pressure is the game.** Every system serves the emotional loop. If it dilutes the dread, cut it.
- **The name is honored.** -10 = perished. No mercy. No rubber banding.
- **Two-axis skill.** Story selection (what to investigate) + interview extraction (how to interview).
- **Content IS logic.** Lookup tables, not runtime calculation. Engine is just a reader.
- **Blind publish.** You never see scores before committing. The gut call is the peak.
- **Unpublished stories haunt.** You never see the score of the story you didn't publish. Ever.
- **The boss is selfish.** Not evil, not a mentor. Self-preserving. Cold.
- **Anticapitalism through mechanics.** The system speaks. The game never preaches.
- **English with Swedish flavor.** International first. Swedish names, places, and the occasional å.
- **Papers Please physicality.** Documents, stamps, tactile feedback. Information on objects, not menus.
