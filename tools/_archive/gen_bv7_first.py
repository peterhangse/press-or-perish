#!/usr/bin/env python3
"""Add first 2 bv7 stories for Industristad."""
import json, os

STORIES_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'stories.json')

NEW_STORIES = [
    {
        "id": "direktorsvillan",
        "title": "The Director's Villa",
        "description": "Ståhlbergs Stålverk built a luxury villa for the mill director using company funds — while cutting worker benefits.",
        "lead_text": "A construction foreman says the new villa on Bergshöjden was billed to a 'facility maintenance' account at the mill.",
        "preview": "An anonymous envelope arrives with a construction invoice marked 'Confidential.'",
        "source_type": "document",
        "difficulty": "hard",
        "base_value": 7,
        "category": "corruption",
        "npc_id": "birger_wik",
        "npc_name": "Birger Wik",
        "npc_title": "Construction Foreman",
        "town": "industristad",
        "interview": {
            "opening_line": "I built that house. Marble floors, imported tiles, a wine cellar. And every invoice went to 'Facility Maintenance — Ståhlbergs Stålverk.' I've got duplicates.",
            "q1_options": [
                {"archetype": "friendly", "text": "That's a big thing to share, Birger. What made you come forward?"},
                {"archetype": "direct", "text": "What's the total cost? And what exactly was billed to the company?"},
                {"archetype": "pressure", "text": "If you built it, you're part of it. Why should anyone trust you now?"},
                {"archetype": "silence", "text": "..."}
            ],
            "branches": {
                "friendly": {
                    "q1_response": "My men built worker housing too. Those apartments? Thin walls, no insulation, shared toilets. Meanwhile Bergström gets Italian marble. Same company. Same budget line. Different world.",
                    "expression_hint": "Stubs out cigarette, finally turns around",
                    "q1_note": "Worker housing vs. director's villa — same budget line",
                    "q2_options": [
                        {"text": "How much did the villa cost compared to the worker housing?"},
                        {"text": "Who authorized billing it to facility maintenance?"},
                        {"text": "Do you have the invoices with you?"}
                    ],
                    "outcomes": [
                        {
                            "tier": 1,
                            "response": "The villa? At least 400,000 kronor. A worker apartment renovation? 8,000. It's right there in the numbers. But try proving the villa isn't a 'company facility.' That's what they'll say.",
                            "expression": "guarded",
                            "feedback": "The cost disparity is clear, but 'company facility' is a plausible defense. Needs more.",
                            "note": "Villa: 400,000 kr. Worker apartment: 8,000 kr."
                        },
                        {
                            "tier": 2,
                            "response": "Bergström's personal secretary signed off on every invoice. Eva Sandberg. She coded them to 'Facility Maintenance — General.' The bookkeeper wouldn't know a villa from a warehouse. It's buried in a budget of millions.",
                            "expression": "open",
                            "feedback": "The billing chain is clear — Bergström's own secretary approved the fraudulent coding. Traceable.",
                            "note": "Secretary Eva Sandberg signed off, coded as 'General' maintenance"
                        },
                        {
                            "tier": 3,
                            "response": "Here. *slides envelope* Twenty-three invoices. Italian marble — 48,000 kronor. Custom kitchen from Stockholm — 62,000. Wine cellar refrigeration — 15,000. All stamped 'Ståhlbergs Stålverk — Facility Maintenance.' The workers' canteen budget was cut by 50,000 the same quarter.",
                            "expression": "open",
                            "feedback": "Twenty-three invoices with specific luxury items, all coded to the mill. The canteen cut in the same quarter is devastating context.",
                            "note": "23 invoices: marble 48k, kitchen 62k, wine cellar 15k"
                        }
                    ]
                },
                "direct": {
                    "q1_response": "Total? North of 400,000 kronor. Italian marble floors — 48,000. Custom cabinetry — 35,000. The wine cellar alone was 15,000 for the refrigeration unit. All billed as 'facility maintenance' at the mill.",
                    "expression_hint": "Pulls out a bundle of carbon copies",
                    "q1_note": "400,000+ kronor total, all billed to mill maintenance",
                    "q2_options": [
                        {"text": "Who authorized these invoices? Is there a paper trail?"},
                        {"text": "Does Bergström actually live there? Is it registered as his?"},
                        {"text": "Were any of your workers uncomfortable with this arrangement?"}
                    ],
                    "outcomes": [
                        {
                            "tier": 1,
                            "response": "Bergström's office authorized everything. His secretary handles the paperwork. The invoices come to me, I send them up, they come back approved. I just build what I'm told.",
                            "expression": "guarded",
                            "feedback": "Confirms the authorization chain but positions himself as just following orders. No documentary proof offered.",
                            "note": "Bergström's office approved all invoices"
                        },
                        {
                            "tier": 2,
                            "response": "The property is registered to 'Ståhlbergs Fastigheter AB' — a subsidiary. Bergström is listed as... wait for it... 'tenant.' Rent? One krona per year. One krona. For a 400,000 kronor villa.",
                            "expression": "open",
                            "feedback": "The subsidiary ownership and symbolic rent is a classic corporate perk disguised as legitimate. One krona rent is indefensible.",
                            "note": "Bergström 'rents' the 400k villa for 1 krona/year"
                        },
                        {
                            "tier": 3,
                            "response": "Here's what'll really burn them. I have the board meeting minutes where they approved cutting the canteen budget by 50,000 kronor. Same meeting — page four — 'Director housing allocation: 420,000 kronor.' Same meeting. Same page. Workers eat slop so the director gets marble.",
                            "expression": "open",
                            "feedback": "Board minutes showing canteen cuts and villa spending approved in the same meeting. The juxtaposition is explosive.",
                            "note": "Same board meeting: cut canteen 50k, allocated villa 420k"
                        }
                    ]
                },
                "pressure": {
                    "q1_response": "Part of it? I'm a contractor. I build what they pay me to build. You want to blame the bricklayer for what the architect designs? Fine. But I'm here now, aren't I?",
                    "expression_hint": "Jaw tightens, turns to face you fully",
                    "q1_note": "Defensive — 'I build what they pay me to build'",
                    "q2_options": [
                        {"text": "Fair enough. So what exactly did you build? Walk me through it."},
                        {"text": "Did you ever question why a private villa was on a company account?"},
                        {"text": "What's in it for you? Why come forward now?"}
                    ],
                    "outcomes": [
                        {
                            "tier": 1,
                            "response": "I questioned it once. Eva Sandberg told me to submit my invoices and keep my mouth shut. So I did. For three years. But now they owe me 32,000 kronor in unpaid bills. So here I am.",
                            "expression": "guarded",
                            "feedback": "He's a disgruntled creditor, not a whistleblower. The unpaid bills motive weakens his credibility, but confirms the billing scheme.",
                            "note": "Wik is owed 32,000 kr — motive for coming forward"
                        },
                        {
                            "tier": 2,
                            "response": "Four bedrooms. Three bathrooms. A sauna. Italian marble in the entrance hall. Custom wine cellar. Heated garage for two cars. This isn't a company guest house — it's a palace. And every kronor came from the same pot that pays for worker safety equipment.",
                            "expression": "open",
                            "feedback": "The detailed specifications make it inarguable — this is a private luxury home. The safety equipment budget connection raises the stakes.",
                            "note": "4 bedrooms, sauna, wine cellar, heated garage — from safety budget"
                        },
                        {
                            "tier": 3,
                            "response": "You want the truth? They didn't just build a house. They made my crew sign non-disclosure agreements. For a 'maintenance project.' When do maintenance workers sign NDAs? When someone has something to hide. I've got my copy right here.",
                            "expression": "open",
                            "feedback": "NDAs for construction workers on a 'maintenance project' proves the company knew this was fraudulent. The signed NDA is a document you can photograph.",
                            "note": "Workers forced to sign NDAs for 'maintenance project'"
                        }
                    ]
                },
                "silence": {
                    "q1_response": "...You're quiet. Good. I don't trust reporters who talk too much. Last guy from Fabriksbladet asked two questions and left. Printed that the villa was a 'company investment in local property.' Useless.",
                    "expression_hint": "Studies you, then reaches into his jacket pocket",
                    "q1_note": "Fabriksbladet whitewashed the story",
                    "q2_options": [
                        {"text": "..."},
                        {"text": "I'm not from Fabriksbladet."},
                        {"text": "What didn't the other reporter bother to ask?"}
                    ],
                    "outcomes": [
                        {
                            "tier": 1,
                            "response": "He didn't ask about the wine cellar. Or the marble. Or why a 'company facility' has a private sauna and a heated two-car garage. He saw the nice facade and wrote a nice story. That's this town.",
                            "expression": "guarded",
                            "feedback": "Luxury details are clear but secondhand — your word against theirs without documents.",
                            "note": "Wine cellar, marble, sauna, heated garage"
                        },
                        {
                            "tier": 2,
                            "response": "He didn't ask why Bergström pays one krona per year in rent. One. For a property worth half a million. You could print that single fact and let people do the math.",
                            "expression": "open",
                            "feedback": "The one-krona rent is a perfect single-fact story. Simple, devastating, impossible to spin.",
                            "note": "1 krona/year rent for a 500,000 kr property"
                        },
                        {
                            "tier": 3,
                            "response": "He didn't ask for these. *pulls out folded papers* Board minutes. The canteen budget was cut 50,000 kronor and the 'director housing allocation' of 420,000 was approved in the same meeting. Same page. And here — my crew's NDAs. They made bricklayers sign confidentiality agreements. For 'maintenance.'",
                            "expression": "open",
                            "feedback": "Board minutes plus NDAs — the company both approved the spending and tried to hide it. Two documents that tell the whole story.",
                            "note": "Board minutes + crew NDAs: approved spending and hid it"
                        }
                    ]
                }
            }
        },
        "headlines": [
            {"text": "DIRECTOR'S NEW HOME BILLED AS MILL MAINTENANCE", "tone": "Factual"},
            {"text": "MARBLE FLOORS FOR THE BOSS, THIN SOUP FOR THE WORKERS", "tone": "Confrontational"},
            {"text": "420,000 KRONOR VILLA — CANTEEN CUT SAME MEETING", "tone": "Exposing"}
        ]
    },
    {
        "id": "tysta_dodsfall",
        "title": "The Silent Deaths",
        "description": "Workers at the chemical plant have been dying at unusually high rates, but the company's health records show nothing unusual.",
        "lead_text": "Five funerals in two years from the chromium division. All men under fifty-five. The company says it's coincidence.",
        "preview": "A widow stands at the factory gate holding a photograph.",
        "source_type": "street",
        "difficulty": "hard",
        "base_value": 7,
        "category": "health",
        "npc_id": "gunhild_persson_i",
        "npc_name": "Gunhild Persson",
        "npc_title": "Factory Worker's Widow",
        "town": "industristad",
        "interview": {
            "opening_line": "My husband Erik worked in the chromium division for eighteen years. He died in March. Forty-seven years old. They said it was 'general health decline.' He was strong as an ox before he started there.",
            "q1_options": [
                {"archetype": "friendly", "text": "I'm sorry for your loss, Gunhild. Can you tell me about Erik?"},
                {"archetype": "direct", "text": "Five deaths in two years from one division. What do the death certificates say?"},
                {"archetype": "pressure", "text": "The company is calling these coincidences. Do you believe that?"},
                {"archetype": "silence", "text": "..."}
            ],
            "branches": {
                "friendly": {
                    "q1_response": "Erik loved fishing. Weekends at the lake, always. When he started losing weight, he said it was the shift work. Then the coughing started. Then the blood. It took fourteen months from the first symptom to the funeral.",
                    "expression_hint": "Holding the photograph against her chest",
                    "q1_note": "14 months from first symptoms to death",
                    "q2_options": [
                        {"text": "Did Erik ever talk about conditions in the chromium division?"},
                        {"text": "Have you spoken to the other widows? Are their stories similar?"},
                        {"text": "What did the doctors say was the cause?"}
                    ],
                    "outcomes": [
                        {
                            "tier": 1,
                            "response": "He said the ventilation never worked properly. Yellow dust on everything. They gave them paper masks — flimsy things that fell apart in an hour. He'd come home with yellow fingers.",
                            "expression": "guarded",
                            "feedback": "Poor ventilation and inadequate masks suggest exposure, but no direct link to deaths established.",
                            "note": "Yellow dust, paper masks that fell apart in an hour"
                        },
                        {
                            "tier": 2,
                            "response": "Maja Lindqvist lost her husband in September. Britta Holm, hers in January. We talk. All the same — weight loss, coughing, blood. And all the death certificates say different things. 'Respiratory failure.' 'Liver disease.' 'Cardiac arrest.' Never the word 'chromium.' Never 'occupational.'",
                            "expression": "open",
                            "feedback": "Three widows, same symptoms, but different causes of death on certificates — a pattern of avoiding the occupational link.",
                            "note": "Three widows, same symptoms, different listed causes of death"
                        },
                        {
                            "tier": 3,
                            "response": "Erik kept a diary. He wrote down every day his eyes burned, every nosebleed, every time the ventilation broke down. And he wrote this, three months before he died: 'Foreman Berg said if we report the ventilation we'll be moved to the loading dock at half pay. So we breathe the dust and shut up.'",
                            "expression": "open",
                            "feedback": "The diary is firsthand documentation — a worker recording his own poisoning, plus the foreman's threat against reporting. Devastating.",
                            "note": "Diary: foreman threatened workers who reported ventilation issues"
                        }
                    ]
                },
                "direct": {
                    "q1_response": "I have Erik's death certificate here. 'Respiratory failure due to chronic pulmonary condition.' No mention of chromium. No mention of occupation. I checked with Maja Lindqvist — her husband's says 'liver disease.' Britta Holm's husband: 'cardiac arrest.' Same division, same symptoms, different causes.",
                    "expression_hint": "Unfolds documents with careful, practiced movements",
                    "q1_note": "Same symptoms, different causes on death certificates",
                    "q2_options": [
                        {"text": "Did anyone request an independent autopsy or occupational health review?"},
                        {"text": "Who signed the death certificates? The same doctor?"},
                        {"text": "What do you know about chromium exposure and its health effects?"}
                    ],
                    "outcomes": [
                        {
                            "tier": 1,
                            "response": "I asked for a review. The company doctor — Dr. Wennerholm — said there was 'no evidence of occupational causation.' The union rep said he'd look into it. That was four months ago. Nothing.",
                            "expression": "guarded",
                            "feedback": "Same company doctor blocking investigation as in the insurance story. Pattern of suppression, but no proof.",
                            "note": "Company doctor found 'no evidence of occupational causation'"
                        },
                        {
                            "tier": 2,
                            "response": "Different doctors signed them, but the cause-of-death summaries all came through Dr. Wennerholm's office first. He reviews all worker deaths at the mill. He decides what to write. And he never writes 'occupational.'",
                            "expression": "open",
                            "feedback": "Wennerholm acting as gatekeeper for cause-of-death classification. He filters out occupational causes before other doctors sign.",
                            "note": "Wennerholm reviews all worker deaths, never writes 'occupational'"
                        },
                        {
                            "tier": 3,
                            "response": "A doctor in Gothenburg — not connected to the mill — told me hexavalent chromium is a known carcinogen. Banned in many countries. Not here. And I found this in Erik's locker. *hands over a paper* Air quality measurements from 1971. Someone at the mill tested it once. The chromium levels were fourteen times the recommended limit. This paper was never shown to the workers.",
                            "expression": "open",
                            "feedback": "Internal air quality test showing 14x the safe limit — the company knew and buried the evidence. Combined with five deaths, this is front-page material.",
                            "note": "Internal test: chromium levels 14x recommended limit, hidden from workers"
                        }
                    ]
                },
                "pressure": {
                    "q1_response": "Coincidence? Five men, same division, same symptoms, all dead before fifty-five? If that's coincidence, then I'm the Queen of Sweden. The company knows. They've always known.",
                    "expression_hint": "Voice rising, gripping the photograph tighter",
                    "q1_note": "'Five men, same symptoms, all dead before 55'",
                    "q2_options": [
                        {"text": "What proof do you have that the company knew about the danger?"},
                        {"text": "Has anyone tried to hold the company accountable? Any legal action?"},
                        {"text": "What happened when you confronted the company directly?"}
                    ],
                    "outcomes": [
                        {
                            "tier": 1,
                            "response": "I went to the personnel office. They gave me a condolence letter and Erik's last paycheck. When I asked about the chromium, the woman behind the desk said she didn't know what I was talking about. 'We don't use chromium here.' They do. Everyone knows they do.",
                            "expression": "guarded",
                            "feedback": "The company denying chromium use when it's common knowledge shows institutional lying, but it's her word against theirs.",
                            "note": "Company denied using chromium — an obvious lie"
                        },
                        {
                            "tier": 2,
                            "response": "A lawyer in Gothenburg agreed to look at it. But he needs proof of exposure. The company controls all the records. Erik's personal doctor documented the symptoms but couldn't prove the cause without the company's workplace data. They won't release it.",
                            "expression": "open",
                            "feedback": "Company withholding workplace data from legal proceedings — obstruction that itself is newsworthy.",
                            "note": "Company refusing to release workplace exposure data to lawyers"
                        },
                        {
                            "tier": 3,
                            "response": "I'll tell you what happened. Bergström himself called me. Personally. Offered 15,000 kronor. He called it a 'goodwill payment.' On the condition I sign a paper saying Erik's death was 'not related to his employment.' Fifteen thousand kronor for my husband's life. And my silence.",
                            "expression": "open",
                            "feedback": "Bergström personally offering hush money is explosive — it proves the company knows the deaths are work-related. Why pay for silence if there's nothing to hide?",
                            "note": "Bergström offered 15,000 kr 'goodwill' for silence agreement"
                        }
                    ]
                },
                "silence": {
                    "q1_response": "...Five funerals. I stood at five funerals. All the same church. All the same coughing in the months before. The priest doesn't say anything either. No one in this town says anything.",
                    "expression_hint": "Long pause, then looks at the photograph",
                    "q1_note": "'Five funerals, same church, same coughing'",
                    "q2_options": [
                        {"text": "..."},
                        {"text": "I'm here to listen, Gunhild."},
                        {"text": "Why do you think no one speaks up?"}
                    ],
                    "outcomes": [
                        {
                            "tier": 1,
                            "response": "Because the mill is everything. It's the jobs, the housing, the school, the football team. You don't speak against the mill. You just... bury your husbands and keep quiet.",
                            "expression": "guarded",
                            "feedback": "Captures the company-town dynamic perfectly, but no evidence of wrongdoing. Just the silence itself.",
                            "note": "'You bury your husbands and keep quiet'"
                        },
                        {
                            "tier": 2,
                            "response": "Erik's foreman — Berg — he came to the funeral. Stood in the back. Didn't sign the guest book. After the service he pulled me aside and said: 'It should have been better. The ventilation. I told them.' Then he left. That was his confession.",
                            "expression": "open",
                            "feedback": "The foreman's admission at the funeral — he told management about the ventilation. An inside witness who confirms the company was warned.",
                            "note": "Foreman Berg admitted at funeral: 'I told them' about ventilation"
                        },
                        {
                            "tier": 3,
                            "response": "Because last time someone spoke, they were destroyed. Sven Bergqvist — the train driver — he reported the loading violations. They blacklisted him. But Erik... Erik was smarter. He wrote everything down. *hands over a small notebook* Dates. Symptoms. Names. Air that tasted like metal. He knew he was dying. He documented it for someone like you.",
                            "expression": "open",
                            "feedback": "Erik's daily log is a martyred worker's testimony — he documented his own death, knowing someone would eventually read it. Powerful and legally significant.",
                            "note": "Erik kept a daily symptom diary knowing he was dying"
                        }
                    ]
                }
            }
        },
        "headlines": [
            {"text": "WIDOW QUESTIONS HUSBAND'S DEATH AT CHEMICAL PLANT", "tone": "Cautious"},
            {"text": "FIVE DEAD UNDER 55 — SAME DIVISION, SAME SYMPTOMS", "tone": "Fact-based"},
            {"text": "COMPANY OFFERED WIDOW 15,000 KR TO STAY SILENT", "tone": "Exposing"}
        ]
    }
]

with open(STORIES_PATH) as f:
    stories = json.load(f)

existing_ids = {s['id'] for s in stories}
added = 0
for s in NEW_STORIES:
    if s['id'] not in existing_ids:
        stories.append(s)
        added += 1
        print(f"  Added: {s['id']} (bv{s['base_value']})")
    else:
        print(f"  Skipped (exists): {s['id']}")

with open(STORIES_PATH, 'w') as f:
    json.dump(stories, f, indent=2, ensure_ascii=False)

print(f"\nAdded {added} stories. Total: {len(stories)}")
