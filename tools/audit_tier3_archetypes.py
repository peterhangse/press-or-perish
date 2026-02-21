#!/usr/bin/env python3
"""Show all tier 3 paths across all 40 stories — archetype + NPC + description."""
import json

with open("data/stories.json") as f:
    stories = json.load(f)

arch_counts = {"friendly": 0, "direct": 0, "pressure": 0, "silence": 0}

for s in sorted(stories, key=lambda x: x.get("base_value", 0)):
    title = s["title"]
    bv = s.get("base_value", 0)
    npc = s.get("npc_name", "?")
    npc_title = s.get("npc_title", "")
    desc = s.get("description", "")[:100]
    interview = s.get("interview", {})
    branches = interview.get("branches", {})
    
    tier3_list = []
    all_paths = []
    for arch, branch in branches.items():
        outcomes = branch.get("outcomes", [])
        q2_opts = branch.get("q2_options", [])
        for i, out in enumerate(outcomes):
            tier = out.get("tier", 0)
            q2_text = q2_opts[i]["text"] if i < len(q2_opts) else "?"
            all_paths.append((arch, i, tier, q2_text))
            if tier == 3:
                tier3_list.append((arch, i, q2_text))
                arch_counts[arch] = arch_counts.get(arch, 0) + 1
    
    print(f'=== base={bv} "{title}" ===')
    print(f'    NPC: {npc} ({npc_title})')
    print(f'    {desc}')
    for arch, i, q2 in tier3_list:
        print(f'    TIER 3: {arch} -> Q2[{i}] "{q2[:80]}"')
    print()

print("--- Tier 3 archetype distribution ---")
for arch, count in sorted(arch_counts.items(), key=lambda x: -x[1]):
    print(f"  {arch}: {count}")
