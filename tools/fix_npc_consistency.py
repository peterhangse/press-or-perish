import json

with open('data/stories.json') as f:
    stories = json.load(f)

fixes = {
    # birgitta_ekberg: core identity = council member (FP)
    ('missing_girl',       'npc_title'): "Council member (FP), Anna's mother",
    ('äldreboende_svält',  'npc_title'): "Council member (FP), daughter of resident",
    # telefonavlyssning stays as-is: "Opposition council member (FP)"

    # erik_persson: farmer who used to play football
    ('dopingskandal',      'npc_title'): "Farmer, former player Småstads IF",

    # gosta_nilsson: retired police officer throughout
    ('bostadsbubblan',     'npc_title'): "Retired police officer",

    # gunnar_ek: farmer in both
    ('kyrkklockorna',      'npc_title'): "Farmer and church neighbor",

    # helena_strand: healthcare assistant throughout
    ('flyktingmottagning', 'npc_title'): "Healthcare assistant, Red Cross volunteer",

    # inga_johansson: retired nurse throughout
    ('polisvåld',          'npc_title'): "Retired nurse, mother of the victim",

    # karl_lindstrom: fill in missing data + match stöld title
    ('ambulansbristen',    'npc_title'): "Municipal worker, technical services",
    ('ambulansbristen',    'npc_name'):  "Karl Lindström",
    ('ambulansbristen',    'npc_id'):    "karl_lindstrom",

    # margareta_lund: teacher throughout
    ('illegal_soptipp',    'npc_title'): "Teacher, nature conservation member",
}

for story in stories:
    sid = story['id']
    for (story_id, field), value in fixes.items():
        if sid == story_id:
            old = story.get(field)
            story[field] = value
            print(f'[{sid}] {field}: "{old}" -> "{value}"')

with open('data/stories.json', 'w', encoding='utf-8') as f:
    json.dump(stories, f, ensure_ascii=False, indent=2)

print('\nDone.')
