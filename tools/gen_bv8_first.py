#!/usr/bin/env python3
"""Add first 2 bv8 stories for Industristad — the biggest scoops."""
import json, os

STORIES_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'stories.json')

NEW_STORIES = [
    {
        "id": "bergstroms_konto",
        "title": "The Bergström Account",
        "description": "The mill director has been funneling company profits into a personal Swiss bank account while the mill reports losses to justify layoffs.",
        "lead_text": "A fired accountant says the books don't add up — millions in profit vanished into 'foreign consulting fees' that go to one account.",
        "preview": "A nervous woman in a headscarf approaches you at the library, carrying a briefcase.",
        "source_type": "document",
        "difficulty": "hard",
        "base_value": 8,
        "category": "corruption",
        "npc_id": "eva_sandberg",
        "npc_name": "Eva Sandberg",
        "npc_title": "Former Chief Accountant",
        "town": "industristad",
        "interview": {
            "opening_line": "I was fired for asking the wrong questions. For nine years I managed the books. Then I found the Zürich transfers and suddenly my 'performance was insufficient.' Let me show you what I found.",
            "q1_options": [
                {"archetype": "friendly", "text": "Nine years and then fired. That must have been a shock. What did you find, Eva?"},
                {"archetype": "direct", "text": "How much money are we talking about? Show me the numbers."},
                {"archetype": "pressure", "text": "You managed the books for nine years. Did you help set up these transfers before you grew a conscience?"},
                {"archetype": "silence", "text": "..."}
            ],
            "branches": {
                "friendly": {
                    "q1_response": "I didn't sleep for a week after I found it. Every quarter, between 80,000 and 150,000 kronor transferred to 'Bergström & Partners Consulting AG' in Zürich. A company that has no phone number, no office, no employees. Just a Swiss bank account.",
                    "expression_hint": "Opens briefcase with trembling fingers, papers meticulously organized",
                    "q1_note": "80-150k kronor per quarter to shell company in Zürich",
                    "q2_options": [
                        {"text": "How long have these transfers been happening?"},
                        {"text": "Did you bring documentation? Can you show me the account numbers?"},
                        {"text": "Does anyone else at the company know about this?"}
                    ],
                    "outcomes": [
                        {
                            "tier": 1,
                            "response": "At least since 1970, when I started handling those accounts. Maybe longer. The previous accountant retired and moved to Spain — which I now find suspicious. The total I could trace: 1.8 million kronor over four years.",
                            "expression": "guarded",
                            "feedback": "1.8 million is a huge number, but 'maybe longer' and a retired predecessor weaken the certainty. Still, the scale demands attention.",
                            "note": "1.8 million kronor traced over four years"
                        },
                        {
                            "tier": 2,
                            "response": "Here. *opens folder* Each quarter's transfer. Bank routing codes that match Swiss institutions. And this — the 'consulting invoices.' All identical template. Same font, same format, different amounts. No description of services. Nobody at the mill has ever met these 'consultants.' Because they don't exist.",
                            "expression": "open",
                            "feedback": "Fake invoices with identical templates, Swiss routing codes, and no evidence of actual consulting. The paper trail is clear and documented.",
                            "note": "Identical invoice templates, Swiss routing, no actual consultants"
                        },
                        {
                            "tier": 3,
                            "response": "I have everything. Transfer records, the shell company's registration — it was formed one month before the first payment. And this. *pulls out a carbon copy* Bergström's personal letter to the Swiss bank, requesting a credit card linked to the account. In his name. His personal name. Not the company's. He's spending the mill's money through a Swiss credit card.",
                            "expression": "open",
                            "feedback": "The personal credit card linked to the shell company is the smoking gun — it proves the money flows directly to Bergström for personal use. Combined with the shell company timing, this is embezzlement with full documentation.",
                            "note": "Bergström's personal credit card linked to the Swiss shell account"
                        }
                    ]
                },
                "direct": {
                    "q1_response": "1.8 million kronor. Confirmed. Between Q1 1970 and Q3 1974. Quarterly transfers of 80,000 to 150,000 kronor to 'Bergström & Partners Consulting AG' in Zürich. A company that was registered one month before the first transfer. No Swiss office, no employees, no phone.",
                    "expression_hint": "Fingers steepled, measured smile gone — dead serious",
                    "q1_note": "1.8M kronor to a shell company with no operations",
                    "q2_options": [
                        {"text": "How did this connect to the layoffs? You mentioned the mill reports losses."},
                        {"text": "What exactly does the paper trail show? Walk me through one transfer."},
                        {"text": "Can Bergström claim these are legitimate business expenses?"}
                    ],
                    "outcomes": [
                        {
                            "tier": 1,
                            "response": "The mill reported losses in 1973 and used that to justify cutting 40 jobs. But the actual P&L — before the consulting fees — showed a modest profit. Remove the fake consulting and the mill is solvent. Those 40 workers lost their jobs to fund Bergström's Swiss account.",
                            "expression": "guarded",
                            "feedback": "The link between phantom consulting fees and layoffs is powerful — workers fired to fund embezzlement. But 'before consulting fees' requires her interpretation.",
                            "note": "40 jobs cut based on losses inflated by fake consulting fees"
                        },
                        {
                            "tier": 2,
                            "response": "Let me show you Q2 1973. Revenue: 4.2 million kronor. Costs: 3.8 million. Profit: 400,000. Then under 'External Consulting': 120,000 to Bergström & Partners AG. Suddenly the profit shrinks to 280,000. Do this every quarter and the 'healthy mill' becomes a 'struggling business.' It's manufactured decline.",
                            "expression": "open",
                            "feedback": "Step-by-step demonstration of how the embezzlement creates fake losses. The phrase 'manufactured decline' is the story — the mill isn't failing, it's being drained.",
                            "note": "Revenue 4.2M, costs 3.8M, then 120k vanishes to Switzerland"
                        },
                        {
                            "tier": 3,
                            "response": "He can try. But I also found this. *pulls out another document* A receipt from a Zürich jewelry store — 28,000 kronor — charged to the Bergström & Partners account. A necklace. Purchased on December 23, 1973. Three days after he announced the layoffs. He bought his wife a diamond necklace with the money he stole from the workers he just fired.",
                            "expression": "open",
                            "feedback": "A jewelry receipt from the Swiss account, purchased days after laying off 40 workers. The timeline is devastating. The personal spending proves it's not consulting — it's theft.",
                            "note": "28k kr necklace from Swiss account — 3 days after layoff announcement"
                        }
                    ]
                },
                "pressure": {
                    "q1_response": "I didn't set it up. It was already there when I took over the accounts. The previous accountant — Lindström — had a system. 'Don't touch the consulting accounts.' That's all he said before he left. I respected that. For years. Until I didn't.",
                    "expression_hint": "Measured smile completely gone, voice flat",
                    "q1_note": "Previous accountant said 'don't touch the consulting accounts'",
                    "q2_options": [
                        {"text": "So when did you start looking? What changed?"},
                        {"text": "You didn't report this for years. Doesn't that make you part of the cover-up?"},
                        {"text": "What exactly can you prove? What would hold up in court?"}
                    ],
                    "outcomes": [
                        {
                            "tier": 1,
                            "response": "What changed? Bergström laid off 40 workers and blamed 'market conditions.' I knew the market conditions. I ran the numbers. The mill was profitable. The losses were manufactured. That's when I opened the consulting files.",
                            "expression": "guarded",
                            "feedback": "Her motivation is clear — the layoffs triggered her investigation. But she's defensive about her own role, which limits what she'll share.",
                            "note": "Layoffs based on manufactured losses triggered her investigation"
                        },
                        {
                            "tier": 2,
                            "response": "You're right. I was part of it. By silence. That's why I made copies before they walked me out. Every quarterly transfer. Every fake invoice. The Swiss registration documents. I can't undo nine years of silence. But I can make sure the next nine are different.",
                            "expression": "open",
                            "feedback": "She admits complicity and provides copies as atonement. Her knowledge of the system from the inside makes the documentation comprehensive.",
                            "note": "Made copies before being fired — quarterly transfers, invoices, Swiss registration"
                        },
                        {
                            "tier": 3,
                            "response": "What holds up in court? This. *lays out documents methodically* Transfer receipts with Bergström's authorization signature. Swiss bank registration showing him as sole beneficiary. And the crown jewel — a personal letter from Bergström to the Zürich bank requesting they 'ensure maximum discretion regarding the Consulting AG account, as Swedish tax authorities have become more vigilant.' He put his fear of getting caught in writing.",
                            "expression": "open",
                            "feedback": "Bergström's own letter asking the Swiss bank for secrecy from tax authorities is an admission of criminal intent. Combined with the authorization signatures and personal beneficiary status — this is a prosecutable case.",
                            "note": "Bergström's letter asking Swiss bank for secrecy from tax authorities"
                        }
                    ]
                },
                "silence": {
                    "q1_response": "...I sat at that desk for nine years. Processing numbers. Making the books balance. And the whole time, under the surface... *opens the briefcase slowly* ...the whole time, the mill was being hollowed out. Like termites in a beam.",
                    "expression_hint": "Briefcase opens, papers arranged with accountant's precision",
                    "q1_note": "'The mill was being hollowed out. Like termites in a beam.'",
                    "q2_options": [
                        {"text": "..."},
                        {"text": "Show me what you found."},
                        {"text": "When did the numbers stop making sense?"}
                    ],
                    "outcomes": [
                        {
                            "tier": 1,
                            "response": "The numbers never made sense. The consulting fees had no corresponding contracts. No deliverables. No meetings. Just money leaving the country and never coming back. I pretended not to see because I had a mortgage. A daughter in school. That's how they keep you quiet.",
                            "expression": "guarded",
                            "feedback": "She understands the system of complicity — mortgages and families as silencing tools. But no specific documents shared yet.",
                            "note": "'No contracts, no deliverables — just money leaving the country'"
                        },
                        {
                            "tier": 2,
                            "response": "It stopped making sense in 1972 when Bergström reported a loss, cut the Christmas bonus for 300 workers, and three weeks later authorized a 150,000 kronor transfer to Zürich. I checked the routing code. Swiss private bank. The money those workers didn't get for Christmas went to Switzerland.",
                            "expression": "open",
                            "feedback": "Christmas bonus cut and Swiss transfer in the same month — the workers' money directly funding Bergström's private account. Emotionally and financially devastating.",
                            "note": "Christmas bonus cut for 300 workers; 150k sent to Zürich same month"
                        },
                        {
                            "tier": 3,
                            "response": "Here. Take it all. *pushes the briefcase across* Eighteen quarters of transfer records. Swiss registration documents. Fake invoices. And Bergström's personal correspondence with the bank — including a request for a credit card and a warning about Swedish tax scrutiny. He knew it was illegal. He wrote it down. And then he fired me for finding it.",
                            "expression": "open",
                            "feedback": "The entire briefcase — four and a half years of documented embezzlement. The personal correspondence admitting awareness of illegality is the cornerstone. Eva is offering everything.",
                            "note": "Complete briefcase: 18 quarters of transfers, fake invoices, Bergström's bank letters"
                        }
                    ]
                }
            }
        },
        "headlines": [
            {"text": "FORMER ACCOUNTANT RAISES QUESTIONS ABOUT MILL FINANCES", "tone": "Cautious"},
            {"text": "1.8 MILLION IN 'CONSULTING FEES' SENT TO SWISS SHELL COMPANY", "tone": "Fact-based"},
            {"text": "BERGSTRÖM'S SWISS ACCOUNT: THE MILL THAT WAS HOLLOWED OUT", "tone": "Exposing"}
        ]
    },
    {
        "id": "dodsolyckan",
        "title": "The Fatal Shortcut",
        "description": "A worker died in a blast furnace accident that the company calls 'human error' — but colleagues say disabled safety systems caused the death.",
        "lead_text": "The emergency shutdown on Furnace 3 was disconnected weeks before the accident. The company says the worker made a mistake.",
        "preview": "A crumpled note is pushed under the office door: 'Ask about Furnace 3. Ask about the safety override.'",
        "source_type": "letter",
        "difficulty": "hard",
        "base_value": 8,
        "category": "labor",
        "npc_id": "arne_sundstrom",
        "npc_name": "Arne Sundström",
        "npc_title": "Furnace Operator",
        "town": "industristad",
        "interview": {
            "opening_line": "Göran Eriksson is dead because they disconnected the emergency shutdown to keep production running during the rush order. Göran didn't make a mistake. The safety system was off. And they covered it up.",
            "q1_options": [
                {"archetype": "friendly", "text": "I can see this is hard for you, Arne. Tell me about Göran."},
                {"archetype": "direct", "text": "Who disconnected the safety system? When? Is there proof?"},
                {"archetype": "pressure", "text": "You work the same furnace. Did you know the shutdown was disabled before the accident?"},
                {"archetype": "silence", "text": "..."}
            ],
            "branches": {
                "friendly": {
                    "q1_response": "Göran was twenty-eight. His wife is pregnant. Due in March. He'd been on the furnace crew for three years. Good worker. Careful. Always checked procedures. The idea that he 'forgot protocol' is a lie. He followed protocol. The protocol was sabotaged.",
                    "expression_hint": "Leaning forward aggressively but voice breaks on 'twenty-eight'",
                    "q1_note": "Göran was 28, wife pregnant, 3 years on crew — careful worker",
                    "q2_options": [
                        {"text": "What exactly happened that day? Take me through it."},
                        {"text": "When was the safety system disconnected? Who ordered it?"},
                        {"text": "Has anything like this happened before at the furnace?"}
                    ],
                    "outcomes": [
                        {
                            "tier": 1,
                            "response": "November 14. Furnace 3 was running a rush order — Bergström wanted double output for a defense contract. The emergency venting system slows production by 20% when it triggers. So they turned it off. Two weeks later, pressure built up and the furnace blew. Göran was standing at the control panel.",
                            "expression": "guarded",
                            "feedback": "Clear timeline and motive (rush order), but Arne's account is secondhand about who ordered the override. Strong on narrative, needs documents.",
                            "note": "Rush order for defense contract; safety disabled for 20% more output"
                        },
                        {
                            "tier": 2,
                            "response": "The shift supervisor — Lindblad — told us on November 1st: 'The emergency vent is down for maintenance.' But I checked. There was no maintenance order. No work ticket. The system was simply... disconnected. Wires cut, not pulled. Someone deliberately disabled it.",
                            "expression": "open",
                            "feedback": "No maintenance order for the 'maintenance' — wires cut, not pulled. Deliberate disabling disguised as routine work. The shift supervisor's lie is documented.",
                            "note": "Wires cut, no maintenance order — supervisor lied about it"
                        },
                        {
                            "tier": 3,
                            "response": "I have the work log. Göran signed in at 06:00. At 06:15, the pressure gauge hit red. He reached for the emergency vent — the button that should have released the pressure. Nothing happened. Because the wires were cut. And here — *shows a memo* — dated October 28: 'Per directive from production management, Furnace 3 emergency venting to be taken offline during the Forsvarets order.' Signed by Bergström's production chief. They ordered a man's death in a memo.",
                            "expression": "open",
                            "feedback": "The production memo ordering the safety system offline is corporate manslaughter on paper. Combined with the work log showing Göran tried to activate it — the company killed him on paper before the furnace did in reality.",
                            "note": "Memo ordering safety offline for defense order — signed by production chief"
                        }
                    ]
                },
                "direct": {
                    "q1_response": "October 28 — two weeks before the accident. The production chief, Nilsson, sent a memo to shift supervisors: 'Emergency venting on Furnace 3 to be taken offline for the duration of the Försvarets Materielverk order.' I saw the memo. I memorized the date.",
                    "expression_hint": "Jaw tight, reciting from memory",
                    "q1_note": "Oct 28 memo from production chief ordering safety offline",
                    "q2_options": [
                        {"text": "Do you have a copy of that memo?"},
                        {"text": "What did the accident investigation conclude? Who conducted it?"},
                        {"text": "Did anyone object when the safety system was taken offline?"}
                    ],
                    "outcomes": [
                        {
                            "tier": 1,
                            "response": "The investigation was internal. Run by Bergström's deputy. Concluded 'operator error — failure to monitor pressure gauge.' No mention of the disabled safety system. No mention of the memo. The report was filed and forgotten. Göran was buried and forgotten.",
                            "expression": "guarded",
                            "feedback": "Internal investigation with predetermined conclusion — classic cover-up. But without the memo or outside investigation, it's Arne's word against the report.",
                            "note": "Internal investigation: 'operator error.' No mention of disabled safety."
                        },
                        {
                            "tier": 2,
                            "response": "Three of us objected. In writing. We signed a letter to the safety committee. Lindblad tore it up in front of us. Said if we didn't like it, we could find work at the sawmill for half the wages. We backed down. Two weeks later Göran was dead.",
                            "expression": "open",
                            "feedback": "Written objections destroyed by the supervisor — three witnesses to the destruction of evidence. The threat and the timeline are damning.",
                            "note": "Three workers' safety objection torn up by supervisor — two weeks before death"
                        },
                        {
                            "tier": 3,
                            "response": "I kept a copy. Hidden. Here. *pulls a folded paper from his boot* The memo. Production management's signature. 'Emergency venting offline.' Dated October 28. And here's the accident report from November 14. See where it says 'all safety systems operational at time of incident'? That's a lie. A documented, verifiable lie. The memo proves the safety was off. The report claims it was on. Someone is lying, and Göran is dead.",
                            "expression": "open",
                            "feedback": "The memo and the accident report directly contradict each other — one says safety was offline, the other says it was operational. This isn't just negligence, it's a cover-up of manslaughter. Two company documents proving a lie.",
                            "note": "Memo says safety offline Oct 28; accident report says 'operational' Nov 14"
                        }
                    ]
                },
                "pressure": {
                    "q1_response": "Yes. I knew. We all knew. Lindblad told us. And I said nothing because I have two kids and the mill is the only employer for fifty kilometers. So yes — I'm complicit. And Göran is dead. You want to judge me? Fine. But print the truth first.",
                    "expression_hint": "Face contorted between guilt and rage",
                    "q1_note": "'I'm complicit. And Göran is dead.'",
                    "q2_options": [
                        {"text": "I'm not here to judge you. I'm here for the facts. What can you prove?"},
                        {"text": "The company blames Göran. Don't you owe him the truth?"},
                        {"text": "Who else knew? How far up does this go?"}
                    ],
                    "outcomes": [
                        {
                            "tier": 1,
                            "response": "Everyone on the furnace crew knew. Eight men. We all saw the disconnected wires. We all heard Lindblad's explanation about 'maintenance.' And we all kept working because what else could we do?",
                            "expression": "guarded",
                            "feedback": "Eight witnesses to the disabled safety system. But eight men who stayed silent — their collective guilt makes them unreliable as individual witnesses.",
                            "note": "Eight furnace crew members knew safety was disconnected"
                        },
                        {
                            "tier": 2,
                            "response": "I owe him everything. Here — Göran's work log from that morning. 06:00 check-in. 06:12 notation: 'Pressure rising faster than normal.' 06:14: 'Attempting emergency vent.' 06:15: nothing. The log ends. He tried to save himself with a system that had been deliberately disabled.",
                            "expression": "open",
                            "feedback": "Göran's own final log entries — he documented the rising pressure and his attempt to use the safety system. His last written words prove he followed procedure and the system failed him.",
                            "note": "Göran's log ends at 06:15 — 'Attempting emergency vent.' Then nothing."
                        },
                        {
                            "tier": 3,
                            "response": "All the way to Bergström. Nilsson wouldn't disable safety on his own — too much liability. And I can prove it. The day after the accident, I went back to the furnace. The wires had been reconnected. Repaired overnight. Someone came in between the accident at 06:15 and the investigation at 10:00 and put the system back together. They fixed the evidence. I photographed the fresh solder at 07:00 that morning. Before they could stop me.",
                            "expression": "open",
                            "feedback": "Evidence tampering photographed — fresh solder proving the safety system was reconnected between the accident and the investigation. This proves deliberate cover-up at the highest level.",
                            "note": "Photographed fresh solder at 07:00 — safety reconnected before investigation"
                        }
                    ]
                },
                "silence": {
                    "q1_response": "...I dream about it. Every night. The sound. Not the explosion — the silence after. When we all knew. When we looked at each other and nobody said 'the vent was off.' Nobody said it. We just... stood there.",
                    "expression_hint": "Stares straight ahead, hands still for the first time",
                    "q1_note": "'Nobody said the vent was off. We just stood there.'",
                    "q2_options": [
                        {"text": "..."},
                        {"text": "You're saying it now."},
                        {"text": "What happened in the silence, Arne?"}
                    ],
                    "outcomes": [
                        {
                            "tier": 1,
                            "response": "What happened? They cleaned up. Literally. By eight AM the furnace area was scrubbed. The investigation team didn't arrive until ten. Two hours to make it look like an operator error. Two hours to bury Göran's truth.",
                            "expression": "guarded",
                            "feedback": "Two-hour gap between accident and investigation — cleanup happened. But this is his account against the official timeline.",
                            "note": "Scene cleaned between 06:15 (accident) and 10:00 (investigation)"
                        },
                        {
                            "tier": 2,
                            "response": "Someone reconnected the safety wires. Between the accident and the investigation. Fresh solder on old terminals. I noticed because I worked on that system — I know what the connections looked like. Old copper, suddenly shiny. They didn't just cover up the cause. They rebuilt the evidence.",
                            "expression": "open",
                            "feedback": "Fresh solder on old terminals — the physical evidence of a cover-up. His technical knowledge of the system makes his observation credible.",
                            "note": "Fresh solder on old terminals — evidence rebuilt before investigation"
                        },
                        {
                            "tier": 3,
                            "response": "I've been carrying this for weeks. *reaches into his boot, pulls out folded papers* The production memo. October 28. 'Emergency venting offline.' And Göran's work log — ending at 06:15. And a photograph. See the solder? Fresh. Shiny. At 07:00 that morning, before they knew anyone was watching. The wires were cut. Göran died. The wires were fixed. The report blamed Göran. That's pre-meditated.",
                            "expression": "open",
                            "feedback": "Three pieces of evidence from one man's boot: the memo ordering safety offline, the victim's final log, and photographic proof of evidence tampering. Together they tell a complete story of corporate manslaughter and cover-up.",
                            "note": "Memo + work log + photo of evidence tampering — complete proof"
                        }
                    ]
                }
            }
        },
        "headlines": [
            {"text": "ACCIDENT INVESTIGATION QUESTIONS REMAIN UNANSWERED", "tone": "Cautious"},
            {"text": "SAFETY SYSTEM WAS OFFLINE WHEN WORKER DIED AT FURNACE 3", "tone": "Fact-based"},
            {"text": "MEMO ORDERED SAFETY OFF — REPORT SAYS IT WAS ON: WHO'S LYING?", "tone": "Exposing"}
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
