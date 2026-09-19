# AGENTS.md — press-or-perish

**Läs `CONTEXT.md` först.** Den är den enda källa som beskriver spelets
struktur, mekanik och data — allt en agent behöver innan den ändrar något.

## Kontrakt

- Ändrar du kod eller data som påverkar struktur, mekanik, UI-språk eller deploy:
  **uppdatera `CONTEXT.md` i samma commit** som ändringen.
- Engine-moduler (`js/engine/`) = rena funktioner utan DOM. UI (`js/ui/`) = DOM.
- Efter innehållsändring: uppdatera `PRD.md` och kör `tools/audit_prd.py`
  (gate). Kör även `tools/validate.py` om `data/` ändrats.
- UI-språk är engelska (med svensk krydda) — ändra inte utan att uppdatera PRD.
- `publish-screen.js` är implementerad men förbikopplad i `main.js` — skriv inte
  om flödet runt den i onödan.