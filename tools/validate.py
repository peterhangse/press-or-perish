#!/usr/bin/env python3
"""Validate Industristad stories against PRD requirements, plus whole-game data checks."""
import json, os
from collections import Counter

DATA = os.path.join(os.path.dirname(__file__), '..', 'data')
stories = json.load(open(os.path.join(DATA, 'stories.json')))
npcs = json.load(open(os.path.join(DATA, 'npcs.json')))

ind = [s for s in stories if s.get('town') == 'industristad']
sma = [s for s in stories if s.get('town', 'smastad') == 'smastad']

print(f"Total stories: {len(stories)}")
print(f"Smastad: {len(sma)}, Industristad: {len(ind)}")

# BV distribution
bv = Counter(s['base_value'] for s in ind)
print("\nIndustristad BV distribution:")
target = {2:7, 3:3, 4:9, 5:7, 6:6, 7:4, 8:4}
all_match = True
for v in sorted(target):
    actual = bv.get(v, 0)
    ok = actual == target[v]
    if not ok: all_match = False
    mark = "ok" if ok else f"WANT {target[v]}"
    print(f"  bv{v}: {actual} {mark}")
print(f"  Distribution: {'PASS' if all_match else 'FAIL'}")

# Structure check
print("\nStructure check:")
issues = []
archetypes = {'friendly','direct','pressure','silence'}
for s in ind:
    sid = s['id']
    if 'interview' not in s:
        issues.append(f"{sid}: missing interview")
        continue
    iv = s['interview']
    if len(iv.get('q1_options', [])) != 4:
        issues.append(f"{sid}: q1_options != 4")
    branches = set(iv.get('branches', {}).keys())
    if branches != archetypes:
        issues.append(f"{sid}: wrong branches: {branches}")
    for arch in archetypes:
        b = iv.get('branches', {}).get(arch, {})
        if len(b.get('q2_options', [])) != 3:
            issues.append(f"{sid}/{arch}: q2_options != 3")
        outs = b.get('outcomes', [])
        if len(outs) != 3:
            issues.append(f"{sid}/{arch}: outcomes != 3")
        else:
            tiers = [o['tier'] for o in outs]
            if tiers != [1,2,3]:
                issues.append(f"{sid}/{arch}: tiers {tiers} != [1,2,3]")
    h = s.get('headlines', [])
    if isinstance(h, dict):
        if not all(f'tier_{i}' in h for i in range(4)):
            issues.append(f"{sid}: headlines missing tier_0..tier_3")
    elif len(h) != 3:
        issues.append(f"{sid}: headlines != 3")

if issues:
    for i in issues:
        print(f"  ISSUE: {i}")
else:
    print("  PASS: All 40 stories have valid structure")
    print(f"  Total interview paths: {len(ind) * 12}")

# Category distribution
cats = Counter(s.get('category','?') for s in ind)
print(f"\nCategory spread: {dict(cats)}")

# NPC usage
npc_usage = Counter(s['npc_id'] for s in ind)
# npcs.json is a list of NPC objects with a 'town' field
ind_npcs = [n for n in npcs if n.get('town') == 'industristad'] if isinstance(npcs, list) else npcs.get('industristad', [])
print(f"\nNPC usage ({len(npc_usage)} unique / {len(ind_npcs)} available):")
for npc, count in npc_usage.most_common(10):
    print(f"  {npc}: {count}x")

# Check required fields
print("\nField completeness:")
required = ['id','title','description','lead_text','preview','source_type','difficulty','base_value','category','npc_id','npc_name','npc_title','town','interview','headlines']
missing = []
for s in ind:
    for f in required:
        if f not in s or not s[f]:
            missing.append(f"{s['id']}: missing {f}")
if missing:
    for m in missing:
        print(f"  ISSUE: {m}")
else:
    print("  PASS: All required fields present")

# Whole-game checks (all towns)
print("\nWhole game:")
ids = Counter(s['id'] for s in stories)
dupes = [i for i, c in ids.items() if c > 1]
print(f"  Unique story IDs: {'PASS' if not dupes else 'FAIL ' + str(dupes)}")
npc_ids = {n['id'] for n in npcs} if isinstance(npcs, list) else set()
unknown = sorted({s['npc_id'] for s in stories} - npc_ids) if npc_ids else []
print(f"  Every story NPC exists in npcs.json: {'PASS' if not unknown else 'FAIL ' + str(unknown)}")
perish = [(s['id'], a, i, o) for s in stories for a, b in s['interview']['branches'].items()
          for i, o in enumerate(b['outcomes']) if o.get('perish')]
no_reason = [f"{sid}/{a}/{i}" for sid, a, i, o in perish if not o.get('perish_reason')]
print(f"  Instant-perish outcomes: {len(perish)} — reasons: {'PASS' if not no_reason else 'FAIL missing ' + str(no_reason)}")
valid_diff = {'easy', 'medium', 'hard', 'expert', 'elite'}
bad_diff = [s['id'] for s in stories if s.get('difficulty') not in valid_diff]
print(f"  Difficulty values: {'PASS' if not bad_diff else 'FAIL ' + str(bad_diff)}")

print("\n=== VALIDATION COMPLETE ===")
