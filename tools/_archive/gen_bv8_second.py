#!/usr/bin/env python3
"""Add last 2 bv8 stories for Industristad — completing the 40-story set."""
import json, os

STORIES_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'stories.json')

NEW_STORIES = [
    {
        "id": "kommunvalet",
        "title": "The Rigged Council",
        "description": "The upcoming municipal election has been quietly shaped by the mill — candidates who threaten corporate interests are being systematically sabotaged.",
        "lead_text": "A council candidate says her campaign was destroyed by anonymous smears that traced back to the mill director's office.",
        "preview": "A woman in a winter coat stops you outside the newspaper office. She says she needs to talk.",
        "source_type": "street",
        "difficulty": "hard",
        "base_value": 8,
        "category": "politics",
        "npc_id": "anna_lena_johansson",
        "npc_name": "Anna-Lena Johansson",
        "npc_title": "Municipal Council Candidate",
        "town": "industristad",
        "interview": {
            "opening_line": "I ran for council on a platform of environmental regulation. Within a week, anonymous pamphlets appeared calling me a communist. My employer — a mill subcontractor — was told to fire me. Bergström doesn't just run the mill. He runs this town.",
            "q1_options": [
                {"archetype": "friendly", "text": "That sounds terrifying, Anna-Lena. How did you realize it was connected to the mill?"},
                {"archetype": "direct", "text": "What evidence do you have linking the smear campaign to Bergström?"},
                {"archetype": "pressure", "text": "Politicians get attacked all the time. What makes your case different?"},
                {"archetype": "silence", "text": "..."}
            ],
            "branches": {
                "friendly": {
                    "q1_response": "The pamphlets appeared the day after I spoke at a town hall about factory emissions. Not the day after I announced. The day after I mentioned the mill. By name. Someone was watching. Someone reported back.",
                    "expression_hint": "Arms crossed, chin up, but eyes betray exhaustion",
                    "q1_note": "Smear pamphlets appeared day after she named the mill",
                    "q2_options": [
                        {"text": "Who else was targeted? Is it just you?"},
                        {"text": "The pamphlets — do you still have copies? Can you trace the printing?"},
                        {"text": "You said your employer was pressured. What happened exactly?"}
                    ],
                    "outcomes": [
                        {
                            "tier": 1,
                            "response": "It's not just me. Lars Kjellberg ran for council in '70 on a worker safety platform. Same thing — anonymous attacks, his wife's employer was pressured. He withdrew. Britt Ekholm in '68 — housing reform. Same pattern. She moved away entirely.",
                            "expression": "guarded",
                            "feedback": "A pattern across multiple elections — three candidates targeted. But each case is circumstantial without direct evidence.",
                            "note": "Three candidates targeted across three elections — same pattern"
                        },
                        {
                            "tier": 2,
                            "response": "My employer — Industristads Byggtjänst — does all the mill's renovation contracts. My boss called me in and said: 'I got a call. From Bergström's office. They said if you're on the council, we lose the contracts.' He didn't even try to hide who called him. He was scared.",
                            "expression": "open",
                            "feedback": "Named witness (her boss) confirming a direct call from Bergström's office. Economic coercion through contract threats — provable if the boss will talk.",
                            "note": "Boss received call from Bergström's office threatening contracts"
                        },
                        {
                            "tier": 3,
                            "response": "I traced the pamphlets. Same paper stock as the mill's internal newsletter. Same typewriter — an Adler Tippa with a chipped 'e'. And this — *shows a pamphlet and a mill newsletter side by side* — look at the margins, the font, the paper quality. Identical. They were printed in the mill's communications office. And the content? Talking points I'd heard Bergström use at a chamber of commerce dinner. His words, his office, his paper. His campaign against democracy.",
                            "expression": "open",
                            "feedback": "Physical forensics — typewriter match, paper match, and content matching Bergström's own rhetoric. The mill's printing press was used to undermine a democratic election. Explosive.",
                            "note": "Typewriter and paper forensically match mill's office — Bergström's words"
                        }
                    ]
                },
                "direct": {
                    "q1_response": "Three things. One: the pamphlets were printed on the same paper as the mill's newsletter — same watermark. Two: my employer was called by Bergström's office directly, told to fire me or lose contracts. Three: I obtained a list.",
                    "expression_hint": "Unfolds a piece of paper, smooths it on her knee",
                    "q1_note": "Paper match, direct call to employer, and 'a list'",
                    "q2_options": [
                        {"text": "What list?"},
                        {"text": "Can your employer confirm the call from Bergström's office?"},
                        {"text": "How did you obtain these materials?"}
                    ],
                    "outcomes": [
                        {
                            "tier": 1,
                            "response": "My employer will confirm it — he's furious. He voted for me. But he can't lose the mill contracts. It's 60% of his revenue. That's how Bergström controls this town — through economic dependency. He doesn't need guns. He has invoices.",
                            "expression": "guarded",
                            "feedback": "The economic control mechanism is clear but the employer may not go on record. 'He has invoices' is a powerful line.",
                            "note": "'He doesn't need guns. He has invoices.'"
                        },
                        {
                            "tier": 2,
                            "response": "A list of every council candidate for the last three elections, with notes beside each name. 'No threat.' 'Manageable.' 'Neutralize.' My name says 'Neutralize — environmental platform incompatible with operations.' It's in Bergström's handwriting. I know his hand — I used to work in the mill's filing department.",
                            "expression": "open",
                            "feedback": "A candidate assessment list in Bergström's handwriting with 'Neutralize' next to her name. This proves the mill systematically evaluates and targets political candidates.",
                            "note": "Bergström's handwritten list: candidates rated 'No threat' to 'Neutralize'"
                        },
                        {
                            "tier": 3,
                            "response": "Here's the list. *unfolds it* Every candidate, three elections. My name: 'Neutralize.' Lars Kjellberg 1970: 'Neutralize.' And at the bottom — budget allocations. 'Anti-Johansson materials: 3,000 kr. Anti-Kjellberg materials: 2,500 kr. Ekholm employer pressure: 1,800 kr.' He budgeted democracy suppression like a line item. He kept a ledger of how much it costs to destroy political opposition.",
                            "expression": "open",
                            "feedback": "Budget allocations for political sabotage — a line-item ledger of democratic suppression. Bergström treated election interference as a business expense. This is industrial-scale corruption of local democracy.",
                            "note": "Bergström's ledger: budgeted amounts for destroying each candidate"
                        }
                    ]
                },
                "pressure": {
                    "q1_response": "Different? Because I can prove it. Other candidates were destroyed and went quietly. I didn't. I kept the pamphlets, I recorded my employer's conversation after the call, and I found documents. Because I used to work in the mill's filing department. I know where they keep things.",
                    "expression_hint": "Daring you to dismiss her",
                    "q1_note": "Kept pamphlets, recorded employer, found internal documents",
                    "q2_options": [
                        {"text": "You recorded your employer without consent? That's legally questionable."},
                        {"text": "What documents did you find from your time at the mill?"},
                        {"text": "Why didn't you go to the police instead of a newspaper?"}
                    ],
                    "outcomes": [
                        {
                            "tier": 1,
                            "response": "The police? In this town? The police chief's brother-in-law works in the mill's security department. I tried. I filed a complaint about the pamphlets. They 'investigated' for two weeks and closed the case. 'No evidence of criminal activity.' Of course not.",
                            "expression": "guarded",
                            "feedback": "Police captured by mill connections. The failed complaint shows institutional corruption, but it's her word on the connection.",
                            "note": "Police chief's brother-in-law works at mill — complaint dismissed in two weeks"
                        },
                        {
                            "tier": 2,
                            "response": "From the filing department I know how their system works. Bergström keeps a personal correspondence file — he's meticulous. I found a carbon copy of a letter to Fabriksbladet's editor: 'I trust the Johansson situation will be handled with appropriate editorial discretion.' The competition newspaper was told what to write about me.",
                            "expression": "open",
                            "feedback": "Bergström directing the competitor newspaper's coverage of a council candidate. The press and the corporation working together to suppress democracy.",
                            "note": "Bergström letter to Fabriksbladet editor about 'handling' her candidacy"
                        },
                        {
                            "tier": 3,
                            "response": "Here. Everything. *opens a folder* The pamphlet paper matches the mill's stock — same watermark. The typewriter matches their Adler Tippa. A candidate list in Bergström's handwriting with budget allocations for political sabotage. A letter to Fabriksbladet coordinating coverage. And my employer's recorded testimony confirming the contract threat. Five pieces of evidence. From five different sources. All pointing to one man. Print it.",
                            "expression": "open",
                            "feedback": "Five independent evidence streams all converging on Bergström — physical forensics, handwritten documents, media collusion, economic coercion, and recorded testimony. An airtight case for systematic corruption of democracy.",
                            "note": "Five evidence streams: forensics, list, letter, media collusion, testimony"
                        }
                    ]
                },
                "silence": {
                    "q1_response": "...Everyone knows. That's what's worst. Everyone in this town knows the mill picks the council. They know it and they accept it. Because the mill is the town. You can't fight your own blood supply.",
                    "expression_hint": "Arms uncross slowly, exhaustion showing through",
                    "q1_note": "'Everyone knows the mill picks the council'",
                    "q2_options": [
                        {"text": "..."},
                        {"text": "You're fighting."},
                        {"text": "What made you different from the ones who gave up?"}
                    ],
                    "outcomes": [
                        {
                            "tier": 1,
                            "response": "I have a daughter. She asked me why I stopped handing out flyers. I didn't have an answer that I could say out loud. So I started again. For her. Because she shouldn't grow up in a town where one man decides who governs.",
                            "expression": "guarded",
                            "feedback": "Powerful personal motivation but no new evidence. The story of silence and complicity in the town sets important context.",
                            "note": "Restarted campaign for her daughter — 'shouldn't grow up in this town'"
                        },
                        {
                            "tier": 2,
                            "response": "Lars Kjellberg — the candidate from '70 — he came to me last week. First time we'd spoken. He said Bergström called him personally in 1970, told him to withdraw or his wife would lose her teaching position. His wife was fired three days after he refused. Three days. Bergström followed through.",
                            "expression": "open",
                            "feedback": "A second victim confirming the pattern — Bergström personally threatening a candidate and following through on the threat. The wife's firing is verifiable through school records.",
                            "note": "1970 candidate: Bergström called personally; wife fired 3 days later"
                        },
                        {
                            "tier": 3,
                            "response": "I found his system. Bergström keeps a list. *slides it across* Every candidate. Every election since 1966. Notes in his handwriting: 'No threat.' 'Manageable.' 'Neutralize.' And budgets — actual kronor amounts — for pamphlets, employer pressure, media coordination. Eight years of systematic democracy suppression. Running the town like a subsidiary.",
                            "expression": "open",
                            "feedback": "Eight years of systematic democratic suppression documented in Bergström's own hand — candidate assessments, action plans, and budgets. This proves the mill treats local democracy as a line of business to be managed.",
                            "note": "Eight years of Bergström's candidate list with budgets for suppression"
                        }
                    ]
                }
            }
        },
        "headlines": [
            {"text": "COUNCIL CANDIDATE CLAIMS CAMPAIGN INTERFERENCE", "tone": "Cautious"},
            {"text": "MILL DIRECTOR'S OFFICE CALLED EMPLOYER: FIRE HER OR LOSE CONTRACTS", "tone": "Fact-based"},
            {"text": "BERGSTRÖM'S DEMOCRACY LEDGER: BUDGETS FOR SILENCING CANDIDATES", "tone": "Exposing"}
        ]
    },
    {
        "id": "svarta_listan",
        "title": "The Blacklist",
        "description": "Workers who report safety violations or organize union activities are being systematically blacklisted across every employer in Industristad.",
        "lead_text": "A former shop steward hasn't been able to find work in eighteen months. Every employer turns him away. Same words: 'No openings.'",
        "preview": "A man sitting alone at a bar asks if you're the new reporter. He says he has something to show you.",
        "source_type": "street",
        "difficulty": "hard",
        "base_value": 8,
        "category": "labor",
        "npc_id": "torsten_mansson",
        "npc_name": "Torsten Månsson",
        "npc_title": "Former Shop Steward, Steel Mill",
        "town": "industristad",
        "interview": {
            "opening_line": "I reported a gas leak at the smelting hall in February. By March I was laid off. 'Restructuring.' Since then I've applied to every employer in Industristad. Thirty-two applications. Thirty-two rejections. And every one says the same thing: 'No positions available at this time.'",
            "q1_options": [
                {"archetype": "friendly", "text": "Thirty-two rejections. That's brutal, Torsten. What do you think is happening?"},
                {"archetype": "direct", "text": "Do you have evidence of coordination between employers? Letters, calls, anything documented?"},
                {"archetype": "pressure", "text": "Couldn't this just be bad luck? The economy is tough. A lot of people are out of work."},
                {"archetype": "silence", "text": "..."}
            ],
            "branches": {
                "friendly": {
                    "q1_response": "I know what's happening. I'm blacklisted. There's a list — the mill circulates it to every employer in the industrial zone. Troublemakers. Safety complainers. Union organizers. If your name is on it, you don't work in this town. You don't work anywhere within a hundred kilometers.",
                    "expression_hint": "Wiping his forehead despite the cold, leaning in",
                    "q1_note": "Claims a blacklist circulates to all employers",
                    "q2_options": [
                        {"text": "How do you know the list exists? Have you seen it?"},
                        {"text": "Who else is on this list? Are there others like you?"},
                        {"text": "How does your family survive without income?"}
                    ],
                    "outcomes": [
                        {
                            "tier": 1,
                            "response": "I know because Bengt Larsson — he runs the hardware store — he told me. Off the record. 'Torsten, I'd hire you today, but I can't.' I asked why. He just shook his head. 'You know why.' That's the closest anyone's come to admitting it.",
                            "expression": "guarded",
                            "feedback": "A store owner afraid to hire him — confirms the climate of fear but Bengt didn't explicitly mention a list.",
                            "note": "Store owner: 'I'd hire you, but I can't. You know why.'"
                        },
                        {
                            "tier": 2,
                            "response": "At least six of us. Gunnar Falk — reported chemical spills. Unemployed since April. Stig Holm — organized a safety meeting. Fired and can't find work. We compared notes. Every rejection letter is nearly identical. Same phrasing. 'No positions available at this time.' Like they're all reading from the same script.",
                            "expression": "open",
                            "feedback": "Six people with identical rejection letters — the shared phrasing implies coordination. Multiple victims strengthen the pattern.",
                            "note": "Six blacklisted workers, all with identically phrased rejections"
                        },
                        {
                            "tier": 3,
                            "response": "One of the six — I won't say who — his sister works in the mill's personnel office. She found the list. Typed on mill letterhead. Twelve names. Each with a reason: 'Safety agitator.' 'Union organizer.' 'Unreliable attitude.' And at the top: 'This list is distributed at the request of the Mill Director to assist member companies of the Industristad Employers' Association in personnel decisions.' Bergström's signature at the bottom.",
                            "expression": "open",
                            "feedback": "The list itself — on mill letterhead, signed by Bergström, distributed through the Employers' Association. Twelve names with reasons. A formal, signed document proving systematic blacklisting.",
                            "note": "Mill letterhead list signed by Bergström — 12 names, distributed to employers"
                        }
                    ]
                },
                "direct": {
                    "q1_response": "I have this. *slides paper across the bar* My rejection letter from Industristads Pappersbruk. And this one from Hamnen AB. And this one from Kemiska Verken. Look at the date stamps. All within three days of each other. And the wording — it's identical. Word for word. Someone sent them a template.",
                    "expression_hint": "Lays out letters in a row, fingers trembling",
                    "q1_note": "Three rejection letters, three days apart, identical wording",
                    "q2_options": [
                        {"text": "Identical phrasing could mean coordination. But who's coordinating?"},
                        {"text": "Have you contacted a lawyer about wrongful termination or blacklisting?"},
                        {"text": "Do you know of other workers who've experienced the same thing?"}
                    ],
                    "outcomes": [
                        {
                            "tier": 1,
                            "response": "The Employers' Association meets every month. All the major employers. One room. One agenda. And after every meeting, certain people stop getting hired. It's an open secret. But open secrets don't make headlines without proof.",
                            "expression": "guarded",
                            "feedback": "The Employers' Association as the coordination mechanism — plausible but unproven. Needs a document or insider.",
                            "note": "Employers' Association monthly meetings — blacklisting decisions made there"
                        },
                        {
                            "tier": 2,
                            "response": "A lawyer in Gothenburg took a look. He said the identical phrasing in the rejections constitutes 'coordinated employer action' — potentially illegal under labor law. But to prosecute, he needs the source. Someone from inside the Employers' Association who'll talk.",
                            "expression": "open",
                            "feedback": "Legal opinion that the identical rejections constitute coordinated and potentially illegal action. A lawyer's assessment adds professional weight.",
                            "note": "Gothenburg lawyer: identical rejections are 'coordinated employer action'"
                        },
                        {
                            "tier": 3,
                            "response": "I found one. An HR manager at Kemiska Verken — she was disgusted by it. She gave me this. *unfolds a paper* A circular from the Industristad Employers' Association. 'The following individuals are flagged for non-hire consideration.' Twelve names. Mine is number four. The letterhead says 'Distributed by request of Ståhlbergs Stålverk — Mill Director H. Bergström.' He signed it. It's official. Blacklisting as company policy.",
                            "expression": "open",
                            "feedback": "The physical circular with twelve names, distributed through the Employers' Association at Bergström's request. An HR manager as a corroborating source. This is documented, coordinated, and signed — systematic labor oppression.",
                            "note": "Employers' Association circular: 12 names flagged for non-hire, signed Bergström"
                        }
                    ]
                },
                "pressure": {
                    "q1_response": "Bad luck? Thirty-two applications? I'm a certified welder with twenty years' experience. Before the gas leak report I had three job offers in one week. After? Nothing. Zero. For eighteen months. That's not luck. That's a system.",
                    "expression_hint": "Sweat despite cold, jaw working",
                    "q1_note": "Certified welder, 20 years experience — zero offers in 18 months",
                    "q2_options": [
                        {"text": "So prove it. Show me something that connects the mill to your rejections."},
                        {"text": "Did the gas leak you reported turn out to be real?"},
                        {"text": "What happens to a town where no one dares speak up?"}
                    ],
                    "outcomes": [
                        {
                            "tier": 1,
                            "response": "The gas leak was real. They fixed it the same week I reported it. Then they fired me the next week. Fix the problem, remove the person who found it. That's how it works. The message to every other worker: keep quiet or join me at the bar.",
                            "expression": "guarded",
                            "feedback": "The irony of fixing the leak and firing the reporter is damning — but circumstantial without documents.",
                            "note": "Gas leak fixed within a week — reporter fired the next week"
                        },
                        {
                            "tier": 2,
                            "response": "The gas leak was real. Hydrogen sulfide — lethal in concentrations. And here's the inspection report that proved it. Arbetarskyddsstyrelsen came three weeks after I reported it. 'Significant safety deficiencies.' The mill was fined 15,000 kronor. They paid the fine and fired me for causing it. The fine cost less than my salary.",
                            "expression": "open",
                            "feedback": "Official safety inspection validating his report. The fine confirms the danger was real — and less than one man's salary. The economics of silencing a worker.",
                            "note": "Safety board confirmed leak, fined mill 15k — then they fired him"
                        },
                        {
                            "tier": 3,
                            "response": "Here. Connection. *slams a paper on the bar* From the Employers' Association. Twelve names. 'Flagged for non-hire consideration.' I'm number four: 'Torsten Månsson — safety agitator, union organizer, unreliable.' Distributed by Ståhlbergs Stålverk. Bergström's name on the letterhead. This is what happens when you report a gas leak that could have killed thirty men. You get erased. From every payroll in the county.",
                            "expression": "open",
                            "feedback": "The blacklist document with his own name and the damning label 'safety agitator' — for reporting a leak that could have killed thirty men. The document plus the inspectors' validation proves he was punished for being right.",
                            "note": "Blacklist: 'Safety agitator, union organizer, unreliable' — for saving lives"
                        }
                    ]
                },
                "silence": {
                    "q1_response": "...My daughter asked me why I don't go to work anymore. She's seven. I told her daddy's on vacation. Eighteen months of vacation. She's starting to figure out that's not true.",
                    "expression_hint": "Stares at his drink, hands flat on the bar",
                    "q1_note": "'Eighteen months of vacation' — daughter starting to notice",
                    "q2_options": [
                        {"text": "..."},
                        {"text": "Torsten."},
                        {"text": "What do you want to happen?"}
                    ],
                    "outcomes": [
                        {
                            "tier": 1,
                            "response": "I want to work. That's all. I'm a welder. A good one. I just want to weld steel and come home to my family. But I reported a gas leak that could have killed thirty men, and now I'm unemployable. In my own town. Because one man decided I was inconvenient.",
                            "expression": "guarded",
                            "feedback": "Heartbreaking simplicity — a man who just wants to work. The injustice is clear but needs documentation to become a story.",
                            "note": "'I reported a gas leak and became unemployable'"
                        },
                        {
                            "tier": 2,
                            "response": "I found five others. Same story. Report a problem, lose your job, never work again. Gunnar, Stig, Per, Birgit, Kjell. We meet at this bar every Thursday. The Blacklist Club, we call ourselves. We laugh about it. Because if we don't laugh, we drink. And some of us are already drinking too much.",
                            "expression": "open",
                            "feedback": "Six people meeting weekly — the 'Blacklist Club.' The dark humor and the drinking reveal the human cost. Multiple witnesses to the same system.",
                            "note": "Six blacklisted workers meet weekly — 'The Blacklist Club'"
                        },
                        {
                            "tier": 3,
                            "response": "A woman — from inside the mill's personnel office — she found us. She came to the bar one Thursday. She was shaking. She brought this. *slides a worn photocopy across* The list. Twelve names. Reasons. 'Safety agitator.' 'Union organizer.' 'Unreliable attitude.' Distributed to every employer through the Association. Signed by Bergström. She risked her job to bring us this. Because she couldn't sleep either.",
                            "expression": "open",
                            "feedback": "An insider whistleblower delivering the blacklist to its victims. Twelve names, formal distribution, Bergström's signature. The woman's courage mirrors Torsten's — both sacrificing security for truth. The document is the story.",
                            "note": "Insider brought the blacklist to victims — 12 names, signed by Bergström"
                        }
                    ]
                }
            }
        },
        "headlines": [
            {"text": "FORMER MILL WORKER STRUGGLES TO FIND NEW EMPLOYMENT", "tone": "Cautious"},
            {"text": "TWELVE NAMES ON A LIST: WHISTLEBLOWERS WHO CAN'T FIND WORK", "tone": "Fact-based"},
            {"text": "BERGSTRÖM'S BLACKLIST: HOW THE MILL ERASES WORKERS WHO SPEAK UP", "tone": "Exposing"}
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
