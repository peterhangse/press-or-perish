#!/usr/bin/env python3
import json
from collections import Counter

with open('data/stories.json') as f:
    stories = json.load(f)

sma = [s for s in stories if s.get('town') == 'smastad']
ind = [s for s in stories if s.get('town') == 'industristad']

print("=== Småstad distribution ===")
bv = Counter(s['base_value'] for s in sma)
for k in sorted(bv): print(f"  bv{k}: {bv[k]}")
cat = Counter(s['category'] for s in sma)
print(f"\nCategories: {dict(cat)}")
src = Counter(s['source_type'] for s in sma)
print(f"Sources: {dict(src)}")
diff = Counter(s['difficulty'] for s in sma)
print(f"Difficulty: {dict(diff)}")

print(f"\n=== Industristad ({len(ind)} stories) ===")
bv2 = Counter(s['base_value'] for s in ind)
for k in sorted(bv2): print(f"  bv{k}: {bv2[k]}")
cat2 = Counter(s['category'] for s in ind)
print(f"Categories: {dict(cat2)}")
src2 = Counter(s['source_type'] for s in ind)
print(f"Sources: {dict(src2)}")

# What NPC IDs are used in existing stories
used_npcs = set(s['npc_id'] for s in ind)
print(f"\nUsed NPCs: {used_npcs}")

# What NPCs are available
with open('data/npcs.json') as f:
    npcs = json.load(f)
ind_npcs = [n for n in npcs if n.get('town') == 'industristad']
available = [n['id'] for n in ind_npcs if n['id'] not in used_npcs]
print(f"Available NPCs ({len(available)}): {available}")
