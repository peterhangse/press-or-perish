#!/usr/bin/env python3
"""Audit PRD.md claims against the actual codebase.

Checks machine-readable PRD header and auditable claims:
- Story count (per town and total)
- NPC count
- Town count
- Achievement count
- CSS file count
- Audio file count
- SFX catalog size
- JS file inventory
- localStorage key listing
- PRD freshness (warn if >30 days old)

Usage: python3 tools/audit_prd.py
"""
import json, os, re, glob
from datetime import datetime, timezone

ROOT = os.path.join(os.path.dirname(__file__), '..')
DATA = os.path.join(ROOT, 'data')

passed = 0
failed = 0
warnings = 0


def ok(label):
    global passed
    passed += 1
    print(f"  ✓ {label}")


def fail(label, expected, actual):
    global failed
    failed += 1
    print(f"  ✗ {label}: expected {expected}, got {actual}")


def warn(label):
    global warnings
    warnings += 1
    print(f"  ⚠ {label}")


# ── Load PRD ──
prd_path = os.path.join(ROOT, 'PRD.md')
if not os.path.exists(prd_path):
    print("FATAL: PRD.md not found")
    exit(1)

with open(prd_path, 'r') as f:
    prd = f.read()
prd_lines = prd.split('\n')

# ── Parse PRD header ──
print("PRD Header:")
header_match = re.search(
    r'PRD_VERSION:\s*([\d.]+)\s*\|\s*STORIES:\s*(\d+)\s*\|\s*NPCS:\s*(\d+)\s*\|\s*TOWNS:\s*(\d+)\s*\|\s*ACHIEVEMENTS:\s*(\d+)\s*\|\s*UPDATED:\s*([\d-]+)',
    prd_lines[0] if prd_lines else ''
)
if not header_match:
    fail("Machine-readable header", "<!-- PRD_VERSION: ... -->", "missing or malformed")
    prd_stories = prd_npcs = prd_towns = prd_achievements = None
    prd_date = None
else:
    prd_version = header_match.group(1)
    prd_stories = int(header_match.group(2))
    prd_npcs = int(header_match.group(3))
    prd_towns = int(header_match.group(4))
    prd_achievements = int(header_match.group(5))
    prd_date = header_match.group(6)
    ok(f"Header found: v{prd_version}, updated {prd_date}")

# ── Load data files ──
print("\nData Files:")
stories = json.load(open(os.path.join(DATA, 'stories.json')))
npcs = json.load(open(os.path.join(DATA, 'npcs.json')))
towns = json.load(open(os.path.join(DATA, 'towns.json')))
boss = json.load(open(os.path.join(DATA, 'boss-dialogue.json')))

# Story count
actual_stories = len(stories)
if prd_stories is not None:
    if actual_stories == prd_stories:
        ok(f"Stories: {actual_stories}")
    else:
        fail("Stories", prd_stories, actual_stories)

# Per-town story count
from collections import Counter
town_counts = Counter(s.get('town', 'unknown') for s in stories)
for town_id in ['smastad', 'industristad', 'kuststad']:
    count = town_counts.get(town_id, 0)
    if count >= 8:  # Minimum for a 5-day run (8 leads/day)
        ok(f"  {town_id}: {count} stories")
    else:
        fail(f"  {town_id} stories", "≥8", count)

# NPC count
actual_npcs = len(npcs)
if prd_npcs is not None:
    if actual_npcs == prd_npcs:
        ok(f"NPCs: {actual_npcs}")
    else:
        fail("NPCs", prd_npcs, actual_npcs)

# Town count
actual_towns = len(towns)
if prd_towns is not None:
    if actual_towns == prd_towns:
        ok(f"Towns: {actual_towns}")
    else:
        fail("Towns", prd_towns, actual_towns)

# Boss dialogue — one entry per town
boss_towns = set(boss.keys()) if isinstance(boss, dict) else set()
for town_id in ['smastad', 'industristad', 'kuststad']:
    if town_id in boss_towns:
        ok(f"  Boss dialogue: {town_id}")
    else:
        fail(f"  Boss dialogue", town_id, "missing")

# ── Interview outcomes ──
print("\nInterview Outcomes:")
total_outcomes = 0
for s in stories:
    iv = s.get('interview', {})
    branches = iv.get('branches', {})
    for arch, branch in branches.items():
        total_outcomes += len(branch.get('outcomes', []))
expected_outcomes = actual_stories * 12  # 4 archetypes × 3 outcomes each
if total_outcomes == expected_outcomes:
    ok(f"Interview outcomes: {total_outcomes} ({actual_stories} × 12)")
else:
    fail("Interview outcomes", expected_outcomes, total_outcomes)

# ── Achievements ──
print("\nAchievements:")
ach_path = os.path.join(ROOT, 'js', 'engine', 'achievements.js')
if os.path.exists(ach_path):
    with open(ach_path) as f:
        ach_src = f.read()
    # Count achievement IDs (id: 'xxx' patterns)
    ach_ids = re.findall(r"id:\s*['\"]([^'\"]+)['\"]", ach_src)
    actual_achievements = len(ach_ids)
    if prd_achievements is not None:
        if actual_achievements == prd_achievements:
            ok(f"Achievements: {actual_achievements}")
        else:
            fail("Achievements", prd_achievements, actual_achievements)
else:
    fail("achievements.js", "exists", "not found")

# ── CSS files ──
print("\nCSS Files:")
css_dir = os.path.join(ROOT, 'css')
css_files = sorted(f for f in os.listdir(css_dir) if f.endswith('.css'))
actual_css = len(css_files)
# Check PRD claim
css_match = re.search(r'(\d+)\s+CSS\s+files', prd)
prd_css = int(css_match.group(1)) if css_match else None
if prd_css is not None:
    if actual_css == prd_css:
        ok(f"CSS files: {actual_css}")
    else:
        fail("CSS files", prd_css, actual_css)
else:
    warn(f"CSS file count not found in PRD (actual: {actual_css})")

# Verify CSS files mentioned in §14.5
for css_file in css_files:
    if css_file in prd:
        ok(f"  {css_file} mentioned in PRD")
    else:
        fail(f"  {css_file}", "mentioned in PRD", "missing from PRD")

# ── Audio files ──
print("\nAudio Files:")
audio_dir = os.path.join(ROOT, 'audio')
if os.path.exists(audio_dir):
    mp3_files = sorted(f for f in os.listdir(audio_dir) if f.endswith('.mp3'))
    for mp3 in mp3_files:
        if mp3 in prd:
            ok(f"  {mp3} mentioned in PRD")
        else:
            fail(f"  {mp3}", "mentioned in PRD", "missing from PRD")
else:
    warn("audio/ directory not found")

# ── SFX catalog ──
print("\nSFX Catalog:")
sfx_path = os.path.join(ROOT, 'js', 'engine', 'sfx-engine.js')
if os.path.exists(sfx_path):
    with open(sfx_path) as f:
        sfx_src = f.read()
    # Count SFX by looking for function definitions in the catalog
    sfx_names = re.findall(r"['\"](\w+)['\"]:\s*(?:function|\()", sfx_src)
    if not sfx_names:
        # Alternative: look for case labels or object keys
        sfx_names = re.findall(r"case\s+['\"](\w+)['\"]", sfx_src)
    sfx_match = re.search(r'(\d+)\s+synthesized\s+(?:SFX|sounds)', prd)
    prd_sfx = int(sfx_match.group(1)) if sfx_match else None
    if sfx_names and prd_sfx is not None:
        if len(sfx_names) == prd_sfx:
            ok(f"SFX count: {len(sfx_names)}")
        else:
            fail("SFX count", prd_sfx, f"{len(sfx_names)} ({', '.join(sfx_names[:5])}...)")
    elif sfx_names:
        ok(f"SFX found: {len(sfx_names)} (PRD count not parseable)")
    else:
        warn("Could not parse SFX catalog")

# ── JS files in PRD tables ──
print("\nJS File Inventory:")
js_engine_files = sorted(os.listdir(os.path.join(ROOT, 'js', 'engine')))
js_ui_files = sorted(os.listdir(os.path.join(ROOT, 'js', 'ui')))
for f in js_engine_files:
    if f.endswith('.js'):
        if f in prd:
            ok(f"  engine/{f} in PRD")
        else:
            fail(f"  engine/{f}", "in PRD", "missing")
for f in js_ui_files:
    if f.endswith('.js'):
        if f in prd:
            ok(f"  ui/{f} in PRD")
        else:
            fail(f"  ui/{f}", "in PRD", "missing")

# ── localStorage keys ──
print("\nlocalStorage Keys:")
# Grep JS files for localStorage usage
ls_keys = set()
for dirpath, _dirs, files in os.walk(os.path.join(ROOT, 'js')):
    for fname in files:
        if not fname.endswith('.js'):
            continue
        with open(os.path.join(dirpath, fname)) as f:
            src = f.read()
        for m in re.finditer(r"localStorage\.\w+Item\(['\"]([^'\"]+)['\"]", src):
            ls_keys.add(m.group(1))
for key in sorted(ls_keys):
    if key in prd:
        ok(f"  {key} documented")
    else:
        fail(f"  {key}", "documented in PRD §12.5", "missing")

# ── PRD freshness ──
print("\nFreshness:")
if prd_date:
    try:
        updated = datetime.strptime(prd_date, '%Y-%m-%d')
        age = (datetime.now() - updated).days
        if age <= 30:
            ok(f"PRD updated {age} days ago ({prd_date})")
        else:
            warn(f"PRD is {age} days old (updated {prd_date}) — consider refreshing")
    except ValueError:
        warn(f"Could not parse date: {prd_date}")
else:
    warn("No UPDATED date in header")

# ── Summary ──
print(f"\n{'='*40}")
print(f"PASSED: {passed}  FAILED: {failed}  WARNINGS: {warnings}")
if failed == 0:
    print("✓ All auditable PRD claims match codebase.")
else:
    print(f"✗ {failed} claim(s) do not match — update PRD.md.")
exit(1 if failed else 0)
