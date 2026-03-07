<!-- PRD_VERSION: 2.0 | STORIES: 120 | NPCS: 84 | TOWNS: 3 | ACHIEVEMENTS: 50 | UPDATED: 2026-03-07 -->
# PRESS OR PERISH — Complete Product Requirements Document
## Version 2.0 · Last updated: 7 March 2026

---

## TABLE OF CONTENTS

1. [Overview & Premise](#1-overview--premise)
2. [How to Play — Full Player Journey](#2-how-to-play--full-player-journey)
3. [Core Gameplay Loop](#3-core-gameplay-loop)
4. [Scoring System](#4-scoring-system)
5. [Interview System (Detail)](#5-interview-system-detail)
6. [Competitor AI](#6-competitor-ai)
7. [Boss System](#7-boss-system)
8. [All Screens & UI](#8-all-screens--ui)
9. [Audio System](#9-audio-system)
10. [Visual Design & Art Style](#10-visual-design--art-style)
11. [Content Inventory](#11-content-inventory)
12. [Data Schemas (Complete)](#12-data-schemas-complete)
13. [Technical Architecture](#13-technical-architecture)
14. [File-by-File Reference](#14-file-by-file-reference)
15. [Deployment & Infrastructure](#15-deployment--infrastructure)
16. [Design Principles](#16-design-principles)
17. [Roadmap & Future Features](#17-roadmap--future-features)

---

## 1. OVERVIEW & PREMISE

**Game:** Press or Perish
**Genre:** Roguelike journalism simulation
**Setting:** 1970s rural Sweden — three fictional towns: Småstad → Industristad → Kuststad
**Platform:** Web browser (HTML/CSS/JS), hosted on Firebase Hosting
**Resolution:** 640×360 fixed canvas, CSS-scaled to fit browser window
**Aesthetic:** Papers Please-inspired pixel art, cold Nordic noir, desaturated 1970s newsprint palette
**Live URL:** https://press-or-perish.web.app
**Repository:** https://github.com/peterhangse/press-or-perish (branch: `main`)

### Premise
You are a fresh journalism graduate from Stockholm University (Class of 1974, Magna Cum Laude). No prestigious paper — Dagens Nyheter, Expressen, Göteborgs-Posten — would hire you. The only job offer: reporter at **Småstad Paper**, a tiny local newspaper run by the gruff editor-in-chief **Gunnar Ek**. Your competitor is **Regionbladet**, a larger regional paper that is systematically outperforming your publication each day.

You have **one week (5 days)** to prove your worth — or perish. If you survive, your boss recommends you to the next town's paper. Three towns, three bosses, fifteen days.

### Town Progression
| Order | Town | Newspaper | Competitor | Boss | Dates |
|---|---|---|---|---|---|
| 1 | Småstad | Småstad Paper | Regionbladet | Gunnar Ek | Nov 10–15, 1974 |
| 2 | Industristad | Industristad Paper | Fabriksbladet | Birgit Ståhl | Nov 17–22, 1974 |
| 3 | Kuststad | Kuststad Paper | Sjöfartstidningen | Ragnar Sjöberg | Nov 24–29, 1974 |

Each town is a self-contained 5-day run with its own stories (40 per town, 120 total), boss, competitor, visual identity, and difficulty curve. Surviving a town triggers a farewell sequence where the outgoing boss recommends you to the next town's editor.

### Win/Lose Conditions
- **WIN (town):** Survive to Friday evening (Day 5) without the deficit reaching -10 or below.
- **WIN (game):** Survive all three towns.
- **LOSE (PERISHED):** Deficit reaches -10 at any point = fired immediately.
- **LOSE (INSTANT PERISH):** Certain interview Q2 choices trigger an immediate firing — red FIRED stamp, slam SFX, game over.

---

## 2. HOW TO PLAY — FULL PLAYER JOURNEY

### 2.1 First Launch: Start Screen
The game opens to a desktop-style start screen with the title **"PRESS OR PERISH"** in large typewritten text. The title is initially non-interactive — clicking it triggers the title music and reveals the menu below.

**Menu options:**
- **New Game** — Skips the tutorial, prompts for name, starts at Day 1
- **Continue** — Resumes a saved game (only visible if a save exists in localStorage)
- **Tutorial** — Runs the full onboarding sequence + Day Zero
- **Highscores** — Shows the Press Archive (all completed runs sorted by points)

A persistent **mute button** (♪ on/off) appears in the top-right corner of the game wrapper, controlling both soundtrack and SFX.

### 2.2 Tutorial Path: Onboarding Sequence
If the player selects Tutorial, they experience a 13-step narrative sequence:

| Step | Type | Content |
|------|------|---------|
| 1 | Diploma | Stockholm University journalism degree. Player types their name on the diploma. |
| 2 | Job Ad | Dagens Nyheter — prestigious, 80,000 kr/month |
| 3 | Rejection | "Unfortunately, we are not currently hiring junior reporters." |
| 4 | Job Ad | Expressen — "Minimum 5 years experience." |
| 5 | Rejection | "No." — Bo Strömberg |
| 6 | Job Ad | Göteborgs-Posten — 340 applicants for one position |
| 7 | Rejection | "We have chosen to proceed with candidates who have professional experience." |
| 8 | Job Ad | Småstad Paper — shabby, 21,500 kr/month, "No experience required." |
| 9 | Acceptance | "You got the job. Nobody else applied." — Gunnar Ek |
| 10 | Boss Meeting (warm) | "Welcome! It's good to have someone young on the team." |
| 11 | Boss Meeting (serious) | "We're dying. Regionbladet is eating our lunch every single day." |
| 12 | Boss Meeting (intense) | "FIVE DAYS. If you can't outperform Regionbladet by then... there's no job." |
| 13 | Title Card | "PRESS or PERISH" — words slam in one-by-one with SFX, then fade |

Each step has a "Continue →" button except the title card (auto-advance). The boss steps 10-12 reuse the same portrait frame, only updating the speech bubble.

### 2.3 Day Zero (Tutorial Day)
After onboarding, a **tutorial day** runs with training wheels:

- **3 leads** on the desk (1 per source type: letter, document, street) — all easy difficulty
- Player picks 1 lead to investigate
- Interview has **2 of 4 Q1 options grayed out** (pressure & silence locked) — teaches player the basic interview mechanic
- After publishing, the competitor scores **14 points** (a massive, intentional shock)
- Results show the blowout with a message: "This is what we're up against."
- Day Zero does NOT affect the real deficit → starts fresh at Day 1

### 2.4 New Game Path
If New Game is selected, the player gets a **name prompt modal** (pre-filled with last used name), then jumps straight to Day 1 with all mechanics unlocked.

### 2.5 The Daily Loop (Days 1-5)
Each day follows this exact sequence:

```
Day Transition Screen (3 seconds, auto-advance)
    ↓
Morning Desk (8 leads, pick 1)
    ↓
Interview (Q1 → NPC response → Q2 → NPC response → tier result)
    ↓
Sleep Screen (deficit change, mood text)
    ↓
Results Screen (Phase 1: your score → Phase 2: "go to sleep" → comparison, deficit, boss quote)
    ↓
Check: deficit ≤ -10 → PERISHED  |  day = 5 → SURVIVED  |  else → next day
```

### 2.6 Town Progression
When a player survives Day 5 of a non-final town:

1. **Survived screen** — Shows stats and "SURVIVED" stamp (same as final game-over screen)
2. **Boss farewell sequence** — The outgoing boss delivers a 3-step farewell cutscene (warm → serious → intense), recommending the player to the next town's editor
3. **Town advance screen** — Shows the new town's onboarding: boss introduction, new rules/context, threat
4. **Day Zero (new town)** — Sticky-note orientation day with 3 easy leads, restricted interview options. Day Zero does NOT affect the real deficit.
5. **Day 1 begins** — Deficit resets to 0, story pool resets, new boss quotes load

Completed town history (deficit, day records, survived status) is preserved in `townHistory[]` for the highscore archive.

---

## 3. CORE GAMEPLAY LOOP

### 3.1 Day Transition
- Shows: Day number, day name (MONDAY–FRIDAY), date (November 11–15, 1974)
- Deficit displayed (from Day 2 onward) with smooth color interpolation (green → amber → red)
- Mood text changes based on deficit severity
- Auto-advances after 3 seconds with an ambient tick SFX

### 3.2 Morning Desk
The desk is the core selection screen. It presents **8 lead story cards** in a grid layout:

**Layout:**
- **Top bar:** A window showing the current town's silhouette (sky gradient, buildings as CSS clip-path, tiny lit windows), plus a **boss sticky note** with today's directive
- **Center:** 8 lead cards in a scrollable grid
- **Bottom:** Action bar with selected lead label and INVESTIGATE button

**Town-specific desk theming:**
- **Småstad:** Warm brown wood desk, residential silhouette (church spire, marketplace), yellow window lights, warm cream lead cards
- **Industristad:** Cold steel-grey desk, factory skyline (smokestacks, paper mill, cranes), animated chimney smoke wisps, orange furnace glows, cooler newsprint-grey lead cards with "HEMLIGT" stamps
- **Kuststad:** Weathered teal desk, harbor silhouette (lighthouse, fishing boats, cargo ships), animated harbor waves, navigation lamps/ship portholes, sea-mist-grey lead cards

**Each lead card shows:**
- **Source badge** — colored tag: Letter (green-ish), Document (amber), Street Tip (blue-ish)
- **Headline** — the story title in bold
- **Lead text** — raw, unpolished description of the tip
- **Source line** — NPC name and title

**Visual flair (randomized per card, seeded by story ID):**
- ~12% chance of coffee ring stain (random position/size)
- ~20% chance of postal stamp on letters (random angle/position)
- ~15% chance of paper clip on documents (random horizontal position)

**Interaction:**
1. Click a lead card → it becomes selected (highlighted border, SFX: paper select)
2. Click again → deselect (SFX: paper deselect)
3. Only 1 lead can be selected at a time
4. Click INVESTIGATE → rubber stamp "ASSIGNED" flash → transition to interview

**Day Zero special:** A fly-in boss note modal appears centered on screen. Clicking it animates the note to the pinned position in the top bar, then reveals the regular desk.

### 3.3 Interview
The interview is the skill-expression core. Two questions, each with distinct strategic options.

**Layout: Two-panel design**
- **Left panel (180px):** NPC pixel art portrait, name, title, expression hint text, notesheet (notes accumulate as you gather information)
- **Right panel:** Story header (title + italic description), dialogue log (scrollable), question buttons

**Flow:**
1. NPC delivers opening line (typewritten word-by-word, ~100ms per word with SFX ticks)
2. "Start Interview" button appears
3. **Q1: Choose 1 of 4 archetype questions** — each styled with a colored dot
4. Your question appears in the dialogue log (right-aligned, dark background)
5. NPC types their Q1 response (NPC-styled, left-aligned, paper background)
6. Note is added to the notesheet on the left
7. Expression hint text updates
8. **Q2: Choose 1 of 3 follow-up questions** (specific to the Q1 path)
9. Your question appears
10. NPC types their Q2 response
11. **Feedback appears:** tier-colored border on NPC response, +points badge, feedback line, note with tier-colored dot, portrait tint overlay, body animation change
12. "Write article →" button appears
13. Click → rubber stamp "FILED" (green) → interview complete → passes result to main game loop

**Instant Perish:** Certain Q2 choices have a `perish: true` flag in the outcome. When triggered: the "Write article" button text becomes "...", clicking it plays the slam SFX, a red FIRED stamp flashes on screen, and after 600ms the game jumps straight to game over. The article is never written.

### 3.4 Sleep/Publish Screen
After the interview, the game skips the traditional headline selection and goes directly to a **sleep screen**:

- Shows mood text based on day and deficit delta
- Displays the deficit change (large number: +N green or -N red)
- "You gained ground" or "You fell behind" label
- Button: "Sleep → Next day" (or "See weekly results" on Day 5)
- SFX: relief (positive) or tension (negative)

### 3.5 Results Screen
Two-phase reveal for maximum tension:

**Phase 1: Your Story**
- Title: "DAY X — STORY FILED"
- Scoring breakdown: News value (4 dot meter, each dot = 2 pts) + Interview bonus (3 dot meter) = Your total
- "Go to sleep" button

**Phase 2: The Competition** (after clicking "Go to sleep")
- Side-by-side newspaper cards slide in: your Småstad Paper (left) vs Regionbladet (right)
- Each shows: masthead, headline, point score
- Competitor breakdown row appears
- Deficit update: animated "before → after" with colored numbers
- **Boss sticky note** flies in from the right: Gunnar's reaction quote (keyed to deficit severity, or story-specific override if the story has `boss_result_quotes`)
- Continue button: "Next day →" / "Final results"

### 3.6 Game Over: Perished
- Hard cut, flash overlay
- Perish soundtrack begins (loops at 0:18 mark)
- Title: "PERISHED" (slam SFX)
- Cold epilogue text (varies by days survived)
- Stats: DAYS, DEFICIT, POINTS
- "Try Again" button → returns to start screen

### 3.7 Game Over: Survived
- Perish/survive soundtrack plays
- Title: "SURVIVED" (slam SFX)
- Message varies by final deficit (from triumphant to barely made it)
- Gunnar epilogue: "You can stay. For now."
- Stats: DAYS (5), DEFICIT, POINTS, AVG
- "Play Again" button → returns to start screen
- Best score saved to localStorage

### 3.8 Town Advancement
When the player survives Day 5 of Småstad or Industristad:

1. **Survived screen** with stats and SURVIVED stamp
2. **Boss farewell cutscene** — 3-step sequence (warm → serious → intense) from the current boss, recommending the player to the next town
3. **Town advance** — New town’s onboarding sequence (boss introduction, context, threat)
4. **Day Zero** — 3 easy leads, restricted Q1 options, does not affect deficit
5. **State reset** — Deficit resets to 0, used story IDs cleared, boss quote pools refreshed. Completed town history is archived in `townHistory[]`.

Surviving the final town (Kuststad) triggers the full game-over survived screen with cumulative stats.

---

## 4. SCORING SYSTEM

### 4.1 Formula
```
Total Points = Base News Value + Tier Bonus
Tier Bonus = tier × 2
```

### 4.2 Base News Values (per story)
Stories have base values of 2-8, distributed across 120 stories (40 per town):

| Base Value | Småstad | Industristad | Kuststad | Total | Description |
|---|---|---|---|---|---|
| 2 pts | 7 | 7 | 7 | 21 | Filler: minor events, soft features |
| 3 pts | 3 | 3 | 3 | 9 | Small items |
| 4 pts | 9 | 9 | 9 | 27 | Decent: local disputes, small scandals |
| 5 pts | 7 | 7 | 7 | 21 | Good local issues |
| 6 pts | 6 | 6 | 6 | 18 | Strong investigations |
| 7 pts | 4 | 4 | 4 | 12 | Major revelations |
| 8 pts | 4 | 4 | 4 | 12 | Top: deaths, major corruption, cover-ups |

### 4.3 Tier System
Each interview resolves to a tier (0-3) based on the Q1→Q2 combination chosen:

| Tier | Bonus | Example (base 6) | Meaning |
|---|---|---|---|
| 0 | +0 | 6 pts | Base facts only |
| 1 | +2 | 8 pts | Basic additional info |
| 2 | +4 | 10 pts | Strong story with details |
| 3 | +6 | 12 pts | Full investigation uncovered |

**Total score range per day:** 2 (base-2, tier 0) to 14 (base-8, tier 3).

### 4.4 Deficit System
- Starts at 0
- Each day: `deficit = deficit + (player_score - competitor_score)`
- Deficit accumulates (can be negative or positive)
- **-10 or below = PERISHED** — immediate game over, no mercy

### 4.5 Deficit Severity (UI)
| Deficit Range | Severity | Color |
|---|---|---|
| > -3 | Safe | Green (#558844) |
| -3 to -7 | Warning | Amber (#cc8822) |
| -7 to -10 | Danger | Red (#cc2222) |

The deficit meter uses smooth color interpolation via `lerpColor()` — not discrete buckets.

### 4.6 Highscore System
- All completed runs (survived or perished) saved to localStorage
- Stores: name, points, deficit, days, survived boolean, ISO date
- Max 50 entries retained
- "Press Archive" modal on start screen shows all runs sorted by points descending

---

## 5. INTERVIEW SYSTEM (DETAIL)

### 5.1 Q1 Archetypes
Every story has exactly 4 opening question options, one per archetype:

| Archetype | CSS Color | Strategy |
|---|---|---|
| Friendly (Trust Builder) | Green `#558844` | Soft, empathetic opener. Low risk. |
| Direct (Neutral Fact-Find) | Amber `#cc8822` | Professional, non-threatening. Gets surface facts. |
| Pressure | Red `#cc2222` | Direct challenge. High risk, higher potential reward. |
| Silence | Blue `#4466aa` | Let them fill the void. Unpredictable. |

### 5.2 Q2 Follow-ups
After Q1, exactly 3 follow-up questions are shown (specific to the Q1 archetype chosen). These are hyper-specific to the story — they reference names, dates, locations, contradictions from the story world.

### 5.3 Lookup Table Resolution
Every Q1→Q2 combination maps to a fixed result via a deterministic lookup table:

```
story.interview.branches[q1_archetype].outcomes[q2_index]
→ { tier, response, expression, feedback, note }
```

**No runtime trust calculation. No hidden state. Content IS the logic.**

- 4 Q1 archetypes × 3 Q2 options = **12 unique paths per story**
- 120 stories × 12 paths = **1,440 total interview outcomes** in the game

### 5.4 Interview Feedback System
After Q2 resolves, the player receives multi-channel feedback:

**Channel A — Notes (left panel):**
- Note dots are colored by tier: grey (T0) → olive (T1) → green (T2) → dark green (T3)
- Tier 2-3 notes use stars (★) instead of bullets (•)
- Tier 2-3 note text gets an underline decoration

**Channel B — Chat (right panel):**
- NPC response border color changes by tier (grey → olive → green → dark green)
- Points badge (+N) floats top-right of the NPC response bubble
- Italic feedback line appears below (e.g., "He's opening up — the story runs deeper than safety records.")

**Channel C — Portrait (left panel):**
- Expression tint overlay: warm green (open/grateful), cool blue (guarded/nervous), red (hostile/defiant)
- Body animation changes: nervous = fast shimmer, hostile = slow rise, open = gentle sway
- Expression hint text updates (e.g., "Looks relieved, opening up")

### 5.5 NPC Expression States
Used in expression hint text and animation:

| Expression | Hint Text | Tint | Body Animation |
|---|---|---|---|
| open | "Looks relieved, opening up" | warm green | gentle sway |
| grateful | "Seems grateful" | warm green | gentle sway |
| guarded | "Arms crossed, skeptical" | cool blue | default idle |
| nervous | "Uneasy, looking around" | cool blue | fast shimmer |
| hostile | "Angry, wants to end the conversation" | red | slow rise |
| defiant | "Defiant, chin raised" | red | slow rise |
| neutral | "Hard to read" | none | default idle |

### 5.6 Instant Perish
Some Q2 outcomes carry a `perish: true` flag. When the player triggers one:

1. NPC delivers the Q2 response (typewritten as normal)
2. The "Write article" button text becomes `...` (ominous)
3. Player clicks → slam SFX plays
4. Red **FIRED** stamp flashes on screen (same stamp animation as ASSIGNED/FILED, but red `stamp-flash red` class)
5. After 600ms delay, game jumps to game-over screen (perished path)

The article is never filed. This mechanic enforces the game's core tension: certain lines of questioning aren't just ineffective — they end your career.

---

## 6. COMPETITOR AI

Each town has its own competitor newspaper, with town-specific score ranges and headlines.

| Town | Competitor | Focus |
|---|---|---|
| Småstad | Regionbladet | Municipal/civic stories |
| Industristad | Fabriksbladet | Labor & industrial stories |
| Kuststad | Sjöfartstidningen | Maritime & shipping stories |

### 6.1 Score Generation
Competitor score is random within day-specific ranges, per town:

**Småstad (Regionbladet):**
| Day | Min | Max |
|---|---|---|
| 1 | 6 | 9 |
| 2 | 7 | 10 |
| 3 | 8 | 11 |
| 4 | 8 | 12 |
| 5 | 9 | 12 |

**Industristad (Fabriksbladet):**
| Day | Min | Max |
|---|---|---|
| 1 | 7 | 10 |
| 2 | 8 | 11 |
| 3 | 8 | 12 |
| 4 | 9 | 12 |
| 5 | 9 | 13 |

**Kuststad (Sjöfartstidningen):**
| Day | Min | Max |
|---|---|---|
| 1 | 7 | 10 |
| 2 | 8 | 11 |
| 3 | 9 | 12 |
| 4 | 9 | 13 |
| 5 | 10 | 13 |

Difficulty escalates across towns: Småstad averages ~8-10 pts/day, Industristad ~9-11, Kuststad ~10-12.

### 6.2 Competitor Headlines
Generated as flavor text based on score, from town-specific headline pools:
- **Score ≥ 11:** Strong headlines (town-themed investigations/exposés)
- **Score 8-10:** Average headlines (routine beat coverage)
- **Score < 8:** Weak headlines (soft features)

---

## 7. BOSS SYSTEM

Each town has its own editor-in-chief. They appear in desk notes, result quotes, game-over text, onboarding, and farewell sequences.

| Town | Boss | Personality |
|---|---|---|
| Småstad | Gunnar Ek | Gruff, self-preserving, cold |
| Industristad | Birgit Ståhl | Stern, demanding, methodical |
| Kuststad | Ragnar Sjöberg | Weathered, terse, pragmatic |

### 7.1 Desk Notes (Morning)
A sticky note pinned on the desk, refreshed daily. Drawn from per-town pools to avoid repeats within a run.

| Condition | Pool |
|---|---|
| Day 1 | "Welcome, {name}. Prove I didn't make a mistake." |
| Day 2-5 | 3 quotes per day pool |
| Deficit ≤ -5 (warning) | 3 warning quotes |
| Deficit ≤ -10 (danger) | 3 danger quotes (overrides day pool) |
| Default fallback | "Deliver." / "Get to work." / "Stories don't write themselves, {name}." |

### 7.2 Result Quotes (End of Day)
Boss reaction on the results screen, shown as a yellow sticky note that flies in.

| Deficit Range | Pool |
|---|---|
| ≤ -12 | critical (4 quotes) |
| -8 to -12 | bad (4 quotes) |
| -3 to -8 | warning (4 quotes) |
| -3 to +2 | neutral (4 quotes) |
| ≥ +2 | good (4 quotes) |
| (also: great pool) | 4 quotes for strong leads |

### 7.3 Story-Specific Boss Quotes
Some stories (e.g., the wolf hunt "vargjakten") have a `boss_result_quotes` field with `positive` and `negative` arrays. If present, tier 0-1 uses `positive` quotes and tier 2-3 uses `negative` quotes. These override the default deficit-keyed quotes.

### 7.4 Game Over Reactions
- **Fired:** "Pack your things, {name}. I already called the temp agency."
- **Survived (barely):** "You survived the week, {name}. Barely."
- **Survived (decent):** "Not bad for a Stockholm kid."
- **Survived (dominant):** "Hmm. Maybe I was wrong about you."

All boss text supports `{name}` placeholder replacement with the player's entered name.

### 7.5 Town-Specific Boss Dialogue Pools
All boss dialogue (desk notes, result quotes, game-over text, onboarding) is stored per-town in `boss-dialogue.json`. Each town’s boss has unique pools:

- **Småstad (Gunnar):** Desk notes reference local civic concerns, survival tone
- **Industristad (Birgit):** Desk notes reference factory output, labor disputes, corporate pressure
- **Kuststad (Ragnar):** Desk notes reference maritime commerce, harbor politics, weather

### 7.6 Farewell Sequences
When the player survives a non-final town, the boss delivers a 3-step farewell cutscene:

| Step | Expression | Content |
|---|---|---|
| 1 | warm | Acknowledges the player's work |
| 2 | serious | Explains the next town's challenges |
| 3 | intense | Recommends player to the next boss |

Farewell dialogue is stored in `towns.json` under each town’s `farewellSequence` array.

---

## 8. ALL SCREENS & UI

### 8.1 Persistent HUD Bar
Visible on desk, interview, publish, and results screens. Sits above the 640×360 canvas.

**Components (left to right):**

1. **Game Clock** — Shows time and phase:
   - Desk: 08:15 Morning
   - Interview: 12:00 Midday
   - Publish: 16:00 Afternoon
   - Sleep: 22:00 Evening
   - Results: 23:00 Night

2. **Week Strip** — 5 day slots (MON-FRI):
   - Current day: highlighted
   - Past days: marked completed with color (green=won, red=lost, neutral=tied)
   - Future days: plain

3. **Deficit Meter** — Shows:
   - "DEFICIT" label
   - Horizontal fill bar (width = % of -10 threshold)
   - Numeric value (color-interpolated)
   - Distance-to-perish message: "X from perishing"
   - Warning/danger classes on the fill bar

4. **Town Name** — Current town displayed in the HUD (e.g., "Småstad", "Industristad", "Kuststad")

### 8.2 Screen: Start
- Brown desk background
- Large title "PRESS OR PERISH" — clickable to start music
- After click: title settles, menu slides in with New Game, Continue (if save exists), Tutorial, Highscores buttons
- Best score display if exists
- Byline: "Created by Peter Hang."

### 8.3 Screen: Onboarding
- Sequential cards rendered in a container
- 13-step sequence (see §2.2)
- Boss steps reuse the same portrait frame
- Title card: staggered word reveal (0.6s apart), slam SFX per word, fade out after 1.5s hold

### 8.4 Screen: Day Transition
- Dark background
- Day number (large), day name, date
- Deficit value (Day 2+) with interpolated color
- Mood text (varies by deficit severity)
- Auto-advances after 3 seconds

### 8.5 Screen: Desk
- Full desk layout (see §3.2)
- Town-specific silhouette window, boss note, 8 lead cards, action bar
- Town theming applied via `#screen-desk.town-{id}` CSS classes (see §10.7)

### 8.6 Screen: Interview
- Two-panel layout (see §3.3 and §5)
- Left: portrait, info, notesheet
- Right: story header, dialogue log, question buttons

### 8.7 Screen: Publish/Sleep
- Dual-purpose screen
- Currently used only for sleep phase (headline auto-selected)
- Shows deficit change, mood text, continue button
- Has a full publish UI (headline choices, newspaper preview) that is wired but bypassed in current flow

### 8.8 Screen: Results
- Two-phase reveal (see §3.5)
- Phase 1: scoring breakdown
- Phase 2: newspaper comparison, deficit update, boss quote sticky note
- Staggered animations: your paper (0ms) → competitor paper (600ms) → bottom section (1200ms) → boss note (1800ms)

### 8.9 Screen: Game Over
- Shared screen for both Perished and Survived
- Different styling (`.gameover-survive` class toggles warm vs cold aesthetic)
- Stats grid: Days, Deficit, Points (+ AVG for survived)
- Epilogue text varies by days survived and deficit
- Restart button returns to start screen with title music

### 8.10 Shared UI Components
- **Rubber Stamp Flash:** CSS animation (scale-in bounce, rotate -8°, fade out). Used on desk (ASSIGNED), interview (FILED), and game over.
- **Film Grain Overlay:** SVG fractal noise at 2.5% opacity over the entire canvas, `mix-blend-mode: overlay`.
- **Flash Overlay:** Brief white/amber flash on screen transitions (300ms).
- **Typewriter Cursor:** Blinking block cursor (█) during word-by-word text reveal.
- **btn-paper:** Shared button style — paper-colored, raised shadow, physical push-in on click.

### 8.11 Screen: Farewell
- Triggered after surviving a non-final town
- 3-step boss dialogue cutscene (reuses onboarding portrait frame layout)
- Each step has expression hint (warm → serious → intense)
- Boss recommends player to next town's editor
- Advances to town-advance screen on completion

### 8.12 Screen: Town Advance
- New town’s onboarding sequence: boss introduction, context, threat
- Uses the same rendering system as §8.3 Onboarding
- Auto-transitions to Day Zero of the new town

---

## 9. AUDIO SYSTEM

### 9.1 Soundtrack (3 MP3 tracks)
Managed by `audio-manager.js`. Only one track plays at a time with crossfade.

| Track | File | Volume | Loop | Usage |
|---|---|---|---|---|
| title | `audio/soundtrack.mp3` | 0.30 | Full loop | Start screen |
| game | `audio/Soundtrack_Ingame.mp3` | 0.25 | Full loop | All gameplay (desk → interview → publish → results) |
| perish | `audio/Soundtrack_perishscreen.mp3` | 0.35 | Loops at 0:18 | Game over (both perished and survived) |

**Features:**
- 3-second fade in/out between tracks
- Mute state persisted in localStorage (`pop_muted`)
- Autoplay retry on user interaction (handles browser autoplay blocking)
- Game track resumes seamlessly after town-advance sequences (no restart)

### 9.2 SFX (12 synthesized sounds)
All SFX are generated in real-time via **Web Audio API** — zero audio files. A-minor harmonic base with ±5% pitch randomization.

| Sound | Duration | Description | Used For |
|---|---|---|---|
| tick | 15ms | Filtered noise burst | Typewriter word-by-word |
| click | 30ms | Sine pitch drop (A5→A4) | Button presses |
| select | 120ms | Bandpass noise + low thud | Picking up lead card |
| deselect | 80ms | Lower-band noise thump | Putting card back |
| stamp | 200ms | Heavy impact: low sine + ink noise | ASSIGNED / FILED / PRESS stamps |
| note | 80ms | Pen scratch noise | Note appearing on notesheet |
| reveal | 400ms | Sawtooth bloom (A2→A3) | Newspaper card slide-in |
| tension | 300ms | Sub-bass throb (D2) | Negative deficit change |
| relief | 250ms | Major arpeggio (A4→C#5→E5) | Positive deficit change |
| slam | 150ms | Square wave + noise hit (E2) | PERISHED, SURVIVED, title words |
| ambientTick | 20ms | Very quiet high ping (A6) | Day transition |
| reject | 100ms | Downward buzz (A3→A2) | Rejection letters in onboarding |

---

## 10. VISUAL DESIGN & ART STYLE

### 10.1 Resolution & Rendering
- Fixed 640×360 canvas
- CSS-scaled to browser: `transform: scale(var(--scale))` calculated as `min(innerWidth/640, innerHeight/394)`
- `image-rendering: pixelated` globally for crisp pixel art
- All user selection disabled (`user-select: none`)

### 10.2 Color Palette
```
Paper & Ink:
  --paper:        #e8dfc8   (warm cream)
  --paper-aged:   #d4c9a8   (yellowed)
  --paper-dark:   #c4b898   (darker aged)
  --ink:          #1a1208   (near-black brown)
  --ink-faded:    #4a3f28   (sepia)
  --ink-light:    #6b5f45   (light sepia)
  --ink-red:      #8b1a1a   (dark red)

Desk & Environment:
  --desk:         #2a1f12   (dark walnut)
  --desk-light:   #3d2e1a   (lighter wood)
  --desk-surface: #352816   (mid wood)
  --lamp:         #f5e4a0   (warm lamp yellow)
  --lamp-dim:     #d4c080   (dimmer lamp)

UI Accents:
  --deficit-red:  #cc2222
  --deficit-warn: #cc8822
  --deficit-safe: #558844
  --highlight:    #f0d060
  --selected:     #d4a840

Question Colors:
  --q-friendly:   #558844 (green)
  --q-direct:     #cc8822 (amber)
  --q-pressure:   #cc2222 (red)
  --q-silence:    #4466aa (blue)
```

### 10.3 Typography
| Font | CSS Variable | Usage |
|---|---|---|
| Special Elite | `--font-headline` | Mastheads, headings, handwritten notes, stamps |
| Courier Prime | `--font-body` | Body text, UI labels, dialogue, notepad |
| Bebas Neue | `--font-numbers` | Large numbers: deficit, scores, day numbers |
| Playfair Display 700/900 | (inline) | Newspaper mastheads on results screen |
| Oswald 500/700 | (inline) | Supplementary heading weight |

### 10.4 Pixel Art Sprite System
NPC portraits are **CSS pixel art** — no images. Each sprite is defined as an array of positioned `<div>` elements.

**Grid:** 15×20 units at 8px per unit = 120×160px portrait
**Method:** Absolutely-positioned `<div class="p">` elements with color classes

**Color classes:**
- Skin tones: `.s-light` `.s-mid` `.s-worn` `.s-pale` `.s-dark`
- Hair: `.h-dark-brown` `.h-brown` `.h-grey` `.h-silver` `.h-blonde` `.h-black`
- Eyes: `.e-dark` `.e-blue` `.e-green` `.e-white`
- Clothes: `.c-worker-blue` `.c-suit-dark` `.c-cardigan-wine` `.c-shirt-check` etc.
- Accessories: `.x-bandage` `.x-tie-red` `.x-glasses` `.x-badge` `.x-sweat` `.x-blush` etc.

**Animations:**
- **Idle sway:** 4s ease-in-out infinite — subtle 1px x/y shifts
- **Eye blink:** 4s cycle — double blink at 94-99% marks
- **Expression animations:** `.anim-nervous` (fast shimmer), `.anim-hostile` (slow rise), `.anim-open` (gentle sway)

**84 NPCs** have full pixel art sprite definitions in `npc-sprites.js` (1202 lines).

### 10.5 Window Background
The desk window shows a **town-specific silhouette** (determined by `currentTown`):

- CSS gradient sky (shifts by time of day: morning blue-grey → afternoon amber → evening dark)
- Town silhouette built with `clip-path: polygon(...)`
- Tiny lit window/light dots as radial gradients
- Town-specific animated effects (see §10.7)

### 10.6 Transitions
- **Hard cuts** between screens — no fades (Papers Please style)
- Brief flash overlay (300ms white/amber) on major transitions
- Staggered slide-in animations on results screen

### 10.7 Town Visual Identity
Each town has a comprehensive visual identity applied via CSS class `.town-{id}` on the desk screen:

**Småstad (small town):**
- Desk surface: warm brown wood
- Wall/frame: warm beige/cream, wood-colored frame
- Skyline: residential silhouette (church spire, marketplace, small office buildings)
- Window lights: warm yellow lamp glow
- Lead cards: warm cream paper with coffee ring stains
- Sky gradients: gentle warm morning → amber afternoon → cozy evening

**Industristad (industrial town):**
- Desk surface: cold steel-grey metal-toned wood
- Wall/frame: dark industrial concrete, steel-grey frame
- Skyline: factory chimneys, paper mill, smokestacks, storage silos, crane structures
- **Animated effects:** 6 chimney smoke wisps (varying animation delays 2.6–3.6s)
- Window lights: orange/amber furnace glow
- Lead cards: cooler newsprint-grey with "HEMLIGT" (classified) stamps
- Boss note: cooler tan tint (Birgit’s style)
- Sky gradients: hazy/polluted greys and browns

**Kuststad (coastal harbor town):**
- Desk surface: weathered salt-bleached coastal wood (cool grey-green)
- Wall/frame: dark coastal concrete, weathered salt-stained frame
- Skyline: rocky shore, fishing boats/masts, harbor cranes, lighthouse, warehouses, cargo ships, fishing huts
- **Animated effects:** 4 harbor wave layers (translateX oscillation, 3.5–4.6s)
- Window lights: navigation lamps, ship portholes, lighthouse beam (warm/red)
- Lead cards: weathered sea-mist paper (pale grey-blue)
- Sky gradients: cold North Sea fog, blues and greys

Each town overrides: desk surface color, wall color, window frame, sky gradients (×3 time-of-day), clip-path silhouette, animated effects, light positions, lead card paper color, button accent color, and boss note tint.

---

## 11. CONTENT INVENTORY

### 11.1 Stories: 120 total (40 per town)

**Per-town category breakdown:**

| Category | Småstad | Industristad | Kuststad | Total |
|---|---|---|---|---|
| Human Interest | 11 | — | — | 11+ |
| Corruption | 10 | — | — | 10+ |
| Crime | 7 | — | — | 7+ |
| Breaking News | 7 | — | — | 7+ |
| Labor | 5 | 13 | — | 18+ |
| Environment | — | 7 | — | 7+ |
| Politics | — | 2 | — | 2+ |
| Other (finance, housing, welfare, health) | — | 4 | — | 4+ |

*(Industristad and Kuststad use additional categories: environment, politics, finance, housing, welfare, health.)*

**Per-town difficulty breakdown:**

| Difficulty | Per Town (target) |
|---|---|
| Easy | ~17 |
| Medium | ~12 |
| Hard | ~11 |

**Per-town base value breakdown:**

| Base Value | Per Town | ×3 Towns |
|---|---|---|
| 2 | 7 | 21 |
| 3 | 3 | 9 |
| 4 | 9 | 27 |
| 5 | 7 | 21 |
| 6 | 6 | 18 |
| 7 | 4 | 12 |
| 8 | 4 | 12 |

**Per story content:**
- Title, description, lead text, preview text
- **Town assignment** (smastad / industristad / kuststad)
- Source type (letter / document / street)
- Difficulty (easy / medium / hard), base value (2-8), category
- NPC reference (npc_id, npc_name, npc_title)
- Interview: opening line + 4 Q1 options + 4 branches (each with Q1 response, expression hint, Q1 note, 3 Q2 options, 3 outcomes)
- Headlines: 4 tiers × 3 options each (text + tone)
- Optional: `boss_result_quotes` with positive/negative arrays
- Optional: `perish: true` on specific Q2 outcomes (instant-perish trigger)

### 11.2 NPCs: 84
Each NPC has:
- id, name, role, age
- default_expression, expressions array
- unique_detail (e.g., bandaged_hand, glasses)
- clothing_color (CSS class reference)
- initial_demeanor (hint text when interview starts)

### 11.3 Boss Dialogue (per town)
Each town's boss has independent dialogue pools in `boss-dialogue.json`:
- Desk notes: day-specific pools (3 per day), warning pool (3), danger pool (3), default pool (3)
- Result quotes: critical (4), bad (4), warning (4), neutral (4), good (4), great (4)
- Game over: fired text, survived text (barely/decent/dominant)
- Onboarding: intro, rules, threat, start

× 3 towns = 3 complete boss dialogue sets.

### 11.4 Day Distribution
Lead generation per day (how many from each difficulty pool), same pattern per town:

| Day | Easy | Medium | Hard | Character |
|---|---|---|---|---|
| 1 | 6 | 2 | 0 | Gentle start |
| 2 | 5 | 2 | 1 | Warming up |
| 3 | 2 | 4 | 2 | Mix |
| 4 | 1 | 2 | 5 | Getting hard |
| 5 | 0 | 2 | 6 | Final push |

Stories are never repeated within a town run (`usedStoryIds` tracked per town, reset on town advance).

### 11.5 Achievements: 50 total (5 categories)

| Category | Count | Examples |
|---|---|---|
| Milestones | 9 | first_byline, survived, press_master, overqualified, front_page_material |
| Interview Mastery | 8 | soft_touch, silent_treatment, full_arsenal, hidden_gem, bulldozer |
| Survival | 8 | clean_sweep, comeback_king, perfect_week, veteran (10 weeks), photo_finish |
| Stories | 12 | stop_the_presses, follow_the_money, pumpkin_pulitzer, journalism_at_its_best |
| Rookie Mistakes | 8 | five_zeroes, wrong_crowd, speedrun, silence_is_awkward |

Achievements are stored in localStorage as `pop_achievements` (JSON array of unlocked achievement IDs). A trophy button in the persistent UI opens the achievements modal showing all 50 with locked/unlocked state.

---

## 12. DATA SCHEMAS (COMPLETE)

### 12.1 stories.json — Array of 120 Story objects (40 per town)

```json
{
  "id": "string",
  "town": "smastad|industristad|kuststad",
  "title": "string",
  "description": "string",
  "lead_text": "string",
  "preview": "string",
  "source_type": "letter|document|street",
  "difficulty": "easy|medium|hard",
  "base_value": 2-8,
  "category": "labor|crime|corruption|human_interest|breaking_news|environment|politics|finance|housing|welfare|health",
  "npc_id": "string",
  "npc_name": "string",
  "npc_title": "string",
  "interview": {
    "opening_line": "string",
    "q1_options": [
      {
        "archetype": "friendly|direct|pressure|silence",
        "text": "string"
      }
    ],
    "branches": {
      "friendly": {
        "q1_response": "string",
        "expression_hint": "string",
        "q1_note": "string",
        "q2_options": [
          { "text": "string" }
        ],
        "outcomes": [
          {
            "tier": 0-3,
            "response": "string",
            "expression": "string",
            "feedback": "string",
            "note": "string"
          }
        ]
      },
      "direct": { "..." },
      "pressure": { "..." },
      "silence": { "..." }
    }
  },
  "headlines": {
    "tier_0": [
      { "text": "string", "tone": "string" }
    ],
    "tier_1": ["..."],
    "tier_2": ["..."],
    "tier_3": ["..."]
  },
  "boss_result_quotes": {
    "positive": ["string"],
    "negative": ["string"]
  }
}
```

### 12.2 npcs.json — Array of 84 NPC objects

```json
{
  "id": "string",
  "name": "string",
  "role": "string",
  "age": "number",
  "default_expression": "string",
  "expressions": ["string"],
  "unique_detail": "string",
  "clothing_color": "string",
  "initial_demeanor": "string"
}
```

### 12.3 boss-dialogue.json (per-town structure)

```json
{
  "smastad": {
    "desk_notes": {
      "day_1": "string",
      "day_2": ["string"],
      "day_3": ["string"],
      "day_4": ["string"],
      "day_5": ["string"],
      "warning": ["string"],
      "danger": ["string"],
      "default": ["string"]
    },
    "result_quotes": {
      "critical": ["string"],
      "bad": ["string"],
      "warning": ["string"],
      "neutral": ["string"],
      "good": ["string"],
      "great": ["string"]
    },
    "gameover_fired": {
      "text": "string",
      "name": "Gunnar Ek"
    },
    "gameover_survived": {
      "barely": "string",
      "decent": "string",
      "dominant": "string",
      "name": "Gunnar Ek"
    },
    "onboarding": {
      "intro": "string",
      "rules": "string",
      "threat": "string",
      "start": "string"
    }
  },
  "industristad": { "...same structure, Birgit Ståhl..." },
  "kuststad": { "...same structure, Ragnar Sjöberg..." }
}
```

### 12.4 Game State (runtime, not persisted to file)

```json
{
  "phase": "start|onboarding|transition|desk|interview|publish|sleep|results|gameover",
  "day": 0-5,
  "deficit": "number",
  "currentTown": "smastad|industristad|kuststad",
  "townIndex": 0-2,
  "townHistory": [{ "townId", "deficit", "dayHistory", "survived": true }],
  "todayLeads": ["storyId"],
  "selectedLead": "storyId|null",
  "interviewPhase": 0-2,
  "q1Choice": "archetype|null",
  "q2Choice": "index|null",
  "tierReached": 0-3,
  "pointsEarned": "number",
  "headlineChosen": "number|null",
  "competitorScore": "number",
  "dayHistory": [{ "day", "storyId", "tier", "points", "competitorScore", "deficit", "headline" }],
  "usedStoryIds": ["string"],
  "usedBossQuotes": ["string"],
  "usedBossNotes": ["string"],
  "runNumber": "number",
  "bestScore": "number",
  "playerName": "string"
}
```

### 12.5 localStorage Keys

| Key | Type | Description |
|---|---|---|
| `pop_muted` | "true"/"false" | Audio mute preference |
| `pop_player_name` | string | Last entered player name |
| `pop_run_count` | number | Total runs started |
| `pop_best_score` | number | Highest total score across all runs |
| `pop_highscores` | JSON array | All completed run records (max 50) |
| `pop_save` | JSON object | Saved game state (full state snapshot for resume) |
| `pop_achievements` | JSON array | Unlocked achievement IDs |

### 12.6 towns.json — Array of 3 Town objects

```json
{
  "id": "smastad|industristad|kuststad",
  "name": "string",
  "order": 0-2,
  "newspaper": "string",
  "competitorName": "string",
  "bossName": "string",
  "perishThreshold": -10,
  "dayZeroDate": "string (e.g., November 10, 1974)",
  "dates": { "1": "string", "2": "string", "3": "string", "4": "string", "5": "string" },
  "competitorScoreRanges": {
    "1": { "min": "number", "max": "number" },
    "2": { "min": "number", "max": "number" },
    "3": { "min": "number", "max": "number" },
    "4": { "min": "number", "max": "number" },
    "5": { "min": "number", "max": "number" }
  },
  "competitorHeadlines": {
    "strong": ["string"],
    "average": ["string"],
    "weak": ["string"]
  },
  "farewellSequence": [
    { "text": "string", "expression": "warm|serious|intense" }
  ]
}
```

### 12.7 Save Data Schema (`pop_save`)

The save is a full snapshot of the game state object (§12.4), written to localStorage after each completed day (skipping Day Zero). On resume, the state is restored and the game continues from the last completed phase. v1 saves (pre-town) are auto-migrated to v2 format on load.

---

## 13. TECHNICAL ARCHITECTURE

### 13.1 Stack
- **Language:** Vanilla JavaScript (ES6 modules, `import`/`export`)
- **Markup:** Single `index.html` with empty screen containers
- **Styling:** 10 CSS files, CSS custom properties, no preprocessor
- **Build:** Zero build tools, zero frameworks, zero dependencies
- **Data:** JSON files fetched at runtime (stories, NPCs, boss dialogue, towns)
- **Audio:** 3 MP3 soundtrack files + Web Audio API synthesized SFX
- **Hosting:** Firebase Hosting (static files)

### 13.2 Architecture Pattern
Clean separation between engine (pure logic) and UI (DOM rendering):

```
index.html          ← Single HTML file, loads main.js as ES module
    ↓
js/main.js          ← Entry point, game loop, screen wiring, boot()
    ↓
js/engine/*         ← Pure game logic (zero DOM access, portable to Godot)
js/ui/*             ← DOM rendering, event handling, animations
data/*              ← JSON content files (stories, NPCs, boss dialogue, towns)
css/*               ← 10 modular CSS files
audio/*             ← 3 MP3 soundtrack files
```

### 13.3 Engine ↔ UI Separation
**Engine modules** (`js/engine/`) are pure functions — no `document`, no `window`, no DOM. They could be ported to GDScript for a Godot migration.

**UI modules** (`js/ui/`) create and manipulate DOM elements, handle events, and call engine functions for game logic.

**Data flow:** `main.js` orchestrates everything — it calls engine functions for logic, UI functions for rendering, and passes data between them.

### 13.4 Achievements System
- **Engine:** `js/engine/achievements.js` — defines all 44 achievements with trigger conditions, checks against game state
- **UI:** `js/ui/achievements-ui.js` — renders achievement modal, trophy button, unlock toast notifications
- **Storage:** `pop_achievements` in localStorage (JSON array of unlocked IDs)
- **Triggers:** Checked at key game events (day end, interview complete, game over, town advance)

### 13.5 Save/Resume System
- **Save:** `GameState.saveToLocalStorage()` writes full state snapshot to `pop_save` after each completed day (skips Day Zero)
- **Load:** `GameState.loadFromLocalStorage()` reads and returns saved state
- **Restore:** `GameState.restoreFromSave()` merges save into active state, with v1→v2 migration for pre-town saves
- **Continue button** on start screen: only visible when `hasSave()` returns true

### 13.6 Content Validation Tools
Python 3 scripts in `tools/` for automated quality checks (stdlib only, no dependencies):
- `validate.py` — structural validation of stories.json (tier distributions, headline counts, base value spread)
- `audit_text_lengths.py` — checks all lead_text and description fields against character limits
- `audit_prd.py` — validates PRD claims against actual codebase (story counts, file inventories, achievement totals)

---

## 14. FILE-BY-FILE REFERENCE

### 14.1 Root Files

| File | Purpose |
|---|---|
| `index.html` | Single-page HTML. Contains HUD bar structure, 8 empty screen divs, flash overlay. Loads all CSS and main.js. |
| `firebase.json` | Firebase Hosting config. Serves from root, ignores infra/docs. |
| `PRD.md` | This document |
| `ROADMAP.md` | Future feature plans |

### 14.2 JavaScript — Engine (`js/engine/`)

| File | Lines | Exports | Description |
|---|---|---|---|
| `game-state.js` | ~208 | `createState()`, `resetDay()`, `recordDay()`, `isPerished()`, `hasSurvived()`, `advanceToNextTown()`, `saveToLocalStorage()`, `loadFromLocalStorage()`, `clearSave()`, `hasSave()`, `restoreFromSave()` | Central state object with town progression (currentTown, townIndex, townHistory). Save/restore system with v1→v2 migration. Perish threshold = -10. |
| `day-generator.js` | ~105 | `generateDayZeroLeads()`, `generateDayLeads()` | Day Zero: 3 easy leads (1 per source type). Days 1-5: 8 leads from difficulty pools (see §11.4). Fisher-Yates shuffle. Avoids used story IDs. Town-scoped story filtering. |
| `interview-engine.js` | ~88 | `getQ1Options()`, `getQ2Options()`, `resolveInterview()`, `getHeadlines()` | Lookup table reader. resolveInterview returns { tier, points, response, expression, feedback, note, perish }. Points = base_value + (tier×2). |
| `scoring-engine.js` | ~72 | `calculatePoints()`, `calculateDeficitDelta()`, `applyDeficit()`, `getDeficitSeverity()`, `getDeficitFillPercent()`, `getPerishDistance()` | All math functions. Deficit threshold = -10. Severity: safe (>-3), warning (-3 to -7), danger (<-7). |
| `competitor-ai.js` | ~92 | `generateCompetitorScore()`, `getCompetitorHeadline()`, `getCompetitorName()` | Per-town competitor with town-specific score ranges and headline pools. Uses townConfig for all values. |
| `data-loader.js` | ~99 | `loadAllData()`, `loadStories()`, `loadNPCs()`, `loadBossDialogue()`, `loadTowns()`, `getStory()`, `getNPC()`, `getTownConfig()`, `getNextTown()`, `getStoriesByTown()` | Fetches and caches all JSON data. Parallel Promise.all loading. Town-aware filtering and lookup. |
| `audio-manager.js` | ~190 | `play()`, `stop()`, `retryPlay()`, `toggleMute()`, `isMuted()`, `getActiveTrack()` | Multi-track audio with 3-second crossfade. Perish track custom loops at 18s via timeupdate event. Mute persisted to localStorage. |
| `sfx-engine.js` | ~416 | `play()`, `warmUp()` | 12 synthesized SFX via Web Audio API. All real-time generated. Catalogue: tick, click, select, deselect, stamp, note, reveal, tension, relief, slam, ambientTick, reject. |
| `achievements.js` | ~309* | `CATEGORIES`, `getAll()`, `getTotal()`, `loadUnlocked()`, `saveUnlocked()`, `checkAchievements()` | 44 achievement definitions across 5 categories. Trigger-based checking at game events. localStorage persistence. |

### 14.3 JavaScript — UI (`js/ui/`)

| File | Lines | Exports | Description |
|---|---|---|---|
| `screen-manager.js` | ~99 | `init()`, `switchTo()`, `getCurrent()`, `flash()` | Manages screen divs. Hard cut transitions (no fades). Show/hide via `.active` class. Toggles HUD bar visibility. Flash overlay for emphasis. |
| `onboarding.js` | ~716 | `start()`, `getPlayerName()`, `startFarewell()` | 13-step narrative sequence. Handles diploma (name input), job ads, rejections, acceptance, boss meeting, title card. Also handles farewell cutscenes between towns and new-town onboarding. |
| `desk-screen.js` | ~422 | `render()` | Renders 8 lead cards with source badges, headlines, lead text, NPC info. Card flair system (coffee stains, stamps, clips). Selection/deselection with SFX. INVESTIGATE stamp. Day Zero fly-in boss note modal. Town-specific CSS class application. |
| `interview-screen.js` | ~659 | `start()` | Full interview flow: Q1→Q2→result. Typewriter dialogue system. Notesheet with tier-colored dots. Feedback system: tier borders, points badges, feedback lines. Portrait tint and body animation. Instant-perish handling (FIRED stamp). |
| `publish-screen.js` | ~218 | `render()`, `showSleep()` | Headline selection (currently bypassed by main.js — auto-picks first headline). Sleep phase: deficit change display, mood text, continue button. Per-town date display. |
| `results-screen.js` | ~358 | `render()` | Two-phase reveal. Phase 1: scoring breakdown with dot meters. Phase 2: side-by-side newspaper comparison (per-town mastheads), deficit update, boss sticky note fly-in. Staggered animations. |
| `transition-screen.js` | ~144 | `show()` | Day header with day number, name, date, deficit color, mood text. 3-second auto-advance. Town-aware date display. |
| `gameover-screen.js` | ~227 | `showPerished()`, `showSurvived()` | Both endings. Stats grid. Cold epilogue text. Perished: varies by days survived. Survived: varies by deficit severity. Town-advance callback for non-final towns. |
| `components.js` | ~133 | `buildWeekStrip()`, `updateWeekStrip()`, `updateDeficitMeter()`, `updateClock()`, `updateWindowSky()`, `getDeficitColor()` | Persistent HUD updates. Deficit color interpolation (lerpColor between RGB values). Week strip day coloring. Clock phase mapping. |
| `npc-sprites.js` | ~1202 | `renderSprite()` | 84 CSS pixel art NPC definitions. Each sprite = array of {x,y,w,h,cls,style} pixel blocks. Renders as absolutely-positioned divs inside a 120×160 container. Includes sprite-body wrapper for animations. |
| `achievements-ui.js` | ~309 | `addAchievementButton()`, `showAchievements()`, `showUnlockToast()` | Trophy button, achievements modal (grid of 44 achievements with locked/unlocked state), unlock toast notification. |

### 14.4 JavaScript — Main

| File | Lines | Description |
|---|---|---|
| `main.js` | ~1148 | Entry point. `boot()` initializes everything: scales canvas, loads data, wires start screen buttons (New Game, Continue, Tutorial), builds HUD. Game flow functions: `startNewRun()`, `startTutorial()`, `resumeSavedGame()`, `startDayZero()`, `startDay()`, `showDesk()`, `startInterview()`, `showPublish()`, `showResults()`, `showGameOver()`, `showEnding()`, `showSurvivedThenAdvance()`, `showTownAdvance()`. Town-aware functions: `getTownConfig()`, `getBossDialogue()`, `getTownStories()`. Boss quote logic: `getBossNote()`, `getBossQuote()`, `getStoryBossQuote()`. Utility: name prompt modal, highscore board, mute button, `pickUnused()` for avoiding repeat quotes, `injectName()` for {name} replacement. |

### 14.5 CSS Files

| File | Purpose |
|---|---|
| `variables.css` (~314 lines) | CSS custom properties, reset, game wrapper/canvas scaling, screen management, flash overlay, shared button styles, stamp animation, film grain overlay, cursor styles, typewriter cursor |
| `components.css` | HUD bar, deficit meter, week strip, game clock, mute button, highscore modal, name prompt modal |
| `onboarding.css` | Diploma, job ads (prestigious vs shabby), rejection letters, acceptance letter, boss meeting layout, title card animation |
| `desk.css` | Desk layout, window (sky gradient + town silhouette), boss note, lead cards grid, lead card flair (coffee/stamp/clip), source badges, action bar, fly-in note modal. **Town-specific overrides** for Småstad, Industristad, Kuststad (desk surface, wall, sky, silhouette, animated effects, lights, card paper color). |
| `interview.css` | Two-panel layout, NPC portrait, expression hint, dialogue log, question buttons (archetype dots), tier-colored borders, points badges, feedback lines, notesheet (lined paper + red margin), tier-colored dots, portrait tint overlays |
| `publish.css` | Newspaper preview, headline choices, publish button, sleep container, deficit change display |
| `results.css` | Side-by-side newspaper cards, scoring breakdown, deficit update, boss sticky note, slide-in animations |
| `transition.css` | Day transition layout, text sizes, deficit display, mood text |
| `sprites.css` (~190 lines) | Base pixel block, sprite container, sprite-body idle sway, eye blink, skin/hair/eye/clothes/accessory color classes, expression body animations (nervous/hostile/open), fallback placeholder |
| `achievements.css` | Achievement modal grid, trophy button, unlock toast notification, locked/unlocked states |

### 14.6 Data Files

| File | Size | Content |
|---|---|---|
| `data/stories.json` | ~28,000 lines | 120 complete story objects (40 per town) with full interview trees |
| `data/npcs.json` | ~1320 lines | 84 NPC profiles |
| `data/boss-dialogue.json` | ~285 lines | Per-town boss quotes (3 towns × desk/results/gameover/onboarding pools) |
| `data/towns.json` | ~350 lines | 3 town configs (competitors, score ranges, farewell sequences, dates) |

### 14.7 Audio Files

| File | Usage |
|---|---|
| `audio/soundtrack.mp3` | Title screen music |
| `audio/Soundtrack_Ingame.mp3` | In-game background loop |
| `audio/Soundtrack_perishscreen.mp3` | Game over screen (loops at 0:18) |

---

## 15. DEPLOYMENT & INFRASTRUCTURE

### 15.1 Deployment Commands
```bash
cd "/Users/gmpethan/Documents/deploy/Game (press or perish)"
git add -A && git commit -m "describe change" && git push
firebase deploy --only hosting
```

### 15.2 Hosting
- **Firebase Hosting** — static file serving
- **Project:** `press-or-perish`
- **Live URL:** https://press-or-perish.web.app
- **Public directory:** `.` (project root)

### 15.3 Local Development
```bash
python3 -m http.server 8091
# → http://localhost:8091
```
No build step needed. ES modules work directly in modern browsers.

### 15.4 Git
- **Repository:** https://github.com/peterhangse/press-or-perish
- **Branch:** `main`
- **Deploy:** Manual push + `firebase deploy`

---

## 16. DESIGN PRINCIPLES

1. **Pressure is the game.** Every system serves the emotional loop. If it dilutes the dread, cut it.
2. **The name is honored.** -10 = perished. No mercy. No rubber-banding.
3. **Two-axis skill.** Story selection (what to investigate) + interview extraction (how to interview).
4. **Content IS logic.** Lookup tables, not runtime calculation. Engine is just a reader.
5. **Blind publish.** You never see scores before committing. The gut call is the peak.
6. **Unpublished stories haunt.** You never see the score of the story you didn't publish. Ever.
7. **The boss is selfish.** Not evil, not a mentor. Self-preserving. Cold.
8. **Anticapitalism through mechanics.** The system speaks. The game never preaches.
9. **English with Swedish flavor.** International first. Swedish names, places, and the occasional å.
10. **Papers Please physicality.** Documents, stamps, tactile feedback. Information on objects, not menus.

---

## 17. ROADMAP & FUTURE FEATURES

See `ROADMAP.md` for the full roadmap. Key future milestones:

### v1.1 — Replayability
- Randomization variables: NPC names, detail swaps, amounts, dates rotate each run
- Seeded PRNG: same seed = same run, shareable
- Daily challenge mode: seed = today's date, one attempt only
- 5th Q1 archetype: Gentle Challenge
- 4th Q2 option per Q1 path (12→20 paths/story)

### v1.2 — Depth
- Trust-conditional Q2 branching (HIGH/MEDIUM/LOW trust modifies responses)
- Between-tier partial scoring
- Topic category tracking across Q1+Q2
- Trust meter hybrid UI (subtle color shift, no numbers)

### v2.0 — Meta-Progression
- 4 journalist characters (The Rookie, The Charmer, The Bulldog, The Networker)
- 4th town: Huvudstad District (high-stakes politics, hardest)
- Per-combination leaderboards (4 characters × 4 towns = 16)
- Character-specific onboarding
- Story journal / clipping archive (review past stories across runs)
- Cross-story threads (Day 1 mill accident → Day 3 land deal)

### v3.0 — Complexity
- NPC choice per lead (2-3 interview targets)
- Sidegrade items (tradeoffs, not power)
- Item unlock achievements

---

*Generated from complete source code analysis of Press or Perish, March 2026.*
