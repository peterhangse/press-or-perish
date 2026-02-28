#!/usr/bin/env python3
"""Add last 2 bv7 stories for Industristad."""
import json, os

STORIES_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'stories.json')

NEW_STORIES = [
    {
        "id": "dubbelagenten",
        "title": "The Double Agent",
        "description": "The local union chairman has been secretly negotiating with management — trading wage increases for personal benefits.",
        "lead_text": "A disgruntled union member found draft agreements in the chairman's office that were never shown to the membership.",
        "preview": "A sealed envelope arrives with photocopied documents and a note: 'Check Folke's deal.'",
        "source_type": "document",
        "difficulty": "hard",
        "base_value": 7,
        "category": "labor",
        "npc_id": "anders_strom",
        "npc_name": "Anders Ström",
        "npc_title": "Union Shop Steward",
        "town": "industristad",
        "interview": {
            "opening_line": "Folke Dahlberg sold us out. I found the papers in his desk when he was in Stockholm. Secret agreements. The membership voted for a 12% raise. Folke settled for 4% — and a company car for himself.",
            "q1_options": [
                {"archetype": "friendly", "text": "That must have been devastating to discover. How long has this been going on?"},
                {"archetype": "direct", "text": "What exactly was in the agreements? What did Dahlberg get personally?"},
                {"archetype": "pressure", "text": "You broke into his desk. That's not exactly clean either, is it?"},
                {"archetype": "silence", "text": "..."}
            ],
            "branches": {
                "friendly": {
                    "q1_response": "Two years. Maybe more. We kept losing negotiations and couldn't figure out why. Management always seemed to know our bottom line. Our strike votes, our breaking points. Now I know — Folke told them everything.",
                    "expression_hint": "Leg bouncing, chain-smoking intensifies",
                    "q1_note": "Two years of leaked negotiation positions",
                    "q2_options": [
                        {"text": "What proof do you have beyond the documents you found?"},
                        {"text": "Have you confronted Folke about this?"},
                        {"text": "How did the workers react to the 4% settlement?"}
                    ],
                    "outcomes": [
                        {
                            "tier": 1,
                            "response": "The workers were furious. We had leverage — the oil crisis means production can't stop. But Folke settled before we could vote on a strike. Said management threatened layoffs. Now I know why — he had his deal already.",
                            "expression": "guarded",
                            "feedback": "Circumstantial — a bad settlement doesn't prove corruption. You need the documents themselves.",
                            "note": "Folke settled before strike vote, claiming layoff threats"
                        },
                        {
                            "tier": 2,
                            "response": "I confronted him. He turned white. Then he said: 'You don't understand how negotiation works.' But I had the carbon copies. Three side agreements. A company Volvo. Paid 'consulting fees' — 800 kronor a month. And a guaranteed supervisor job for his son.",
                            "expression": "open",
                            "feedback": "Three documented side deals — car, consulting fees, nepotism. Folke's reaction when confronted confirms their authenticity.",
                            "note": "Volvo, 800 kr/month 'consulting,' supervisor job for his son"
                        },
                        {
                            "tier": 3,
                            "response": "Here. *slams papers on the table* Three side agreements, all signed by Folke and Bergström's deputy. But this is the one that matters — a letter from Bergström: 'As discussed, the 4% settlement protects both parties. Your continued cooperation is valued.' Bergström is thanking our union chairman for selling his own members short.",
                            "expression": "open",
                            "feedback": "Bergström's letter proves the collaboration was explicit and mutual. The mill director thanking the union chairman for betraying workers. Explosive.",
                            "note": "Bergström letter: 'Your continued cooperation is valued'"
                        }
                    ]
                },
                "direct": {
                    "q1_response": "Three side agreements. One: company Volvo 142, registered to Folke's wife. Two: 'consulting fees' of 800 kronor per month to a company Folke's brother runs. Three: his son Lars gets a supervisor position without the normal qualifications.",
                    "expression_hint": "Spreads photocopies across the table",
                    "q1_note": "Company car, 800 kr/month consulting, nepotism hire",
                    "q2_options": [
                        {"text": "Are these originals or copies? Can they be verified?"},
                        {"text": "What did the union membership actually vote for versus what Folke agreed to?"},
                        {"text": "Has Folke done this in previous negotiations too?"}
                    ],
                    "outcomes": [
                        {
                            "tier": 1,
                            "response": "Carbon copies. The originals are in Bergström's office, probably. But these are clearly company letterhead. You can see the watermark. And Folke's signature — I know his handwriting.",
                            "expression": "guarded",
                            "feedback": "Carbon copies are evidence but weaker than originals. Folke could claim forgery.",
                            "note": "Carbon copies on company letterhead with Folke's signature"
                        },
                        {
                            "tier": 2,
                            "response": "We voted to demand 12% with a strike mandate. Folke came back three days later with 4% and no strike. He told us management threatened to close the mill. We believed him. Meanwhile, his wife was driving a new Volvo.",
                            "expression": "open",
                            "feedback": "The gap between the mandate (12% + strike) and the result (4%, no strike) is stark. The timeline and the car make the corruption visible.",
                            "note": "Voted 12% + strike mandate; got 4% with no strike"
                        },
                        {
                            "tier": 3,
                            "response": "I went back further. Three previous negotiations — same pattern. Workers demanded, Folke settled for less, and something always appeared. The car was 1973. Before that, his apartment was renovated — 'a company benefit for long-serving employees.' No other employee got that offer. The consulting payments started in 1972. It's systematic.",
                            "expression": "open",
                            "feedback": "Three years of escalating personal benefits tied to each under-delivered negotiation. The pattern over time proves this isn't a one-off — it's a business arrangement.",
                            "note": "Three years of side deals tied to each negotiation"
                        }
                    ]
                },
                "pressure": {
                    "q1_response": "I didn't break in. The drawer was unlocked. I was looking for the actuarial tables for the pension discussion. What I found was... different. And yes, I took copies. Someone had to.",
                    "expression_hint": "Defensive, but pulls out papers anyway",
                    "q1_note": "Found documents while looking for pension data",
                    "q2_options": [
                        {"text": "What exactly did you find? Show me everything."},
                        {"text": "Why you? Why not go to the national union instead of a newspaper?"},
                        {"text": "Is Folke popular with the workers? Will they believe this?"}
                    ],
                    "outcomes": [
                        {
                            "tier": 1,
                            "response": "Folke is... respected. Not loved, but respected. Thirty years in the movement. People trust him because they've always trusted him. That's what makes this so ugly.",
                            "expression": "guarded",
                            "feedback": "Context about Folke's reputation, but no new evidence. The betrayal angle is strong emotionally.",
                            "note": "Folke: 30 years in the movement, respected and trusted"
                        },
                        {
                            "tier": 2,
                            "response": "I tried the national union. Called Stockholm. They said they'd 'investigate internally.' That was two months ago. Nothing. Maybe they knew. Maybe the rot goes higher. That's when I called you.",
                            "expression": "open",
                            "feedback": "National union inaction suggests either incompetence or complicity. The leak goes to the press as last resort — credible and significant.",
                            "note": "National union promised to investigate — two months, nothing"
                        },
                        {
                            "tier": 3,
                            "response": "Fine — everything. Three side agreements, two personal letters from Bergström, and this: a handwritten note from Folke to Bergström. 'The boys will accept 4%. Hold firm at 3% for two days, then offer 4. They'll feel like they won.' Our chairman scripted the entire negotiation against us.",
                            "expression": "open",
                            "feedback": "Folke's own handwritten note coaching management on how to manipulate the union. He scripted the workers' own defeat. This is the most devastating document.",
                            "note": "Folke coached Bergström: 'Hold firm at 3%, offer 4, they'll feel they won'"
                        }
                    ]
                },
                "silence": {
                    "q1_response": "...Thirty years I've worked alongside Folke. Thirty years. And the whole time... *long pause* ...the whole time he was selling us. Do you know what that feels like? Like finding out your father is a stranger.",
                    "expression_hint": "Stares at the road, leg stops bouncing",
                    "q1_note": "'Like finding out your father is a stranger'",
                    "q2_options": [
                        {"text": "..."},
                        {"text": "What made you finally look?"},
                        {"text": "Take your time, Anders."}
                    ],
                    "outcomes": [
                        {
                            "tier": 1,
                            "response": "Something didn't add up. Every negotiation, Folke knew exactly when to fold. Always had a reason. 'They'll close the mill.' 'The economy's bad.' But it was always just enough to stop us fighting. Always exactly management's number.",
                            "expression": "guarded",
                            "feedback": "Pattern recognition without proof — compelling context but circumstantial.",
                            "note": "Folke always settled at exactly management's number"
                        },
                        {
                            "tier": 2,
                            "response": "His wife's car. A Volvo 142, factory new, appeared one week after the last settlement. Folke said she inherited money. But I know Folke's wife — her family has nothing. So I looked. And I found the rest.",
                            "expression": "open",
                            "feedback": "The car is the thread that unraveled the whole scheme. Tangible, visible, verifiable through vehicle registration.",
                            "note": "New Volvo appeared one week after settlement — traced to company"
                        },
                        {
                            "tier": 3,
                            "response": "I found... everything. Side agreements. Letters. And this — the worst part. *unfolds a paper with shaking hands* In Folke's own handwriting: 'The boys will accept 4%. Hold firm at 3% for two days, then offer 4. They'll feel like they won.' He choreographed our defeat. For a Volvo and a monthly envelope.",
                            "expression": "open",
                            "feedback": "Folke's handwritten coaching note to management — the union chairman scripting the negotiation against his own members. For material gain. The ultimate betrayal.",
                            "note": "Folke's handwritten note coaching Bergström against the workers"
                        }
                    ]
                }
            }
        },
        "headlines": [
            {"text": "UNION CHAIRMAN SETTLED FOR LESS THAN MANDATE", "tone": "Cautious"},
            {"text": "SECRET DEALS: COMPANY CAR AND CASH FOR CHAIRMAN", "tone": "Fact-based"},
            {"text": "UNION BOSS COACHED MANAGEMENT: 'THEY'LL FEEL THEY WON'", "tone": "Exposing"}
        ]
    },
    {
        "id": "hamnens_hemlighet",
        "title": "The Harbor's Secret",
        "description": "Suspicious cargo has been moving through the harbor at night — drums of industrial waste being loaded onto unmarked barges.",
        "lead_text": "A dockworker says unmarked barges arrive after midnight. The cargo stinks of chemicals. No manifests. No records.",
        "preview": "A dockworker slips you a note at the pub: 'Pier 4, midnight. Bring a camera if you dare.'",
        "source_type": "street",
        "difficulty": "hard",
        "base_value": 7,
        "category": "environment",
        "npc_id": "sven_bergqvist",
        "npc_name": "Sven Bergqvist",
        "npc_title": "Harbor Crane Operator",
        "town": "industristad",
        "interview": {
            "opening_line": "I operate the night crane when they need me. Three times this month — unmarked drums. No shipping documents. The foreman says it's 'surplus materials.' Surplus doesn't burn your eyes when a drum leaks.",
            "q1_options": [
                {"archetype": "friendly", "text": "That sounds dangerous, Sven. How long has this been going on?"},
                {"archetype": "direct", "text": "How many drums? Where are they going? What markings, if any?"},
                {"archetype": "pressure", "text": "You're operating the crane that loads them. Doesn't that make you complicit?"},
                {"archetype": "silence", "text": "..."}
            ],
            "branches": {
                "friendly": {
                    "q1_response": "Since September, at least. Maybe longer — I only work the night shift twice a week. But when I'm there, it's always the same. Flatbed trucks arrive around one AM. No license plates. Drums get loaded onto barges that head south. No paperwork.",
                    "expression_hint": "Hands still shaking slightly, eyes on the road",
                    "q1_note": "Since September — trucks with no plates, barges heading south",
                    "q2_options": [
                        {"text": "Where do you think the barges are taking the drums?"},
                        {"text": "What company do the trucks come from?"},
                        {"text": "Has anyone else at the harbor noticed?"}
                    ],
                    "outcomes": [
                        {
                            "tier": 1,
                            "response": "South, toward the open sea. One of the other crane guys says they dump at the trench — 30 kilometers out. Deep enough that no one checks. But I can't prove that. The barges just... leave.",
                            "expression": "guarded",
                            "feedback": "Dumping at sea is alleged but unverified. The midnight operations are suspicious but not yet tied to a specific company.",
                            "note": "Barges allegedly dump at deep-sea trench 30 km out"
                        },
                        {
                            "tier": 2,
                            "response": "No plates on the trucks, but I recognized a driver. Nils — he drives for Bergström's transport division during the day. Same truck, different shift. And the drums? I got close to one that was leaking. Yellow residue. It smelled like the chromium division.",
                            "expression": "open",
                            "feedback": "Identified driver from Bergström's transport division + yellow residue matching chromium waste. Connects the mill to the illegal dumping.",
                            "note": "Driver identified from Bergström's transport; drums match chromium waste"
                        },
                        {
                            "tier": 3,
                            "response": "Last week a drum cracked when I was loading it. Bright yellow liquid poured out. The foreman made us hose down the pier at four AM. No protective gear. My eyes burned for two days. And then he gave me this — *shows a crumpled paper* — 500 kronor cash and a note: 'For your extra work. Not a word.' Unsigned, but I know the handwriting. It's Bergström's logistics chief.",
                            "expression": "open",
                            "feedback": "Physical evidence: the bribe note, the cracked drum, the health effects. Plus an identifiable handwriting. This connects corporate management directly to illegal waste dumping.",
                            "note": "500 kr bribe after drum cracked; note from logistics chief"
                        }
                    ]
                },
                "direct": {
                    "q1_response": "I counted thirty-two drums last Tuesday alone. Standard industrial 200-liter size. Mark on the side — a white X, nothing else. The barge 'Elsa-Marie' takes them. Registered in Gothenburg but I've never seen it in daylight.",
                    "expression_hint": "Pulls out a scrap of paper with notes",
                    "q1_note": "32 drums, 200-liter, white X, barge 'Elsa-Marie'",
                    "q2_options": [
                        {"text": "Can you identify where the drums originate? Which factory?"},
                        {"text": "Who's running this operation? Who gives the orders?"},
                        {"text": "Have any drums been damaged or leaked during loading?"}
                    ],
                    "outcomes": [
                        {
                            "tier": 1,
                            "response": "The trucks come from the industrial zone. Could be the steel mill, the chemical plant, even the paper mill. Hard to tell at night. But the volume — thirty-two drums a week — that's industrial scale.",
                            "expression": "guarded",
                            "feedback": "Scale is clear (32 drums/week), but the source factory isn't identified. Needs more investigation.",
                            "note": "32 drums/week from industrial zone — source unclear"
                        },
                        {
                            "tier": 2,
                            "response": "The harbor master — Bengt Ohlsson — he's in on it. I saw him meet the truck driver before the loading started. Handed him an envelope. And the harbor log for those nights? All it says is 'scheduled maintenance — no vessel traffic.' Lie. Documented lie.",
                            "expression": "open",
                            "feedback": "The harbor master falsifying logs is corruption on top of illegal dumping. The envelope suggests payment for cooperation.",
                            "note": "Harbor master falsified logs, handed envelope to driver"
                        },
                        {
                            "tier": 3,
                            "response": "One drum fell last month. It cracked open on the pier. The foreman brought in a hose and washed it into the harbor. I grabbed a piece of the label before it dissolved — *shows a torn, stained fragment* See? 'Ståhlbergs Stålverk — Chromium Processing Residue — CATEGORY III HAZARDOUS.' They're dumping Category III toxic waste at sea. And the harbor master signs off on it.",
                            "expression": "open",
                            "feedback": "The label fragment directly identifies the source (Ståhlbergs), the contents (chromium residue), and the classification (Category III hazardous). Combined with falsified harbor logs — this is criminal.",
                            "note": "Label: 'Ståhlbergs — Chromium Residue — CATEGORY III HAZARDOUS'"
                        }
                    ]
                },
                "pressure": {
                    "q1_response": "Complicit? I load whatever comes through the gate. I don't ask what's in the containers. But when one leaks and your eyes burn for two days — you start asking questions your bosses don't want to hear.",
                    "expression_hint": "Eyes red-rimmed, jaw tight",
                    "q1_note": "Eyes burned for two days after drum leaked",
                    "q2_options": [
                        {"text": "Your eyes — did you see a doctor? Is there a record?"},
                        {"text": "If you're just following orders, why come to me now?"},
                        {"text": "Who would know what's actually in those drums?"}
                    ],
                    "outcomes": [
                        {
                            "tier": 1,
                            "response": "I didn't go to a doctor. The foreman said it was 'solvent fumes' and gave me eye drops from the first aid kit. No forms. No incident report. That's when I knew — they're deliberately keeping this off the books.",
                            "expression": "guarded",
                            "feedback": "No incident report for a chemical exposure is itself a violation. But without medical documentation, his account is uncorroborated.",
                            "note": "No incident report filed for chemical exposure"
                        },
                        {
                            "tier": 2,
                            "response": "Because one of the barge crew told me where they go. Ten nautical miles out. They open the valves and let the drums sink. He said the water turns yellow for an hour. Then it's gone. Thirty-two drums a week. Into the fishing waters.",
                            "expression": "open",
                            "feedback": "Eyewitness account of ocean dumping in fishing waters. 'The water turns yellow' is a vivid detail that connects to the chromium waste.",
                            "note": "Drums dumped 10 miles out — water turns yellow for an hour"
                        },
                        {
                            "tier": 3,
                            "response": "I took a photo. One photo. *shows a Polaroid* See the drums? See the marking? And look at the truck — that's a Ståhlbergs transport truck. The logo's been painted over but you can still see the outline. This is the steel mill dumping hazardous waste at sea, using the harbor as a laundering point.",
                            "expression": "open",
                            "feedback": "A photograph of drums being loaded from a company truck with a painted-over logo. Visual evidence that's impossible to deny. The painted-over logo shows intent to conceal.",
                            "note": "Polaroid: drums + truck with painted-over Ståhlbergs logo"
                        }
                    ]
                },
                "silence": {
                    "q1_response": "...The water was my life, you know. I grew up on boats. My father fished these waters. Now I'm loading drums of poison onto barges that dump them where he used to set his nets.",
                    "expression_hint": "Stares out the window, hands still",
                    "q1_note": "'Loading poison where my father used to fish'",
                    "q2_options": [
                        {"text": "..."},
                        {"text": "Your father's waters..."},
                        {"text": "What do you need people to know, Sven?"}
                    ],
                    "outcomes": [
                        {
                            "tier": 1,
                            "response": "The fish are dying. The fishermen know it but they blame overfishing, currents, temperature. Nobody connects it to the barges that leave at two AM. Nobody wants to.",
                            "expression": "guarded",
                            "feedback": "Environmental impact is mentioned but not proven — the connection between dumping and declining fish stocks is his theory.",
                            "note": "Fish dying but nobody connects it to the barges"
                        },
                        {
                            "tier": 2,
                            "response": "They dump ten miles out. Where the herring spawn. A barge crew member told me the water turns yellow when the drums open. Yellow. Like the residue from the chromium division. My father caught a hundred kilos a day there. Now the catch is a tenth of what it was.",
                            "expression": "open",
                            "feedback": "Herring spawning grounds contaminated — connects industrial waste to collapsing fish stocks. The ecological and economic impact is devastating.",
                            "note": "Dumping at herring spawning grounds — catch down 90%"
                        },
                        {
                            "tier": 3,
                            "response": "I kept a log. Every night shift — date, number of drums, truck arrival time, barge departure time. Three months of data. And last week I did something stupid. I followed the barge in my father's old boat. At dawn. And I saw them. The valves open. The drums go down. The water turns yellow. I was there. I can testify.",
                            "expression": "open",
                            "feedback": "Three months of logged data plus eyewitness testimony of the actual dumping. He followed them and saw it himself. Combined with a willingness to testify — this breaks the story wide open.",
                            "note": "Three-month log + eyewitness: followed barge, saw dumping"
                        }
                    ]
                }
            }
        },
        "headlines": [
            {"text": "MIDNIGHT CARGO: UNMARKED DRUMS LEAVE HARBOR", "tone": "Investigative"},
            {"text": "INDUSTRIAL WASTE DUMPED IN FISHING WATERS", "tone": "Fact-based"},
            {"text": "STEEL MILL TOXIC DRUMS FOUND IN HERRING SPAWNING GROUNDS", "tone": "Exposing"}
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
