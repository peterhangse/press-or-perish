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
| `js/engine/` | Ren logik utan DOM: `game-state`, `day-generator`, `interview-engine`, `scoring-engine`, `competitor-ai`, `data-loader`, `audio-manager`, `achievements` |
| `js/ui/` | 11 DOM-renderare: desk, interview, publish, results, transition, gameover, onboarding, components (HUD), npc-sprites, achievements-ui, screen-manager |
| `data/` | 4 JSON: `stories.json` (120), `npcs.json` (84), `boss-dialogue.json`, `towns.json` (3) |
| `css/` | 10 tematiska ark (variabler + town-teman `town-{id}`) |
| `tools/` | Python-auditverktyg (stdlib) — `validate.py`, `audit_prd.py` m.fl. |
| `PRD.md` | 17 sektioners kravdokument v2.0 (maskinläsbar versionsrad + räknare) |

## Mekanik (dagsslinga)

1. **Dagövergång** (~3 s) → 2. **Desk** (08:15): välj 1 av 8 lead-kort (svårighet
   stiger per dag) → 3. **Intervju** (12:00): Q1 = 1 av 4 arketyper
   (friendly/direct/pressure/silence) → NPC-svar → Q2 = 3 storyspecifika
   följdfrågor → tier 0–3. **Deterministisk lookup**:
   `story.interview.branches[q1].outcomes[q2]` = `{tier, response, perish?}`.
   Poäng = `base_value + tier×2` → 4. **Resultat** (23:00): poäng vs konkurrent,
   deficit ändras → vid **deficit ≤ −10 = PERISHED** (game over).
3 städer × 5 dagar, alla med egna stories, boss och escalation.

**Kända detaljer:**
- `publish-screen.js` (rubrikval + sömn) är **implementerad men förbikopplad** —
  main.js auto-pickar rubrik 0 och hoppar direkt till resultat. Död kod idag.
- Dag 0/tutorial (onboarding 13 steg), räknas inte på deficit.
- 50 achievements, 1 440 intervjuutfall totalt.

## Regler/kontrakt (viktigt!)

- **"Content IS logic"** — allt sitter i JSON-lookup-tabeller; engine är bara en
  läsare. Ingen dold state/hästartik.
- `js/engine/` = rena funktioner utan DOM ("portabla till Godot"); `js/ui/` =
  DOM + events.
- **Efter ändring:** uppdatera `PRD.md` och kör `tools/audit_prd.py` (gate).
  `tools/validate.py` och `audit_text_lengths.py` kontrollerar innehållsgränser.
- Dock: räkna/sifferdrift finns (PRD säger 44 achievements, kod har 50).

## Köra / deploya

- Lokalt: `python3 -m http.server 8000` (kräver modern webbläsare, ES-moduler).
- Deploy: push till `main` → GitHub Actions (`firebase-hosting-merge.yml`)
  deployar live automatiskt till https://press-or-perish.web.app.
- Firebase-projekt `press-or-perish`, publicerar från reporoten (ignorerar `*.md`).