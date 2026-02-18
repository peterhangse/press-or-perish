#!/usr/bin/env python3
"""Generate short factual notes for interview responses in stories.json.

Scores each sentence by informativeness (numbers, names, dates, factual verbs)
and picks the most fact-dense one as the note.
"""

import json
import re
import os

STORIES_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'stories.json')


def score_sentence(sent):
    """Score a sentence by how informative/factual it is."""
    score = 0
    lower = sent.lower()

    # Numbers = concrete facts
    score += len(re.findall(r'\d+', sent)) * 3

    # Proper nouns (capitalized words mid-sentence) = specific details
    words = sent.split()
    for w in words[1:]:
        if w[0:1].isupper() and not w.isupper() and len(w) > 2:
            score += 2

    # Time/date words
    time_words = [
        'january', 'february', 'march', 'april', 'may', 'june',
        'july', 'august', 'september', 'october', 'november', 'december',
        'monday', 'tuesday', 'wednesday', 'thursday', 'friday',
        'morning', 'evening', 'night', 'week', 'month', 'year',
        'spring', 'summer', 'autumn', 'winter', 'last', 'since',
    ]
    for tw in time_words:
        if tw in lower:
            score += 2

    # Causal/factual connectors
    fact_words = [
        'because', 'caused', 'broke', 'costs', 'paid', 'removed',
        'installed', 'built', 'sold', 'bought', 'signed', 'called',
        'reported', 'died', 'injured', 'arrested', 'fired', 'hired',
        'permit', 'document', 'contract', 'money', 'budget', 'million',
        'kronor', 'percent', 'council', 'board', 'meeting', 'vote',
        'inspection', 'accident', 'corruption', 'bribe',
    ]
    for fw in fact_words:
        if fw in lower:
            score += 2

    # Penalty for emotional/filler content
    filler = [
        '!', '?', 'i feel', 'i think', 'i mean', 'i know', 'you know',
        'well', 'listen', 'look', 'please', 'sigh', 'crying', 'yell',
        '*', 'silence', 'pause',
    ]
    for f in filler:
        if f in lower:
            score -= 2

    # Penalty for very short sentences
    if len(sent) < 15:
        score -= 3

    # Bonus for medium-length (good factual sentences tend to be 30-80 chars)
    if 25 <= len(sent) <= 80:
        score += 1

    return score


def extract_note(text):
    """Extract a short factual note from a dialogue response."""
    if not text:
        return '...'

    # Split into sentences
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    # Also split on em dash
    expanded = []
    for s in sentences:
        parts = re.split(r'\s+\u2014\s+', s)
        expanded.extend(parts)
    sentences = [s.strip() for s in expanded if s.strip() and len(s.strip()) > 4]

    if not sentences:
        return text[:40] if text else '...'

    # Score each sentence and pick the best
    scored = [(score_sentence(s), s) for s in sentences]
    scored.sort(key=lambda x: x[0], reverse=True)
    best = scored[0][1]

    # Clean up dialogue markers
    strip_patterns = [
        r'^\.{2,}\s*',
        r'^\*[^*]+\*\s*',
        r'^Yes,?\s*', r'^No,?\s*',
        r'^Well,?\s*', r'^Look,?\s*', r'^Listen,?\s*',
        r'^Okay,?\s*', r'^Fine,?\s*', r'^Right,?\s*',
        r'^Sure,?\s*', r'^But\s+', r'^And\s+',
        r'^I mean,?\s*', r'^You know,?\s*',
        r'^Honestly,?\s*', r'^Frankly,?\s*',
        r'^To be honest,?\s*', r'^The truth is,?\s*',
        r'^Between us,?\s*', r'^Off the record,?\s*',
    ]

    cleaned = best
    for pat in strip_patterns:
        cleaned = re.sub(pat, '', cleaned, flags=re.IGNORECASE).strip()

    if not cleaned:
        cleaned = best

    # Remove trailing punctuation
    cleaned = cleaned.rstrip('.!?')

    # Truncate to ~50 chars at word boundary
    if len(cleaned) > 50:
        words = cleaned[:50].rsplit(' ', 1)
        cleaned = words[0] if len(words) > 1 else cleaned[:47]
        cleaned = cleaned.rstrip(',;:-') + '...'

    # Capitalize first letter
    if cleaned:
        cleaned = cleaned[0].upper() + cleaned[1:]

    return cleaned


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
