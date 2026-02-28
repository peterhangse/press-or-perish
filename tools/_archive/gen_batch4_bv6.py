#!/usr/bin/env python3
"""Generate 6 Industristad stories with base_value 6 (hard — serious scandals)."""
import json, os

STORIES = [
  {
    "id": "giftigt_grundvatten",
    "title": "Poisoned Wells",
    "description": "Residents near the chemical plant report brown water and dead fish in the creek.",
    "lead_text": "Three families on Fabriksgatan have stopped drinking tap water. Their well water turned brown last month.",
    "preview": "A typed letter with a water test report arrives at the newsroom.",
    "source_type": "letter",
    "difficulty": "hard",
    "base_value": 6,
    "category": "environment",
    "npc_id": "astrid_lindkvist",
    "npc_name": "Astrid Lindkvist",
    "npc_title": "Retired Nurse, Fabriksgatan Resident",
    "town": "industristad",
    "interview": {
      "opening_line": "I've been a nurse for thirty-two years. I know what chemicals do to a body. And I know what I'm smelling in my water.",
      "q1_options": [
        {"archetype": "friendly", "text": "You must be worried for your neighbors, Astrid. When did you first notice it?"},
        {"archetype": "direct", "text": "Do you have the water test results? What chemicals were found?"},
        {"archetype": "pressure", "text": "The plant says their runoff is within legal limits. Are you saying they're lying?"},
        {"archetype": "silence", "text": "..."}
      ],
      "branches": {
        "friendly": {
          "q1_response": "September. I noticed the tomatoes in my garden had black spots. Then the water started smelling like metal. Three of us on the street went to the pharmacy for test kits.",
          "expression_hint": "Pulling back a curtain to show the garden",
          "q2_options": [
            {"text": "What did the pharmacy test kits show?"},
            {"text": "Have any of your neighbors gotten sick?"},
            {"text": "Did you contact the plant about it?"}
          ],
          "outcomes": [
            {"tier": 1, "response": "The kits aren't very precise - just showed 'elevated metals.' But we can taste it. The children won't drink it anymore.", "expression": "concerned", "feedback": "Anecdotal evidence but no hard data. Needs more.", "note": "Pharmacy kits showed 'elevated metals'"},
            {"tier": 2, "response": "My neighbor Greta, she's 74 - she's had stomach problems since October. And the Lindqvist children have rashes. I wrote it all down. Dates, symptoms, everything. Here.", "expression": "open", "feedback": "A documented health log from a trained nurse. Credible evidence.", "note": "Nurse's log: stomach problems, rashes since October"},
            {"tier": 3, "response": "I sent a sample to the university lab in Gothenburg. Paid for it myself - 200 kronor. Hexavalent chromium. Four times the safe limit. The plant is the only possible source. I have the lab report right here.", "expression": "determined", "feedback": "Independent lab results with specific chemical and levels. Devastating.", "note": "Hexavalent chromium 4x safe limit - university lab report"}
          ],
          "q1_note": "Black spots on tomatoes, metallic water since September"
        },
        "direct": {
          "q1_response": "I paid for a proper analysis from Gothenburg University. Here. Hexavalent chromium at 0.21 milligrams per liter. The Swedish limit is 0.05. And cadmium traces.",
          "expression_hint": "Placing a lab report on the table",
          "q2_options": [
            {"text": "Has the municipality seen these results?"},
            {"text": "How many households are affected?"},
            {"text": "What's the plant's position on this?"}
          ],
          "outcomes": [
            {"tier": 1, "response": "I sent a copy to the environmental office. They said they'd 'look into it.' That was six weeks ago. Nothing happened.", "expression": "frustrated", "feedback": "Municipal inaction confirmed, but no documentation of the cover-up.", "note": "Environmental office: 'look into it' — six weeks ago"},
            {"tier": 2, "response": "At least twelve houses on Fabriksgatan and Bruksgatan. I've been going door to door. Seven families are buying bottled water now. Out of their own pockets. The plant won't even acknowledge the complaint.", "expression": "open", "feedback": "Scale of the problem quantified. Multiple affected families documented.", "note": "12 houses, 7 families buying bottled water"},
            {"tier": 3, "response": "I got hold of the plant's own internal monitoring reports through a friend who works there. Their own numbers show the contamination. They've known since June. But the report was marked 'internal only - do not distribute.' Here's the copy.", "expression": "resolute", "feedback": "The plant's own data proves they knew. A cover-up with documentary evidence.", "note": "Plant's own report shows contamination since June — marked 'do not distribute'"}
          ],
          "q1_note": "Chromium 0.21 mg/L — limit is 0.05"
        },
        "pressure": {
          "q1_response": "Legal limits? They set their own monitoring schedule. They test when they want, where they want. I'm saying the system lets them poison us legally.",
          "expression_hint": "Voice rising, finger pointing at the factory chimneys",
          "q2_options": [
            {"text": "But do you have proof the water is actually contaminated?"},
            {"text": "Who at the plant is responsible for environmental monitoring?"},
            {"text": "Are you saying the regulatory system itself is broken?"}
          ],
          "outcomes": [
            {"tier": 1, "response": "Proof? Taste my water. Look at my garden. But no, I don't have a lab report with a stamp on it, if that's what you mean. Not yet.", "expression": "defensive", "feedback": "Emotional but no hard evidence. The anger is real but the story needs data.", "note": "No lab confirmation yet"},
            {"tier": 2, "response": "Karl-Axel Bergström signs off on the monitoring reports himself. Environmental director AND production director. Same man. You see the problem? The fox guarding the henhouse.", "expression": "accusatory", "feedback": "Clear conflict of interest at the top. Structural problem exposed.", "note": "Bergström signs both production and environmental reports"},
            {"tier": 3, "response": "I found out through a source at the county office that the plant was supposed to install new filtration in 1972. They got a two-year extension. Then another. The money went to the new office building instead. And the county inspector? He's Bergström's brother-in-law.", "expression": "triumphant", "feedback": "Corruption chain: skipped filtration, diverted funds, nepotistic oversight. Explosive.", "note": "Filtration money → office building. Inspector is Bergström's brother-in-law"}
          ],
          "q1_note": "Plant sets its own monitoring schedule"
        },
        "silence": {
          "q1_response": "...You're not the first reporter I've talked to. The last one from Fabriksbladet sat right there. Listened. Wrote nothing. I need to know you're different.",
          "expression_hint": "Searching your face for sincerity",
          "q2_options": [
            {"text": "I'm listening. Tell me what the other reporter didn't want to hear."},
            {"text": "What happened when Fabriksbladet came?"},
            {"text": "What would it take for you to trust me with the full story?"}
          ],
          "outcomes": [
            {"tier": 1, "response": "He said 'we'll run it next week.' That was in October. I called the office three times. Last time they said the story 'didn't meet editorial standards.' Someone got to them.", "expression": "bitter", "feedback": "Evidence of competitor suppressing the story, but no new facts about the contamination.", "note": "Fabriksbladet killed the story after October visit"},
            {"tier": 2, "response": "I'll tell you what I told him AND what I found after. The plant dumps at night. Between 2 and 4 AM. I've been watching. I photographed the discharge pipe running full bore at 3 AM last Tuesday. Brown water straight into Bruksån.", "expression": "conspiratorial", "feedback": "Photographic evidence of nighttime dumping. Major.", "note": "Night dumping photographed at 3 AM — discharge into Bruksån"},
            {"tier": 3, "response": "After Fabriksbladet buried it, I started keeping a proper file. Dates, photos, the lab report, health records from seven families. And yesterday I got this — a resignation letter from the plant's former chemist. He quit because they told him to falsify the water quality data. His name is Stig Åberg. He's willing to talk. On the record.", "expression": "resolved", "feedback": "A complete investigative file plus a whistleblower willing to go on record. Front page.", "note": "Former chemist quit over falsified data — willing to testify"}
          ],
          "q1_note": "Fabriksbladet already killed this story"
        }
      }
    },
    "headlines": [
      {"text": "Residents Report Discolored Water Near Chemical Plant", "tone": "Cautious"},
      {"text": "Lab Tests Reveal Contamination in Industristad Wells", "tone": "Fact-based"},
      {"text": "POISON IN THE TAP — Chemical Plant Knew Since June", "tone": "Exposing"}
    ]
  },
  {
    "id": "fackforradaren",
    "title": "The Union Traitor",
    "description": "A union shop steward is secretly negotiating with management behind the membership's back.",
    "lead_text": "I saw Persson in Bergström's office after hours. Twice. Something's going on.",
    "preview": "An anonymous note slipped under the newsroom door, typed on a factory typewriter.",
    "source_type": "letter",
    "difficulty": "hard",
    "base_value": 6,
    "category": "labor",
    "npc_id": "arne_sundstrom",
    "npc_name": "Arne Sundström",
    "npc_title": "Welder, Union Member",
    "town": "industristad",
    "interview": {
      "opening_line": "I've been in the union twenty years. I know what loyalty looks like. And I know what betrayal looks like. Persson is selling us out.",
      "q1_options": [
        {"archetype": "friendly", "text": "Twenty years is a long time, Arne. What did you see that convinced you?"},
        {"archetype": "direct", "text": "What specifically did you witness? Dates, times, who was present?"},
        {"archetype": "pressure", "text": "This is a serious accusation. Persson could sue. Are you prepared for that?"},
        {"archetype": "silence", "text": "..."}
      ],
      "branches": {
        "friendly": {
          "q1_response": "I stayed late to fix a welding rig on a Thursday — October 17th. Saw Persson coming out of the executive corridor. He looked like he'd seen a ghost when he noticed me. Said he was 'checking something.' At ten at night.",
          "expression_hint": "Clenching and unclenching his fists",
          "q2_options": [
            {"text": "Did you confront him about it?"},
            {"text": "Has Persson's behavior changed recently in union meetings?"},
            {"text": "Was anyone else with him?"}
          ],
          "outcomes": [
            {"tier": 1, "response": "I asked him the next day. He laughed it off. Said I was seeing things. But I know what I saw. The man was sweating.", "expression": "frustrated", "feedback": "One sighting, denied. His word against Persson's.", "note": "Persson denied late-night visit to executive corridor"},
            {"tier": 2, "response": "In the last two meetings, he's been pushing for 'reasonable expectations' on the wage demand. Those are management's words. Last year he wanted 15%. Now suddenly 6% is 'realistic.' Something changed.", "expression": "suspicious", "feedback": "Clear shift in negotiating position. Pattern of compromise.", "note": "Wage demand dropped from 15% to 6% — using management language"},
            {"tier": 3, "response": "I talked to his wife at the market. She let slip they're buying a summer cottage. On a shop steward's salary? And last month Persson's son got a foreman position. The kid is 22 with no experience. You tell me that's a coincidence.", "expression": "bitter", "feedback": "Personal enrichment — cottage + son's promotion. Quid pro quo evidence.", "note": "New cottage + son promoted to foreman at 22"}
          ],
          "q1_note": "Persson seen in executive corridor at 10 PM, October 17th"
        },
        "direct": {
          "q1_response": "October 17th, around 22:00. Executive corridor, third floor. Then again October 31st, same time. I wrote it down both times. Also who was still in the building — only Bergström's light was on upstairs.",
          "expression_hint": "Pulling a small notebook from his breast pocket",
          "q2_options": [
            {"text": "Do you know what they discussed?"},
            {"text": "Has anyone else noticed Persson's meetings?"},
            {"text": "What do you think management is getting from Persson?"}
          ],
          "outcomes": [
            {"tier": 1, "response": "No. Closed doors. But I know this: the week after the first meeting, Persson suddenly dropped the overtime pay demand from negotiations. Just took it off the table. The members never voted on that.", "expression": "angry", "feedback": "Correlation between meetings and concessions, but no direct proof of deal.", "note": "Overtime demand dropped after first meeting — no member vote"},
            {"tier": 2, "response": "Mats in the paint shop saw it too. And there's a third meeting I didn't see but heard about — September. Before the contract talks even started. Persson already knew what he was going to give up.", "expression": "open", "feedback": "Multiple witnesses and a pattern of pre-negotiation meetings.", "note": "Second witness: Mats. Third meeting in September before talks began"},
            {"tier": 3, "response": "I got hold of the draft contract Persson showed management. It's not the version the members voted on. Three clauses removed: overtime rates, safety committee veto, and the asbestos clause. He's negotiating with a version the members have never seen.", "expression": "resolved", "feedback": "Documentary proof — a secret contract with removed protections. The smoking gun.", "note": "Secret contract draft: overtime, safety veto, and asbestos clause removed"}
          ],
          "q1_note": "Two meetings logged: Oct 17 and Oct 31, executive corridor"
        },
        "pressure": {
          "q1_response": "Sue me? For what? For telling the truth? I've got 312 union brothers counting on honest representation. If Persson is making deals with management, they deserve to know.",
          "expression_hint": "Standing up, voice carrying",
          "q2_options": [
            {"text": "But what if there's an innocent explanation?"},
            {"text": "What are you prepared to do about it?"},
            {"text": "Is this personal between you and Persson?"}
          ],
          "outcomes": [
            {"tier": 1, "response": "An innocent explanation for meeting the boss in secret at night? While negotiating our contract? I'm not stupid and neither are you.", "expression": "defiant", "feedback": "Strong conviction but still circumstantial. Needs documentation.", "note": "Sundström insists: no innocent explanation for secret meetings"},
            {"tier": 2, "response": "This isn't personal. Three of us — me, Mats, and Gunvor — we've been tracking this for weeks. We filed a complaint with the regional union office. They said they'd investigate. That was a month ago. Nothing.", "expression": "resigned", "feedback": "Organized group complaint, regional union inaction. Institutional failure.", "note": "Three workers filed complaint — regional union took no action"},
            {"tier": 3, "response": "I'll tell you what I'm prepared to do. I have a tape. Persson called me from the plant phone last week to 'discuss strategy.' I recorded it. He says, and I quote: 'Bergström promised the safety clause stays if we drop overtime. It's the best deal we'll get.' He's admitting it. On tape.", "expression": "triumphant", "feedback": "Audio evidence of the deal. Persson in his own words admitting negotiation with Bergström.", "note": "Tape recording: 'Bergström promised safety clause stays if we drop overtime'"}
          ],
          "q1_note": "312 union members relying on honest representation"
        },
        "silence": {
          "q1_response": "...Look. I didn't want to come here. I tried the union structure first. I tried talking to Persson. I even wrote to the national office. Nobody wants to touch this. You're my last option.",
          "expression_hint": "Sitting heavily, suddenly looking tired",
          "q2_options": [
            {"text": "What happened when you talked to Persson?"},
            {"text": "Why do you think nobody wants to investigate?"},
            {"text": "Take your time. What's the most important thing you need people to know?"}
          ],
          "outcomes": [
            {"tier": 1, "response": "He told me to mind my own business. Said I was jealous because I didn't get the shop steward position. Maybe I am. But that doesn't make what he's doing right.", "expression": "honest", "feedback": "Honest admission of possible bias. Credible but thin on evidence.", "note": "Persson dismissed concerns — Arne admits possible jealousy"},
            {"tier": 2, "response": "Because Persson has connections everywhere. His brother is on the county council. His predecessor retired quietly with a management consultancy contract. This is how it works in Industristad. You play ball, you get taken care of.", "expression": "weary", "feedback": "Pattern of institutional corruption — previous steward also compromised.", "note": "Previous steward got management consultancy. Persson's brother on county council"},
            {"tier": 3, "response": "The most important thing? Forty-seven men in the steel section work with asbestos insulation daily. No masks, no protective suits. The safety clause in our contract was supposed to fix that. Persson traded it away. Men will die from this deal. That's what's at stake.", "expression": "breaking", "feedback": "Human cost crystallized — asbestos exposure traded away. Life-and-death stakes.", "note": "47 men exposed to asbestos daily — safety clause traded away"}
          ],
          "q1_note": "Exhausted every internal channel before coming to press"
        }
      }
    },
    "headlines": [
      {"text": "Union Questions Arise Over Contract Negotiations", "tone": "Cautious"},
      {"text": "Shop Steward Held Secret Meetings With Management", "tone": "Fact-based"},
      {"text": "BETRAYED — Union Boss Cut Secret Deal on Worker Safety", "tone": "Exposing"}
    ]
  },
  {
    "id": "osynliga_skadorna",
    "title": "The Invisible Injuries",
    "description": "Workers at the steel mill are reporting hearing loss and lung problems that aren't in official health records.",
    "lead_text": "My husband can't hear me anymore unless I shout. The company doctor says he's fine.",
    "preview": "A woman approaches you at the market, looking over her shoulder.",
    "source_type": "street",
    "difficulty": "hard",
    "base_value": 6,
    "category": "labor",
    "npc_id": "gunhild_persson_i",
    "npc_name": "Gunhild Persson",
    "npc_title": "Steelworker's Wife",
    "town": "industristad",
    "interview": {
      "opening_line": "They'll say I'm a worried wife making a fuss. But I've talked to the other wives. It's not just my husband. It's all of them.",
      "q1_options": [
        {"archetype": "friendly", "text": "It must be frightening watching your husband's health change. How many families have you spoken with?"},
        {"archetype": "direct", "text": "How many workers are affected? What are the specific symptoms?"},
        {"archetype": "pressure", "text": "If the company doctor is lying, that's a criminal matter. Are you ready to make that claim?"},
        {"archetype": "silence", "text": "..."}
      ],
      "branches": {
        "friendly": {
          "q1_response": "Fourteen wives that I know of. We started talking at the school pickup — our kids go to Bruksskolan. One by one, the same story. Hearing problems. Coughing that won't stop. Headaches.",
          "expression_hint": "Counting on her fingers, each name a weight",
          "q2_options": [
            {"text": "Has anyone tried to get a second medical opinion?"},
            {"text": "Have you noticed when the symptoms started getting worse?"},
            {"text": "What does the company doctor actually say when they go in?"}
          ],
          "outcomes": [
            {"tier": 1, "response": "The company doctor — Dr. Holm — he does the checkups. Same thing every time: 'within normal range.' But my husband can't hear the phone ring anymore. That's not normal.", "expression": "pleading", "feedback": "Pattern of dismissal by company doctor, but no counter-evidence yet.", "note": "Dr. Holm: 'within normal range' despite hearing loss"},
            {"tier": 2, "response": "Three of us went to Dr. Ekblad in town — paid out of pocket. He diagnosed Sven with 40% hearing loss in both ears and early-stage COPD. The company record says 'healthy.' I have both reports. They don't match.", "expression": "angry", "feedback": "Two conflicting medical records. Company doctor clearly understating damage.", "note": "Independent doctor: 40% hearing loss, COPD. Company record says 'healthy'"},
            {"tier": 3, "response": "Agnes Forsberg's husband died last year. Lung cancer. The company doctor had cleared him three months before. I got hold of his actual company health file through Agnes — it had notes that were crossed out. Someone altered his records. Agnes has the originals her husband kept secretly.", "expression": "resolute", "feedback": "Altered health records, death possibly related. Documentary evidence of cover-up.", "note": "Dead worker's records altered — original copies exist showing crossed-out notes"}
          ],
          "q1_note": "14 families with same symptoms — hearing, coughing, headaches"
        },
        "direct": {
          "q1_response": "I've counted at least fourteen in the steel section. Symptoms: progressive hearing loss, chronic cough, headaches, and three cases of what looks like nervous system damage — tremors, memory problems. All men under fifty.",
          "expression_hint": "Reading from a small notebook",
          "q2_options": [
            {"text": "What workplace conditions could cause all these symptoms together?"},
            {"text": "Are these workers all in the same department?"},
            {"text": "Has anyone filed an occupational injury report?"}
          ],
          "outcomes": [
            {"tier": 1, "response": "Steel section and the alloy department. High noise, metal dust, and they started using a new chemical treatment for the steel two years ago. Nobody was told what was in it.", "expression": "matter-of-fact", "feedback": "Environmental factors identified but no specific chemical or proof of negligence.", "note": "New chemical treatment introduced 2 years ago — composition unknown"},
            {"tier": 2, "response": "Sven filed an injury report last March. It was rejected by the company. The safety officer — who reports to management — ruled it 'age-related hearing loss.' Sven is 38. I have the rejection letter.", "expression": "frustrated", "feedback": "Documented rejection of legitimate claim. Safety officer conflict of interest.", "note": "Injury report rejected: '38-year-old diagnosed with age-related hearing loss'"},
            {"tier": 3, "response": "I've been building a file for six months. Fourteen cases documented. Independent medical exams for five of them. A chemical analysis of the dust in the ventilation — it contains manganese compounds well above safe levels. And the company's own safety manual says those filters should be changed monthly. They haven't been changed in over a year.", "expression": "methodical", "feedback": "Complete investigative file: cases, independent exams, dust analysis, maintenance neglect.", "note": "Manganese dust above limits, filters unchanged for over a year, 14 documented cases"}
          ],
          "q1_note": "14 workers, hearing loss, COPD symptoms, tremors"
        },
        "pressure": {
          "q1_response": "Criminal? Maybe it should be. But you know how it works. The company doctor reports to the company. The safety inspector is married to the HR director. Nobody wants to be the one who speaks up.",
          "expression_hint": "Looking around the market square nervously",
          "q2_options": [
            {"text": "So the system is rigged to protect the company. Who benefits?"},
            {"text": "Is there anyone inside the plant willing to confirm this?"},
            {"text": "What would it take to prove the company doctor is falsifying records?"}
          ],
          "outcomes": [
            {"tier": 1, "response": "Everyone benefits from silence. The company keeps costs down. The union doesn't have to fight. The town keeps its largest employer happy. Only the workers lose.", "expression": "bitter", "feedback": "Structural analysis but no individual evidence. Good context, weak story.", "note": "Systemic silence — company, union, and town all complicit"},
            {"tier": 2, "response": "There's a nurse at the company clinic — she's been keeping her own notes. Separate from Dr. Holm's official records. She told me she's documented cases where Holm changed diagnoses after meeting with management. She won't go on record but she'd let you see the notes.", "expression": "guarded", "feedback": "Insider witness with separate documentation. Could be verified.", "note": "Clinic nurse keeps parallel records — Holm changes diagnoses after management meetings"},
            {"tier": 3, "response": "I already have proof. My husband secretly copied his own health file from the clinic when the nurse stepped out. The original says 'suspected occupational hearing damage — recommend specialist.' Dr. Holm's filed version says 'hearing within normal parameters.' Two different documents, same date, same patient. That's not a mistake. That's fraud.", "expression": "fierce", "feedback": "Original vs filed medical record — identical date, contradictory findings. Fraud proof.", "note": "Two versions of same health file: original says 'occupational damage,' filed version says 'normal'"}
          ],
          "q1_note": "Company doctor reports to company, safety inspector married to HR director"
        },
        "silence": {
          "q1_response": "...My husband doesn't know I'm here. He'd be furious. They all would. The men don't want to be seen as weak. They just... keep going. And getting sicker.",
          "expression_hint": "Voice dropping almost to a whisper",
          "q2_options": [
            {"text": "Why are the men afraid to speak up themselves?"},
            {"text": "What does a typical day look like for your husband now?"},
            {"text": "What made you decide to come forward despite the risk?"}
          ],
          "outcomes": [
            {"tier": 1, "response": "Because the last man who complained about working conditions was transferred to the night shift in the worst department. Everyone knows what happened to Rolf Jansson.", "expression": "fearful", "feedback": "Culture of retaliation established but still secondhand knowledge.", "note": "Rolf Jansson transferred to night shift after complaint"},
            {"tier": 2, "response": "He comes home grey. Not tired — grey. He sits in the kitchen and doesn't talk because he can barely hear. Last week he couldn't grip a cup — his hand was shaking. He's 38 years old. He used to carry me over the threshold. Now he can't hold a cup.", "expression": "breaking", "feedback": "Devastating human detail. The personal cost made concrete and publishable.", "note": "38-year-old can't grip a cup — tremors, hearing loss, grey complexion"},
            {"tier": 3, "response": "Because Erik Forsberg died in May. Same section, same symptoms, same doctor saying 'fine.' The death certificate says 'natural causes.' But nothing about a 45-year-old dying of lung failure is natural when he worked in metal dust for twenty years. I spoke to his widow. She has his personal health diary. He wrote: 'Dr. Holm told me to stop worrying. The dust is harmless.' Three months before he died.", "expression": "shaking", "feedback": "A death, a diary, a doctor's assurance. The cover-up has already cost a life.", "note": "Erik Forsberg dead at 45 — diary quotes Dr. Holm: 'dust is harmless'"}
          ],
          "q1_note": "Husband doesn't know she's speaking to press"
        }
      }
    },
    "headlines": [
      {"text": "Steel Workers Report Health Concerns at Annual Checkup", "tone": "Cautious"},
      {"text": "Independent Doctors Contradict Company Health Records", "tone": "Fact-based"},
      {"text": "SICK AND SILENCED — Steel Mill Workers Denied Medical Truth", "tone": "Exposing"}
    ]
  },
  {
    "id": "bostadsbranden",
    "title": "The Housing Fire",
    "description": "A fire in worker housing killed two people. The fire department's report raises questions about building safety codes.",
    "lead_text": "The fire exit was bolted shut. From the outside. Those people never had a chance.",
    "preview": "A document stamped 'CONFIDENTIAL' with the county fire inspector's seal arrives via courier.",
    "source_type": "document",
    "difficulty": "hard",
    "base_value": 6,
    "category": "housing",
    "npc_id": "torsten_mansson",
    "npc_name": "Torsten Månsson",
    "npc_title": "County Fire Inspector",
    "town": "industristad",
    "interview": {
      "opening_line": "I sent that report to my superiors four months ago. About the blocked exits, the missing smoke alarms, the overcrowding. They told me to revise it. 'Tone it down.' I revised nothing. So they shelved it.",
      "q1_options": [
        {"archetype": "friendly", "text": "That must have been a difficult position, Torsten. What made you decide to send it to us?"},
        {"archetype": "direct", "text": "I need to see the original report. What specific violations did you document?"},
        {"archetype": "pressure", "text": "Two people are dead. Your report could have prevented it. Why didn't you go public sooner?"},
        {"archetype": "silence", "text": "..."}
      ],
      "branches": {
        "friendly": {
          "q1_response": "Because Margareta Nilsson and her four-year-old are dead. And my report is sitting in a drawer because it would have embarrassed the housing company. Which is owned by the municipality. Which employs me.",
          "expression_hint": "Wiping forehead, looking at the floor",
          "q2_options": [
            {"text": "Who specifically told you to revise the report?"},
            {"text": "How bad were the conditions in the building?"},
            {"text": "Are there other buildings with the same problems?"}
          ],
          "outcomes": [
            {"tier": 1, "response": "My supervisor, Kjell Åkesson. He said the timing was 'politically difficult' because the housing company was up for a municipal review. Politics over lives.", "expression": "disgusted", "feedback": "Named superior who ordered suppression, but still one person's word.", "note": "Supervisor Kjell Åkesson: 'politically difficult' timing"},
            {"tier": 2, "response": "The building had fire exits bolted from outside — supposedly to prevent break-ins. No smoke alarms on three floors. Overcrowded — eleven people in four apartments designed for six. The wiring was from the 1940s. I documented everything with photographs.", "expression": "professional", "feedback": "Comprehensive list of violations with photographic evidence.", "note": "Exits bolted, no alarms, overcrowded, 1940s wiring — all photographed"},
            {"tier": 3, "response": "I inspected fourteen buildings in the Bruksbo area. Same owner — Industristadens Bostäder AB. Eleven of them have critical fire safety violations. The one that burned was number 7 on my list. There are six buildings ranked worse than it. Here's the full report — the one they didn't want you to see.", "expression": "determined", "feedback": "Eleven buildings with critical violations. The next fire is a matter of time.", "note": "11 of 14 buildings have critical violations — original report provided"}
          ],
          "q1_note": "Margareta Nilsson and 4-year-old dead — report shelved"
        },
        "direct": {
          "q1_response": "Here. Twenty-three pages. The building at Bruksvägen 14 had seven critical violations. Class A fire risk. I recommended immediate evacuation of the top two floors. They said 'noted' and did nothing.",
          "expression_hint": "Opening a battered briefcase, pulling out a thick report",
          "q2_options": [
            {"text": "Who signed off on ignoring your recommendation?"},
            {"text": "What exactly were the seven critical violations?"},
            {"text": "When was the last time this building passed an inspection?"}
          ],
          "outcomes": [
            {"tier": 1, "response": "The housing company's board acknowledged receipt. Minutes say 'fire safety improvements to be scheduled pending budget review.' That was March. The fire was in November. Eight months of nothing.", "expression": "flat", "feedback": "Paper trail of delay but no smoking gun on individual responsibility.", "note": "Board acknowledged in March — no action for 8 months"},
            {"tier": 2, "response": "Seven violations: locked emergency exits, no smoke detectors on 3 of 4 floors, exposed wiring, blocked stairwell with storage, non-fire-rated doors, no fire extinguishers, and occupancy at 180% of design capacity. Any one of these is enough to close a building.", "expression": "clinical", "feedback": "Seven specific, damning violations. Each individually newsworthy.", "note": "7 critical violations — any single one grounds for closure"},
            {"tier": 3, "response": "It 'passed' in 1971. But I pulled the file — the inspector who passed it was Henrik Melin. He now works for Industristadens Bostäder as their 'safety consultant.' Hired three months after the inspection. You understand what I'm saying.", "expression": "pointed", "feedback": "The inspector who approved the building now works for the building owner. Corruption.", "note": "1971 inspector Henrik Melin now employed by the housing company he cleared"}
          ],
          "q1_note": "23-page report, 7 critical violations, evacuation recommended"
        },
        "pressure": {
          "q1_response": "You think I don't know that? You think I sleep at night? I followed procedure. I filed the report. The system failed, not me. But two people are dead and I have to live with that.",
          "expression_hint": "Voice cracking, gripping the table edge",
          "q2_options": [
            {"text": "But did you do everything in your power? Could you have gone higher?"},
            {"text": "Who else knew about the fire risks besides you and your supervisor?"},
            {"text": "What's stopping the same thing from happening in the other buildings tomorrow?"}
          ],
          "outcomes": [
            {"tier": 1, "response": "I could have gone to the county governor. I didn't. I followed the chain of command. That was my mistake.", "expression": "defeated", "feedback": "Honest admission of failure, but doesn't advance the investigation much.", "note": "Inspector admits he should have escalated to county governor"},
            {"tier": 2, "response": "The housing company board knew. The municipal building committee knew — I sent a copy there too. The chairman of that committee is also on the housing company board. Same people on both sides of the table.", "expression": "bitter", "feedback": "Overlapping board membership — structural conflict of interest.", "note": "Municipal committee chairman also sits on housing company board"},
            {"tier": 3, "response": "Nothing. Nothing is stopping it. And here. I brought this. It's the insurance file for Bruksvägen 14. The building was insured for three times its value. The premium was raised in September — two months before the fire. By the owner. You do the math.", "expression": "shaking", "feedback": "Insurance fraud angle — building over-insured and premium raised before fire. Potential arson motive.", "note": "Building insured at 3x value, premium raised 2 months before fire"}
          ],
          "q1_note": "Inspector followed procedure — system failed"
        },
        "silence": {
          "q1_response": "...I've been carrying this report for four months. Four months of knowing those buildings are death traps and being told to shut up about it. Then the fire happened. And I just... I can't anymore.",
          "expression_hint": "Breaking down, hands trembling",
          "q2_options": [
            {"text": "I need to understand the timeline. When exactly did things start going wrong?"},
            {"text": "Who is ultimately responsible for those buildings?"},
            {"text": "Tell me about Margareta. Tell me about the people who lived there."}
          ],
          "outcomes": [
            {"tier": 1, "response": "The buildings were workers' housing, built by the steel company in the '40s. Sold to Industristadens Bostäder in 1968. Since then — no renovations, no maintenance, nothing. Just rent increases.", "expression": "weary", "feedback": "Historical context and neglect pattern, but no individual accountability.", "note": "No renovations since 1968 sale — only rent increases"},
            {"tier": 2, "response": "Industristadens Bostäder AB. The board: Karl-Axel Bergström, chairman. The same Bergström who runs the steel mill. Margareta Nilsson worked in his canteen. She lived in his building. She died because he wouldn't spend money on fire exits for his own employee.", "expression": "devastated", "feedback": "Bergström connection — mill director also housing company chairman. Worker died in his building.", "note": "Bergström chairs both steel mill and housing company — victim was his employee"},
            {"tier": 3, "response": "Margareta was 29. Her daughter Elsa was four. They were on the third floor. The fire door was bolted from outside — a padlock, put there by the caretaker on orders from the housing company to 'prevent unauthorized access.' I photographed it. There's a memo from the housing company manager ordering the locks installed. Here, dated August. Three months before Margareta and Elsa burned.", "expression": "devastated", "feedback": "The memo that killed them. A direct order to lock the fire exits. With names and dates. Devastating.", "note": "Memo ordering fire exits padlocked — dated August, 3 months before deaths"}
          ],
          "q1_note": "Four months of carrying a shelved fire safety report"
        }
      }
    },
    "headlines": [
      {"text": "Fire Department Reviews Building Safety After Deadly Fire", "tone": "Cautious"},
      {"text": "Shelved Report Warned of Fire Risks at Bruksvägen 14", "tone": "Fact-based"},
      {"text": "THEY KNEW — Locked Exits, Shelved Reports, Two Dead", "tone": "Exposing"}
    ]
  },
  {
    "id": "hamnutbyggnaden",
    "title": "The Harbor Expansion",
    "description": "The planned harbor expansion will displace fishing families, but the contract was awarded without public bidding.",
    "lead_text": "The contract went to Bergström's cousin's construction firm. No other bids were invited.",
    "preview": "A thick envelope with municipal procurement documents lands on your desk.",
    "source_type": "document",
    "difficulty": "hard",
    "base_value": 6,
    "category": "politics",
    "npc_id": "eva_sandberg",
    "npc_name": "Eva Sandberg",
    "npc_title": "Municipal Procurement Officer",
    "town": "industristad",
    "interview": {
      "opening_line": "I'm bound by professional secrecy. I can't comment on individual procurement decisions. But I can tell you... the process in this case was unusual.",
      "q1_options": [
        {"archetype": "friendly", "text": "I appreciate the difficult position you're in, Eva. What would 'usual' look like in contrast?"},
        {"archetype": "direct", "text": "Was the harbor contract put out for public tender? Yes or no?"},
        {"archetype": "pressure", "text": "I have the procurement file. The contract was sole-sourced to Västkust Bygg. Why?"},
        {"archetype": "silence", "text": "..."}
      ],
      "branches": {
        "friendly": {
          "q1_response": "A contract of this size — 14 million kronor — would normally require public tender with at least three qualified bidders. A minimum four-week response period. Committee review. It's not complicated. It's just... the rules.",
          "expression_hint": "Speaking carefully, each word weighed",
          "q2_options": [
            {"text": "And those rules weren't followed here?"},
            {"text": "Who has the authority to bypass the normal process?"},
            {"text": "Why do you think normal procedures were skipped?"}
          ],
          "outcomes": [
            {"tier": 1, "response": "I can't comment on specific cases. But hypothetically, if someone submitted a 'time-critical' exception request... the committee chairman can approve sole-source procurement. It's meant for emergencies.", "expression": "guarded", "feedback": "Procedural loophole explained, but she won't confirm specifics.", "note": "Emergency exception allows sole-source — chairman approves"},
            {"tier": 2, "response": "The exception request was filed by the harbor director. Approved by the committee chairman. Both signatures dated the same day. A 14-million-kronor decision in one day. In my twelve years here, I've never seen that happen.", "expression": "pointed", "feedback": "Same-day approval of massive contract. Procedural red flag on record.", "note": "14M contract approved in one day — unprecedented in 12 years"},
            {"tier": 3, "response": "Here. I shouldn't have this, but I made a copy. The exception request cites 'urgent structural concerns at the harbor.' I requested the engineering report that supposedly justified the urgency. It doesn't exist. There is no structural assessment. The urgency was fabricated.", "expression": "resolved", "feedback": "Fabricated justification for bypassing procurement. Documentary proof of fraud.", "note": "Engineering report justifying urgency doesn't exist — fabricated basis"}
          ],
          "q1_note": "14M contract normally requires public tender with 3+ bidders"
        },
        "direct": {
          "q1_response": "No. It was sole-sourced under an emergency exception. The documentation says 'time-critical harbor structural repair.' But I handle all the paperwork. There was no emergency. The harbor is fine.",
          "expression_hint": "Measured tone but firm eye contact",
          "q2_options": [
            {"text": "Who signed the emergency exception?"},
            {"text": "What's the connection between Västkust Bygg and the decision-makers?"},
            {"text": "Were any other companies considered at any stage?"}
          ],
          "outcomes": [
            {"tier": 1, "response": "The committee chairman, Nils Kronberg. He has the authority for emergency exceptions. But in my experience, those are for broken pipes and collapsed roofs. Not 14-million-kronor expansion projects.", "expression": "dry", "feedback": "Named decision-maker misusing emergency powers. Good but needs the connection.", "note": "Chairman Nils Kronberg approved emergency exception for expansion project"},
            {"tier": 2, "response": "Västkust Bygg AB. Owned by Rolf Bergström. Karl-Axel Bergström's first cousin. The same Karl-Axel Bergström who sits on the harbor board that recommended the expansion in the first place.", "expression": "pointed", "feedback": "Family corruption chain: Bergström recommended expansion, cousin got contract.", "note": "Västkust Bygg owned by Bergström's cousin Rolf — Bergström on harbor board"},
            {"tier": 3, "response": "I pulled all the records. No other company was contacted. No market survey. No price comparison. And the contract price — 14.2 million — is roughly 40% above the national average for comparable harbor work. I had an independent engineer estimate the job at 8 to 9 million. The municipality is overpaying by at least 5 million kronor.", "expression": "precise", "feedback": "40% over market price with no competitive bidding. 5M kronor overpayment documented.", "note": "Contract 40% above market — 5M kronor overpayment, no comparative bids sought"}
          ],
          "q1_note": "Sole-sourced under false emergency exception — no real emergency"
        },
        "pressure": {
          "q1_response": "Because I was told to process it. The order came from above. From the municipal director's office. I raised my concerns in writing. I was told to 'facilitate the process and stop asking questions.'",
          "expression_hint": "Producing a printed email from her folder",
          "q2_options": [
            {"text": "Do you have that written instruction?"},
            {"text": "Is the municipal director involved in this?"},
            {"text": "Why are you telling me this now?"}
          ],
          "outcomes": [
            {"tier": 1, "response": "I have the internal memo. But it's carefully worded — 'expedite processing' and 'prioritize municipal development goals.' They're good at not saying what they mean.", "expression": "frustrated", "feedback": "Institutional pressure documented but in coded language. Hard to prove intent.", "note": "Memo says 'expedite processing' — coded directive to skip safeguards"},
            {"tier": 2, "response": "The municipal director rubber-stamps what the committee chairman wants. And Kronberg... Kronberg is up for re-election. Bergström is his largest campaign donor. Check the contribution records — they're public. 50,000 kronor in 1973.", "expression": "knowing", "feedback": "Campaign finance connection: Bergström funds Kronberg who approved the contract.", "note": "Bergström donated 50,000kr to Kronberg in 1973 — Kronberg approved the contract"},
            {"tier": 3, "response": "Because yesterday I found this on my desk. An unsigned note: 'Career advice: some files are better left closed.' They're threatening me. And I decided if they're going to ruin my career anyway, I might as well make sure the truth comes out first. Here — everything. The fake emergency request, the contract, the price comparison, and the campaign donations. All of it.", "expression": "defiant", "feedback": "Whistleblower with complete file, under threat. Every angle documented.", "note": "Threatening note received — providing complete file: fake emergency, contract, donations"}
          ],
          "q1_note": "Ordered from above to process sole-source contract"
        },
        "silence": {
          "q1_response": "...I've worked in procurement for twelve years. I believe in the system. Transparent spending, competitive bidding, accountability. It's not glamorous but it matters. This contract violated everything I've spent my career upholding.",
          "expression_hint": "Hands folded, speaking with quiet conviction",
          "q2_options": [
            {"text": "What specifically about this contract is wrong?"},
            {"text": "What happens to the fishing families in the expansion zone?"},
            {"text": "What do you need me to do with this information?"}
          ],
          "outcomes": [
            {"tier": 1, "response": "Wrong process, wrong price, wrong contractor. But I can't prove intent. I can only show you that every safeguard designed to prevent corruption was systematically bypassed.", "expression": "measured", "feedback": "Clear structural analysis but no smoking gun on motive.", "note": "Every procurement safeguard systematically bypassed"},
            {"tier": 2, "response": "Twelve fishing families will lose their moorings. They've been there for generations. The expansion plan doesn't include relocation provisions. I asked about it — was told 'they'll find somewhere.' These are people's livelihoods being erased for a contract that should never have been awarded.", "expression": "emotional", "feedback": "Human cost added to corruption angle. Families displaced without provision.", "note": "12 fishing families displaced — no relocation provisions in contract"},
            {"tier": 3, "response": "Print it. All of it. Because I've also found that this isn't the first time. Västkust Bygg has received four municipal contracts in three years. All sole-sourced. All above market rate. Total: 31 million kronor. This isn't one corrupt deal — it's a pipeline. And I have every file.", "expression": "steely", "feedback": "Systematic corruption: 4 contracts, 31M kronor, all sole-sourced to same family firm.", "note": "4 contracts in 3 years totaling 31M — all sole-sourced to Bergström's cousin"}
          ],
          "q1_note": "12 years in procurement — every safeguard bypassed"
        }
      }
    },
    "headlines": [
      {"text": "Harbor Expansion Contract Awarded Without Public Tender", "tone": "Cautious"},
      {"text": "14 Million Kronor Contract Went to Board Member's Cousin", "tone": "Fact-based"},
      {"text": "THE FAMILY BUSINESS — How Bergström Steers Millions to His Own", "tone": "Exposing"}
    ]
  },
  {
    "id": "skolmaten_skandalen",
    "title": "The School Lunch Scandal",
    "description": "The school lunch program is serving food unfit for children while the budget mysteriously shrank.",
    "lead_text": "My daughter found mold in her meatball. This was the third time this month.",
    "preview": "A parent stops you outside Bruksskolan with a Tupperware container of evidence.",
    "source_type": "street",
    "difficulty": "hard",
    "base_value": 6,
    "category": "welfare",
    "npc_id": "anna_lena_johansson",
    "npc_name": "Anna-Lena Johansson",
    "npc_title": "Parent, School Board Member",
    "town": "industristad",
    "interview": {
      "opening_line": "I've been raising this at every school board meeting since September. They smile, they nod, and nothing changes. Our children are eating garbage.",
      "q1_options": [
        {"archetype": "friendly", "text": "It's clear you care deeply about this, Anna-Lena. How long has the quality been declining?"},
        {"archetype": "direct", "text": "What's the school lunch budget now versus last year? Where did the money go?"},
        {"archetype": "pressure", "text": "If children are being served expired food, that's a health code violation. Have you reported it?"},
        {"archetype": "silence", "text": "..."}
      ],
      "branches": {
        "friendly": {
          "q1_response": "Since they changed suppliers in August. The old company — Lindströms Catering — was local. Good food. Then suddenly a new company nobody had heard of. 'Norrland Mat AB.' Cheaper, they said. Better value.",
          "expression_hint": "Opening the Tupperware to show grayish meatballs",
          "q2_options": [
            {"text": "Who made the decision to switch suppliers?"},
            {"text": "What are the specific complaints about the food?"},
            {"text": "Has anybody looked into this Norrland Mat AB?"}
          ],
          "outcomes": [
            {"tier": 1, "response": "The school board approved it on the municipal education director's recommendation. It was presented as a cost-saving measure. The kids call the new food 'punishment porridge.'", "expression": "weary", "feedback": "Standard complaint with a good quote but no financial details.", "note": "New supplier recommended by municipal education director"},
            {"tier": 2, "response": "I've been keeping samples in my freezer. Mold, gristle, once a piece of plastic in the soup. And the portions are smaller — the children are hungry by 2 PM. The teachers have started bringing extra bread because the kids can't concentrate.", "expression": "angry", "feedback": "Physical evidence preserved, documented pattern, school impact.", "note": "Frozen food samples, smaller portions, teachers bring extra bread"},
            {"tier": 3, "response": "I looked into Norrland Mat AB. It was registered in June — two months before getting the contract. One employee. The registered address is a post box in Sundsvall. And the owner? Göran Månsson. The education director's brother-in-law. They created a company to funnel school lunch money to family.", "expression": "furious", "feedback": "Shell company owned by education director's relative. Fraud scheme exposed.", "note": "Norrland Mat AB: shell company, one employee, owned by director's brother-in-law"}
          ],
          "q1_note": "Supplier changed in August — Norrland Mat AB replaced local company"
        },
        "direct": {
          "q1_response": "Last year: 12 kronor per meal. This year: 8 kronor. The board approved the reduction because the new supplier 'offered better rates.' But 8 kronor doesn't buy a real meal. Where's the other 4 kronor going? That's 500 children times 4 kronor times 180 school days. You do the math.",
          "expression_hint": "Pulling out a calculator, punching numbers",
          "q2_options": [
            {"text": "That's 360,000 kronor. Where is that money now?"},
            {"text": "Did the board question the budget reduction?"},
            {"text": "What happens to schoolchildren who don't eat enough?"}
          ],
          "outcomes": [
            {"tier": 1, "response": "The budget line just says 'transferred to school development fund.' I asked what that fund pays for. Nobody could tell me. There's no report, no accounting. 360,000 kronor into a black hole.", "expression": "exasperated", "feedback": "Missing money identified but no trail to follow yet.", "note": "360,000kr transferred to unaccounted 'school development fund'"},
            {"tier": 2, "response": "I was the only one who voted against it. The education director said the savings would fund new textbooks. I asked to see the textbook purchase order. There isn't one. The money simply disappeared from the school budget into the general municipal account.", "expression": "resolute", "feedback": "Money trail dead end — moved to general account with no spending record.", "note": "Textbook promise was fiction — money moved to general municipal account"},
            {"tier": 3, "response": "I hired an accountant friend to trace it. The 'school development fund' paid three invoices to Norrland Mat AB for 'consulting services.' On top of the catering contract. 120,000 kronor for consulting from a company with one employee and no office. The education director approved all three invoices. It's embezzlement.", "expression": "devastating", "feedback": "Double billing: catering contract plus fake consulting invoices. Complete fraud trail.", "note": "3 fake consulting invoices totaling 120,000kr from same shell company — embezzlement"}
          ],
          "q1_note": "Budget cut from 12kr to 8kr per meal — 360,000kr missing"
        },
        "pressure": {
          "q1_response": "Reported it? To whom? The school board is controlled by the same party that appointed the education director. The health inspector says he needs 'formal complaints in writing.' I've sent four. Ask him how many he's followed up on.",
          "expression_hint": "Slamming a folder of unanswered letters on the desk",
          "q2_options": [
            {"text": "So the oversight system itself has failed?"},
            {"text": "What exactly did the health inspector say?"},
            {"text": "Is anyone on the board willing to challenge the director?"}
          ],
          "outcomes": [
            {"tier": 1, "response": "Failed? It was designed to fail. The health inspector gets his budget approved by the same committee the education director sits on. Nobody bites the hand that funds them.", "expression": "cynical", "feedback": "Structural analysis of conflicts of interest. Good context.", "note": "Health inspector budget controlled by same committee as education director"},
            {"tier": 2, "response": "The health inspector told me off the record — and I have him on tape saying this — 'Anna-Lena, I know the food is bad. But if I write up the school, they'll cut my department.' He's scared for his own job. The system is designed so nobody can afford to do the right thing.", "expression": "bitter", "feedback": "Recorded admission from health inspector. Systemic failure documented.", "note": "Health inspector on tape: 'I know the food is bad' but fears budget cuts"},
            {"tier": 3, "response": "Last week's board meeting: I presented a motion to return to the previous supplier. The education director called a recess, spoke to three board members privately, and they voted my motion down 5 to 1. After the meeting, one of them whispered to me: 'Sorry, Anna-Lena. Månsson told us the director has photos from the Christmas party. It's blackmail.' They're being coerced.", "expression": "shaken", "feedback": "Blackmail to maintain the fraud scheme. Board members coerced into compliance.", "note": "Board members blackmailed with Christmas party photos — coerced into voting down reform"}
          ],
          "q1_note": "Four formal complaints to health inspector — zero followed up"
        },
        "silence": {
          "q1_response": "...I'll tell you why this matters. It's not just meatballs. It's about who this town serves. The mill director's children go to private school. The workers' children get mold. That's Industristad in one sentence.",
          "expression_hint": "Voice quiet but fierce",
          "q2_options": [
            {"text": "Tell me more about the families affected."},
            {"text": "Has the quality affected the children's health?"},
            {"text": "What would you want to see happen?"}
          ],
          "outcomes": [
            {"tier": 1, "response": "Three hundred worker families rely on school lunch as their children's main meal. Many of them can't afford to send packed lunches. When the school serves slop, those kids go hungry. It's a class issue.", "expression": "steady", "feedback": "Social context established — important for framing but needs specific evidence.", "note": "School lunch is main meal for 300 worker families"},
            {"tier": 2, "response": "The school nurse reported a 40% increase in stomach complaints since September. She documented it. Twelve children absent in one week in October — all with food poisoning symptoms. She reported it to the education director. He told her to 'stop keeping unofficial statistics.'", "expression": "controlled anger", "feedback": "Health data from school nurse, suppressed by same director running the scheme.", "note": "40% increase in stomach complaints — school nurse told to stop tracking"},
            {"tier": 3, "response": "I want people to know that Norrland Mat AB was previously called Norr Catering. It was shut down by the food safety board in Sundsvall last year for serving contaminated meat to a retirement home. Six elderly people hospitalized. They just changed the name and moved here. The education director knew — he approved a supplier that was already banned. I have the Sundsvall inspection report.", "expression": "cold fury", "feedback": "The supplier was previously shut down for food contamination. Renamed and rehired. Criminal negligence.", "note": "Supplier previously shut down in Sundsvall for contaminated meat — renamed and rehired"}
          ],
          "q1_note": "Mill director's kids in private school — workers' kids get mold"
        }
      }
    },
    "headlines": [
      {"text": "Parents Express Concern Over School Lunch Quality", "tone": "Cautious"},
      {"text": "School Lunch Supplier Connected to Education Director's Family", "tone": "Fact-based"},
      {"text": "FEEDING ON OUR CHILDREN — How a Shell Company Stole School Lunch Money", "tone": "Exposing"}
    ]
  }
]

def main():
    path = os.path.join(os.path.dirname(__file__), '..', 'data', 'stories.json')
    with open(path, 'r', encoding='utf-8') as f:
        stories = json.load(f)

    existing_ids = {s['id'] for s in stories}
    added = 0
    for s in STORIES:
        if s['id'] not in existing_ids:
            stories.append(s)
            added += 1
            print(f"  Added: {s['id']} (bv{s['base_value']})")
        else:
            print(f"  Skip (exists): {s['id']}")

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(stories, f, indent=2, ensure_ascii=False)

    ind = [s for s in stories if s.get('town') == 'industristad']
    print(f"\nTotal Industristad stories: {len(ind)}")
    from collections import Counter
    bv = Counter(s['base_value'] for s in ind)
    print(f"BV distribution: {dict(sorted(bv.items()))}")

if __name__ == '__main__':
    main()
