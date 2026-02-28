#!/usr/bin/env python3
"""Add the last bv6 story for Industristad."""
import json, os

STORIES_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'stories.json')

NEW_STORIES = [
    {
        "id": "forsakringsfusket",
        "title": "The Insurance Scam",
        "description": "A pattern of denied worker injury claims at the steel mill, despite clear medical evidence.",
        "lead_text": "Three workers with the same lung condition. Three denied claims. Same insurance doctor.",
        "preview": "A retired mill nurse hands you a folder outside the pharmacy.",
        "source_type": "document",
        "difficulty": "hard",
        "base_value": 6,
        "category": "corruption",
        "npc_id": "sigrid_aberg",
        "npc_name": "Sigrid Åberg",
        "npc_title": "Retired Mill Nurse",
        "town": "industristad",
        "interview": {
            "opening_line": "I kept copies. I knew someday someone would ask. The insurance doctor — Dr. Wennerholm — he never examined them properly. Just ticked 'denied' and moved on.",
            "q1_options": [
                {"archetype": "friendly", "text": "You kept records all these years, Sigrid? That took real courage."},
                {"archetype": "direct", "text": "How many claims were denied? What's the pattern you found?"},
                {"archetype": "pressure", "text": "Did the company pay Dr. Wennerholm to deny claims? That's fraud."},
                {"archetype": "silence", "text": "..."}
            ],
            "branches": {
                "friendly": {
                    "q1_response": "I was the one who saw them coughing. Who filled out the initial forms. Then the forms came back stamped 'insufficient evidence.' The same men I'd watched deteriorate over years.",
                    "expression_hint": "Hands trembling, but voice steady",
                    "q1_note": "She filled out forms that came back 'insufficient evidence'",
                    "q2_options": [
                        {"text": "How many workers were affected? Can you name some of them?"},
                        {"text": "Did you ever confront anyone at the mill about this?"},
                        {"text": "What exactly is in the folder you kept?"}
                    ],
                    "outcomes": [
                        {
                            "tier": 1,
                            "response": "At least a dozen over the years. Gösta Fredriksson, Rune Hellström, others. All the same symptoms. All denied. I mentioned it to the head nurse once. She told me to mind my station.",
                            "expression": "guarded",
                            "feedback": "Names and pattern, but no proof of deliberate fraud. Could be bureaucratic indifference.",
                            "note": "At least a dozen denied, same symptoms"
                        },
                        {
                            "tier": 2,
                            "response": "Fourteen workers between 1968 and 1973. I have their names, dates, symptoms. Every one examined by Dr. Wennerholm. Every one denied. The company doctor before him approved similar claims without issue.",
                            "expression": "open",
                            "feedback": "Clear statistical pattern with dates. The switch in approval rates when the doctor changed is damning.",
                            "note": "14 workers denied by same doctor, previous doctor approved similar cases"
                        },
                        {
                            "tier": 3,
                            "response": "Here. Fourteen files. Each one shows the worker's symptoms, my notes, and Wennerholm's denial. But look at this — I found his contract. He's not independent. Ståhlbergs Stålverk pays him a retainer of 2,000 kronor per month. He's their employee evaluating their liability. It's rigged.",
                            "expression": "open",
                            "feedback": "The contract proves the insurance doctor was on the company payroll — a direct conflict of interest. Every denial is now suspect.",
                            "note": "Dr. Wennerholm paid 2,000 kr/month retainer by the mill"
                        }
                    ]
                },
                "direct": {
                    "q1_response": "Fourteen denied claims between 1968 and 1973. All lung-related. All examined by the same insurance doctor — Dr. Wennerholm. The approval rate for similar claims before he started was over 80%. Under him, it dropped to zero.",
                    "expression_hint": "Opens the folder, points at columns of numbers",
                    "q1_note": "Approval rate dropped from 80% to 0% under new doctor",
                    "q2_options": [
                        {"text": "Who hired Dr. Wennerholm? Was it the insurance company or the mill?"},
                        {"text": "What happened to the workers whose claims were denied?"},
                        {"text": "Do you have documentation I can verify independently?"}
                    ],
                    "outcomes": [
                        {
                            "tier": 1,
                            "response": "The insurance company appointed him, officially. But I heard — just heard, mind you — that Bergström's office recommended him. I can't prove that part.",
                            "expression": "guarded",
                            "feedback": "Statistical pattern is strong, but the connection to mill management is hearsay.",
                            "note": "Bergström may have recommended the doctor — unconfirmed"
                        },
                        {
                            "tier": 2,
                            "response": "Three are dead. Gösta Fredriksson can barely breathe. Without the insurance payout, they couldn't afford proper treatment. One man — Arne Lundqvist — sold his house to pay for care. Died six months later.",
                            "expression": "open",
                            "feedback": "The human cost is devastating — deaths tied to denied claims. Strong emotional and factual weight.",
                            "note": "Three dead, one sold house for medical care"
                        },
                        {
                            "tier": 3,
                            "response": "Every file, every date, every denial letter. And this — a letter from Bergström to the insurance company: 'We appreciate Wennerholm's thorough approach to claim evaluation.' Dated two weeks after Wennerholm denied four claims in one batch. They were congratulating him for saving them money.",
                            "expression": "open",
                            "feedback": "Bergström's letter praising the denials is a smoking gun. The mill actively celebrated workers being denied compensation.",
                            "note": "Bergström congratulated insurance company after batch denials"
                        }
                    ]
                },
                "pressure": {
                    "q1_response": "I... I wouldn't say fraud exactly. But it's not right. The doctor barely looked at them. Five minutes per examination. You can't diagnose industrial lung disease in five minutes.",
                    "expression_hint": "Pulls folder closer, protective",
                    "q1_note": "Five-minute examinations for complex conditions",
                    "q2_options": [
                        {"text": "If it's not fraud, what would you call systematically denying valid claims?"},
                        {"text": "The workers who were denied — some of them are very sick. Don't they deserve the truth?"},
                        {"text": "Show me the files. Let the evidence speak for itself."}
                    ],
                    "outcomes": [
                        {
                            "tier": 1,
                            "response": "I'd call it... convenient negligence. The mill saves money. The doctor keeps his contract. The workers suffer in silence. It's how things work here.",
                            "expression": "guarded",
                            "feedback": "She's being careful. 'Convenient negligence' is her framing — accurate but not explosive.",
                            "note": "'Convenient negligence' — mill saves money, workers suffer"
                        },
                        {
                            "tier": 2,
                            "response": "You're right. They do deserve the truth. Here — look at Rune Hellström's file. Twenty-two years in the smelting hall. Coughing blood. Wennerholm wrote 'chronic bronchitis, non-occupational.' Non-occupational! After twenty-two years breathing steel dust!",
                            "expression": "open",
                            "feedback": "The Hellström case is a perfect example — 22 years of exposure dismissed as non-occupational. Absurd on its face.",
                            "note": "22-year worker's lung disease called 'non-occupational'"
                        },
                        {
                            "tier": 3,
                            "response": "Fine. Here. All fourteen files. And there's something else — I found a memo. Internal. Bergström calculated that denying these claims saved the company 340,000 kronor. He put a number on their suffering. Three hundred and forty thousand.",
                            "expression": "open",
                            "feedback": "The internal memo calculating savings from denied claims is the smoking gun. Bergström put a price on workers' health.",
                            "note": "Internal memo: denials saved company 340,000 kronor"
                        }
                    ]
                },
                "silence": {
                    "q1_response": "...You're not going to push? Good. I've been pushed enough. I kept these files because... because someone should know. Fourteen men. Good men. Thrown away like broken tools.",
                    "expression_hint": "Opens folder slowly, as if releasing something heavy",
                    "q1_note": "Fourteen men 'thrown away like broken tools'",
                    "q2_options": [
                        {"text": "..."},
                        {"text": "Take your time. I'm listening."},
                        {"text": "What do you want people to know, Sigrid?"}
                    ],
                    "outcomes": [
                        {
                            "tier": 1,
                            "response": "I want them to know it wasn't an accident. It wasn't bad luck. Someone decided these men weren't worth the paperwork. That's all. Someone decided.",
                            "expression": "guarded",
                            "feedback": "Powerful sentiment but no specifics. 'Someone decided' — but who?",
                            "note": "'Someone decided these men weren't worth the paperwork'"
                        },
                        {
                            "tier": 2,
                            "response": "Gösta used to sing in the factory choir. Beautiful baritone. Now he can't finish a sentence without coughing. And the insurance company says it's not work-related. After thirty years in the smelting hall. It's obscene.",
                            "expression": "open",
                            "feedback": "The Gösta detail is heartbreaking — a singer who can't speak. Thirty years dismissed as coincidence.",
                            "note": "Choir singer who can no longer finish a sentence"
                        },
                        {
                            "tier": 3,
                            "response": "I want them to know about this. *slides a carbon copy across* It's from Bergström to the board. 'Worker compensation liability successfully reduced by 340,000 kronor through revised medical evaluation procedures.' Revised. That's what they call it. Revised.",
                            "expression": "open",
                            "feedback": "The carbon copy from Bergström to the board proves this was deliberate policy, not individual negligence. Corporate decision to deny claims.",
                            "note": "Board memo: 'compensation liability reduced by 340,000 kr'"
                        }
                    ]
                }
            }
        },
        "headlines": [
            {"text": "MILL NURSE QUESTIONS INJURY CLAIM PROCESS", "tone": "Cautious"},
            {"text": "14 WORKERS DENIED — SAME DOCTOR, SAME RESULT", "tone": "Factual"},
            {"text": "STEEL MILL SAVED 340,000 BY DENYING SICK WORKERS", "tone": "Exposing"}
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
