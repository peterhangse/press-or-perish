# Copilot Instructions — Press or Perish

## PRD Sync Rule
After any code change that adds, removes, or modifies game mechanics, data files, screens, audio, CSS, or JS modules — **update PRD.md to match**. The PRD is the AI context document. If it drifts from reality, it misleads all future development.

## What to Update (by change type)

| Change Type | PRD Sections to Update |
|---|---|
| New story | §4 (base value table), §11 (content inventory), §12 (schema if new fields) |
| New screen | §2 (player journey), §3 (gameplay loop), §8 (screens & UI), §14 (file reference) |
| New mechanic | §3 (gameplay loop), §5 (interview system), §16 (design principles if relevant) |
| New town | §1 (overview), §2 (player journey), §6 (competitor), §7 (boss), §10 (visual identity), §11 (content inventory), §12 (schemas) |
| New CSS file | §10 (visual design), §13 (tech architecture — CSS count), §14 (CSS file table) |
| New JS module | §13 (tech architecture), §14 (file reference tables) |
| New achievement | §11.5 (achievement count/categories) |
| Audio change | §9 (audio system), §14 (audio files) |
| localStorage change | §12.5 (localStorage keys) |
| Save system change | §12.7 (save schema), §13.5 (save/resume system) |
| Scoring change | §4 (scoring system) |
| Boss dialogue change | §7 (boss system), §11.3 (boss dialogue inventory) |

## PRD Version Header
Update the machine-readable comment on line 1 of PRD.md:
```
<!-- PRD_VERSION: X.X | STORIES: N | NPCS: N | TOWNS: N | ACHIEVEMENTS: N | UPDATED: YYYY-MM-DD -->
```

## Validation
After PRD changes, run `python3 tools/audit_prd.py` to verify claims match codebase.

## Code Conventions
- Engine modules (`js/engine/`): pure functions, zero DOM access
- UI modules (`js/ui/`): DOM rendering, event handling
- Data: JSON files in `data/`, fetched at runtime
- CSS: modular files in `css/`, CSS custom properties only
- No build tools, no frameworks, no dependencies
- All SFX synthesized via Web Audio API (no audio files for SFX)
- Town theming via CSS classes `.town-{id}` on container elements
