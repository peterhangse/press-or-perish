# CONTEXT.md — press-or-perish

**"Press or Perish"** — journalistsimulerings-roguelike (Papers Please-inspirerad)
i 1970-talets Småland. Spelaren är nyutexaminerad reporter som måste överleva
5 dagar × 3 städer utan att bli sparkad. Ren vanilla JS/HTML/CSS, **ingen build,**
**ingen backend** — dombaserad rendering, inte `<canvas>`.

## Teknik (verifierat)

- Vanilla JS ES-moduler + `fetch()` av JSON. Ingen ramverksfil, ingen buntare.
- `index.html` laddar `js/main.js` + 10 CSS-filer. Cache-busting via `?v=<n>`.
- **UI-språk = engelska** (`lang="en"`) med svensk krydda (namn, platser,
  stämplar som "MOTTAGET"). OBS: äldre beskrivningar påstod svensk UI — det är
  inaktuellt; det är ett internationellt val enligt PRD.
- All grafik är CSS pixel-art (div-block), inga bildfiler. Google Fonts.
- Ljud: 3 MP3-spår i `audio/` + 12 SFX syntade live i Web Audio (`sfx-engine.js`).

## Struktur

| Sökväg | Roll |
|---|---|
| `js/main.js` | Orkestrerare + flöde (ingen game-loop — event/callback-styrd state-maskin) |
| `js/engine/` | Ren logik utan DOM: `game-state`, `day-generator`, `interview-engine`, `scoring-engine`, `competitor-ai`, `data-loader`, `audio-manager`, `achievements`, `settings` |
| `js/ui/` | 13 DOM-moduler: desk, interview, publish, results, transition, gameover, onboarding, components (HUD), npc-sprites, achievements-ui, screen-manager, settings-ui, keyboard |
| `data/` | 4 JSON: `stories.json` (120), `npcs.json` (84), `boss-dialogue.json`, `towns.json` (3) |
| `css/` | 10 tematiska ark (variabler + town-teman `town-{id}`) |
| `tools/` | Python-auditverktyg (stdlib) — `validate.py`, `audit_prd.py` m.fl. |
| `PRD.md` | 17 sektioners kravdokument v2.0 (maskinläsbar versionsrad + räknare) |

## Mekanik (dagsslinga)

1. **Dagövergång** (~3 s) → 2. **Desk** (08:15): välj 1 lead-kort av 4
   (Småstad), 6 (Industristad) eller 8 (Kuststad) — `leadsPerDay` i towns.json;
   svårighetsmixen skalas ner (`scaleMix`) → 3. **Intervju** (12:00): Q1 = 1 av 4 arketyper
   (friendly/direct/pressure/silence) → NPC-svar → Q2 = 3 storyspecifika
   följdfrågor → tier 0–3. **Deterministisk lookup**:
   `story.interview.branches[q1].outcomes[q2]` = `{tier, response, perish?, perish_reason?}`.
   Poäng = `base_value + max(tier×2, Q1-bonus)`; Q1-bonus (+2) bara om grenen
   kan nå tier 3 (`Q1_BONUS_MIN_TIER`). Ordningen på Q1/Q2 **blandas** vid
   visning (index i datan är fortfarande nyckeln) → 4. **Resultat** (23:00):
   poäng vs konkurrent, deficit ändras → vid **deficit ≤ −10 = PERISHED**.
3 städer × 5 dagar, alla med egna stories, boss och escalation.
Konkurrenten tar ("scoop") ett lead du valde bort om det är värt ≥ 6 och mer än
ditt (+1 poäng åt dem); ett annat bortvalt lead (≥ 4) ligger kvar nästa dag
som STILL OPEN (`SCOOP_RULES` i competitor-ai.js). Dag 4–5 delar även ut
`expert`/`elite`-stories (Kuststad). Konkurrentens intervall i `towns.json` är
balanserade med `node tools/simulate_balance.mjs` (kör spelets egen motor).

**Kända detaljer:**
- `publish-screen.js` (rubrikval + sömn) är **implementerad men förbikopplad** —
  main.js auto-pickar rubrik 0 och hoppar direkt till resultat. Död kod idag.
- Dag 0/tutorial (onboarding 13 steg), räknas inte på deficit.
- Intervjun visar NPC:ns namn och titel från storyn (`npc_name`/`npc_title`),
  samma text som lead-kortet. `npcs.json` ger sprite, demeanor och reservroll.
  Samma NPC kan ha olika roller i olika stories (t.ex. Gunnar Ek som bonde).
- Dev-knappen "⚙ Skip to town" visas bara i dev-läge: localhost/127.0.0.1
  eller `?dev` i URL:en (`isDevMode()` i main.js).
- `prefers-reduced-motion: reduce` hanteras globalt i `css/variables.css`:
  animationer hoppar till slutläget, flash-overlay stängs av.
- 55 achievements (audit räknar 60 inkl. 5 kategori-id), 1 440 intervjuutfall,
  3 med direkt avsked (vargjakten, mill_accident, farja_forsenad) med
  `perish_reason` som visas på game over. Dag 0 kan aldrig ge avsked.
- **Sparning (pop_save v3):** sparas vid varje beslut — desk delad, lead valt,
  Q1 vald, svaret avgjort (deficit räknas ut direkt i `resolveDay`). Omladdning
  ger samma desk/intervju/resultat. Avsked tar bort sparfilen direkt.
- **Inställningar** (`pop_settings`, ⚙ i HUD): volym musik/effekter,
  textfart, större text (auto på små skärmar), reduce motion. Tangentbord:
  Enter/Space, 1–8, Esc (`ui/keyboard.js`).
- Första gången kör New Game introt + dag 0 (`pop_intro_seen`).
- Källor minns tidigare möten i samma runda (`npcMemory`).

## Regler/kontrakt (viktigt!)

- **"Content IS logic"** — allt sitter i JSON-lookup-tabeller; engine är bara en
  läsare. Ingen dold state/hästartik.
- `js/engine/` = rena funktioner utan DOM ("portabla till Godot"); `js/ui/` =
  DOM + events.
- **Efter ändring:** uppdatera `PRD.md` och kör `tools/audit_prd.py` (gate).
  `tools/validate.py` och `audit_text_lengths.py` kontrollerar innehållsgränser.

## Köra / deploya

- Lokalt: `python3 -m http.server 8000` (kräver modern webbläsare, ES-moduler).
- Deploy: push till `main` → GitHub Actions (`firebase-hosting-merge.yml`)
  deployar live automatiskt till https://press-or-perish.web.app.
- Firebase-projekt `press-or-perish`, publicerar från reporoten (ignorerar `*.md`,
  dolda filer, `musik_audio/` och `tools/`).
- Cache-busting: höj `?v=<n>` i `index.html` när CSS/JS ändras (nu `v=16`).
  OBS: bara index.html-länkarna har `?v`; moduler importeras utan, så
  `firebase.json` sätter no-cache på JS.
- `tools/validate.py` körs igen (Industristad-kontroller + hela spelet: unika
  id, NPC finns, perish_reason). Industristads gamla regel "tiers [1,2,3] per
  gren" flaggar några avvikande stories — informativt, inte fel.