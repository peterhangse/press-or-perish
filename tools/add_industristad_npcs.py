#!/usr/bin/env python3
"""Add 28 Industristad NPCs to npcs.json"""
import json, os

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

with open('data/npcs.json', 'r') as f:
    npcs = json.load(f)

# Remove any existing Industristad NPCs (idempotent)
npcs = [n for n in npcs if n.get('town') != 'industristad']

new_npcs = [
    {
        "id": "solveig_lindgren", "name": "Solveig Lindgren", "role": "Canteen worker", "age": 47,
        "default_expression": "guarded", "expressions": ["guarded", "open", "nervous", "neutral"],
        "unique_detail": "apron_stains", "clothing_color": "#7a6a5a",
        "initial_demeanor": "Busy, wiping hands on apron, sighs when she sees you", "town": "industristad"
    },
    {
        "id": "gustav_nilsson_i", "name": "Gustav Nilsson", "role": "Dock worker", "age": 38,
        "default_expression": "neutral", "expressions": ["neutral", "guarded", "open", "hostile", "defiant"],
        "unique_detail": "anchor_tattoo", "clothing_color": "#4a5a7a",
        "initial_demeanor": "Leaning against crates, arms crossed, sizing you up", "town": "industristad"
    },
    {
        "id": "ove_hedberg", "name": "Ove Hedberg", "role": "Maintenance worker", "age": 52,
        "default_expression": "guarded", "expressions": ["guarded", "nervous", "open", "defiant"],
        "unique_detail": "oil_stained_hands", "clothing_color": "#5a5a4a",
        "initial_demeanor": "Keeps looking over his shoulder, fidgeting with wrench", "town": "industristad"
    },
    {
        "id": "bengt_larsson_i", "name": "Bengt Larsson", "role": "Municipal planner", "age": 55,
        "default_expression": "confident", "expressions": ["confident", "evasive", "nervous", "hostile"],
        "unique_detail": "thick_glasses", "clothing_color": "#5a5a6a",
        "initial_demeanor": "Jovial handshake, too eager to be helpful", "town": "industristad"
    },
    {
        "id": "lars_erik_nordin", "name": "Lars-Erik Nordin", "role": "Fishing club chairman", "age": 61,
        "default_expression": "neutral", "expressions": ["neutral", "guarded", "open", "nostalgic"],
        "unique_detail": "fishing_hat", "clothing_color": "#6a7a5a",
        "initial_demeanor": "Sitting by the river, staring at the water, barely looks up", "town": "industristad"
    },
    {
        "id": "tommy_andersson_i", "name": "Tommy Andersson", "role": "Apprentice welder", "age": 19,
        "default_expression": "nervous", "expressions": ["nervous", "guarded", "open", "defiant"],
        "unique_detail": "welding_burns", "clothing_color": "#5a6a8a",
        "initial_demeanor": "Fidgeting, glancing back toward the factory gate", "town": "industristad"
    },
    {
        "id": "lennart_engstrom", "name": "Lennart Engström", "role": "Retired mill worker", "age": 68,
        "default_expression": "nostalgic", "expressions": ["nostalgic", "guarded", "open", "defiant", "neutral"],
        "unique_detail": "cane", "clothing_color": "#6a5a4a",
        "initial_demeanor": "Sitting on a park bench, coat buttoned against the cold", "town": "industristad"
    },
    {
        "id": "folke_dahlberg", "name": "Folke Dahlberg", "role": "Senior union steward", "age": 58,
        "default_expression": "defiant", "expressions": ["defiant", "guarded", "open", "hostile", "neutral"],
        "unique_detail": "union_badge", "clothing_color": "#8a4a4a",
        "initial_demeanor": "Standing firm, jaw set, measures you with one look", "town": "industristad"
    },
    {
        "id": "gunhild_persson_i", "name": "Gunhild Persson", "role": "Factory worker's wife", "age": 44,
        "default_expression": "nervous", "expressions": ["nervous", "guarded", "open", "defiant"],
        "unique_detail": "worn_shawl", "clothing_color": "#7a6a6a",
        "initial_demeanor": "Holding a cup of coffee with both hands, not drinking", "town": "industristad"
    },
    {
        "id": "per_olov_strand", "name": "Per-Olov Strand", "role": "Shift foreman", "age": 41,
        "default_expression": "guarded", "expressions": ["guarded", "nervous", "evasive", "open", "hostile"],
        "unique_detail": "clipboard", "clothing_color": "#5a5a5a",
        "initial_demeanor": "Checking his watch repeatedly, wants this to be quick", "town": "industristad"
    },
    {
        "id": "kerstin_holmberg", "name": "Kerstin Holmberg", "role": "Industrial nurse", "age": 36,
        "default_expression": "neutral", "expressions": ["neutral", "nervous", "open", "defiant", "guarded"],
        "unique_detail": "nurse_cap", "clothing_color": "#ffffff",
        "initial_demeanor": "Professional composure, hands folded, but eyes betray concern", "town": "industristad"
    },
    {
        "id": "maj_britt_karlsson", "name": "Maj-Britt Karlsson", "role": "Union secretary", "age": 33,
        "default_expression": "nervous", "expressions": ["nervous", "guarded", "open", "defiant", "hostile"],
        "unique_detail": "filing_folders", "clothing_color": "#6a5a7a",
        "initial_demeanor": "Glancing at the door, speaks in a low voice", "town": "industristad"
    },
    {
        "id": "margareta_olsson_i", "name": "Margareta Olsson", "role": "Librarian", "age": 49,
        "default_expression": "neutral", "expressions": ["neutral", "open", "guarded", "nostalgic"],
        "unique_detail": "reading_glasses", "clothing_color": "#7a7a6a",
        "initial_demeanor": "Adjusting glasses, quiet authority, patient listener", "town": "industristad"
    },
    {
        "id": "ulla_bjork", "name": "Ulla Björk", "role": "Tenant association chair", "age": 42,
        "default_expression": "defiant", "expressions": ["defiant", "open", "nervous", "guarded"],
        "unique_detail": "petition_papers", "clothing_color": "#6a6a5a",
        "initial_demeanor": "Standing in a damp hallway, pointing at walls, already angry", "town": "industristad"
    },
    {
        "id": "erik_svensson_i", "name": "Erik Svensson", "role": "Steel worker", "age": 31,
        "default_expression": "guarded", "expressions": ["guarded", "open", "hostile", "nervous", "defiant"],
        "unique_detail": "hard_hat", "clothing_color": "#4a6a8a",
        "initial_demeanor": "Calloused hands, direct eye contact, few words", "town": "industristad"
    },
    {
        "id": "bo_fredriksson_i", "name": "Bo Fredriksson", "role": "Fire inspector", "age": 45,
        "default_expression": "nervous", "expressions": ["nervous", "guarded", "open", "evasive"],
        "unique_detail": "inspector_badge", "clothing_color": "#5a5a6a",
        "initial_demeanor": "Keeps adjusting his tie, avoids looking you in the eye", "town": "industristad"
    },
    {
        "id": "eva_sandberg", "name": "Eva Sandberg", "role": "Hospital administrator", "age": 48,
        "default_expression": "confident", "expressions": ["confident", "evasive", "nervous", "hostile"],
        "unique_detail": "pearl_necklace", "clothing_color": "#7a6a7a",
        "initial_demeanor": "Seated behind desk, fingers steepled, measured smile", "town": "industristad"
    },
    {
        "id": "anna_lena_johansson", "name": "Anna-Lena Johansson", "role": "Welder", "age": 22,
        "default_expression": "defiant", "expressions": ["defiant", "guarded", "open", "nervous"],
        "unique_detail": "welding_mask_up", "clothing_color": "#5a7a6a",
        "initial_demeanor": "Arms crossed, chin up, daring you to ask the wrong question", "town": "industristad"
    },
    {
        "id": "birger_wik", "name": "Birger Wik", "role": "Shipyard manager", "age": 54,
        "default_expression": "evasive", "expressions": ["evasive", "confident", "nervous", "hostile", "guarded"],
        "unique_detail": "cigaret", "clothing_color": "#4a4a5a",
        "initial_demeanor": "Smoking by the office window, not turning around immediately", "town": "industristad"
    },
    {
        "id": "astrid_lindkvist", "name": "Astrid Lindkvist", "role": "Harbor resident", "age": 39,
        "default_expression": "defiant", "expressions": ["defiant", "nervous", "open", "guarded"],
        "unique_detail": "rubber_boots", "clothing_color": "#6a7a6a",
        "initial_demeanor": "Standing at her garden fence, pointing toward the factory smoke", "town": "industristad"
    },
    {
        "id": "sven_bergqvist", "name": "Sven Bergqvist", "role": "Train driver", "age": 46,
        "default_expression": "neutral", "expressions": ["neutral", "nervous", "open", "guarded", "defiant"],
        "unique_detail": "railway_cap", "clothing_color": "#4a4a6a",
        "initial_demeanor": "Sitting in the train cab, still shaking slightly", "town": "industristad"
    },
    {
        "id": "sigrid_aberg", "name": "Sigrid Åberg", "role": "Municipal accountant", "age": 37,
        "default_expression": "nervous", "expressions": ["nervous", "guarded", "open", "defiant"],
        "unique_detail": "calculator", "clothing_color": "#6a6a7a",
        "initial_demeanor": "Speaking barely above a whisper, clutching a folder to her chest", "town": "industristad"
    },
    {
        "id": "dragan_kovacevic", "name": "Dragan Kovačević", "role": "Construction worker", "age": 28,
        "default_expression": "guarded", "expressions": ["guarded", "nervous", "open", "hostile", "defiant"],
        "unique_detail": "wool_cap", "clothing_color": "#5a6a5a",
        "initial_demeanor": "Cautious, speaks slowly in accented Swedish, watching for foreman", "town": "industristad"
    },
    {
        "id": "rune_hellstrom", "name": "Rune Hellström", "role": "Blast furnace worker", "age": 43,
        "default_expression": "neutral", "expressions": ["neutral", "guarded", "open", "hostile", "nervous"],
        "unique_detail": "burn_scar", "clothing_color": "#5a4a4a",
        "initial_demeanor": "Sitting on the factory steps, staring at nothing, heavy breathing", "town": "industristad"
    },
    {
        "id": "gosta_fredriksson", "name": "Gösta Fredriksson", "role": "Retired insulation worker", "age": 71,
        "default_expression": "open", "expressions": ["open", "guarded", "nostalgic", "defiant", "nervous"],
        "unique_detail": "oxygen_tube", "clothing_color": "#7a7a7a",
        "initial_demeanor": "In his kitchen, wheezing between sentences, wife hovering nearby", "town": "industristad"
    },
    {
        "id": "torsten_mansson", "name": "Torsten Månsson", "role": "Mine foreman", "age": 50,
        "default_expression": "evasive", "expressions": ["evasive", "hostile", "nervous", "guarded", "open"],
        "unique_detail": "mining_lamp", "clothing_color": "#4a4a4a",
        "initial_demeanor": "Sweating despite the cold, keeps wiping his forehead", "town": "industristad"
    },
    {
        "id": "arne_sundstrom", "name": "Arne Sundström", "role": "Dockworker", "age": 35,
        "default_expression": "defiant", "expressions": ["defiant", "open", "hostile", "nervous", "guarded"],
        "unique_detail": "docker_hook", "clothing_color": "#5a5a7a",
        "initial_demeanor": "Leaning forward aggressively, jaw tight, needs to tell someone", "town": "industristad"
    },
    {
        "id": "anders_strom", "name": "Anders Ström", "role": "Truck driver", "age": 32,
        "default_expression": "nervous", "expressions": ["nervous", "guarded", "open", "hostile"],
        "unique_detail": "driver_gloves", "clothing_color": "#6a5a5a",
        "initial_demeanor": "Chain-smoking, keeps looking at the road, leg bouncing", "town": "industristad"
    },
]

npcs.extend(new_npcs)

with open('data/npcs.json', 'w') as f:
    json.dump(npcs, f, indent=2, ensure_ascii=False)

smastad = len([n for n in npcs if n.get('town') == 'smastad'])
industristad = len([n for n in npcs if n.get('town') == 'industristad'])
print(f"Total NPCs: {len(npcs)} (Småstad: {smastad}, Industristad: {industristad})")
