#!/usr/bin/env python3
"""Generate Industristad batch 3: 7 stories at base_value 5 (medium-hard)."""
import json, os

STORIES = [
{
    "id": "asbestlarmet",
    "title": "The Asbestos Alarm",
    "description": "Workers at the paper mill report breathing problems. The insulation in the old wing was installed in the 1950s.",
    "lead_text": "Three workers on sick leave with lung problems. All from the same wing of the paper mill.",
    "preview": "A union safety representative slides a document across the table at a diner.",
    "source_type": "document",
    "difficulty": "medium",
    "base_value": 5,
    "category": "labor",
    "npc_id": "folke_dahlberg",
    "npc_name": "Folke Dahlberg",
    "npc_title": "Union Safety Representative",
    "town": "industristad",
    "interview": {
        "opening_line": "I've been trying to get them to test the insulation for two years. Two years. Now three men are coughing blood.",
        "q1_options": [
            {"archetype": "friendly", "text": "That must weigh on you, Folke. Tell me about these workers."},
            {"archetype": "direct", "text": "Do you have the sick leave reports and the insulation test requests?"},
            {"archetype": "pressure", "text": "If asbestos is killing workers and management knew, that's criminal negligence."},
            {"archetype": "silence", "text": "..."}
        ],
        "branches": {
            "friendly": {
                "q1_response": "Rolf has been there twenty-two years. Never missed a day. Now he can't walk up stairs without stopping to breathe. His wife calls me every week asking if it's getting better. I can't tell her the truth.",
                "expression_hint": "Voice cracking, looking down at the table",
                "q2_options": [
                    {"text": "Has a doctor confirmed the connection to the insulation?"},
                    {"text": "What did management say when you reported the sick workers?"},
                    {"text": "Are there more workers affected that we don't know about?"}
                ],
                "outcomes": [
                    {"tier": 1, "response": "The company doctor says it's 'seasonal bronchitis.' Seasonal bronchitis that only affects workers in building C. Right.", "expression": "guarded", "feedback": "A suspicious diagnosis, but no hard proof of asbestos connection.", "note": "Company doctor diagnosed 'seasonal bronchitis'"},
                    {"tier": 2, "response": "Dr. Lindqvist at the hospital ran his own tests. He thinks it's asbestosis. He wrote to the factory but never got a response. I have a copy of his letter — dated March.", "expression": "open", "feedback": "An independent doctor's diagnosis plus a paper trail. Strong evidence.", "note": "Hospital doctor diagnosed asbestosis, letter dated March"},
                    {"tier": 3, "response": "It's not three men. It's seven. Four more are showing symptoms but afraid to report it — they'll lose their overtime shifts. And Rolf... Rolf told me last week he found a memo from 1968 where the factory engineer recommended replacing the insulation. They buried it.", "expression": "open", "feedback": "Seven victims, a buried 1968 memo, and systemic intimidation. This is a cover-up story.", "note": "1968 memo recommended replacement — buried. Seven workers affected."}
                ],
                "q1_note": "Rolf — 22 years, can't walk stairs"
            },
            "direct": {
                "q1_response": "I filed formal complaints in February and again in June. Here — carbon copies. Both stamped 'received' by the safety office. No response. The sick leave reports are with personnel, but I have the dates: Rolf Anderson went off March 15, Sture Elm March 28, Karl-Axel Bohlin April 3.",
                "expression_hint": "Pulling a manila folder from his bag, organized tabs",
                "q2_options": [
                    {"text": "Who specifically received these complaints?"},
                    {"text": "Has the company done any asbestos testing at all?"},
                    {"text": "Can I see the original insulation specifications?"}
                ],
                "outcomes": [
                    {"tier": 1, "response": "Filed with safety office. Staffed by one person — Yvonne Berg. She's not the problem. She forwarded it to plant director Nyman. After that, silence.", "expression": "guarded", "feedback": "Clear chain of responsibility, but need more on what Nyman knew.", "note": "Complaints forwarded to plant director Nyman — no response"},
                    {"tier": 2, "response": "They did one test in 1971. Only in building A — the new wing. Of course that came back clean. Building C, where the sick workers are? Never tested. The test report even says 'remaining buildings to follow.' They never followed.", "expression": "open", "feedback": "A selective test that conveniently avoided the problem building. Documented evasion.", "note": "1971 test only covered new wing — old wing never tested"},
                    {"tier": 3, "response": "Look at this. The original 1953 installation order for building C. 'Sprayed chrysotile insulation, 40mm.' Chrysotile is white asbestos. This was standard then, but they've known it's dangerous since the sixties. And here — the 1971 test report explicitly excludes building C. Someone decided not to look.", "expression": "open", "feedback": "The 1953 spec proves asbestos exists. The 1971 test proves they deliberately avoided confirming it. Devastating combination.", "note": "1953 spec confirms chrysotile. 1971 test deliberately excluded building C."}
                ],
                "q1_note": "Two formal complaints, both ignored"
            },
            "pressure": {
                "q1_response": "Don't you think I know that? I've been saying exactly that. But you try filing criminal charges against the biggest employer in town. The police chief's brother-in-law works in management.",
                "expression_hint": "Jaw tightening, leaning forward",
                "q2_options": [
                    {"text": "So the police won't investigate their own family connections?"},
                    {"text": "Then your only weapon is the press. What can you give me right now?"},
                    {"text": "What would happen to these workers if the factory closed tomorrow?"}
                ],
                "outcomes": [
                    {"tier": 1, "response": "I didn't say that. I said it's complicated. Everyone here depends on that factory. You report this wrong and the whole town turns on the messenger.", "expression": "guarded", "feedback": "He's warning you about the politics but not giving facts. You pushed too hard.", "note": "Political complications — town depends on factory"},
                    {"tier": 2, "response": "Fine. Here's what I can give you. Three names, three dates, one company doctor who diagnosed 'bronchitis' instead of asbestosis. And my two complaints that went into a black hole. Print that and see what happens.", "expression": "open", "feedback": "He's angry but cooperative. Solid factual foundation with a clear misdiagnosis angle.", "note": "Three cases, misdiagnosis, two buried complaints"},
                    {"tier": 3, "response": "You want criminal negligence? I'll give you criminal negligence. The factory's own insurance company sent an inspector in 1970. He recommended immediate asbestos removal. Cost estimate: 400,000 kronor. Nyman wrote 'too expensive' in the margin. Four years later, men are dying. I have a copy of that inspection report.", "expression": "open", "feedback": "An insurance inspection with a written refusal to act. 'Too expensive' while workers sicken. This is the story.", "note": "'Too expensive' — Nyman rejected 1970 insurance recommendation"}
                ],
                "q1_note": "Police chief's brother-in-law in management"
            },
            "silence": {
                "q1_response": "...You're not going to make this easy for me, are you? Fine. I'll start from the beginning. The insulation in building C is from 1953. Sprayed asbestos. We've known it's dangerous for a decade. Management won't test it because they don't want to know.",
                "expression_hint": "Sighs heavily, then speaks with slow deliberation",
                "q2_options": [
                    {"text": "Who decides whether to test?"},
                    {"text": "What happens to the workers who are already sick?"},
                    {"text": "Is there documentation that management was warned?"}
                ],
                "outcomes": [
                    {"tier": 1, "response": "Plant director Nyman has the final say on maintenance and safety. He's been in that chair since '69. Good at saying 'we'll look into it.' Never looks into anything.", "expression": "guarded", "feedback": "Names the decision-maker but no proof of deliberate cover-up.", "note": "Nyman has authority — 'we'll look into it' but never acts"},
                    {"tier": 2, "response": "Rolf is the worst. The hospital diagnosed probable asbestosis. The company doctor overruled it — said bronchitis. Rolf's wife told me he coughs blood at night. And the company is fighting his sick leave claim. They want him back on the floor in building C.", "expression": "open", "feedback": "Competing medical opinions plus the company fighting the sick leave. Human angle with institutional cruelty.", "note": "Company fighting sick leave claim — wants sick worker back in contaminated building"},
                    {"tier": 3, "response": "In 1968, their own engineer — Bertil Sköld — wrote a memo saying the insulation in building C should be replaced 'as a matter of urgency.' Sköld retired the next year. The memo was filed and forgotten. I found it in the union archive last month. They've known for six years.", "expression": "open", "feedback": "A six-year cover-up with their own engineer's warning. Combined with sick workers, this is explosive.", "note": "1968 engineer memo — 'matter of urgency' — filed and forgotten"}
                ],
                "q1_note": "1953 asbestos, management refuses to test"
            }
        }
    },
    "headlines": [
        {"text": "Paper Mill Workers Report Breathing Problems", "tone": "Cautious"},
        {"text": "Three Sick, Asbestos Suspected in Factory Wing", "tone": "Factual"},
        {"text": "WORKERS COUGH BLOOD — FACTORY IGNORED ASBESTOS WARNINGS FOR YEARS", "tone": "Sensational"}
    ]
},
{
    "id": "hamnutbyggnaden",
    "title": "The Harbor Expansion",
    "description": "Plans to expand the industrial harbor would demolish the old fishing quarter. Residents say they were never consulted.",
    "lead_text": "The council approved the harbor expansion quietly. Forty families will lose their homes.",
    "preview": "A folded council meeting agenda arrives by mail, key paragraphs circled in red.",
    "source_type": "document",
    "difficulty": "medium",
    "base_value": 5,
    "category": "politics",
    "npc_id": "astrid_lindkvist",
    "npc_name": "Astrid Lindkvist",
    "npc_title": "Fiskarbacken Resident",
    "town": "industristad",
    "interview": {
        "opening_line": "They decided on a Monday evening. Half the council was absent. No one told us until the survey team showed up in our garden.",
        "q1_options": [
            {"archetype": "friendly", "text": "That must have been a shock, Astrid. How long has your family lived here?"},
            {"archetype": "direct", "text": "Was the decision published in advance? Is there a public comment period?"},
            {"archetype": "pressure", "text": "This looks like the council snuck this through while no one was watching."},
            {"archetype": "silence", "text": "..."}
        ],
        "branches": {
            "friendly": {
                "q1_response": "My husband's family has been here since 1910. His grandfather built this house with his own hands after the big fire. Five generations of fishermen. And they send a letter saying 'compulsory acquisition' like it's nothing.",
                "expression_hint": "Standing at the fence, pointing toward the harbor, voice tight",
                "q2_options": [
                    {"text": "How many families are affected? Are they all fishermen?"},
                    {"text": "What compensation are they offering?"},
                    {"text": "Have you tried to organize the neighbors?"}
                ],
                "outcomes": [
                    {"tier": 1, "response": "At least forty families. Some are fishermen, some retired dock workers. The compensation letter says 'market value' but everyone knows these houses aren't worth much on paper. Our whole lives are here.", "expression": "guarded", "feedback": "Human impact confirmed but no smoking gun on the process.", "note": "40 families, compensation at 'market value' likely below real worth"},
                    {"tier": 2, "response": "Forty-three families. I've been going door to door. Half didn't even know. The compensation is 60,000 kronor for a house — my husband's friend was offered 200,000 for a smaller place in the new district last year. They're robbing us.", "expression": "open", "feedback": "Concrete compensation disparity with a comparable sale. This shows systematic undervaluation.", "note": "60,000 offered — comparable house sold for 200,000 last year"},
                    {"tier": 3, "response": "Here's what I found out. The harbor expansion contract goes to Ståhlbergs Bygg AB. Guess who sits on the council zoning committee? Ståhlberg's nephew, Rolf Ståhlberg Jr. He voted for the expansion. It's in the minutes — I checked. They're demolishing our homes to give a contract to family.", "expression": "open", "feedback": "Conflict of interest — Ståhlberg's nephew on zoning committee voted for a family company contract. This is corruption.", "note": "Ståhlberg nephew on zoning committee voted for family company contract"}
                ],
                "q1_note": "Five generations, compulsory acquisition"
            },
            "direct": {
                "q1_response": "The agenda listed it as 'harbor infrastructure review.' Not 'demolish Fiskarbacken.' The public comment period was two weeks — in July, when everyone's at their summer houses. Four comments were submitted. Four. For forty-three homes.",
                "expression_hint": "Pulling out a folder with the council agenda and timeline",
                "q2_options": [
                    {"text": "Who drafted the proposal? Is it the council or the port authority?"},
                    {"text": "What exactly does the expansion include besides the demolitions?"},
                    {"text": "Were any council members absent who might have voted differently?"}
                ],
                "outcomes": [
                    {"tier": 1, "response": "The port authority drafted it with input from the economic development board. Standard process, they'll say. But the language was designed to bore people into not reading it.", "expression": "guarded", "feedback": "Bureaucratic obfuscation confirmed but hard to prove intent.", "note": "Deliberately boring language to avoid public scrutiny"},
                    {"tier": 2, "response": "The proposal was drafted by port director Stig Wennberg. But look at page 14 — the cost-benefit analysis was done by an outside consultant: Ståhlbergs Konsult AB. The same family that owns the construction company bidding on the project.", "expression": "open", "feedback": "The cost-benefit analysis was done by a company connected to the winning bidder. Clear conflict of interest.", "note": "Cost-benefit by Ståhlbergs Konsult — same family as construction bidder"},
                    {"tier": 3, "response": "Five council members were absent. Three wrote to the chair requesting postponement because they hadn't had time to review the 200-page proposal — it was distributed 48 hours before the vote. The chair overruled them. I have their letters and the timestamp on the document distribution. This was railroaded.", "expression": "open", "feedback": "A 200-page proposal distributed 48 hours before vote, postponement requests denied. Procedural manipulation.", "note": "200-page proposal, 48hrs before vote, postponement denied"}
                ],
                "q1_note": "Comment period in July, 4 responses for 43 homes"
            },
            "pressure": {
                "q1_response": "That's exactly what happened. But when I said that to the local paper, Fabriksbladet, they printed one paragraph on page eight. Their editor plays golf with Ståhlberg. You can't fight that.",
                "expression_hint": "Bitter laugh, shaking her head",
                "q2_options": [
                    {"text": "So Fabriksbladet killed the story. Do you have proof of that connection?"},
                    {"text": "Who benefits most from this expansion? Follow the money."},
                    {"text": "Are the residents willing to fight this publicly?"}
                ],
                "outcomes": [
                    {"tier": 1, "response": "Everyone knows they play golf together. But 'everyone knows' doesn't go in a newspaper, does it? All I know is the competition buried it.", "expression": "guarded", "feedback": "Hearsay about the competitor paper. No usable facts.", "note": "Fabriksbladet allegedly buried the story"},
                    {"tier": 2, "response": "Follow the money? Fine. Ståhlbergs Bygg gets the demolition contract. Ståhlbergs Transport gets the harborcrane installation. And Ståhlbergs Fastigheter is already buying land in the new district where they'll 'relocate' us — at prices they set. Three contracts, one family.", "expression": "open", "feedback": "Three contracts to one family across demolition, construction, and relocation. Corporate self-dealing.", "note": "Three Ståhlberg companies — demolition, crane, relocation"},
                    {"tier": 3, "response": "I'll tell you who benefits. Last week I found a land registry filing. Ståhlbergs Fastigheter bought twelve plots in the new district in June — before the council vote in August. They knew. They bought the relocation land before the decision was even made. That's insider trading, isn't it?", "expression": "open", "feedback": "Land purchases before the public decision. Pre-knowledge of the vote. This is the front page.", "note": "Ståhlberg bought relocation land in June — vote wasn't until August"}
                ],
                "q1_note": "Local paper buried the story"
            },
            "silence": {
                "q1_response": "...I wasn't going to talk to another reporter. Fabriksbladet already let us down. But my neighbor said your paper is different. So here I am. The council decided to demolish Fiskarbacken for a harbor expansion that mostly benefits one company.",
                "expression_hint": "Long pause, then steady, determined voice",
                "q2_options": [
                    {"text": "Which company benefits?"},
                    {"text": "What have the residents been told about their options?"},
                    {"text": "Can I see the official documents — the council decision, the acquisition letters?"}
                ],
                "outcomes": [
                    {"tier": 1, "response": "Ståhlbergs, obviously. Everyone in this town knows everything leads back to Ståhlbergs. But proving it is another thing.", "expression": "guarded", "feedback": "She names the suspect but has no proof. You need to dig elsewhere.", "note": "Ståhlbergs suspected but no proof"},
                    {"tier": 2, "response": "The letters say we have 90 days to accept the offer or face expropriation proceedings. 60,000 for houses worth triple that. And there's no appeal process mentioned — I checked with a lawyer in Gothenburg. He said the notice is legally deficient. Missing the mandatory 30-day appeal window.", "expression": "open", "feedback": "A legally deficient notice is procedural ammunition. Combined with undervaluation, the residents have a case.", "note": "Acquisition notice missing mandatory 30-day appeal window"},
                    {"tier": 3, "response": "Here. I copied these from the municipal archive before they noticed. Council member attendance records, the vote tally — 7 to 5, with the chair breaking the tie — and the contract award to Ståhlbergs Bygg, signed the same day as the vote. Same day. The contract was ready before they voted. This was decided in advance.", "expression": "open", "feedback": "Contract signed the same day as the vote — prepared in advance. Combined with the razor-thin margin and absences, this proves the fix was in.", "note": "Contract signed same day as vote — prepared in advance"}
                ],
                "q1_note": "Council decided, one company benefits"
            }
        }
    },
    "headlines": [
        {"text": "Harbor Expansion to Displace Families in Fishing Quarter", "tone": "Factual"},
        {"text": "Forty Families Face Eviction for Port Deal", "tone": "Narrative"},
        {"text": "COUNCIL PUSHED THROUGH HARBOR DEAL — SAME FAMILY WINS EVERY CONTRACT", "tone": "Exposing"}
    ]
},
{
    "id": "kemikaliedumpen",
    "title": "The Chemical Dump",
    "description": "A tip about barrels buried behind the chemical plant. The soil smells sharp and the grass won't grow.",
    "lead_text": "Something is wrong with the ground behind Industrikemi AB. Nothing grows there anymore.",
    "preview": "A former truck driver catches your arm outside the post office.",
    "source_type": "street",
    "difficulty": "medium",
    "base_value": 5,
    "category": "environment",
    "npc_id": "anders_strom",
    "npc_name": "Anders Ström",
    "npc_title": "Former Truck Driver",
    "town": "industristad",
    "interview": {
        "opening_line": "I drove those barrels, you understand? They told me it was waste product. Harmless, they said. But the smell... I still have headaches from it.",
        "q1_options": [
            {"archetype": "friendly", "text": "That sounds frightening, Anders. How long were you driving those loads?"},
            {"archetype": "direct", "text": "Where exactly were the barrels dumped? How many and over what time period?"},
            {"archetype": "pressure", "text": "If those barrels are toxic and they told you it was harmless, you were lied to. And the ground is poisoned."},
            {"archetype": "silence", "text": "..."}
        ],
        "branches": {
            "friendly": {
                "q1_response": "Two years. '71 to '73. Every Thursday night. They always wanted it done at night. I should have asked why. My wife says I should see a doctor about the headaches, but what am I going to tell them?",
                "expression_hint": "Chain-smoking, leg bouncing, keeps looking at the road",
                "q2_options": [
                    {"text": "Did anyone else drive those routes? Any other witnesses?"},
                    {"text": "What did the barrels look like? Any markings or labels?"},
                    {"text": "Why did you stop driving for them?"}
                ],
                "outcomes": [
                    {"tier": 1, "response": "Just me for the night runs. They liked that I kept quiet. The barrels were standard steel drums, no labels I could read. Just numbers.", "expression": "guarded", "feedback": "Confirms the operation but limited physical evidence.", "note": "Night runs, unmarked steel drums with number codes"},
                    {"tier": 2, "response": "The barrels had a stencil — 'IK-process 4' and a skull symbol. I saw them stack about thirty per load, once a week. For two years. That's over three thousand barrels in the ground. And last year the well in Söderby started tasting strange.", "expression": "open", "feedback": "A skull symbol, a quantity estimate, and contaminated water. Environmental crime with reach.", "note": "IK-process 4 skull symbol, ~3000 barrels, Söderby well contaminated"},
                    {"tier": 3, "response": "I'll tell you why I stopped. I got sick. Lost feeling in my fingers for a month. The company doctor said 'stress.' But I saw the shipping manifest once — I wasn't supposed to. It listed 'chlorinated solvents, class 3 toxic waste.' They were burying class 3 toxic waste in an unlined pit behind the factory. And the water table is six meters down.", "expression": "open", "feedback": "Classified toxic waste in an unlined pit near the water table. Plus health effects on the driver. Environmental catastrophe.", "note": "Chlorinated solvents class 3, unlined pit, water table 6m down"}
                ],
                "q1_note": "Every Thursday night for two years"
            },
            "direct": {
                "q1_response": "Behind the factory, east side, past the old loading dock. There's a clearing — used to be a field. They dug a trench about fifty meters long. I'd back in, the forklift would unload, and they'd cover it with dirt. Thirty barrels each time, once a week, January '71 through December '72.",
                "expression_hint": "Drawing a rough map on a napkin",
                "q2_options": [
                    {"text": "Is the trench still accessible? Could someone verify it's there?"},
                    {"text": "Who gave you the orders? Names."},
                    {"text": "Do you have any of the delivery documents?"}
                ],
                "outcomes": [
                    {"tier": 1, "response": "They built a parking lot over it last spring. Concrete. But if you dig, it's there. The orders came from the logistics manager, Torbjörn Wik.", "expression": "guarded", "feedback": "Location confirmed but now paved over. One name.", "note": "Parking lot built over dump site spring '74. Logistics manager Torbjörn Wik."},
                    {"tier": 2, "response": "I kept one delivery slip. Just one — I knew something was wrong. It lists the load as '40 drums process residue, IK-4 class.' Signed by shift supervisor Henrik Rönn. The dump site coordinates match the parking lot they poured last spring — I noted the kilometer marker.", "expression": "open", "feedback": "A physical delivery document with a signature and matching coordinates. Documentary proof.", "note": "Delivery slip: 40 drums IK-4, signed Henrik Rönn, coordinates match"},
                    {"tier": 3, "response": "I kept one delivery slip. But more important — I know where the second dump is. Not just the east field. There's another one, under the football pitch they donated to the town in '73. Right after they stopped using the east field. They donated the pitch so no one would ever dig there. Three thousand barrels under a children's football field.", "expression": "open", "feedback": "A second dump site under a public football field — donated specifically to prevent discovery. Children playing over toxic waste.", "note": "Second dump under football pitch — donated to prevent discovery"}
                ],
                "q1_note": "50m trench, 30 barrels/week, '71-'72"
            },
            "pressure": {
                "q1_response": "Damn right I was lied to. And the ground is poisoned. You want to know how I know? My dog drank from a puddle behind the factory last autumn. Dead in three days. The vet said organ failure.",
                "expression_hint": "Voice rising, then catching himself, looking around",
                "q2_options": [
                    {"text": "Did the vet document the cause of death? Could it be tested?"},
                    {"text": "Have you reported this to the environmental authorities?"},
                    {"text": "Who else at the factory knows about the dumping?"}
                ],
                "outcomes": [
                    {"tier": 1, "response": "The vet wrote 'suspected poisoning.' I kept the receipt. But I didn't report it — who am I going to report it to? The county environmental board meets once a quarter. Half of them work for Industrikemi.", "expression": "guarded", "feedback": "A dead dog and a vet suspecting poisoning. Emotional but thin on proof.", "note": "Dog died — vet suspected poisoning. Environmental board compromised."},
                    {"tier": 2, "response": "The vet has tissue samples frozen. He told me — off the record — the liver showed traces consistent with chlorinated compounds. And three kids in Söderby have rashes that won't go away. Same neighborhood as the well that tastes strange. You connect those dots.", "expression": "open", "feedback": "Vet tissue samples plus sick children near a affected well. Human health impact elevates everything.", "note": "Vet has tissue samples — chlorinated compounds. Three kids with rashes near affected well."},
                    {"tier": 3, "response": "Everyone on the night shift knows. But here's the thing — foreman Göte Nyberg authorized every load. And Göte retired last year with a house in Spain. A foreman. A house in Spain. On his salary? He was paid to keep quiet. I can give you his old address and the name of every driver who worked the night shift.", "expression": "open", "feedback": "A foreman who retired to Spain on a foreman's salary. Hush money. Plus a list of witnesses.", "note": "Foreman Göte Nyberg — Spanish retirement home on foreman's salary. Witness list available."}
                ],
                "q1_note": "Dog died from puddle water behind factory"
            },
            "silence": {
                "q1_response": "...I've been carrying this for three years. Couldn't sleep. Started drinking. My wife almost left. I need to tell someone who'll actually do something with it. They buried barrels of chemical waste behind the factory. I drove the truck.",
                "expression_hint": "Long exhale, shoulders dropping, finally unburdening",
                "q2_options": [
                    {"text": "Start from the beginning. When did the first load go out?"},
                    {"text": "What do you need from me to feel safe telling this story?"},
                    {"text": "Do you know what was in the barrels?"}
                ],
                "outcomes": [
                    {"tier": 1, "response": "January 1971 was the first run. I remember because it was freezing, minus twenty, and the ground was so hard they had to wait a week to dig. It went on for two years, maybe more after I left.", "expression": "guarded", "feedback": "Timeline confirmed but no details on what was dumped or proof of harm.", "note": "Dumping started January 1971, ground too frozen at first"},
                    {"tier": 2, "response": "I wasn't supposed to see the labels. But one barrel was cracked and I read it while they were sealing the leak. 'Trikloreten — farligt avfall.' Trichloroethylene. That stuff causes cancer. And they were just... putting it in the ground.", "expression": "open", "feedback": "He read the label: trichloroethylene, classified as hazardous waste. A known carcinogen buried uncontained.", "note": "Trichloroethylene — classified hazardous waste — buried uncontained"},
                    {"tier": 3, "response": "I know what was in them because I stole one. It's in my garage. Sealed, unopened. I took it because I knew someday someone would need proof. If you get it tested, you'll have everything you need. It's the same stuff they put in the ground — hundreds of barrels of it.", "expression": "open", "feedback": "He has a physical barrel. Testable evidence of exactly what was dumped. This is the story of the year.", "note": "Physical barrel in his garage — testable proof of waste composition"}
                ],
                "q1_note": "Couldn't sleep for three years, drove the truck"
            }
        }
    },
    "headlines": [
        {"text": "Former Driver Reports Chemical Waste Behind Factory", "tone": "Factual"},
        {"text": "The Ground Behind Industrikemi Won't Grow Grass Anymore", "tone": "Narrative"},
        {"text": "THOUSANDS OF TOXIC BARRELS BURIED IN SECRET — CHILDREN PLAY ABOVE", "tone": "Sensational"}
    ]
},
{
    "id": "varvsarbetarna",
    "title": "The Shipyard Workers",
    "description": "The shipyard is advertising for workers but former employees say conditions are deadly. Two men died last year.",
    "lead_text": "Two dead in twelve months. The shipyard keeps advertising for more hands.",
    "preview": "A crumpled leaflet with 'KILLERS' written across a shipyard job ad.",
    "source_type": "letter",
    "difficulty": "medium",
    "base_value": 5,
    "category": "labor",
    "npc_id": "rune_hellstrom",
    "npc_name": "Rune Hellström",
    "npc_title": "Former Shipyard Welder",
    "town": "industristad",
    "interview": {
        "opening_line": "I worked that yard for eight years. Saw Bo Mattsson fall thirty meters because the scaffold wasn't bolted. They cleaned the blood and had a new man up there the next morning.",
        "q1_options": [
            {"archetype": "friendly", "text": "I'm sorry about Bo. Were you close?"},
            {"archetype": "direct", "text": "The scaffold wasn't bolted — was this documented? Was there an investigation?"},
            {"archetype": "pressure", "text": "If the scaffold wasn't bolted and the company knew, they killed Bo Mattsson."},
            {"archetype": "silence", "text": "..."}
        ],
        "branches": {
            "friendly": {
                "q1_response": "Bo was my best friend. We started the same week. His daughter asks me why her father isn't coming home. I don't know what to say. The company sent flowers. Flowers.",
                "expression_hint": "Staring at nothing, heavy breathing",
                "q2_options": [
                    {"text": "Has Bo's family pursued any legal action?"},
                    {"text": "You said two deaths — who was the second?"},
                    {"text": "Are workers afraid to speak up about safety?"}
                ],
                "outcomes": [
                    {"tier": 1, "response": "The family can't afford a lawyer. The union offered 'condolences.' Condolences. No legal support, nothing. They're too afraid of losing the yard contract to fight the company.", "expression": "guarded", "feedback": "Union failure to support the family. Sad but circumstantial.", "note": "Union offered condolences only — no legal support for family"},
                    {"tier": 2, "response": "The second was Dragan, a Yugoslav welder. Last March. Gas leak in a confined space. No ventilation, no gas detector. The company said he 'failed to follow procedure.' But there was no procedure — I've seen the safety manual. The chapter on confined spaces is three lines long.", "expression": "open", "feedback": "Two deaths, both due to missing safety procedures. Safety manual inadequacy is provable.", "note": "Second death — Dragan, gas leak in confined space. Safety manual has 3 lines on confined spaces."},
                    {"tier": 3, "response": "I'll tell you about the workers. They're afraid. Half are immigrant workers, Yugoslav and Finnish. No union membership, no Swedish, no rights. The company prefers them because they don't complain. They can't complain. Two men died and the only report is a one-page internal memo I copied from the foreman's desk. 'Resolved — no further action.' That's what two lives are worth.", "expression": "open", "feedback": "Exploited immigrant workers, no safety reporting, internal memo saying 'resolved.' Systemic negligence targeting the vulnerable.", "note": "Immigrant workers exploited — can't complain. Internal memo: 'Resolved — no further action.'"}
                ],
                "q1_note": "Bo fell 30 meters, company sent flowers"
            },
            "direct": {
                "q1_response": "The work inspection report listed 'contributing factor: improperly secured scaffolding.' But the conclusion said 'worker error.' Bo's error, apparently, for trusting the scaffold his company built. The report was done by an inspector who used to work at the yard.",
                "expression_hint": "Pulling a folded photocopy from his jacket",
                "q2_options": [
                    {"text": "A former yard employee inspected his own old workplace? Can you prove that?"},
                    {"text": "Were there previous safety violations at the yard?"},
                    {"text": "What did the company change after Bo's death?"}
                ],
                "outcomes": [
                    {"tier": 1, "response": "Inspector Erik Holst worked at Bergdahl Varv from '65 to '70 as safety coordinator. Then he moved to the county inspection board. I know because he was my supervisor. Print that.", "expression": "guarded", "feedback": "Conflict of interest in the inspection but need more to prove it affected the outcome.", "note": "Inspector Holst was former yard safety coordinator '65-'70"},
                    {"tier": 2, "response": "Fourteen violations in three years. I copied the list from the union files. Everything from missing guardrails to unlicensed crane operators. Twelve resulted in 'warnings.' None in shutdowns. And after each warning, the same violations reappeared within a month.", "expression": "open", "feedback": "Fourteen violations, only warnings, systematic non-compliance. A pattern of impunity.", "note": "14 violations, 3 years, warnings only, same issues recur monthly"},
                    {"tier": 3, "response": "After Bo died, they installed the bolt. One bolt. The exact scaffold where he fell. Nothing else changed. But here's the damning part — I found the maintenance log. The scaffold was reported as defective three weeks before Bo's fall. The foreman signed the report and wrote 'repair when convenient.' Convenient. Bo died three weeks later because the repair wasn't convenient enough.", "expression": "open", "feedback": "'Repair when convenient' — three weeks later a man is dead. The signed log proves foreknowledge.", "note": "Scaffold reported defective 3 weeks before death — 'repair when convenient'"}
                ],
                "q1_note": "Inspection said 'worker error,' inspector was ex-employee"
            },
            "pressure": {
                "q1_response": "Yes, they killed him. And I'll say that in print if you need me to. They killed Bo Mattsson and they killed Dragan Petrović and they'll kill someone else before Christmas if nothing changes.",
                "expression_hint": "Leaning forward aggressively, jaw tight",
                "q2_options": [
                    {"text": "That's a serious accusation. What evidence can back it up?"},
                    {"text": "Is the company aware of the risks and choosing to ignore them?"},
                    {"text": "Would other workers testify?"}
                ],
                "outcomes": [
                    {"tier": 1, "response": "Backs it up? Two dead men back it up. But I know how newspapers work — you need paper. I don't have the paper. They don't let us keep copies of anything.", "expression": "guarded", "feedback": "Willing to speak but no documentation. His testimony alone isn't enough.", "note": "No documentation — company prevents workers from keeping copies"},
                    {"tier": 2, "response": "I stole the accident report on Dragan before they filed it. Look at this — 'ventilation equipment available but not deployed.' Available. They had gas detectors in a locker fifty meters away. They just didn't bother. And the report recommends 'continued monitoring.' A man is dead and they recommend monitoring.", "expression": "open", "feedback": "Safety equipment existed but wasn't used. Post-mortem recommendation is toothless. Provable negligence.", "note": "Gas detectors in locker 50m away — not deployed. Report: 'continued monitoring'"},
                    {"tier": 3, "response": "Other workers? The Yugoslav boys can't talk — they'll be deported. But Per-Henrik Olsen, the crane operator, he'll talk. He was there when Bo fell. And he told me something he's never told anyone: the foreman ordered them to use the scaffold that morning even though everyone could see the missing bolt. Per-Henrik heard him say, 'We're behind schedule, use it anyway.' Use it anyway.", "expression": "open", "feedback": "An eyewitness heard the order to use a known-defective scaffold. Direct testimony of reckless endangerment.", "note": "Foreman ordered use of known-defective scaffold — witness Per-Henrik Olsen"}
                ],
                "q1_note": "Will say they killed Bo on the record"
            },
            "silence": {
                "q1_response": "...I quit because I knew I'd be next. The crane cable above my station was fraying. I reported it twice. Nothing. I walked out. Then Bo fell. And I thought — what if I'd reported it louder? What if I'd called the papers then?",
                "expression_hint": "Sitting on factory steps, staring at nothing",
                "q2_options": [
                    {"text": "You reported the fraying cable? To whom, and was it recorded?"},
                    {"text": "Is the crane cable still fraying?"},
                    {"text": "What would need to change for the yard to be safe?"}
                ],
                "outcomes": [
                    {"tier": 1, "response": "I told foreman Anderberg. Verbally and once in writing on the weekly checklist. He checked 'noted.' That was it.", "expression": "guarded", "feedback": "Verbal and written reports were 'noted' and ignored. But you need the checklist as proof.", "note": "Reported to foreman Anderberg — 'noted' on checklist, never actioned"},
                    {"tier": 2, "response": "I don't know about the cable. But I know this: after Bo died, the insurance company calculated the premium increase at 15,000 kronor per year. The company told the insurer they'd fixed all defects. I saw the letter because the secretary left it on the copier. They lied on an insurance claim to keep premiums down. That's fraud.", "expression": "open", "feedback": "Insurance fraud — claiming defects fixed that weren't. A new crime on top of the negligence.", "note": "Company lied on insurance claim — said defects fixed when they weren't"},
                    {"tier": 3, "response": "I went back last week. Climbed the fence at night. I took photographs. The scaffold where Bo fell has one bolt replaced but three others are loose. The crane cable is still fraying — you can see the broken strands. And there's a new crew of Finnish workers up there every morning. I have the photos in my car. Six rolls of film.", "expression": "open", "feedback": "Photographic evidence of current danger plus the continuation of the same negligence after two deaths. Undeniable.", "note": "Photos of ongoing defects — scaffold bolts loose, cable fraying, new immigrant crew at risk"}
                ],
                "q1_note": "Quit after cable reports ignored, before Bo's death"
            }
        }
    },
    "headlines": [
        {"text": "Two Dead in Twelve Months at City Shipyard", "tone": "Factual"},
        {"text": "He Saw His Friend Fall — Now He's Speaking Up", "tone": "Personal"},
        {"text": "SHIPYARD KNEW SCAFFOLD WAS BROKEN — ORDERED WORKERS UP ANYWAY", "tone": "Exposing"}
    ]
},
{
    "id": "staldammen",
    "title": "The Steel Dust",
    "description": "Residents near the steel mill report a constant layer of metallic dust on everything. Children play in it.",
    "lead_text": "The windshields are coated every morning. The flowers turned grey. The children cough.",
    "preview": "A woman in an apron flags you down while pointing at factory smokestacks.",
    "source_type": "street",
    "difficulty": "medium",
    "base_value": 5,
    "category": "environment",
    "npc_id": "astrid_lindkvist",
    "npc_name": "Astrid Lindkvist",
    "npc_title": "Söderby Resident",
    "town": "industristad",
    "interview": {
        "opening_line": "See that? That grey coating on my laundry? That's from the mill. Every single day. My grandchildren play in the yard and breathe this in.",
        "q1_options": [
            {"archetype": "friendly", "text": "How long has this been going on, Astrid? When did you first notice?"},
            {"archetype": "direct", "text": "Have you had the dust tested? Do you know what's in it?"},
            {"archetype": "pressure", "text": "If the mill is showering residential areas with metal dust, the county board should shut them down."},
            {"archetype": "silence", "text": "..."}
        ],
        "branches": {
            "friendly": {
                "q1_response": "It's always been dusty here. But the last two years — since they doubled production — it's gotten unbearable. I used to grow tomatoes. Now nothing grows right. The leaves get this grey film and they wilt.",
                "expression_hint": "Pointing at the factory smoke, voice cracking with frustration",
                "q2_options": [
                    {"text": "Have other neighbors complained about their gardens?"},
                    {"text": "Has anyone connected the health issues to the dust?"},
                    {"text": "Did something change at the mill two years ago?"}
                ],
                "outcomes": [
                    {"tier": 1, "response": "Everyone complains, but to whom? The municipality says it's within regulations. 'Within regulations.' My grandchild has asthma since last winter.", "expression": "guarded", "feedback": "Community impact but no proof it exceeds legal limits.", "note": "Municipality says within regulations — grandchild developed asthma"},
                    {"tier": 2, "response": "The teacher at Söderby school sent a letter to the health board. Fourteen children with respiratory issues in her class alone. Fourteen out of twenty-two. She has attendance records showing the pattern — worst on days with easterly wind, when the smoke blows toward the school.", "expression": "open", "feedback": "A teacher documented the wind-pattern correlation. Fourteen children affected. Statistical evidence.", "note": "14 of 22 children with respiratory issues — worse on easterly wind days"},
                    {"tier": 3, "response": "My neighbor, retired chemistry teacher Olle Grahn, collected samples for six months. He sent them to the university lab in Lund — paid out of his own pocket. The report came back last week: iron oxide, manganese particles, and traces of hexavalent chromium. Chromium. That causes cancer. And it's falling on our children's playground.", "expression": "open", "feedback": "Lab-confirmed hexavalent chromium — a known carcinogen — in the dust. University lab results. This is an environmental and public health crisis.", "note": "University lab: iron oxide, manganese, hexavalent chromium in dust samples"}
                ],
                "q1_note": "Worse since 2 years — production doubled"
            },
            "direct": {
                "q1_response": "Tested? Where? By whom? The nearest lab is in Gothenburg. But I'll tell you what I've done — I collected the dust from my windowsill every morning for two months. Jars of it. If someone tells me where to send it, I'll send it today.",
                "expression_hint": "Opening a cabinet to show rows of labeled glass jars",
                "q2_options": [
                    {"text": "Those samples are valuable. Has anyone official collected air quality data here?"},
                    {"text": "When is the dust worst — time of day, wind direction?"},
                    {"text": "Has the mill responded to any complaints at all?"}
                ],
                "outcomes": [
                    {"tier": 1, "response": "The county measured air quality once. In 1970. On a Sunday. The mill doesn't run full production on Sundays. Of course the readings were fine.", "expression": "guarded", "feedback": "Air quality measured on a low-production day. Suspicious but circumstantial.", "note": "Air quality tested once — on a Sunday when production is low"},
                    {"tier": 2, "response": "The mill installed new electrostatic filters in '71. The county approved. But Olle — my neighbor, he's a retired chemist — he says those filters have a rated life of three years. It's been four. Nobody has checked if they're still working. And the dust got worse in '73.", "expression": "open", "feedback": "Expired pollution filters. Timeline matches the increase in complaints. Maintenance failure.", "note": "Electrostatic filters expired after 3-year rated life — no replacement in 4 years"},
                    {"tier": 3, "response": "I tracked the mill's complaints log through a freedom-of-information request. One hundred and twelve complaints in the last two years. All answered with the same form letter: 'We will investigate.' Not one investigation was conducted. I have the log and every form letter. Identical text, different dates. They copied and pasted away our health.", "expression": "open", "feedback": "112 complaints, identical form responses, zero investigations. A paper trail of systematic non-compliance.", "note": "112 complaints, identical form letters, zero investigations conducted"}
                ],
                "q1_note": "Two months of dust samples in labeled jars"
            },
            "pressure": {
                "q1_response": "The county board? Half of them used to work at the mill! This town was built for the mill. We're just here to serve it. When the mill coughs, the town swallows.",
                "expression_hint": "Arms crossed, bitter, daring you to do something",
                "q2_options": [
                    {"text": "If the county board is compromised, who has the authority to act?"},
                    {"text": "What would it take to get independent testing done?"},
                    {"text": "Are people getting sick? Can you name specific cases?"}
                ],
                "outcomes": [
                    {"tier": 1, "response": "The national environmental protection agency, maybe. But they respond to reports from the county board. And the county board won't report it. It's a circle.", "expression": "guarded", "feedback": "Regulatory capture — every watchdog watches the wrong way. Structural problem but no smoking gun.", "note": "Regulatory capture — county board won't report to national agency"},
                    {"tier": 2, "response": "Sick? Let me show you the list. I went door to door last month. Seventeen households reporting respiratory problems. Three cancer cases in Tallvägen alone — all diagnosed in the last four years. And Tallvägen is directly downwind from the mill's main stack.", "expression": "open", "feedback": "A cancer cluster in the downwind neighborhood. Three cases in one street. Statistical alarm.", "note": "Three cancer cases on Tallvägen — directly downwind from main stack"},
                    {"tier": 3, "response": "Fine. Here's what you need to know. The mill applied for a production increase permit in 1972. The county required 'updated emission filtering.' The mill submitted a certificate saying new filters were installed. My neighbor Olle climbed the fence last month and photographed the filter housing. The seals are original — from 1969. They never replaced them. They submitted a false certificate.", "expression": "open", "feedback": "A false emission certificate to the county. Fraud plus endangerment. With photographic proof.", "note": "False certificate — filters never replaced. Photographed original 1969 seals."}
                ],
                "q1_note": "County board is compromised — former mill employees"
            },
            "silence": {
                "q1_response": "...I've been talking about this for two years. No one listens. The municipality says it's fine. The mill says it's fine. But you know what? My curtains used to be white. Now they're grey. My husband's cough is getting worse. And the children...",
                "expression_hint": "Trailing off, touching a grey-stained curtain",
                "q2_options": [
                    {"text": "When you say 'the children' — what's happening to them?"},
                    {"text": "Has a doctor connected your husband's cough to the dust?"},
                    {"text": "You said you talked for two years — who did you talk to?"}
                ],
                "outcomes": [
                    {"tier": 1, "response": "The school nurse says they have more asthma inhalers than any school in the county. But she won't say it on the record. She's afraid of losing her job.", "expression": "guarded", "feedback": "School nurse confirms an asthma crisis but won't go public. Suggestive but no quotes.", "note": "School nurse: most asthma inhalers in county, won't speak publicly"},
                    {"tier": 2, "response": "I wrote to the county health officer. His response: 'The mill's emissions are within the parameters set by the 1968 permit.' The 1968 permit. Before the production increase. They're measuring against outdated limits. The permit needs to be updated but no one will do it.", "expression": "open", "feedback": "Emissions measured against a permit issued before production doubled. Regulatory loophole.", "note": "Emissions measured against 1968 permit — before production doubled"},
                    {"tier": 3, "response": "My husband died last month. Lung cancer. He never smoked. The doctor at the hospital told me — privately, in the hallway — that he'd seen four cases from this neighborhood in two years. He said 'environmental factors are likely contributing.' He won't write that down. But he looked me in the eye and said it. Four dead from one street. Tell me the dust is fine.", "expression": "open", "feedback": "Four lung cancer deaths in one street. A doctor privately confirming environmental causes. This is a public health catastrophe.", "note": "Husband dead — lung cancer, never smoked. Doctor: 4 cases from one street, 'environmental factors'"}
                ],
                "q1_note": "Two years of talking, nobody listening"
            }
        }
    },
    "headlines": [
        {"text": "Residents Near Mill Report Constant Dust and Health Complaints", "tone": "Cautious"},
        {"text": "Grey Dust Covers Söderby — Is the Mill Making People Sick?", "tone": "Questioning"},
        {"text": "CANCER CLUSTER FOUND DOWNWIND FROM STEEL MILL — COUNTY USED OUTDATED LIMITS", "tone": "Exposing"}
    ]
},
{
    "id": "invandrarbaracken",
    "title": "The Immigrant Barracks",
    "description": "Yugoslav guest workers at the steel mill are housed in former military barracks. Conditions are reportedly dreadful.",
    "lead_text": "Twenty men in a barracks built for ten soldiers. No heating after midnight. Shared toilet for forty.",
    "preview": "A note in broken Swedish, pushed under the newspaper office door.",
    "source_type": "letter",
    "difficulty": "medium",
    "base_value": 5,
    "category": "human_interest",
    "npc_id": "dragan_kovacevic",
    "npc_name": "Dragan Kovačević",
    "npc_title": "Steel Mill Worker, Guest Worker",
    "town": "industristad",
    "interview": {
        "opening_line": "Please — not my name in the paper. They send us home if we complain. But someone must know how we live.",
        "q1_options": [
            {"archetype": "friendly", "text": "I understand, Dragan. I can protect your identity. Tell me what life is like in the barracks."},
            {"archetype": "direct", "text": "I won't print your name. How many workers are housed there? What are the exact conditions?"},
            {"archetype": "pressure", "text": "These conditions sound illegal. If the housing authority inspected, the company would be shut down."},
            {"archetype": "silence", "text": "..."}
        ],
        "branches": {
            "friendly": {
                "q1_response": "We came for better life. Back home I am teacher. Here I am piece of machine. We work, we sleep, we work again. The barracks has no hot water since October. Mold on walls. My friend Zoran is coughing all night. We can't see doctor — they say time off is contract violation.",
                "expression_hint": "Speaking slowly in accented Swedish, watching for the foreman",
                "q2_options": [
                    {"text": "What did you do back home? What brought you to Sweden?"},
                    {"text": "Who manages the barracks? Is it the company or a housing provider?"},
                    {"text": "You said no doctor visits — what happens when someone is seriously ill?"}
                ],
                "outcomes": [
                    {"tier": 1, "response": "The barracks is company property. The foreman has keys. We pay 800 kronor per month from our salary. For mold and cold water. Swedish workers get company apartments in town with central heating and their own bathroom.", "expression": "guarded", "feedback": "Two-tier housing system. Swedish workers get apartments, immigrants get barracks. But no proof of code violations.", "note": "800 kr/month for barracks — Swedish workers get heated apartments"},
                    {"tier": 2, "response": "Mirko broke his arm last month. Foreman drove him to hospital but told the doctor Mirko fell at home, not at work. No workers' compensation. Mirko paid the hospital bill himself — three months' savings. The foreman said if he reported it as workplace accident, his contract would be 'reviewed.'", "expression": "open", "feedback": "Fabricated accident reports to avoid workers' comp. The foreman is systematically covering up workplace injuries.", "note": "Workplace injuries reported as home accidents — foreman threatens contracts"},
                    {"tier": 3, "response": "I have photographs. I borrowed camera from the church volunteer, Mrs. Engström. Mold, broken windows, electrical wires hanging. The toilet overflows twice a week. And here — the contract we signed in Belgrade. It promises 'furnished apartment with private facilities.' This is what they gave us instead. We were lied to before we even came.", "expression": "open", "feedback": "Photos of conditions plus a contract that promised something entirely different. Documentary proof of fraudulent recruitment.", "note": "Photos of conditions. Contract promised 'furnished apartment' — got military barracks."}
                ],
                "q1_note": "Former teacher — no hot water, mold, can't see doctor"
            },
            "direct": {
                "q1_response": "Forty-two workers in four barracks buildings. Originally military, from the war. Two toilets per building, one shower — cold water only since October. No insulation. Last week it was minus fifteen and the heating stopped at midnight. Company says energy savings.",
                "expression_hint": "Cautious, speaking in precise measured facts",
                "q2_options": [
                    {"text": "How much rent are you paying for these conditions?"},
                    {"text": "Has anyone from the housing inspection ever visited?"},
                    {"text": "What does your employment contract say about housing?"}
                ],
                "outcomes": [
                    {"tier": 1, "response": "Eight hundred kronor each. Per month. Deducted from salary before we see it. For comparison, my colleague Sven — Swedish worker, same job — pays 650 for a two-room apartment in town with heating included.", "expression": "guarded", "feedback": "Workers paying more for worse housing. Discrimination visible but circumstantial.", "note": "800kr for barracks vs 650kr for Swedish workers' heated apartments"},
                    {"tier": 2, "response": "Housing inspection? Once. They came in April — warmest month. Everything looked acceptable. But they gave us two weeks' notice. Two weeks! The company repaired the worst things, brought in temporary heaters, fixed one toilet. Inspector came, checked boxes, left. Next day the heaters were removed.", "expression": "open", "feedback": "Stage-managed inspection with adequate notice to temporarily fix problems. Regulatory theater.", "note": "Inspection with 2 weeks notice — temporary repairs removed next day"},
                    {"tier": 3, "response": "I kept records. Every day since I arrived. Temperature, water availability, incidents. In my language, hidden in my mattress. Fourteen months of daily logs. On December 3, the heating failed completely. Minus eighteen outside. We burned wooden pallets in a metal barrel inside the barracks. The fire department came. The company said 'the workers were careless.' We were trying not to freeze to death.", "expression": "open", "feedback": "Fourteen months of daily documentation. The pallet fire incident — workers blamed for trying to survive. Powerful narrative with documentary support.", "note": "14 months of daily logs. Pallet fire in -18° — company blamed workers for 'carelessness'"}
                ],
                "q1_note": "42 workers, 4 barracks, cold water, -15° with no heating"
            },
            "pressure": {
                "q1_response": "Illegal? Maybe. But who enforces? The inspector comes when the company says come. And we can't complain — our work permits are tied to this employer. If they cancel contract, we go home. Home is worse. That is how they control us.",
                "expression_hint": "Looking directly at you for the first time, fierce and sad",
                "q2_options": [
                    {"text": "So the work permit system traps you. Has anyone tried to change employers?"},
                    {"text": "Are there documents proving the company controls the housing inspections?"},
                    {"text": "What would you want Swedish people to know about your situation?"}
                ],
                "outcomes": [
                    {"tier": 1, "response": "Two men tried to leave. Applied to another factory. Their foreman found out and reported them to immigration as 'abandoning contracted employment.' They were deported within a week. The message was clear.", "expression": "guarded", "feedback": "Deportation used as punishment. Modern serfdom. But you'd need to verify with immigration records.", "note": "Two workers deported for trying to change employers"},
                    {"tier": 2, "response": "Goran tried to join the union. The local chapter said his membership was 'under review' for six months. Six months. Swedish workers join the same day. When he finally got in, his foreman transferred him to the worst shift — nights, the dangerous press line. Coincidence, they said.", "expression": "open", "feedback": "Discrimination in union access and retaliatory shift assignment. Institutional racism in the labor movement.", "note": "Union membership delayed 6 months — then retaliatory transfer to dangerous shift"},
                    {"tier": 3, "response": "I want them to know this: the recruitment agency in Belgrade is run by the factory owner's cousin. They charge each worker 5,000 kronor — a year's salary in Yugoslavia — as 'placement fee.' We arrive in debt to the company. Debt-bonded labor. In Sweden. In 1974. And every month 200 kronor is deducted from our pay to 'repay' the fee. We work for free for the first six months.", "expression": "open", "feedback": "Debt bondage through a family-run recruitment scheme. Workers arrive pre-enslaved. This isn't a labor story — it's a human trafficking story.", "note": "Recruitment agency owned by factory owner's cousin — 5000kr debt bondage, 200kr/month deduction"}
                ],
                "q1_note": "Work permits tied to employer — can't leave"
            },
            "silence": {
                "q1_response": "...I am afraid. Every day afraid. Afraid to sleep because of cold. Afraid to be sick because of contract. Afraid to talk because of deportation. And now afraid because I am talking to you. But Zoran is very sick and nobody helps him.",
                "expression_hint": "Almost whispering, eyes down, hands shaking slightly",
                "q2_options": [
                    {"text": "What's wrong with Zoran?"},
                    {"text": "How many workers feel the way you do?"},
                    {"text": "Has anyone from the Swedish church or social services tried to help?"}
                ],
                "outcomes": [
                    {"tier": 1, "response": "Zoran coughs blood. Every morning. He works the furnace — the hottest position. He is not getting better. But he cannot stop working or they cancel contract.", "expression": "guarded", "feedback": "A desperately ill worker afraid to stop working. Human tragedy but you need medical documentation.", "note": "Zoran coughing blood — works furnace — can't stop without losing contract"},
                    {"tier": 2, "response": "All of us. Forty-two men afraid of the same things. Mrs. Engström from the church — she is only Swedish person who comes. She brings food, helps with letters home. She told the social worker. The social worker visited once, wrote a report. Nothing changed. I asked Mrs. Engström to get me a copy of that report. It says 'conditions adequate for temporary workforce.' Adequate.", "expression": "open", "feedback": "A social worker's report dismissing the conditions as 'adequate.' Official indifference documented.", "note": "Social worker report: 'conditions adequate for temporary workforce'"},
                    {"tier": 3, "response": "Mrs. Engström helped me write letters. To the labor board. To the immigration office. To the newspaper in Gothenburg. One reply came back — from a labor researcher at the university. She said our situation is 'consistent with patterns of labor exploitation documented at twelve Swedish industrial sites.' Twelve sites. We are not alone. And she has data she wants to share with a journalist. Her name is Dr. Karin Vesterberg. Please — call her.", "expression": "open", "feedback": "A university researcher with data on systematic exploitation across twelve sites. This story goes from local to national. The researcher is offering her data.", "note": "Dr. Karin Vesterberg — university labor researcher — data on exploitation at 12 Swedish sites"}
                ],
                "q1_note": "Afraid every day — Zoran very sick"
            }
        }
    },
    "headlines": [
        {"text": "Guest Workers Housed in Unheated Former Military Barracks", "tone": "Factual"},
        {"text": "No Hot Water, No Doctor — Life Inside the Immigrant Barracks", "tone": "Narrative"},
        {"text": "DEBT-BONDED WORKERS TRAPPED IN FROZEN BARRACKS — COMPANY POCKETS RENT", "tone": "Exposing"}
    ]
},
{
    "id": "pensionsranet",
    "title": "The Pension Raid",
    "description": "Retired mill workers say their pensions have been quietly reduced. The mill's pension fund was supposedly 'restructured.'",
    "lead_text": "Pension checks dropped by 30% in September. No one told them why.",
    "preview": "A letter from a pensioner's wife, written in a careful hand, asking for help.",
    "source_type": "letter",
    "difficulty": "medium",
    "base_value": 5,
    "category": "finance",
    "npc_id": "gosta_fredriksson",
    "npc_name": "Gösta Fredriksson",
    "npc_title": "Retired Mill Worker",
    "town": "industristad",
    "interview": {
        "opening_line": "Thirty-eight years I worked that mill. They promised a pension. In writing. And now they just... take it away? I can't pay the heating bill, son.",
        "q1_options": [
            {"archetype": "friendly", "text": "Thirty-eight years is a lifetime, Gösta. Tell me what happened to your pension."},
            {"archetype": "direct", "text": "Do you have the original pension agreement and the new reduced amount?"},
            {"archetype": "pressure", "text": "If they reduced contracted pensions without notice, that's breach of contract."},
            {"archetype": "silence", "text": "..."}
        ],
        "branches": {
            "friendly": {
                "q1_response": "I retired in '71. Pension was 2,400 kronor a month. September comes, the check is 1,680. I called the personnel office. The girl said 'the fund was restructured.' What does that mean? I asked for someone who could explain. Put on hold. Hung up on. Three times.",
                "expression_hint": "Wheezing between sentences, wife hovering nearby",
                "q2_options": [
                    {"text": "How many other retirees have been affected?"},
                    {"text": "Did you ever get a written explanation?"},
                    {"text": "What was the pension fund invested in?"}
                ],
                "outcomes": [
                    {"tier": 1, "response": "I know at least ten others at the pensioners' club who got smaller checks. But some don't notice — their wives manage the money. And some are too proud to admit they're struggling.", "expression": "guarded", "feedback": "Multiple retirees affected but no documents or details on why.", "note": "At least 10 retirees with reduced pensions"},
                    {"tier": 2, "response": "Written explanation? This is what they sent. A one-page letter, dated August 28. 'Due to portfolio adjustments, pension disbursements will be recalculated effective September 1.' Recalculated. Thirty percent cut and they call it 'recalculated.' No details on the 'adjustments.' No appeal process.", "expression": "open", "feedback": "The notification letter is vague — no details, no appeal. Publishable evidence of how they communicated a massive cut.", "note": "Letter: 'portfolio adjustments' — 30% cut with no details, no appeal"},
                    {"tier": 3, "response": "My son-in-law is an accountant in Stockholm. He looked into it. The pension fund had 14 million kronor two years ago. Now it has 6 million. Eight million gone. He checked corporate filings — the mill took a 'loan' from the pension fund to finance the new production line. A loan. From our retirement money. With no plan to repay it.", "expression": "open", "feedback": "8 million kronor taken from the pension fund to finance factory expansion. The workers' retirement money was used to grow the owners' profits.", "note": "8 million 'loaned' from pension fund for production line — no repayment plan"}
                ],
                "q1_note": "2,400 → 1,680 — no explanation"
            },
            "direct": {
                "q1_response": "Here. My employment contract from 1933. Section 12 — pension terms. 'Full pension equivalent to 60% of final salary, guaranteed by company pension fund, not subject to reduction.' Not subject to reduction. And here's the September check — 1,680 kronor instead of 2,400.",
                "expression_hint": "Spreading papers across kitchen table with shaking hands",
                "q2_options": [
                    {"text": "Has anyone challenged the company legally on this?"},
                    {"text": "Is there a pension fund board? Who oversees it?"},
                    {"text": "Can I photograph these documents?"}
                ],
                "outcomes": [
                    {"tier": 1, "response": "Legal challenge? With what money? We live on the pension. Or what's left of it. The union said they'd 'look into it.' That was in October. Nothing since.", "expression": "guarded", "feedback": "Contractual violation clear but no legal action underway. Union passive.", "note": "Union said they'd 'look into it' in October — nothing since"},
                    {"tier": 2, "response": "The pension fund board has three members. Two are company-appointed: the CFO and the plant director. The third is supposed to be a worker representative — but it's the former union chairman, Arne Grip. Arne retired in '70 on a full pension. His pension wasn't cut. That tells you everything.", "expression": "open", "feedback": "The pension board is stacked with company men. And the one 'worker representative' got his full pension — while others were cut.", "note": "Pension board: 2 company execs + 1 ex-union chair whose pension wasn't cut"},
                    {"tier": 3, "response": "Photograph them. Here's something else — my son-in-law got the pension fund's annual report through the corporate registry. In 1972, the fund held 14.2 million kronor. In 1973, it was 8.1 million. The annual report lists 'investment in company operations' of 6 million. They used our pension money to buy the new rolling mill. Our retirement funded their expansion. And the auditor? The auditor signed off on it. Same auditing firm that handles the company's books.", "expression": "open", "feedback": "Pension fund raided for 6 million to buy equipment. Auditor conflict of interest. The retirees financed the very expansion that makes the owners richer while their pensions shrink.", "note": "6M pension fund used for rolling mill. Same auditor for company and pension fund."}
                ],
                "q1_note": "Contract says 'not subject to reduction'"
            },
            "pressure": {
                "q1_response": "Of course it's breach of contract. But who's going to enforce it? The company has lawyers. We have a rusty coffee pot and each other. You want to know how scared we are? Last week Evert refused to accept the reduced check. They told him he could 'take it or leave it.' Leave thirty-eight years of earned pension.",
                "expression_hint": "Coughing, then speaking with quiet fury",
                "q2_options": [
                    {"text": "How much is the total impact across all retirees? What's the scale?"},
                    {"text": "Would the retirees be willing to be named in print?"},
                    {"text": "What happened to the money that was in the fund?"}
                ],
                "outcomes": [
                    {"tier": 1, "response": "There must be two hundred of us drawing from that fund. If everyone lost 30%, that's... a lot of money that went somewhere. But where? Nobody tells us.", "expression": "guarded", "feedback": "Scale is significant — 200 retirees — but no specifics on where the money went.", "note": "~200 retirees affected by cuts, money destination unknown"},
                    {"tier": 2, "response": "Eight of us will talk. We met at Evert's kitchen last week. He's the bravest — he served in the merchant navy during the war, not afraid of the company. And Signe, widow of a mill worker, she'll talk. Her husband died on the job in '68 and she depends entirely on the survivor's pension. That was cut too.", "expression": "open", "feedback": "Group of named sources including a war veteran and a worker's widow. Human faces for the story.", "note": "8 retirees willing to be named — includes war veteran and worker's widow on survivor's pension"},
                    {"tier": 3, "response": "One of the pensioners — I won't say who — used to be the fund administrator before he retired. He told me the board approved a 'temporary reallocation' of fund assets in February '73. The minutes say temporary. There's no repayment schedule. No interest. And the fund's bylaws require a two-thirds majority to change pension terms — the vote was 2-1. The worker representative voted against but was overruled. They broke their own rules.", "expression": "open", "feedback": "'Temporary' reallocation with no repayment, approved by a 2-1 vote when bylaws require two-thirds. They violated their own governance to raid the fund.", "note": "Bylaws require 2/3 majority — vote was 2-1. Worker rep voted against. No repayment schedule."}
                ],
                "q1_note": "Evert told 'take it or leave it'"
            },
            "silence": {
                "q1_response": "...My wife cried when that check came. We already live on potatoes and herring most days. I promised her a good retirement. I worked for it. And now I sit here and I can't even... I can't even keep her warm.",
                "expression_hint": "Voice breaking, wife puts hand on his shoulder",
                "q2_options": [
                    {"text": "What would a proper pension amount mean for your daily life?"},
                    {"text": "Have other retirees reached out to each other?"},
                    {"text": "Do you still have your original pension documents?"}
                ],
                "outcomes": [
                    {"tier": 1, "response": "Seven hundred kronor a month. That's what we lost. It's the heating bill. It's medicine. It's whether I can buy my grandchildren Christmas presents. Small things that make life worth living.", "expression": "guarded", "feedback": "The human cost is clear but you need more than one man's story. Get the documents.", "note": "700kr/month — difference between heating and cold, medicine and none"},
                    {"tier": 2, "response": "We've started meeting at the church on Tuesdays. Last week, twenty-three showed up. Some of them brought their pension letters. All identical wording. Same date. Same cut. This was planned. Coordinated. They did this to all of us at once so no one could fight it alone.", "expression": "open", "feedback": "Twenty-three retirees organized. Identical letters prove a coordinated action. Group testimony.", "note": "23 retirees meeting at church — identical letters, coordinated cut"},
                    {"tier": 3, "response": "I found something in my papers last night. From 1965, when they set up the pension fund. The founding document. It says — here, read it yourself — 'Fund assets shall not be used for purposes other than pension disbursement without unanimous consent of all beneficiaries.' Unanimous. They didn't ask a single one of us. Two lawyers and an accountant could turn this into a criminal case. Will you print that clause?", "expression": "open", "feedback": "The founding document requires unanimous consent for any non-pension use of fund assets. They had no consent at all. This is the legal bombshell.", "note": "Founding document: 'unanimous consent of all beneficiaries' required — none were asked"}
                ],
                "q1_note": "Can't keep his wife warm anymore"
            }
        }
    },
    "headlines": [
        {"text": "Retired Workers Report Sudden Pension Cuts at Mill", "tone": "Cautious"},
        {"text": "Thirty-Eight Years at the Mill — Then a Pension Cut Without Warning", "tone": "Personal"},
        {"text": "MILL RAIDED WORKERS' PENSION FUND TO FINANCE EXPANSION — RETIREES GO COLD", "tone": "Sensational"}
    ]
}
]

def main():
    path = os.path.join(os.path.dirname(__file__), '..', 'data', 'stories.json')
    with open(path, 'r', encoding='utf-8') as f:
        all_stories = json.load(f)
    
    existing_ids = {s['id'] for s in all_stories}
    added = 0
    for s in STORIES:
        if s['id'] not in existing_ids:
            all_stories.append(s)
            added += 1
            print(f"  + {s['id']} (bv{s['base_value']})")
        else:
            print(f"  = {s['id']} (already exists)")
    
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(all_stories, f, indent=2, ensure_ascii=False)
    
    print(f"\nAdded {added} stories. Total: {len(all_stories)}")

if __name__ == '__main__':
    main()
