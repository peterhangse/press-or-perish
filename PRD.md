# PRESS OR PERISH — Complete Product Requirements Document
## Version 1.0 · Last updated: 21 February 2026

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
**Setting:** 1970s rural Sweden, fictional town "Småstad"
**Platform:** Web browser (HTML/CSS/JS), hosted on Firebase Hosting
**Resolution:** 640×360 fixed canvas, CSS-scaled to fit browser window
**Aesthetic:** Papers Please-inspired pixel art, cold Nordic noir, desaturated 1970s newsprint palette
**Live URL:** https://press-or-perish.web.app
**Repository:** https://github.com/peterhangse/press-or-perish (branch: `main`)

### Premise
You are a fresh journalism graduate from Stockholm University (Class of 1974, Magna Cum Laude). No prestigious paper — Dagens Nyheter, Expressen, Göteborgs-Posten — would hire you. The only job offer: reporter at **Småstad Paper**, a tiny local newspaper run by the gruff editor-in-chief **Gunnar Ek**. Your competitor is **Regionbladet**, a larger regional paper that is systematically outperforming your publication each day.

You have **one week (5 days)** to prove your worth — or perish.

### Win/Lose Conditions
- **WIN:** Survive to Friday evening (Day 5) without the deficit reaching -10 or below.
- **LOSE (PERISHED):** Deficit reaches -10 at any point = fired immediately.

---

## 2. HOW TO PLAY — FULL PLAYER JOURNEY

### 2.1 First Launch: Start Screen
The game opens to a desktop-style start screen with the title **"PRESS OR PERISH"** in large typewritten text. The title is initially non-interactive — clicking it triggers the title music and reveals the menu below.

**Menu options:**
- **New Game** — Skips the tutorial, prompts for name, starts at Day 1
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
- **Top bar:** A window showing a Småstad town silhouette (morning sky gradient, buildings as CSS clip-path, tiny lit windows), plus a **boss sticky note** with today's directive
- **Center:** 8 lead cards in a scrollable grid
- **Bottom:** Action bar with selected lead label and INVESTIGATE button

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

---

## 4. SCORING SYSTEM

### 4.1 Formula
```
Total Points = Base News Value + Tier Bonus
Tier Bonus = tier × 2
```

### 4.2 Base News Values (per story)
Stories have base values of 2-8, distributed across 40 stories:

| Base Value | Count | Description |
|---|---|---|
| 2 pts | 7 stories | Filler: minor events, soft features |
| 3 pts | 3 stories | Small items |
| 4 pts | 9 stories | Decent: local disputes, small scandals |
| 5 pts | 7 stories | Good local issues |
| 6 pts | 6 stories | Strong investigations |
| 7 pts | 4 stories | Major revelations |
| 8 pts | 4 stories | Top: deaths, major corruption, cover-ups |

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
- 40 stories × 12 paths = **480 total interview outcomes** in the game

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

---

## 6. COMPETITOR AI

The competitor is **Regionbladet**, a larger regional newspaper.

### 6.1 Score Generation
Competitor score is random within day-specific ranges:

| Day | Min | Max | Character |
|---|---|---|---|
| 1 | 6 | 9 | Easy start |
| 2 | 7 | 10 | Building |
| 3 | 8 | 11 | Mid difficulty |
| 4 | 8 | 12 | Getting stronger |
| 5 | 9 | 12 | Strong finish |

**Average competitor output: ~8-10 pts/day.**

### 6.2 Competitor Headlines
Generated as flavor text based on score:
- **Score ≥ 11:** Strong headlines (e.g., "Exposes corruption in municipal leadership")
- **Score 8-10:** Average headlines (e.g., "City council debates school closure")
- **Score < 8:** Weak headlines (e.g., "Award for local sports club")

---

## 7. BOSS SYSTEM

**Gunnar Ek** is the editor-in-chief. He appears in two contexts:

### 7.1 Desk Notes (Morning)
A sticky note pinned on the desk, refreshed daily. Drawn from pools to avoid repeats within a run.

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

### 8.2 Screen: Start
- Brown desk background
- Large title "PRESS OR PERISH" — clickable to start music
- After click: title settles, menu slides in with New Game, Tutorial, Highscores buttons
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
- Town silhouette window, boss note, 8 lead cards, action bar

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

**28 NPCs** have full pixel art sprite definitions in `npc-sprites.js` (1203 lines).

### 10.5 Window Background
The desk window shows a **Småstad town silhouette:**
- CSS gradient sky (morning colors)
- Town silhouette built with `clip-path: polygon(...)`
- Tiny lit window dots as radial gradients
- Background shifts by time of day: morning (blue-grey) → afternoon (amber) → evening (dark)

### 10.6 Transitions
- **Hard cuts** between screens — no fades (Papers Please style)
- Brief flash overlay (300ms white/amber) on major transitions
- Staggered slide-in animations on results screen

---

## 11. CONTENT INVENTORY

### 11.1 Stories: 40 total

**By category:**
| Category | Count |
|---|---|
| Human Interest | 11 |
| Corruption | 10 |
| Crime | 7 |
| Breaking News | 7 |
| Labor | 5 |

**By difficulty:**
| Difficulty | Count |
|---|---|
| Easy | 17 |
| Medium | 12 |
| Hard | 11 |

**By base value:**
| Base Value | Count |
|---|---|
| 2 | 7 |
| 3 | 3 |
| 4 | 9 |
| 5 | 7 |
| 6 | 6 |
| 7 | 4 |
| 8 | 4 |

**Per story content:**
- Title, description, lead text, preview text
- Source type (letter / document / street)
- Difficulty (easy / medium / hard), base value (2-8), category
- NPC reference (npc_id, npc_name, npc_title)
- Interview: opening line + 4 Q1 options + 4 branches (each with Q1 response, expression hint, Q1 note, 3 Q2 options, 3 outcomes)
- Headlines: 4 tiers × 3 options each (text + tone)
- Optional: `boss_result_quotes` with positive/negative arrays

### 11.2 NPCs: 28
Each NPC has:
- id, name, role, age
- default_expression, expressions array
- unique_detail (e.g., bandaged_hand, glasses)
- clothing_color (CSS class reference)
- initial_demeanor (hint text when interview starts)

### 11.3 Boss Dialogue
- Desk notes: day-specific pools (3 per day), warning pool (3), danger pool (3), default pool (3)
- Result quotes: critical (4), bad (4), warning (4), neutral (4), good (4), great (4)
- Game over: fired text, survived text (barely/decent/dominant)
- Onboarding: intro, rules, threat, start

### 11.4 Day Distribution
Lead generation per day (how many from each difficulty pool):

| Day | Easy | Medium | Hard | Character |
|---|---|---|---|---|
| 1 | 6 | 2 | 0 | Gentle start |
| 2 | 5 | 2 | 1 | Warming up |
| 3 | 2 | 4 | 2 | Mix |
| 4 | 1 | 2 | 5 | Getting hard |
| 5 | 0 | 2 | 6 | Final push |

Stories are never repeated within a run (`usedStoryIds` tracked).

---

## 12. DATA SCHEMAS (COMPLETE)

### 12.1 stories.json — Array of 40 Story objects

```json
{
  "id": "string",
  "title": "string",
  "description": "string",
  "lead_text": "string",
  "preview": "string",
  "source_type": "letter|document|street",
  "difficulty": "easy|medium|hard",
  "base_value": 2-8,
  "category": "labor|crime|corruption|human_interest|breaking_news",
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

### 12.2 npcs.json — Array of 28 NPC objects

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

### 12.3 boss-dialogue.json

```json
{
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
}
```

### 12.4 Game State (runtime, not persisted to file)

```json
{
  "phase": "start|onboarding|transition|desk|interview|publish|sleep|results|gameover",
  "day": 0-5,
  "deficit": "number",
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

---

## 13. TECHNICAL ARCHITECTURE

### 13.1 Stack
- **Language:** Vanilla JavaScript (ES6 modules, `import`/`export`)
- **Markup:** Single `index.html` with empty screen containers
- **Styling:** 9 CSS files, CSS custom properties, no preprocessor
- **Build:** Zero build tools, zero frameworks, zero dependencies
- **Data:** JSON files fetched at runtime
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
data/*              ← JSON content files (stories, NPCs, boss dialogue)
css/*               ← 9 modular CSS files
audio/*             ← 3 MP3 soundtrack files
```

### 13.3 Engine ↔ UI Separation
**Engine modules** (`js/engine/`) are pure functions — no `document`, no `window`, no DOM. They could be ported to GDScript for a Godot migration.

**UI modules** (`js/ui/`) create and manipulate DOM elements, handle events, and call engine functions for game logic.

**Data flow:** `main.js` orchestrates everything — it calls engine functions for logic, UI functions for rendering, and passes data between them.

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
| `game-state.js` | ~82 | `createState()`, `resetDay()`, `recordDay()`, `isPerished()`, `hasSurvived()` | Central state object. Pure data, no DOM. Default state includes phase, day, deficit, leads, history, meta. Perish threshold = -10. |
| `day-generator.js` | ~101 | `generateDayZeroLeads()`, `generateDayLeads()` | Day Zero: 3 easy leads (1 per source type). Days 1-5: 8 leads from difficulty pools (see §11.4). Fisher-Yates shuffle. Avoids used story IDs. |
| `interview-engine.js` | ~72 | `getQ1Options()`, `getQ2Options()`, `resolveInterview()`, `getHeadlines()` | Lookup table reader. ~30 lines of core logic. resolveInterview returns { tier, points, response, expression, feedback, note }. Points = base_value + (tier×2). |
| `scoring-engine.js` | ~66 | `calculatePoints()`, `calculateDeficitDelta()`, `applyDeficit()`, `getDeficitSeverity()`, `getDeficitFillPercent()`, `getPerishDistance()` | All math functions. Deficit threshold = -10. Severity: safe (>-3), warning (-3 to -7), danger (<-7). |
| `competitor-ai.js` | ~79 | `generateCompetitorScore()`, `getCompetitorHeadline()`, `getCompetitorName()` | Random score in day-specific range. 3 headline pools (strong/average/weak). Competitor name: "Regionbladet". |
| `data-loader.js` | ~62 | `loadAllData()`, `loadStories()`, `loadNPCs()`, `loadBossDialogue()`, `getStory()`, `getNPC()` | Fetches and caches JSON data. Parallel Promise.all loading. |
| `audio-manager.js` | ~176 | `play()`, `stop()`, `retryPlay()`, `toggleMute()`, `isMuted()`, `getActiveTrack()` | Multi-track audio with 3-second crossfade. Perish track custom loops at 18s via timeupdate event. Mute persisted to localStorage. |
| `sfx-engine.js` | ~417 | `play()`, `warmUp()` | 12 synthesized SFX via Web Audio API. All real-time generated. Catalogue: tick, click, select, deselect, stamp, note, reveal, tension, relief, slam, ambientTick, reject. |

### 14.3 JavaScript — UI (`js/ui/`)

| File | Lines | Exports | Description |
|---|---|---|---|
| `screen-manager.js` | ~74 | `init()`, `switchTo()`, `getCurrent()`, `flash()` | Manages 8 screen divs. Hard cut transitions (no fades). Show/hide via `.active` class. Toggles HUD bar visibility. Flash overlay for emphasis. |
| `onboarding.js` | ~320 | `start()`, `getPlayerName()` | 13-step narrative sequence. Handles diploma (name input), job ads, rejections, acceptance, boss meeting, title card. Boss steps reuse persistent portrait frame. Title card word-by-word slam animation. |
| `desk-screen.js` | ~300 | `render()` | Renders 8 lead cards with source badges, headlines, lead text, NPC info. Card flair system (coffee stains, stamps, clips). Selection/deselection with SFX. INVESTIGATE stamp. Day Zero fly-in boss note modal. |
| `interview-screen.js` | ~530 | `start()` | Full interview flow: Q1→Q2→result. Typewriter dialogue system. Notesheet with tier-colored dots. Feedback system: tier borders, points badges, feedback lines. Portrait tint and body animation. Expression hint updates. |
| `publish-screen.js` | ~175 | `render()`, `showSleep()` | Headline selection (currently bypassed by main.js — auto-picks first headline). Sleep phase: deficit change display, mood text, continue button. Date display: November 10-15, 1974. |
| `results-screen.js` | ~270 | `render()` | Two-phase reveal. Phase 1: scoring breakdown with dot meters. Phase 2: side-by-side newspaper comparison, deficit update, boss sticky note fly-in. Staggered animations. |
| `transition-screen.js` | ~80 | `show()` | Day header with day number, name, date, deficit color, mood text. 3-second auto-advance. |
| `gameover-screen.js` | ~150 | `showPerished()`, `showSurvived()` | Both endings. Stats grid. Cold epilogue text. Perished: varies by days survived. Survived: varies by deficit severity. |
| `components.js` | ~135 | `buildWeekStrip()`, `updateWeekStrip()`, `updateDeficitMeter()`, `updateClock()`, `updateWindowSky()`, `getDeficitColor()` | Persistent HUD updates. Deficit color interpolation (lerpColor between RGB values). Week strip day coloring. Clock phase mapping. |
| `npc-sprites.js` | ~1203 | `renderSprite()` | 28 CSS pixel art NPC definitions. Each sprite = array of {x,y,w,h,cls,style} pixel blocks. Renders as absolutely-positioned divs inside a 120×160 container. Includes sprite-body wrapper for animations. |

### 14.4 JavaScript — Main

| File | Lines | Description |
|---|---|---|
| `main.js` | ~740 | Entry point. `boot()` initializes everything: scales canvas, loads data, wires start screen buttons, builds HUD. Game flow functions: `startNewRun()`, `startTutorial()`, `startDayZero()` (with 4 sub-functions), `startDay()`, `showDesk()`, `startInterview()`, `showPublish()`, `showResults()`, `showGameOver()`, `showEnding()`. Boss quote logic: `getBossNote()`, `getBossQuote()`, `getStoryBossQuote()`. Utility: name prompt modal, highscore board, mute button, `pickUnused()` for avoiding repeat quotes, `injectName()` for {name} replacement. |

### 14.5 CSS Files

| File | Purpose |
|---|---|
| `variables.css` (~314 lines) | CSS custom properties, reset, game wrapper/canvas scaling, screen management, flash overlay, shared button styles, stamp animation, film grain overlay, cursor styles, typewriter cursor |
| `components.css` | HUD bar, deficit meter, week strip, game clock, mute button, highscore modal, name prompt modal |
| `onboarding.css` | Diploma, job ads (prestigious vs shabby), rejection letters, acceptance letter, boss meeting layout, title card animation |
| `desk.css` | Desk layout, window (sky gradient + town silhouette), boss note, lead cards grid, lead card flair (coffee/stamp/clip), source badges, action bar, fly-in note modal |
| `interview.css` | Two-panel layout, NPC portrait, expression hint, dialogue log, question buttons (archetype dots), tier-colored borders, points badges, feedback lines, notesheet (lined paper + red margin), tier-colored dots, portrait tint overlays |
| `publish.css` | Newspaper preview, headline choices, publish button, sleep container, deficit change display |
| `results.css` | Side-by-side newspaper cards, scoring breakdown, deficit update, boss sticky note, slide-in animations |
| `transition.css` | Day transition layout, text sizes, deficit display, mood text |
| `sprites.css` (~190 lines) | Base pixel block, sprite container, sprite-body idle sway, eye blink, skin/hair/eye/clothes/accessory color classes, expression body animations (nervous/hostile/open), fallback placeholder |

### 14.6 Data Files

| File | Size | Content |
|---|---|---|
| `data/stories.json` | ~10,000 lines | 40 complete story objects with full interview trees |
| `data/npcs.json` | ~600 lines | 28 NPC profiles |
| `data/boss-dialogue.json` | 95 lines | Boss quotes for desk, results, game over, onboarding |

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

### v1.1 — Replayability
- Randomization variables: NPC names, detail swaps, amounts, dates rotate each run
- Seeded PRNG: same seed = same run, shareable
- Daily challenge mode: seed = today's date, one attempt only
- High score tracking improvements
- 5th Q1 archetype: Gentle Challenge
- 4th Q2 option per Q1 path (12→20 paths/story, 800 total outcomes)

### v1.2 — Depth
- Trust-conditional Q2 branching (HIGH/MEDIUM/LOW trust modifies responses)
- Between-tier partial scoring
- Topic category tracking across Q1+Q2
- Trust meter hybrid UI (subtle color shift, no numbers)

### v2.0 — Meta-Progression
- 4 journalist characters (The Rookie, The Charmer, The Bulldog, The Networker)
- 4 towns (Småstad, Industristad, Kuststad, Huvudstad District)
- Per-combination leaderboards (4×4 = 16)
- Character-specific onboarding
- Sound design expansion
- Cross-story threads (Day 1 mill accident → Day 3 land deal)

### v3.0 — Complexity
- NPC choice per lead (2-3 interview targets)
- Sidegrade items (tradeoffs, not power)
- Item unlock achievements

---

*Generated from complete source code analysis of Press or Perish, commit 5c460aa, February 2026.*
