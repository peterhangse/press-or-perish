import json
from collections import Counter

with open('data/stories.json') as f:
    stories = json.load(f)

print(f'Total stories: {len(stories)}')
print()

towns = Counter(s.get('town','unknown') for s in stories)
print('BY TOWN:')
for k,v in towns.most_common(): print(f'  {k}: {v}')

print()
print('BY BASE_VALUE:')
bv = Counter(s.get('base_value') for s in stories)
for k,v in sorted(bv.items()): print(f'  {k}: {v}')

print()
print('BY SOURCE_TYPE:')
st = Counter(s.get('source_type') for s in stories)
for k,v in st.most_common(): print(f'  {k}: {v}')

print()
print('BY DIFFICULTY:')
d = Counter(s.get('difficulty') for s in stories)
for k,v in d.most_common(): print(f'  {k}: {v}')

print()
print('BY CATEGORY:')
c = Counter(s.get('category') for s in stories)
for k,v in c.most_common(): print(f'  {k}: {v}')

print()
print('STORY IDS:')
for s in stories:
    print(f'  {s["id"]} | bv={s["base_value"]} | {s["difficulty"]} | {s["source_type"]} | {s["category"]} | {s["town"]}')
