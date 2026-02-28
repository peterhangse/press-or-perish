#!/usr/bin/env python3
"""Generate short factual notes for interview responses in stories.json.

A journalist's notepad captures KEY FACTS, EVIDENCE, and REVELATIONS —
not emotional reactions or stage directions. This algorithm:
1. Strips stage directions (*action text*)
2. Scores sentences by journalistic value (evidence > names > specifics > filler)
3. Strongly favors LATER sentences (revelations come at the end)
4. Combines top facts when a single sentence isn't enough
"""

import json
import re
import os

STORIES_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'stories.json')


def strip_stage_directions(text):
    """Remove *action descriptions* from text."""
    return re.sub(r'\*[^*]+\*\s*', '', text).strip()


def score_sentence(sent, position_ratio=0.0):
    """Score a sentence by journalistic newsworthiness.
    
    position_ratio: 0.0 = first sentence, 1.0 = last sentence
    """
    score = 0
    lower = sent.lower()
    words = sent.split()

    # === HARD DISQUALIFIERS ===
    # Pure filler / emotional / meta
    if re.match(r'^(well|look|listen|okay|fine|right|sure|yes|no|i mean|you know|hmm|huh)\b', lower):
        score -= 5
    if len(sent) < 12:
        score -= 8
    # Pure questions
    if sent.strip().endswith('?') and not any(w in lower for w in ['who', 'where', 'how much', 'how many']):
        score -= 6
    # Pure refusals
    if re.search(r"(get out|leave|we're done|no comment|i can't|nothing to say)", lower):
        score -= 6

    # === EVIDENCE — the gold standard ===
    evidence_words = [
        'document', 'notebook', 'logbook', 'ledger', 'diary', 'minutes',
        'contract', 'receipt', 'invoice', 'letter', 'email', 'report',
        'proof', 'evidence', 'photo', 'recording', 'copy', 'paper',
        'analyzed', 'tested', 'confirmed', 'verified', 'certified',
        'signed', 'stamp', 'seal', 'filed', 'register', 'ampoule',
    ]
    for w in evidence_words:
        if w in lower:
            score += 6

    # === SPECIFIC NAMED DETAILS ===
    # Numbers (amounts, dates, percentages)
    nums = re.findall(r'\d[\d,.\s]*(?:kronor|kr|percent|%|million|billion)?', lower)
    score += len(nums) * 4

    # Proper nouns (names, places) — mid-sentence capitalized words
    for w in words[1:]:
        if w[0:1].isupper() and not w.isupper() and len(w) > 2 and w not in ('I', 'The', 'But', 'And', 'He', 'She', 'We', 'They'):
            score += 3

    # === CONNECTIONS / POWER STRUCTURES ===
    connection_words = [
        'brother', 'sister', 'wife', 'husband', 'cousin', 'son', 'daughter',
        'related', 'connected', 'together', 'relationship', 'conflict of interest',
        'council', 'board', 'chairman', 'commissioner', 'inspector', 'mayor',
        'owns', 'controls', 'runs', 'manages', 'decided', 'approved',
    ]
    for w in connection_words:
        if w in lower:
            score += 4

    # === CONSEQUENCES / DAMAGE ===
    consequence_words = [
        'died', 'dead', 'killed', 'sick', 'injured', 'blood', 'broke',
        'damaged', 'destroyed', 'contaminated', 'poisoned', 'collapsed',
        'fired', 'arrested', 'convicted', 'threatened', 'blackmail',
        'missing', 'disappeared', 'covered up', 'hidden', 'silenced',
    ]
    for w in consequence_words:
        if w in lower:
            score += 4

    # === SUBSTANCE / SPECIFICS ===
    substance_words = [
        'nandrolone', 'steroid', 'substance', 'chemical', 'asbestos',
        'mercury', 'lead', 'arsenic', 'doping', 'injection',
        'money', 'budget', 'cost', 'price', 'worth', 'paid', 'bribe',
        'permit', 'license', 'regulation', 'law', 'illegal', 'violation',
    ]
    for w in substance_words:
        if w in lower:
            score += 3

    # === ADMISSIONS / REVELATIONS ===
    reveal_words = [
        'admitted', 'confessed', 'the truth', 'turns out', 'actually',
        'secretly', 'nobody knows', 'what really happened',
        'all names', 'all dates', 'all doses', 'everything',
        'i can prove', 'i have proof', 'i saw', 'i heard', 'witness',
    ]
    for w in reveal_words:
        if w in lower:
            score += 5

    # === POSITION BONUS ===
    # Revelations tend to come LATER in NPC responses
    score += position_ratio * 4

    # Medium-length sentences are ideal for notes
    if 25 <= len(sent) <= 100:
        score += 1

    return score


def extract_note(text):
    """Extract a short factual note capturing the KEY journalistic detail."""
    if not text:
        return '...'

    # Strip stage directions first
    clean = strip_stage_directions(text)
    if not clean:
        clean = text

    # Split into sentences (period, exclamation, question mark, em dash)
    sentences = re.split(r'(?<=[.!?])\s+', clean.strip())
    expanded = []
    for s in sentences:
        parts = re.split(r'\s+\u2014\s+', s)
        expanded.extend(parts)
    sentences = [s.strip() for s in expanded if s.strip() and len(s.strip()) > 4]

    if not sentences:
        return clean[:50] if clean else '...'

    # Score each sentence with position bonus
    n = len(sentences)
    scored = []
    for i, s in enumerate(sentences):
        pos = i / max(n - 1, 1)  # 0.0 for first, 1.0 for last
        score = score_sentence(s, pos)
        scored.append((score, i, s))
    scored.sort(key=lambda x: x[0], reverse=True)

    best_score, best_idx, best = scored[0]

    # If best score is very low, try combining top 2 short fragments
    if best_score < 3 and len(scored) > 1:
        top2 = sorted(scored[:2], key=lambda x: x[1])  # order by position
        combined = top2[0][2].rstrip('.!?') + '. ' + top2[1][2]
        if len(combined) <= 65:
            best = combined

    # Clean up
    best = best.strip()

    # Remove leading filler
    filler_starts = [
        r'^\.{2,}\s*',
        r'^Yes,?\s+', r'^No,?\s+',
        r'^Well,?\s+', r'^Look,?\s+', r'^Listen,?\s+',
        r'^Okay,?\s+', r'^Fine,?\s+', r'^Right,?\s+',
        r'^Sure,?\s+', r'^But\s+', r'^And\s+',
        r'^I mean,?\s+', r'^You know,?\s+',
        r'^Honestly,?\s+', r'^Frankly,?\s+',
        r'^To be honest,?\s+', r'^The truth is,?\s+',
        r'^Between us,?\s+', r'^Off the record,?\s+',
    ]
    for pat in filler_starts:
        best = re.sub(pat, '', best, flags=re.IGNORECASE).strip()

    if not best:
        best = scored[0][2]

    # Remove trailing punctuation
    best = best.rstrip('.!?')

    # Truncate to ~55 chars at word boundary
    if len(best) > 55:
        words = best[:55].rsplit(' ', 1)
        best = words[0] if len(words) > 1 else best[:52]
        best = best.rstrip(',;:-') + '...'

    # Capitalize first letter
    if best:
        best = best[0].upper() + best[1:]

    return best


def main():
    with open(STORIES_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    total_notes = 0
    for story in data:
        branches = story.get('interview', {}).get('branches', {})
        for arch, branch in branches.items():
            q1_resp = branch.get('q1_response', '')
            branch['q1_note'] = extract_note(q1_resp)
            total_notes += 1

            for outcome in branch.get('outcomes', []):
                resp = outcome.get('response', '')
                outcome['note'] = extract_note(resp)
                total_notes += 1

    with open(STORIES_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Generated {total_notes} notes across {len(data)} stories.")
    print()
    print("=== SAMPLE NOTES ===")
    for story in data[:8]:
        print(f"\n  {story['title']}")
        for arch, branch in story.get('interview', {}).get('branches', {}).items():
            print(f"    {arch} Q1: \"{branch['q1_note']}\"")
            for i, o in enumerate(branch.get('outcomes', [])):
                print(f"      Q2[{i}]: \"{o['note']}\"")


if __name__ == '__main__':
    main()
