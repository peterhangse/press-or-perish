#!/usr/bin/env python3
"""Audit all stories for tier 3 availability."""
import json

with open("data/stories.json") as f:
    stories = json.load(f)

no_tier3 = []
for s in sorted(stories, key=lambda x: x.get("base_value", 0)):
    title = s["title"]
    bv = s.get("base_value", 0)
    interview = s.get("interview", {})
    branches = interview.get("branches", {})
    max_tier = 0
    tier3_paths = []
    all_paths = []
    for arch, branch in branches.items():
        outcomes = branch.get("outcomes", [])
        for i, out in enumerate(outcomes):
            tier = out.get("tier", 0)
            all_paths.append((arch, i, tier))
            if tier > max_tier:
                max_tier = tier
            if tier == 3:
                tier3_paths.append(f"{arch} -> Q2[{i}]")
    tag = "OK" if max_tier >= 3 else "MISS"
    print(f"base={bv} [{tag}] max_tier={max_tier} \"{title}\"")
    if max_tier < 3:
        no_tier3.append((bv, title, all_paths))
        for arch, qi, t in all_paths:
            print(f"    {arch} -> Q2[{qi}]: tier {t}")

print(f"\n--- {len(no_tier3)} stories WITHOUT tier 3 ---")
for bv, title, _ in no_tier3:
    print(f"  base={bv} \"{title}\"")
