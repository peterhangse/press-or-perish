#!/usr/bin/env python3
"""Audit all player-facing text for character length violations.

Limits (based on analysis of what already reads well):
  lead_text      ≤ 90 chars
  Q2 option text ≤ 70 chars
  Q1 response    ≤ 130 chars
  Onboarding     ≤ 150 chars
  Farewell       ≤ 130 chars
"""
import json, os, sys

DATA = os.path.join(os.path.dirname(__file__), '..', 'data')

LIMITS = {
    'lead_text': 90,
    'q2_option': 70,
    'q1_response': 130,
    'onboarding': 150,
    'farewell': 130,
}

def audit_stories(stories):
    violations = []
    for s in stories:
        sid = s['id']
        town = s.get('town', 'smastad')

        # Lead text
        lt = s.get('lead_text', '')
        if len(lt) > LIMITS['lead_text']:
            violations.append((town, sid, 'lead_text', len(lt), lt))

        iv = s.get('interview', {})

        # Q1 responses
        for q1 in iv.get('q1_options', []):
            arch = q1.get('archetype', '?')
            for branch in q1.get('branches', []):
                resp = branch.get('response', '')
                if len(resp) > LIMITS['q1_response']:
                    violations.append((town, sid, f'q1/{arch}/response', len(resp), resp))

                # Q2 options
                q2 = branch.get('q2', {})
                for i, opt in enumerate(q2.get('options', [])):
                    txt = opt.get('text', '')
                    if len(txt) > LIMITS['q2_option']:
                        violations.append((town, sid, f'q2/{arch}/opt{i+1}', len(txt), txt))

    return violations


def audit_towns(towns):
    violations = []
    for t in towns:
        tid = t.get('id', '?')

        for i, step in enumerate(t.get('onboardingSteps', [])):
            txt = step.get('text', '')
            if len(txt) > LIMITS['onboarding']:
                violations.append(('towns', tid, f'onboarding[{i}]', len(txt), txt))

        for i, step in enumerate(t.get('farewellSequence', [])):
            txt = step.get('text', '')
            if len(txt) > LIMITS['farewell']:
                violations.append(('towns', tid, f'farewell[{i}]', len(txt), txt))

    return violations


def main():
    stories = json.load(open(os.path.join(DATA, 'stories.json')))
    towns = json.load(open(os.path.join(DATA, 'towns.json')))

    v_stories = audit_stories(stories)
    v_towns = audit_towns(towns)
    all_v = v_stories + v_towns

    if not all_v:
        print("✅ No violations found.")
        return 0

    # Group by category
    by_cat = {}
    for town, sid, field, length, text in all_v:
        cat = field.split('/')[0] if '/' in field else field
        by_cat.setdefault(cat, []).append((town, sid, field, length, text))

    total = len(all_v)
    print(f"⚠️  {total} violation(s) found\n")

    for cat in sorted(by_cat):
        items = by_cat[cat]
        # Determine limit
        if cat == 'lead_text':
            limit = LIMITS['lead_text']
        elif cat == 'q2':
            limit = LIMITS['q2_option']
        elif cat == 'q1':
            limit = LIMITS['q1_response']
        elif cat.startswith('onboarding'):
            limit = LIMITS['onboarding']
        elif cat.startswith('farewell'):
            limit = LIMITS['farewell']
        else:
            limit = '?'

        print(f"── {cat} (limit: {limit}) ── {len(items)} violation(s)")
        for town, sid, field, length, text in sorted(items, key=lambda x: -x[3]):
            over = length - (limit if isinstance(limit, int) else 0)
            print(f"  [{town}/{sid}] {field}  {length} chars (+{over})")
            print(f"    \"{text}\"")
        print()

    return 1


if __name__ == '__main__':
    sys.exit(main())
