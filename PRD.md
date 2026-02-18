# PRESS OR PERISH — Product Requirements Document
## MVD (Minimum Viable Demo) v0.1

---

## 0. DEPLOY — "Push it live"

```bash
cd "/Users/gmpethan/Documents/deploy/Game (press or perish)"
git add -A && git commit -m "describe your change" && git push
```

- **Live site:** https://press-or-perish.web.app
- **GitHub repo:** https://github.com/peterhangse/press-or-perish
- **Auto-deploy:** Push to `main` → GitHub Action → Firebase Hosting (~1 min)
- **Local test:** `python3 -m http.server 8091` → http://localhost:8091

---

## 1. GAME OVERVIEW

**Genre:** Roguelike journalism game
**Setting:** 1970s rural Sweden, fictional town "Småstad"
**Platform:** Web (HTML/CSS/JS), hosted on Firebase
**Resolution:** 640×360 fixed canvas, scaled to browser
**Aesthetic:** Papers Please-inspired pixel art, cold Nordic noir, desaturated 1970s palette

**Premise:** You're a fresh journalism graduate from Stockholm. No prestigious paper would hire you. The only job offer: reporter at Småstads Tidning, a tiny local newspaper in a small Swedish town. Your editor-in-chief already wants to fire you. You have one week (5 days) to prove your worth — or perish.

**Core Loop:** Each day: read leads → pick 2 stories → interview NPCs → publish 1 story blind → see results vs competitor → deficit updates → next day or fired.

**Win condition:** Survive to Friday evening (Day 5) without the deficit reaching -15.
**Lose condition:** Deficit reaches -15 at any point = PERISHED (fired).

---

## 2. SCORING SYSTEM

### Two-Axis Skill
1. **Story Selection (Axis 1):** Recognize which leads have highest base news value from raw, unpolished tips
2. **Interview Extraction (Axis 2):** Choose the right questions to extract maximum info from NPCs

### Formula
```
Total Score = Base News Value + Tier Bonus
Tier Bonus = tier_reached × 2
```

### Base News Values
| Base Value | Description | Count in pool |
|---|---|---|
| 2 pts | Filler: event notices, minor incidents, soft features | ~8 stories |
| 4 pts | Decent: local disputes, small scandals, community issues | ~12 stories |
| 6 pts | Good: real investigations, hidden connections | ~12 stories |
| 8 pts | Top: deaths, major corruption, cover-ups | ~8 stories |

### Information Tiers
| Tier | Label shown to player | Bonus | Example total (base 6) |
|---|---|---|---|
| 0 | Base story | +0 | 6 pts |
| 1 | Basic info | +2 | 8 pts |
| 2 | Detailed story | +4 | 10 pts |
| 3 | Full investigation | +6 | 12 pts |

**Score range per day:** 2 pts (base-2 filler, Tier 0) to 14 pts (base-8 top story, Tier 3).

### Hidden Gems (~6 of 40 stories)
Some leads that LOOK like base-2 or base-4 (boring permit, routine report) actually have base-value 6 or 8. The lead text contains subtle clues for observant players. The competitor AI does NOT recognize hidden gems.

### Deficit System
- Starts at 0
- Lost day: `deficit = deficit - (competitor_score - player_score)`
- Won day: `deficit = min(0, deficit + (player_score - competitor_score))`
- **-15 = PERISHED.** No mercy.

### Competitor AI
- 70-80% chance of picking a top-2 base-value lead from the day's 8
- Achieves 70-80% of max tier on their chosen story
- Does NOT spot hidden gems — chases obvious big stories
- Average ~8-10 pts/day

---

## 3. GAME FLOW

### First Launch
1. **Onboarding sequence** (plays once per save)
   - Journalism degree diploma
   - 3-4 flashy job ads → rejection letters (hard cuts)
   - One shabby ad: "Småstads Tidning — Reporter"
   - Meet the boss: warm opener → twist → ultimatum
   - Title card: PRESS OR PERISH
2. **Day Zero** (tutorial)
   - 3 leads (1 per source type)
   - Interview 1: 2 Q1 options only (others grayed)
   - Interview 2: all 4 Q1 options
   - Publish → sleep → results
   - Competitor shock: massive story player couldn't find
3. **Day 1 begins** (full game)

### Return Launches
- Start screen → "Ny omgång" → Day 1 (skip onboarding)

### Daily Loop (5 days)
```
Day Transition (torn calendar, morning message, deficit status)
  ↓
Morning Desk (8 leads, 3 source zones, boss note, competitor clip)
  ↓
Player picks 2 leads
  ↓
Interview 1 (Q1: 4 options → response → Q2: 3 options → response → tier)
  ↓
Interview 2 (same structure, different NPC)
  ↓
Publish Screen (2 stories side-by-side, NO scores, blind choice)
  ↓
Sleep Screen (3-5 sec, black, headline ghosted, doubt)
  ↓
Results Screen (your newspaper → competitor newspaper → points → boss → deficit → feedback)
  ↓
Check: deficit ≤ -15 → PERISHED | day = 5 → SURVIVED | else → next day
```

### If Interview Terminates (Aggressive on sensitive NPC)
- NPC walks out. Player gets Tier 0 for that story.
- Player still does Interview 2 with other lead.
- At publish: has 1 Tier-0 dud + 1 real story. Choice still exists but one option is bad.

---

## 4. INTERVIEW SYSTEM

### Structure
- **Q1:** Player chooses 1 of 4 archetype questions
- See NPC Q1 response + expression change
- **Q2:** Player chooses 1 of 3 follow-up questions (hyper-specific to story)
- See NPC Q2 response + expression change + tier result

### Q1 Archetypes (4)
| Archetype | Color | Description |
|---|---|---|
| Trust Builder | Green (#4a8a4a) | Soft, empathetic opener. Low risk, enables deeper Q2. |
| Neutral Fact-Find | Olive (#6a6a4a) | Professional, non-threatening. Gets surface facts. Safe. |
| Pressure Push | Orange (#8a5a2a) | Direct challenge with evidence. High risk, high reward. |
| Aggressive Accusation | Red (#8a2a2a) | Confrontation. Can crack NPC or terminate interview. |

### Q2 Options (3 per Q1 path)
- Hyper-specific to the story — reference names, dates, contradictions
- NOT transferable between stories
- Each maps to a fixed tier outcome via lookup table

### Lookup Table Engine
Every Q1→Q2 combination maps directly to a fixed result:
```
outcomes[q1_archetype].followups[q2_index] → { tier, response, expression }
```
No runtime trust calculation. No hidden state. Content IS the logic.

**12 paths per story. 40 stories × 12 = 480 total outcomes.**

### NPC Expression States
Each NPC has expression variants that update TWICE per interview:
- After Q1 (reflects how they reacted to opening)
- After Q2 (reflects the outcome)

Expression keyed to lookup result — just CSS class swap.

Core NPCs (5): 4 expressions each (defensive, guarded, warming, open)
Other NPCs (35): 2 expressions each (default, reactive)

---

## 5. SCREENS & UI

### Persistent UI (visible on all screens)
- **Deficit meter:** Vertical bar, right side. Ticks at -5, -10, -15. Animated fill. Danger flash at -12+. Label: "X points from perishing"
- **Week strip:** Mon-Fri horizontal. Past days crossed with scores. Today = red. Future = grayed.
- **Clock:** Shows time of day. Morning → Midday → Afternoon → Evening.
- **Window:** Background behind NPC in interview. Reflects deficit (calm → hellscape, 5-6 CSS states).

### Screen: Start
- "Småstads Tidning" masthead, faded desk background
- "Ny omgång" button
- Best score display (if exists)

### Screen: Onboarding
- Sequential narrative cards with hard cuts between
- Job ads with rejection letters
- Boss meeting with pixel portrait
- Title card: PRESS OR PERISH

### Screen: Day Transition
- Torn calendar page (yesterday fades/rotates away)
- New day: "Tisdag. Dag 2 av 5."
- Deficit status: "Deficit: −5. 10 points from perishing."
- Hard cut to desk

### Screen: Morning Desk
- 640×360 desk surface with lamp glow, felt mat, coffee, ashtray
- **3 source zones:**
  - Left: Letters (envelopes, handwritten notes, anonymous tips)
  - Center: Official Documents (police reports, permits, council minutes)
  - Right: Street (map pins/location markers — going out into town)
- 8 leads as physical documents, slightly overlapping within zones
- Click lead → expand to read (English text, Swedish names)
- Click "Pursue →" to select. Max 2.
- Bottom tray: 2 slots + "Start interviews →" (active when both filled)
- Boss note (Day 2+): yesterday's critique
- Competitor clip (Day 2+): what Länstidningen published + their score

### Screen: Interview
- **Left panel (~200px):** NPC pixel art + nameplate (name, role, age) + environment background + deficit-reactive window
- **Right panel:** Notepad header + NPC dialogue bubble + question cards
- Notepad updates after each question with scribbled notes + tier tag
- NPC dialogue: English text, Swedish NPC names, atmospheric stage directions in italics
- Question cards: archetype color tag + question text
- Q1: 4 cards. Q2: 3 cards (appear after Q1 response)

### Screen: Publish
- Two story cards side-by-side: headline (from tier reached) + notepad summary
- **NO score, NO base value shown**
- Player clicks one → "PUBLISH" stamp appears → click to confirm

### Screen: Sleep
- Hard cut to black
- Clock ticking (implied, not audible in MVD)
- Chosen headline ghosted in faint text
- 3-5 seconds duration
- Hard cut to results

### Screen: Results
- Your newspaper front page: "Småstads Tidning" masthead, headline, vague body text
- Hard cut → competitor front page: "Länstidningen", headline, score
- Points comparison: your total vs theirs, win/loss stamp
- Boss reaction: pixel portrait + dialogue
- Deficit update: animated old → new value
- Feedback hint if didn't max: vague ("There was more to this story...")
- "Nästa dag →" button

### Screen: Game Over (Perished)
- Hard cut → boss pixel portrait
- "Pack your things."
- Final deficit, total score, days survived
- "Try Again" button

### Screen: Game Over (Survived)
- Cold: "You kept your job. For now."
- Total score across 5 days
- Unlock tease: "There are other towns. Other stories."
- "Play Again" button

---

## 6. CONTENT REQUIREMENTS

### Stories: 40 total
| Category | Easy (Day 1-2) | Medium (Day 3) | Hard (Day 4-5) | Total |
|---|---|---|---|---|
| Labor | 4 | 2 | 2 | 8 |
| Crime | 3 | 2 | 3 | 8 |
| Corruption/Politics | 3 | 1 | 4 | 8 |
| Human Interest | 3 | 2 | 3 | 8 |
| Breaking News | 3 | 1 | 4 | 8 |
| **Total** | **16** | **8** | **16** | **40** |

Source types: ~14 letters, ~13 official documents, ~13 street.
Hidden gems: ~6 total (scattered across categories).
Each day's 8 leads: mix of all 3 source types.

### Per Story
- Lead text (English, Swedish names, raw/unpolished)
- NPC profile (name, role, age, sprite ref, aggressive_terminates flag)
- 4 tier headlines (basic → full investigation)
- 4 tier descriptions
- 4 Q1 questions (1 per archetype, story-specific text)
- 4 Q1 NPC responses (1 per archetype)
- 12 Q2 questions (3 per Q1 path, hyper-specific)
- 12 Q2 NPC responses
- 12 tier assignments (which tier each Q1→Q2 path reaches)
- 4 feedback texts (1 per tier, vague hints)

### Boss Dialogue
Keyed to deficit ranges: 0, -1 to -5, -6 to -9, -10 to -12, -13 to -14.
Day-specific overrides for Day 1 and Day 5.
Win reactions (barely vs dominant). Fired reaction.

### NPCs: 40 total
- 5 core (Karl, Svensson, Kristina, Håkansson, Anna): 4 expressions
- 35 simpler: 2 expressions each

---

## 7. DATA SCHEMAS

### stories.json — Array of Story objects
```json
{
  "id": "SMST-001",
  "title": "The Mill Accident",
  "category": "labor",
  "difficulty": 1,
  "base_value": 6,
  "is_hidden_gem": false,
  "npc": {
    "name": "Karl Lindström",
    "role": "Mill Worker",
    "age": 34,
    "sprite": "karl",
    "aggressive_terminates": true
  },
  "lead": {
    "type": "street",
    "text": "Karl at the mill hurt himself yesterday...",
    "source_label": "Anonymous tip",
    "time": "Slipped under the door"
  },
  "tiers": {
    "0": { "headline": "Worker injured at Småstad mill", "description": "..." },
    "1": { "headline": "Third accident at mill — inspections delayed", "description": "..." },
    "2": { "headline": "Workers forced to use broken machinery", "description": "..." },
    "3": { "headline": "Mill owner covered up failures for property sale", "description": "..." }
  },
  "outcomes": {
    "trust_builder": {
      "q1_text": "This must have been really difficult...",
      "q1_response": { "text": "...", "expression": "warming" },
      "followups": [
        { "text": "Q2 question...", "tier": 1, "response": "...", "expression": "warming" },
        { "text": "Q2 question...", "tier": 3, "response": "...", "expression": "open" },
        { "text": "Q2 question...", "tier": 2, "response": "...", "expression": "warming" }
      ]
    },
    "neutral_factfind": { "q1_text": "...", "q1_response": {...}, "followups": [...] },
    "pressure_push": { "q1_text": "...", "q1_response": {...}, "followups": [...] },
    "aggressive_accusation": {
      "q1_text": "...",
      "q1_response": { "text": "...", "expression": "defensive", "terminated": true },
      "followups": null
    }
  },
  "feedback": {
    "tier_3": "You got the full story...",
    "tier_2": "There was a financial angle you didn't reach...",
    "tier_1": "Your source was holding something back...",
    "tier_0": "They shut down. Read the room next time."
  }
}
```

### npcs.json — Array of NPC objects
```json
{
  "id": "karl",
  "name": "Karl Lindström",
  "role": "Mill Worker",
  "age": 34,
  "default_expression": "guarded",
  "expressions": ["defensive", "guarded", "warming", "open"],
  "unique_detail": "bandaged_hand",
  "clothing_color": "worker-blue"
}
```

### boss-dialogue.json
```json
{
  "deficit_ranges": {
    "0": ["First day. Don't embarrass me."],
    "-1_to_-5": ["Länstidningen got {comp}. You got {player}. Did you even TRY?"],
    "-6_to_-9": ["You're making me look like a fool. I stuck my neck out hiring a Stockholm kid."],
    "-10_to_-12": ["One more day like this and you're done. DONE."],
    "-13_to_-14": ["I'm writing your termination letter right now."]
  },
  "day_overrides": {
    "5": "Today's the day. Don't disappoint me."
  },
  "win": {
    "barely": "Fine. You kept your job. Don't expect flowers.",
    "dominant": "Hmm. Maybe I was wrong about you."
  },
  "fired": "Pack your things."
}
```

---

## 8. VISUAL SPECS

### Canvas
- Fixed 640×360, CSS-scaled to browser maintaining aspect ratio
- `image-rendering: pixelated` globally

### Color Palette (from mockups)
```css
--paper: #e8dfc8;
--paper-dark: #d4c9a8;
--paper-aged: #c9b98a;
--ink: #1a1208;
--ink-faded: #4a3f2a;
--ink-red: #8b1a1a;
--desk: #2a1f12;
--lamp: #f5e4a0;
--green-felt: #1a2e1a;
--deficit-red: #cc2222;
```

### Typography
- **Special Elite** — headings, mastheads, handwritten notes
- **Courier Prime** — body text, UI labels, notepad
- **Bebas Neue** — large numbers (deficit, scores, day numbers)

### Pixel Art Characters
- 14×22 pixel grid, rendered at 3x scale
- Max 6-8 colors per NPC
- No outlines — forms defined by contrast
- Clothes = instant social signal
- One unique detail per character (bandage, badge, brooch, etc.)
- Expression changes: eyebrow position + pupil direction + mouth shape
- Body shared, face as separate overlay layer

### Window Backgrounds (deficit-reactive)
| Deficit | Scene |
|---|---|
| 0 to -3 | Pale winter day, bare trees, quiet |
| -4 to -7 | Overcast, darker, wind |
| -8 to -11 | Grey, heavy clouds, almost dark |
| -12 to -14 | Storm, near-black, hostile |
| Positive | Softer light, hint of sun |

### Time-of-Day Lighting
| Phase | Time | Lighting |
|---|---|---|
| Desk | Morning | Cool blue-grey, lamp warm |
| Interview | Midday | Neutral |
| Publish | Afternoon | Amber, late light |
| Results | Evening | Dark, lamp dominant |

### Transitions
- Hard cuts between screens (no fades)
- Brief loading flash between major screen changes (Papers Please style)

---

## 9. TECH ARCHITECTURE

### Stack
- Vanilla HTML/CSS/JS with ES6 modules
- Zero build tools, zero frameworks
- JSON data files for all content
- Firebase Hosting for deployment

### File Structure
```
index.html
PRD.md
ROADMAP.md
css/
  variables.css, onboarding.css, desk.css, interview.css,
  publish.css, results.css, transition.css, sprites.css, components.css
js/
  main.js
  engine/
    game-state.js      — central state, localStorage
    day-generator.js   — pick 8 leads per day, assign competitor
    interview-engine.js — lookup table reader
    scoring-engine.js  — points, deficit, win/lose
    competitor-ai.js   — story selection + score simulation
  ui/
    screen-manager.js  — flow orchestration
    onboarding.js      — intro narrative
    desk-screen.js     — leads, zones, selection
    interview-screen.js — NPC, questions, expressions
    publish-screen.js  — blind choice + sleep
    results-screen.js  — newspapers, score, boss, deficit
    transition-screen.js — torn page, morning message
    components.js      — deficit meter, week strip, clock, window
data/
  stories.json         — 40 stories with full lookup tables
  npcs.json            — NPC profiles + expressions
  boss-dialogue.json   — deficit-keyed reactions
assets/
  fonts/
```

### Engine Separation
- `js/engine/` = pure logic, zero DOM access, portable to Godot/GDScript
- `js/ui/` = DOM rendering, event handling, animations
- `data/` = all game content in JSON, the Godot migration path

---

## CONTENT CREATION GUIDELINES

### Story Batch Creation Process
When creating new stories (40+ entries, ~9400 lines JSON), **never** write large JSON inline via terminal commands or Python heredocs — shell escaping and size limits cause corruption.

**Proven workflow:**
1. Write each batch as a **separate JSON file** using `create_file` (4-6 stories per batch, ~1400 lines each)
2. Validate each batch independently (`python3 -c "import json; json.load(open('batch.json'))"`)
3. Merge all batches into `stories.json` with a simple Python script
4. Run schema validation against the full dataset
5. Clean up batch files

**Why this works:** `create_file` handles arbitrary UTF-8 content without shell escaping issues. Batches of 4-6 stories stay within reliable size limits. Merge is a trivial `json.load` + `json.dump`.

### Story Schema (per story)
Each story must include: `id`, `title`, `description`, `lead_text`, `preview`, `source_type` (letter|document|street), `difficulty` (easy|medium|hard), `base_value` (2-8), `category`, `npc_id`, `npc_name`, `npc_title`, `interview` (opening_line, q1_options[4], branches{friendly,direct,pressure,silence} each with q1_response, expression_hint, q2_options[3], outcomes[3] with tier/response/expression/feedback), `headlines` (tier_0 through tier_3, each with 3 options [{text, tone}]).

### Language Rule
All game text in **English**. Only character names, place names, and newspaper names stay in **Swedish** (e.g., Småstads Tidning, Gunnar Ek, Regionbladet).
