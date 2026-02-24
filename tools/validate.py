#!/usr/bin/env python3
"""Validate all Industristad stories against PRD requirements."""
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
    if len(s.get('headlines', [])) != 3:
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
ind_npcs = npcs.get('industristad', [])
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

print("\n=== VALIDATION COMPLETE ===")
