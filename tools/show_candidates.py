#!/usr/bin/env python3
"""Extract the best promotion candidate for each story missing tier 3."""
import json

with open("data/stories.json") as f:
    stories = json.load(f)

missing = []
for s in sorted(stories, key=lambda x: x.get("base_value", 0)):
    interview = s.get("interview", {})
    branches = interview.get("branches", {})
    max_tier = 0
    for arch, branch in branches.items():
        for out in branch.get("outcomes", []):
            t = out.get("tier", 0)
            if t > max_tier:
                max_tier = t
    if max_tier >= 3:
        continue
    
    # Find best candidate to promote (highest existing tier, prefer friendly/direct over pressure/silence)
    best = None
    best_score = -1
    arch_pref = {"friendly": 4, "direct": 3, "pressure": 2, "silence": 1}
    for arch, branch in branches.items():
        q2_opts = branch.get("q2_options", [])
        outcomes = branch.get("outcomes", [])
        for i, out in enumerate(outcomes):
            tier = out.get("tier", 0)
            score = tier * 10 + arch_pref.get(arch, 0)
            if score > best_score:
                best_score = score
                q2_text = q2_opts[i]["text"] if i < len(q2_opts) else "?"
                best = {
                    "arch": arch,
                    "q2_idx": i,
                    "q2_text": q2_text,
                    "current_tier": tier,
                    "response": out.get("response", ""),
                    "feedback": out.get("feedback", ""),
                    "note": out.get("note", ""),
                    "expression": out.get("expression", ""),
                }
    
    print(f'=== base={s["base_value"]} "{s["title"]}" ===')
    print(f'  Description: {s.get("description", "")[:120]}')
    print(f'  Promote: {best["arch"]} -> Q2[{best["q2_idx"]}] (tier {best["current_tier"]} -> 3)')
    print(f'  Q2 question: {best["q2_text"]}')
    print(f'  Current response: {best["response"][:150]}')
    print(f'  Current feedback: {best["feedback"]}')
    print(f'  Current note: {best["note"]}')
    print()
