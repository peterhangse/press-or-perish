#!/usr/bin/env python3
"""Show all Q2 options for all archetypes on the 20 recently-upgraded stories."""
import json

TARGETS = [
    "The Dog Show in Småstad",
    "The Church Bells That Never Stop",
    "The Shoplifting at ICA",
    "The New Parking Lot by the Square",
    "Christmas Bazaar at the Factory",
    "The Water Leak on Storgatan",
    "The Power Outage",
    "The Teacher Shortage",
    "The Land Deal",
    "The Road Project That Never Gets Finished",
    "The School Food Nobody Wants to Eat",
    "The Ice Rink Running Out of Money",
    "The Library's Last Days",
    "The Traffic Accident at the School",
    "The Bootleg Liquor",
    "The Municipality's Christmas Party",
    "The Factory Closure",
    "The Municipal Storage",
    "The Fire in Eriksson's Barn",
    "The Dead Cat with the Note",
]

with open("data/stories.json") as f:
    stories = json.load(f)

for s in sorted(stories, key=lambda x: x.get("base_value", 0)):
    if s["title"] not in TARGETS:
        continue
    title = s["title"]
    bv = s["base_value"]
    npc = s.get("npc_name", "?")
    npc_title = s.get("npc_title", "")
    demeanor = ""
    # try to get NPC demeanor from npcs.json
    interview = s.get("interview", {})
    branches = interview.get("branches", {})
    
    print(f'=== base={bv} "{title}" — {npc} ({npc_title}) ===')
    for arch in ["friendly", "direct", "pressure", "silence"]:
        if arch not in branches:
            continue
        branch = branches[arch]
        q2_opts = branch.get("q2_options", [])
        outcomes = branch.get("outcomes", [])
        print(f"  [{arch}]")
        for i, (q2, out) in enumerate(zip(q2_opts, outcomes)):
            tier = out.get("tier", 0)
            marker = " <<<T3" if tier == 3 else ""
            print(f"    Q2[{i}] (tier {tier}{marker}): \"{q2['text'][:80]}\"")
    print()
