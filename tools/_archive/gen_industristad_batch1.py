#!/usr/bin/env python3
"""Generate Industristad stories batch 1: easy bv2-3 (stories 1-8)"""
import json, os

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

stories = [
  {
    "id": "fabrikslunchen",
    "title": "The Factory Lunch",
    "description": "Workers at the steel mill say the canteen food has gotten worse since the budget cuts.",
    "lead_text": "The meatballs taste like cardboard now. It's been getting worse since September.",
    "preview": "A canteen worker flags you down outside the factory gate.",
    "source_type": "street",
    "difficulty": "easy",
    "base_value": 2,
    "category": "human_interest",
    "npc_id": "solveig_lindgren",
    "npc_name": "Solveig Lindgren",
    "npc_title": "Canteen Worker",
    "town": "industristad",
    "interview": {
      "opening_line": "I shouldn't be talking to you. But someone has to say it — the food is getting worse and the workers deserve better.",
      "q1_options": [
        {"archetype": "friendly", "text": "That takes courage, Solveig. What's changed in the kitchen?"},
        {"archetype": "direct", "text": "How much has the canteen budget been cut? Do you have figures?"},
        {"archetype": "pressure", "text": "Some say management is pocketing the canteen budget. Is that what's happening?"},
        {"archetype": "silence", "text": "..."}
      ],
      "branches": {
        "friendly": {
          "q1_response": "We used to cook real food. Fresh potatoes, proper meat. Now it's powdered mash and the cheapest mince they can find. The men work twelve-hour shifts — they need proper meals.",
          "expression_hint": "Shaking her head, genuine frustration",
          "q2_options": [
            {"text": "Has anyone complained to management about the food quality?"},
            {"text": "What exactly are you serving now compared to before?"},
            {"text": "Do the workers talk about it? How does it affect morale?"}
          ],
          "outcomes": [
            {"tier": 1, "response": "Oh, we've complained. The kitchen manager brought it up at the monthly meeting. Bergström's secretary said 'adjust expectations'. That was it.", "expression": "guarded", "feedback": "You got confirmation of complaints ignored, but no details on where the money went.", "note": "Bergström's secretary said 'adjust expectations'"},
            {"tier": 2, "response": "Before: fresh herring on Fridays, homemade soup, real cream in the sauce. Now: tinned fish, packet soup, margarine. The budget went from 8 kronor per meal to 4.50. In six months.", "expression": "open", "feedback": "Concrete before/after with exact figures. Publishable comparison.", "note": "Budget went from 8 kronor per meal to 4.50"},
            {"tier": 3, "response": "The men are furious. But here's the thing — the canteen budget was cut to pay for the new executive dining room on the third floor. Bergström had it remodeled. Crystal glasses, white tablecloths. While his workers eat slop.", "expression": "open", "feedback": "Perfect contrast — workers eating cheap while executives dine in luxury. The story writes itself.", "note": "Budget cut to pay for executive dining room"}
          ],
          "q1_note": "Fresh potatoes became powdered mash"
        },
        "direct": {
          "q1_response": "Cut by almost half. We were at 8 kronor per head per meal. Now we're at 4.50. Started in July when the new accountant took over.",
          "expression_hint": "Pulls out a crumpled paper from her apron",
          "q2_options": [
            {"text": "Who authorized the cuts? Was it the factory director?"},
            {"text": "Do you have written records of the budget changes?"},
            {"text": "How many workers eat in the canteen each day?"}
          ],
          "outcomes": [
            {"tier": 2, "response": "Bergström signed it personally. The order came on a memo — I kept a copy. It says 'streamline catering operations'. Streamline. That's their word for starving workers.", "expression": "defiant", "feedback": "You have the director's name on the memo. Documentary evidence.", "note": "Bergström signed the order personally"},
            {"tier": 1, "response": "I've kept the purchase orders. I can show you — September versus March. The difference is shocking.", "expression": "guarded", "feedback": "Records exist but you didn't get the story behind the cuts.", "note": "Purchase orders show the difference"},
            {"tier": 1, "response": "About 400 workers per shift. Two shifts. That's 800 meals a day. At 3.50 less per meal, that's... a lot of money going somewhere.", "expression": "neutral", "feedback": "Scale is clear but you missed the destination of the funds.", "note": "800 meals a day, 3.50 less per meal"}
          ],
          "q1_note": "Budget cut from 8 to 4.50 kronor per meal"
        },
        "pressure": {
          "q1_response": "I... I didn't say that. I just said the food is worse. I don't know where the money goes. I just cook.",
          "expression_hint": "Steps back, looking around nervously",
          "q2_options": [
            {"text": "Solveig, someone is taking money meant for workers' food. Who?"},
            {"text": "I understand you're scared. But these workers trust you to feed them properly."},
            {"text": "If you don't tell me, who will? The workers can't speak up without losing their jobs."}
          ],
          "outcomes": [
            {"tier": 0, "response": "I'm not saying any more. I have bills to pay. Write about something else.", "expression": "hostile", "feedback": "She shut down completely. Too much pressure too fast.", "note": "Refuses to comment further"},
            {"tier": 2, "response": "*pause* ...The kitchen manager told me in confidence. The savings are going to renovate the third floor. Executive offices. But I didn't tell you that.", "expression": "nervous", "feedback": "You got the destination through empathy after pressure. Good recovery.", "note": "Savings going to renovate executive offices"},
            {"tier": 1, "response": "The union should be handling this. Talk to them. I'm just a cook.", "expression": "nervous", "feedback": "She redirected you. The story stays thin.", "note": "Suggests talking to the union instead"}
          ],
          "q1_note": "I just cook"
        },
        "silence": {
          "q1_response": "...*fidgets with her apron* Look, I came to you because nobody else listens. The men deserve real food. That's all.",
          "expression_hint": "Fills the silence by talking more",
          "q2_options": [
            {"text": "Take your time. What do the workers deserve to know?"},
            {"text": "What would happen if this story ran in the paper?"},
            {"text": "What haven't you told anyone yet?"}
          ],
          "outcomes": [
            {"tier": 1, "response": "They deserve to know that 800 meals a day got worse so someone could save money. Not for safety. Not for wages. Just... savings.", "expression": "guarded", "feedback": "Emotional truth but no hard details.", "note": "800 meals got worse to save money"},
            {"tier": 2, "response": "If it ran... Bergström would be embarrassed. The union would finally have to act. And maybe — maybe — I'd get my kitchen budget back.", "expression": "open", "feedback": "She named the power structure. Bergström + union inaction.", "note": "Bergström would be embarrassed, union would have to act"},
            {"tier": 3, "response": "*long pause* I found an invoice in the kitchen office. For a chandelier. 12,000 kronor. Delivered to the third-floor dining room. Same month they cut our meat budget by 60%. I took a photo of it. Here.", "expression": "open", "feedback": "Invoice proof — chandelier vs meatballs. Devastating contrast.", "note": "Invoice for 12,000 kr chandelier, same month meat budget cut 60%"}
          ],
          "q1_note": "Nobody else listens"
        }
      }
    },
    "headlines": {
      "tier_0": [
        {"text": "Workers complain about canteen food", "tone": "Factual"},
        {"text": "Steel mill canteen under scrutiny", "tone": "Neutral"},
        {"text": "Lunch quality declining at the factory", "tone": "Mild"}
      ],
      "tier_1": [
        {"text": "Canteen budget slashed — workers feel the difference", "tone": "Questioning"},
        {"text": "800 workers affected by canteen cuts", "tone": "Scale"},
        {"text": "Factory canteen: from fresh food to packet soup", "tone": "Contrast"}
      ],
      "tier_2": [
        {"text": "Director ordered canteen cuts while renovating executive offices", "tone": "Revealing"},
        {"text": "Memo reveals: Bergström signed the order to cut worker meals", "tone": "Documented"},
        {"text": "Workers eat worse so executives can dine better", "tone": "Confrontational"}
      ],
      "tier_3": [
        {"text": "12,000-kr chandelier bought with money cut from worker lunches", "tone": "Sensational"},
        {"text": "EXPOSED: Factory spent worker food budget on executive luxury", "tone": "Exposing"},
        {"text": "Invoice proves: workers' meals sacrificed for director's dining room", "tone": "Evidence-based"}
      ]
    }
  },
  {
    "id": "hamnkatten",
    "title": "The Harbor Cats",
    "description": "The dock workers' stray cat colony is being culled by order of the harbor master.",
    "lead_text": "They're going to kill the cats. All of them. The harbor master signed the order yesterday.",
    "preview": "A dockworker stops you near the harbor gates, upset.",
    "source_type": "street",
    "difficulty": "easy",
    "base_value": 2,
    "category": "human_interest",
    "npc_id": "gustav_nilsson_i",
    "npc_name": "Gustav Nilsson",
    "npc_title": "Dock Worker",
    "town": "industristad",
    "interview": {
      "opening_line": "Fifteen cats. They've been here longer than any of us. Hans Dahl wants them gone by Friday because some Gothenburg shipping executive complained about 'hygiene'.",
      "q1_options": [
        {"archetype": "friendly", "text": "That must be hard. How long have the cats been part of the harbor?"},
        {"archetype": "direct", "text": "Who ordered the cull and on what grounds?"},
        {"archetype": "pressure", "text": "Is it true this is really about the port authority wanting to impress outside investors?"},
        {"archetype": "silence", "text": "..."}
      ],
      "branches": {
        "friendly": {
          "q1_response": "Twenty years at least. Old Göran started feeding them in the fifties. They keep the rats away — that's the point. Without them, the grain stores would be overrun.",
          "expression_hint": "Softer now, scratching behind a cat's ear",
          "q2_options": [
            {"text": "Do the cats actually serve a pest control function?"},
            {"text": "How are the other dock workers reacting?"},
            {"text": "Has anyone tried to negotiate with the harbor master?"}
          ],
          "outcomes": [
            {"tier": 2, "response": "The health inspector said last year that the cats are the most effective rat control on the docks. It's in the annual report. Dahl knows this — he just doesn't care because his boss in Gothenburg doesn't like fur on his suit.", "expression": "defiant", "feedback": "Official recognition of cats' value + personal motive for the cull. Good angle.", "note": "Health inspector recognized cats as effective rat control"},
            {"tier": 1, "response": "Most of the guys are angry but won't say anything. Dahl controls the shift assignments. You speak up, you get the night shift for a month.", "expression": "guarded", "feedback": "Worker intimidation, but secondary to the main story.", "note": "Dahl controls shift assignments, workers afraid to speak"},
            {"tier": 3, "response": "Birger tried. Dahl laughed and said 'This isn't a petting zoo, it's a port.' But here's the thing — Dahl just signed a contract with Göteborgs Hamn AB to take over operations. The cats are the least of it. He's privatizing the whole harbor and nobody knows.", "expression": "open", "feedback": "The cats are a symptom — the real story is harbor privatization. Huge.", "note": "Dahl signed privatization contract with Göteborgs Hamn AB"}
          ],
          "q1_note": "They've been here twenty years, keep rats away"
        },
        "direct": {
          "q1_response": "Hans Dahl, harbor master. Official reason: 'sanitary concerns'. Unofficial reason: a Gothenburg shipping executive visited last week and saw a cat on a loading pallet.",
          "expression_hint": "Shrugs matter-of-factly",
          "q2_options": [
            {"text": "Has the harbor done a health assessment?"},
            {"text": "Can I see the order? Is it documented?"},
            {"text": "What will happen to the rats without the cats?"}
          ],
          "outcomes": [
            {"tier": 1, "response": "No assessment. No vet consulted. Just a memo from Dahl to 'resolve the feral animal situation by Friday'. That's his idea of process.", "expression": "neutral", "feedback": "No process followed, but a thin story on its own.", "note": "No health assessment or vet consultation"},
            {"tier": 2, "response": "It's pinned on the break room board. I can show you. It says 'by order of the harbor master, effective immediately'. No consultation with workers or the health board.", "expression": "neutral", "feedback": "Documented proof of unilateral decision — bypassing required process.", "note": "Order posted without health board consultation"},
            {"tier": 1, "response": "The grain stores will be infested within a month. We'll spend more on rat poison than we ever spent on cat food. But Dahl doesn't think that far ahead.", "expression": "defiant", "feedback": "Practical argument but not a strong news angle.", "note": "Grain stores will be infested without cats"}
          ],
          "q1_note": "Gothenburg executive complained about hygiene"
        },
        "pressure": {
          "q1_response": "Investors? I... maybe. There's been talk about the harbor changing ownership. But I'm a dock worker, not a businessman.",
          "expression_hint": "Caught off guard, defensive",
          "q2_options": [
            {"text": "What kind of ownership changes? Who's buying?"},
            {"text": "The workers deserve to know if their harbor is being sold. Are you going to stay quiet?"},
            {"text": "Hans Dahl isn't doing this for hygiene. What has he been up to lately?"}
          ],
          "outcomes": [
            {"tier": 2, "response": "I heard — this is just what I heard — that Göteborgs Hamn AB is interested in taking over port operations. Dahl's been having lunch with their people at Hotel Strand.", "expression": "nervous", "feedback": "Privatization rumor with specific details. Worth investigating.", "note": "Göteborgs Hamn AB interested, Dahl dining with them"},
            {"tier": 1, "response": "I'm not staying quiet, am I? I'm talking to you. But the cats are the issue. Write about the cats.", "expression": "hostile", "feedback": "He wants the story small. You missed the bigger picture.", "note": "Wants focus on cats, not politics"},
            {"tier": 0, "response": "Dahl's the harbor master. He does what he does. Leave me out of the politics. I just want the cats to live.", "expression": "hostile", "feedback": "Pushed too hard on the wrong topic. He came about cats, not corruption.", "note": "Refuses to discuss harbor politics"}
          ],
          "q1_note": "Talk about harbor changing ownership"
        },
        "silence": {
          "q1_response": "...You're not going to ask? Fine. I'll tell you what I think. I think the cats are the canary in the coal mine. Everything that makes this harbor human is being stripped away.",
          "expression_hint": "Grows more passionate in the silence",
          "q2_options": [
            {"text": "What else is being stripped away?"},
            {"text": "Tell me about the harbor. What it was and what it's becoming."},
            {"text": "Why does this matter so much to you personally?"}
          ],
          "outcomes": [
            {"tier": 3, "response": "The break room is closing. The Christmas bonus was cancelled. And now the cats. You know why? Because Dahl is preparing the harbor for sale. I saw the brochure on his desk — 'Modern Port Operations by Göteborgs Hamn AB.' Our harbor, sold to a Gothenburg company. And none of us were told.", "expression": "open", "feedback": "Through silence, he connected the dots himself. Cats → privatization → worker betrayal. Complete story.", "note": "Saw privatization brochure on Dahl's desk"},
            {"tier": 2, "response": "It was a place where men could work with dignity. Old Göran and the cats. Coffee in the break room. Now it's all efficiency reports and Gothenburg suits. We're numbers now.", "expression": "nostalgic", "feedback": "Emotional portrait of a workplace losing its soul. Good texture.", "note": "Harbor losing its human character"},
            {"tier": 1, "response": "My father worked this harbor for forty years. He used to say the cats were the soul of the place. If they go... I don't know. Feels like the harbor dies too.", "expression": "guarded", "feedback": "Personal but not newsworthy beyond a feature piece.", "note": "Father worked the harbor forty years"}
          ],
          "q1_note": "Everything human is being stripped away"
        }
      }
    },
    "headlines": {
      "tier_0": [
        {"text": "Harbor cats face removal order", "tone": "Factual"},
        {"text": "Dock workers upset over cat cull", "tone": "Human interest"},
        {"text": "Harbor master orders stray cats removed", "tone": "Direct"}
      ],
      "tier_1": [
        {"text": "No assessment done before harbor cat cull ordered", "tone": "Questioning"},
        {"text": "Workers say cats keep rats away — master says remove them", "tone": "Contrast"},
        {"text": "Harbor cat colony to be destroyed after executive complaint", "tone": "Revealing"}
      ],
      "tier_2": [
        {"text": "Harbor master bypassed health board to order cat cull", "tone": "Procedural"},
        {"text": "Sources: Harbor master courting Gothenburg investors", "tone": "Political"},
        {"text": "Workers silenced as harbor master pushes changes", "tone": "Worker angle"}
      ],
      "tier_3": [
        {"text": "REVEALED: Harbor master preparing secret sale to Gothenburg company", "tone": "Sensational"},
        {"text": "Cat cull was just the start — harbor privatization underway", "tone": "Investigative"},
        {"text": "Brochure found: Industristad harbor being sold without worker consultation", "tone": "Evidence-based"}
      ]
    }
  },
  {
    "id": "rostiga_racket",
    "title": "The Rusted Railing",
    "description": "Safety railings at the loading dock haven't been replaced despite three incident reports.",
    "lead_text": "The railing on dock 4 is rusted through. Third report filed. Nothing done.",
    "preview": "Anonymous maintenance report left in the newsroom mailbox.",
    "source_type": "document",
    "difficulty": "easy",
    "base_value": 2,
    "category": "labor",
    "npc_id": "ove_hedberg",
    "npc_name": "Ove Hedberg",
    "npc_title": "Maintenance Worker",
    "town": "industristad",
    "interview": {
      "opening_line": "I filed three work orders this year. Three. Each time the same answer: 'budget pending'. Meanwhile a man fell off dock 4 last month and broke his collarbone.",
      "q1_options": [
        {"archetype": "friendly", "text": "That must be frustrating. Three reports and nothing done?"},
        {"archetype": "direct", "text": "Show me what's wrong with the railing. I want specifics."},
        {"archetype": "pressure", "text": "Someone broke their collarbone because of this. Isn't that criminal negligence?"},
        {"archetype": "silence", "text": "..."}
      ],
      "branches": {
        "friendly": {
          "q1_response": "Frustrating isn't the word. I'm the one who has to look at that railing every day knowing someone could go over. And when they do, it'll be my signature on the report saying it was flagged.",
          "expression_hint": "Grips his wrench tighter, jaw tightening",
          "q2_options": [
            {"text": "Who receives the work orders? Where does the chain break?"},
            {"text": "Tell me about the man who fell. What happened exactly?"},
            {"text": "Do you have copies of the three reports?"}
          ],
          "outcomes": [
            {"tier": 2, "response": "I send them to facilities management. Facilities sends them to finance. Finance sends them to Bergström's office. And Bergström's office sends them to the bottom of a pile. The whole system is designed to lose paperwork.", "expression": "defiant", "feedback": "You mapped the negligence chain all the way to the director. Structural failure.", "note": "Reports go from facilities to finance to Bergström's office — designed to lose paperwork"},
            {"tier": 1, "response": "Arne Andersson. Slipped on ice, grabbed the railing, railing gave way. Fell four meters onto concrete. He was off work for six weeks. Nobody even visited him.", "expression": "guarded", "feedback": "You got the human story but not the systemic problem.", "note": "Arne Andersson fell four meters, off work six weeks"},
            {"tier": 3, "response": "Three copies. Dated and stamped. And I have the responses — two form letters saying 'under review' and one that says 'maintenance budget allocated to priority projects'. You know what the priority project was? Repainting the executive parking lot.", "expression": "open", "feedback": "Documentary proof: three reports ignored, money spent on cosmetics instead. Gold.", "note": "Maintenance budget went to repainting executive parking lot"}
          ],
          "q1_note": "My signature on the report saying it was flagged"
        },
        "direct": {
          "q1_response": "Come look. *leads you outside* See that? You can push your finger through the metal. It's like wet cardboard. The posts are barely connected to the concrete.",
          "expression_hint": "Shows you firsthand, tapping the railing",
          "q2_options": [
            {"text": "How long has it been like this?"},
            {"text": "Are other safety installations also in this condition?"},
            {"text": "What would a replacement cost?"}
          ],
          "outcomes": [
            {"tier": 1, "response": "Since at least April. It was already bad in the winter but the rust accelerated in the spring rain. By summer it was a death trap.", "expression": "neutral", "feedback": "Timeline established but no accountability.", "note": "Dangerous since at least April"},
            {"tier": 2, "response": "The fire extinguishers on level 2 expired in March. The emergency exit on the east side has been locked shut for six months — 'to prevent theft'. If there's a fire, people will die.", "expression": "nervous", "feedback": "Pattern of safety failures beyond just the railing. Systemic neglect.", "note": "Fire extinguishers expired, emergency exit locked shut"},
            {"tier": 1, "response": "Maybe 2,000 kronor for materials. I could do the labor myself. But they won't approve it. Two thousand kronor to save someone's life — and they say 'budget pending'.", "expression": "defiant", "feedback": "Cost is trivial, making the neglect worse. But thin for a splash.", "note": "Replacement cost: 2,000 kronor"}
          ],
          "q1_note": "You can push your finger through the metal"
        },
        "pressure": {
          "q1_response": "Criminal? Maybe. But who's going to prosecute? The safety inspector plays cards with the factory manager every Thursday.",
          "expression_hint": "Bitter laugh, shakes his head",
          "q2_options": [
            {"text": "Are you saying the safety inspector isn't doing his job?"},
            {"text": "If someone dies because of this railing, who is responsible?"},
            {"text": "Why haven't the workers filed a collective complaint through the union?"}
          ],
          "outcomes": [
            {"tier": 2, "response": "He did one inspection this year. Spent twenty minutes. Signed off on everything. I watched him — he didn't even go to dock 4. Just walked through zone A and ticked every box.", "expression": "defiant", "feedback": "Safety inspector rubber-stamping without actual inspection. Corruption angle.", "note": "Inspector spent twenty minutes, didn't visit dock 4"},
            {"tier": 1, "response": "Legally? The company. Practically? Nobody. It'll be an 'accident'. Like Arne's fall was an 'accident'. Like everything here is an 'accident'.", "expression": "hostile", "feedback": "Cynicism but no evidence.", "note": "Everything is called an 'accident'"},
            {"tier": 1, "response": "The union? Pettersson? He plays golf with management. The union here protects itself, not us.", "expression": "hostile", "feedback": "Union criticism but no proof of safety cover-up.", "note": "Union protects itself, not workers"}
          ],
          "q1_note": "Safety inspector plays cards with factory manager"
        },
        "silence": {
          "q1_response": "*long pause* You know what keeps me up at night? The next person who grabs that railing won't break a collarbone. They'll die. And everyone will act surprised.",
          "expression_hint": "Voice drops, deadly serious",
          "q2_options": [
            {"text": "What would you need to happen to prevent that?"},
            {"text": "Show me what you have. The reports, the photos, everything."},
            {"text": "Why did you come to the paper instead of the police?"}
          ],
          "outcomes": [
            {"tier": 1, "response": "Someone with authority to say 'fix it'. Not a memo. Not a form. Just someone who cares enough to spend 2,000 kronor.", "expression": "guarded", "feedback": "Heartfelt but no ammunition for the story.", "note": "Needs someone with authority to act"},
            {"tier": 2, "response": "Here. Three work orders. Two responses. And these photos I took last week — you can see the rust, the broken welds, the concrete crumbling. All dated.", "expression": "open", "feedback": "Full documentation trail. Photos + reports + dates.", "note": "Photos showing rust, broken welds, crumbling concrete — all dated"},
            {"tier": 3, "response": "Because the police would call the safety inspector. And the safety inspector would call Bergström. And Bergström would call my boss. And I'd be out by Monday. *pause* But I kept a logbook. Every deficiency I've reported for three years. Forty-seven items. Only six were fixed. The rest — 'budget pending'. I have the whole record at home.", "expression": "open", "feedback": "Three years of documented negligence. 47 reports, 6 fixed. This isn't one railing — it's systemic.", "note": "Logbook: 47 deficiency reports in 3 years, only 6 fixed"}
          ],
          "q1_note": "The next person will die"
        }
      }
    },
    "headlines": {
      "tier_0": [
        {"text": "Rusted railing at loading dock raises concern", "tone": "Factual"},
        {"text": "Dock worker injured after railing collapse", "tone": "Personal"},
        {"text": "Maintenance issues reported at the harbor", "tone": "Neutral"}
      ],
      "tier_1": [
        {"text": "Three safety reports filed — no action taken", "tone": "Questioning"},
        {"text": "2,000 kronor could prevent next dock accident", "tone": "Scale"},
        {"text": "Worker fell four meters — management says 'budget pending'", "tone": "Quote-driven"}
      ],
      "tier_2": [
        {"text": "Safety inspector signed off without visiting dangerous dock", "tone": "Exposing"},
        {"text": "Reports show: maintenance budget diverted to executive areas", "tone": "Documented"},
        {"text": "Photos reveal: loading dock railings rusted through", "tone": "Evidence"}
      ],
      "tier_3": [
        {"text": "THREE YEARS: 47 safety reports, only 6 fixed — worker's logbook reveals pattern", "tone": "Sensational"},
        {"text": "EXPOSED: Systematic safety neglect at the harbor — full record kept", "tone": "Investigative"},
        {"text": "Maintenance worker's secret logbook documents years of ignored dangers", "tone": "Evidence-based"}
      ]
    }
  },
  {
    "id": "fabriksvagen",
    "title": "The Factory Road",
    "description": "A new municipal road was built that only seems to serve the factory director's private estate.",
    "lead_text": "They built a road for one man. Taxpayer money. For one man's driveway.",
    "preview": "Municipal planning document found in a council committee appendix.",
    "source_type": "document",
    "difficulty": "easy",
    "base_value": 2,
    "category": "corruption",
    "npc_id": "bengt_larsson_i",
    "npc_name": "Bengt Larsson",
    "npc_title": "Municipal Planner",
    "town": "industristad",
    "interview": {
      "opening_line": "The Lindvägen extension? It was approved through normal channels. I don't see what the issue is.",
      "q1_options": [
        {"archetype": "friendly", "text": "I'm sure you followed procedure, Bengt. Can you walk me through how this road was planned?"},
        {"archetype": "direct", "text": "The road ends at Rolf Bergström's property. Who requested the extension?"},
        {"archetype": "pressure", "text": "Public funds for a private road to the factory director's estate. How do you explain that?"},
        {"archetype": "silence", "text": "..."}
      ],
      "branches": {
        "friendly": {
          "q1_response": "Of course. It was part of the 1974 infrastructure plan. The committee approved it in March. It serves... the area.",
          "expression_hint": "Too rehearsed, straightens his glasses",
          "q2_options": [
            {"text": "How many residents live along the extended road?"},
            {"text": "Who sits on the infrastructure committee that approved it?"},
            {"text": "Was there a public consultation before the decision?"}
          ],
          "outcomes": [
            {"tier": 2, "response": "Well... currently, it's... the Bergström estate is the only property. But there are plans for future development. Eventually. The committee felt it was forward-thinking.", "expression": "evasive", "feedback": "He admitted only one property is served. 'Forward-thinking' — wonderful euphemism.", "note": "Only the Bergström estate is currently served by the road"},
            {"tier": 3, "response": "The committee... *adjusts glasses nervously* ...Bergström's wife Karin sits on the infrastructure committee. She recused herself for the vote, technically. But she presented the proposal. And the cost estimate. And the route map.", "expression": "nervous", "feedback": "Conflict of interest: director's wife proposed, designed, and priced her own road. Perfect.", "note": "Bergström's wife sits on the committee, presented the proposal herself"},
            {"tier": 1, "response": "Public consultation? For a road extension? That's not required for projects under 500,000 kronor.", "expression": "confident", "feedback": "He's hiding behind procedure. You didn't crack it.", "note": "No public consultation required for projects under 500,000 kr"}
          ],
          "q1_note": "Part of the 1974 infrastructure plan"
        },
        "direct": {
          "q1_response": "The extension was requested by... the infrastructure committee. As part of area development. Mr. Bergström's property happens to be along the route.",
          "expression_hint": "Choosing words very carefully",
          "q2_options": [
            {"text": "What was the total cost of the road extension?"},
            {"text": "Were alternative routes considered?"},
            {"text": "Is Bergström connected to anyone on the committee?"}
          ],
          "outcomes": [
            {"tier": 1, "response": "The total cost was 340,000 kronor. For 1.2 kilometers of asphalt. That's within normal per-kilometer pricing.", "expression": "confident", "feedback": "Cost figures but no scandal angle.", "note": "340,000 kronor for 1.2 km"},
            {"tier": 2, "response": "Alternative? No. The route was... determined by the terrain. *pause* Look, I just draw the maps. The committee decides.", "expression": "nervous", "feedback": "No alternatives considered for a road serving one property. Suspicious.", "note": "No alternative routes considered"},
            {"tier": 2, "response": "Connected? Well, his wife Karin is on the committee. But she... declared a conflict of interest. On paper.", "expression": "evasive", "feedback": "Conflict of interest confirmed, but 'on paper' suggests it's a formality.", "note": "Wife Karin on committee, declared conflict 'on paper'"}
          ],
          "q1_note": "Bergström's property 'happens to be' along the route"
        },
        "pressure": {
          "q1_response": "That's a very loaded characterization. The road serves the Lindvägen area. The fact that a prominent citizen lives there doesn't make it corrupt.",
          "expression_hint": "Defensive, crossing arms",
          "q2_options": [
            {"text": "How many other citizens live on Lindvägen?"},
            {"text": "If this road is legitimate, you won't mind me seeing the committee minutes?"},
            {"text": "Bengt, are you comfortable putting your name on this if it comes out?"}
          ],
          "outcomes": [
            {"tier": 2, "response": "Currently... one household. But the zoning plan allows for up to twelve plots. In the future. Theoretically.", "expression": "nervous", "feedback": "One household. 340,000 kronor. The numbers speak for themselves.", "note": "Currently one household on the road, zoning allows future development"},
            {"tier": 1, "response": "The minutes are public record. You're welcome to request them through the registrar. I have nothing to hide.", "expression": "hostile", "feedback": "He's stonewalling you with procedure.", "note": "Minutes available through public records"},
            {"tier": 1, "response": "I followed procedure. My conscience is clear. Now if you'll excuse me, I have a site visit.", "expression": "hostile", "feedback": "He's done talking. You got nothing explosive.", "note": "Claims he followed procedure"}
          ],
          "q1_note": "A prominent citizen doesn't make it corrupt"
        },
        "silence": {
          "q1_response": "...*fidgets* Listen, I'm a civil servant. I do what the committee tells me. If you want to know why that road exists, ask the committee.",
          "expression_hint": "Growing uncomfortable in the silence",
          "q2_options": [
            {"text": "What would the committee say if I asked them?"},
            {"text": "You seem uncomfortable, Bengt. What aren't you telling me?"},
            {"text": "Did anyone on the committee benefit personally from this road?"}
          ],
          "outcomes": [
            {"tier": 1, "response": "They'd say exactly what I said. Infrastructure plan. Area development. Future housing. The official story.", "expression": "evasive", "feedback": "He's repeating the party line. You didn't break through.", "note": "Repeats the official story"},
            {"tier": 2, "response": "I'm not uncomfortable. I'm... look, between us? I flagged this internally. I wrote a memo saying the cost-benefit was questionable. I was told to proceed. That's all I can say.", "expression": "nervous", "feedback": "He flagged it and was overruled. Internal dissent documented.", "note": "Wrote internal memo questioning cost-benefit, told to proceed"},
            {"tier": 3, "response": "*closes door* Karin Bergström drew the original route map. Before the committee meeting. Before any feasibility study. The route was decided before the process even started. I have the original sketch with her handwriting on it. Date-stamped three months before the committee 'approved' it.", "expression": "open", "feedback": "Pre-decided route, director's wife's handwriting, months before formal approval. The whole process was a sham.", "note": "Karin Bergström's handwritten route map dated 3 months before committee approval"}
          ],
          "q1_note": "Do what the committee tells me"
        }
      }
    },
    "headlines": {
      "tier_0": [
        {"text": "New road extended to Lindvägen area", "tone": "Factual"},
        {"text": "Municipal road project under review", "tone": "Neutral"},
        {"text": "Questions raised about road extension", "tone": "Cautious"}
      ],
      "tier_1": [
        {"text": "340,000-kronor road serves one property", "tone": "Questioning"},
        {"text": "Planner flagged road project — was told to proceed", "tone": "Revealing"},
        {"text": "No public consultation for costly road extension", "tone": "Procedural"}
      ],
      "tier_2": [
        {"text": "Factory director's wife on committee that approved road to their estate", "tone": "Conflict of interest"},
        {"text": "Only one household on 340,000-kronor road — director's family", "tone": "Exposing"},
        {"text": "Internal memo questioned road — planner overruled", "tone": "Documented"}
      ],
      "tier_3": [
        {"text": "EXPOSED: Director's wife drew road route months before committee 'approved' it", "tone": "Sensational"},
        {"text": "Pre-dated sketch proves: road decision was made before any process", "tone": "Evidence-based"},
        {"text": "Sham approval: factory family designed their own taxpayer-funded road", "tone": "Confrontational"}
      ]
    }
  },
  {
    "id": "fiskeklubben",
    "title": "The Fishing Club",
    "description": "The local fishing club has lost access to their stretch of river due to factory pollution.",
    "lead_text": "We haven't been able to fish the Industriån for two years. The water is dead.",
    "preview": "Letter from the fishing club chairman, handwritten on club stationery.",
    "source_type": "letter",
    "difficulty": "easy",
    "base_value": 2,
    "category": "human_interest",
    "npc_id": "lars_erik_nordin",
    "npc_name": "Lars-Erik Nordin",
    "npc_title": "Fishing Club Chairman",
    "town": "industristad",
    "interview": {
      "opening_line": "Forty years I've fished this river. My father before me. Now the trout are gone and the water smells like ammonia.",
      "q1_options": [
        {"archetype": "friendly", "text": "Forty years is a long relationship with a river. When did things start to change?"},
        {"archetype": "direct", "text": "What's killing the fish? Is it the chemical plant upstream?"},
        {"archetype": "pressure", "text": "The municipality says the water quality is within acceptable limits. Is that accurate?"},
        {"archetype": "silence", "text": "..."}
      ],
      "branches": {
        "friendly": {
          "q1_response": "The trout started disappearing around '72. First the big ones. Then the minnows. By last summer you couldn't find anything alive downstream from the chemical plant.",
          "expression_hint": "Staring at the water, voice flattening",
          "q2_options": [
            {"text": "Have you tested the water yourself?"},
            {"text": "What's the club doing about it? Any formal complaints?"},
            {"text": "Does the chemical plant acknowledge any responsibility?"}
          ],
          "outcomes": [
            {"tier": 1, "response": "We complained to the county board last spring. They said they'd send an inspector. That was fourteen months ago.", "expression": "guarded", "feedback": "Bureaucratic inaction confirmed but no evidence of what's in the water.", "note": "County board promised inspector fourteen months ago, never came"},
            {"tier": 2, "response": "A teacher at the school — he's a hobby chemist — tested it for us. High levels of ammonia and something he called phenol compounds. He said it's industrial waste. Definitely not natural.", "expression": "open", "feedback": "Independent water test with chemical identification. Strong supporting evidence.", "note": "Teacher found high ammonia and phenol compounds — industrial waste"},
            {"tier": 1, "response": "Acknowledge? They won't even meet with us. Their factory manager said we're 'hobbyists with an agenda'. Forty years and I'm a hobbyist.", "expression": "defiant", "feedback": "Dismissive attitude from the plant but no hard evidence.", "note": "Chemical plant calls fishing club 'hobbyists with an agenda'"}
          ],
          "q1_note": "Trout disappeared around '72, water smells like ammonia"
        },
        "direct": {
          "q1_response": "The chemical plant. Industrikemin AB. Their discharge pipe runs straight into the river about 800 meters upstream from our fishing grounds.",
          "expression_hint": "Points upstream, matter-of-fact",
          "q2_options": [
            {"text": "Does the plant have a permit for river discharge?"},
            {"text": "Is there any other possible source of contamination?"},
            {"text": "How many people are affected beyond the fishing club?"}
          ],
          "outcomes": [
            {"tier": 2, "response": "They have a permit from 1968. It allows 'treated wastewater' discharge. But treated? I've seen the pipe. The water coming out is yellow-brown. That's not treated.", "expression": "defiant", "feedback": "1968 permit for 'treated' water vs visible untreated discharge. Permit violation angle.", "note": "1968 permit allows 'treated wastewater' but discharge is yellow-brown"},
            {"tier": 1, "response": "There's a small dairy upstream, but they've been there for decades without issue. It's the chemical plant. Everyone knows.", "expression": "neutral", "feedback": "Common knowledge but no hard proof.", "note": "Only the chemical plant is the new factor"},
            {"tier": 1, "response": "The allotment gardens downstream — families grow vegetables there, water them from the river. Children play by the banks in summer. It's not just about fish.", "expression": "guarded", "feedback": "Human impact angle but no documentation.", "note": "Families grow food using river water, children play by the banks"}
          ],
          "q1_note": "Discharge pipe 800 meters upstream"
        },
        "pressure": {
          "q1_response": "Acceptable limits? What limits? They haven't tested the water since 1971. I requested the data through the county board — they said it was 'archived'.",
          "expression_hint": "Scoffing, genuinely angry",
          "q2_options": [
            {"text": "Can you prove the water hasn't been tested?"},
            {"text": "Who at the county board handled your request?"},
            {"text": "What do the 'archived' results from 1971 show?"}
          ],
          "outcomes": [
            {"tier": 1, "response": "I have the letter. I wrote to them. They wrote back saying they 'cannot locate current monitoring data'. Make of that what you will.", "expression": "defiant", "feedback": "Admission of missing data but not explosive.", "note": "County board 'cannot locate current monitoring data'"},
            {"tier": 2, "response": "A clerk named Gunvor Ek. She was helpful at first but then went quiet. Called me back a week later and said 'I've been told to direct all inquiries to the county environmental officer'. I haven't heard back since.", "expression": "guarded", "feedback": "A clerk was told to stop helping. Internal silencing. Good lead.", "note": "Clerk Gunvor Ek told to redirect inquiries, went quiet"},
            {"tier": 3, "response": "That's the thing. The 1971 results SHOULD show the water was already contaminated. A former county inspector I know — now retired — told me that the results were 'adjusted' before filing. The original readings were double the permitted levels. Someone changed the numbers.", "expression": "open", "feedback": "Falsified water quality data from a retired insider. If you can verify this, it's massive.", "note": "Retired inspector says 1971 results were 'adjusted' — original readings double the limit"}
          ],
          "q1_note": "Haven't tested since 1971, data 'archived'"
        },
        "silence": {
          "q1_response": "...My grandson asked me last summer why we don't fish anymore. I didn't know what to tell him. How do you explain to a seven-year-old that someone poisoned his river?",
          "expression_hint": "Old eyes wet, staring at the empty water",
          "q2_options": [
            {"text": "What would you want your grandson to know about this river?"},
            {"text": "Who poisoned it, Lars-Erik?"},
            {"text": "What are you afraid will happen if nobody writes about this?"}
          ],
          "outcomes": [
            {"tier": 1, "response": "That it used to be alive. That his great-grandfather caught salmon here. That this town used to care about something besides production quotas.", "expression": "nostalgic", "feedback": "Beautiful personal story but not a news piece.", "note": "Great-grandfather caught salmon here"},
            {"tier": 2, "response": "Industrikemin AB. And the county that let them do it. And the municipality that looks the other way because the plant employs 300 people. Everyone's complicit.", "expression": "defiant", "feedback": "He named the whole system. Multiple actor accountability.", "note": "Chemical plant, county, and municipality all complicit"},
            {"tier": 3, "response": "That the children get sick. The allotment gardens downstream — three families had to stop growing because the vegetables tasted wrong. And little Maja from Strandgatan... she had rashes all summer after swimming. The doctor said 'eczema'. But I've seen that water. That's not eczema. That's poison.", "expression": "open", "feedback": "Children's health affected. Medical dismissal of symptoms. This elevates from environmental to public health.", "note": "Children with rashes after swimming, doctor misdiagnosed as 'eczema'"}
          ],
          "q1_note": "How do you explain to a seven-year-old"
        }
      }
    },
    "headlines": {
      "tier_0": [
        {"text": "Fishing club loses access to river stretch", "tone": "Factual"},
        {"text": "Trout population collapses in Industriån", "tone": "Environmental"},
        {"text": "Local fishermen concerned about river quality", "tone": "Mild"}
      ],
      "tier_1": [
        {"text": "River water untested since 1971 — county board admits", "tone": "Questioning"},
        {"text": "Fishing club: 'The water is dead'", "tone": "Quote-driven"},
        {"text": "Chemical plant discharge pipe runs into local fishing waters", "tone": "Connecting"}
      ],
      "tier_2": [
        {"text": "Chemical plant discharges untreated waste — 1968 permit violated", "tone": "Exposing"},
        {"text": "County clerk silenced after helping fishing club", "tone": "Cover-up"},
        {"text": "Children, gardens, fish: the full cost of river pollution", "tone": "Human impact"}
      ],
      "tier_3": [
        {"text": "FALSIFIED: Retired inspector says 1971 water results were altered", "tone": "Sensational"},
        {"text": "Children sick from swimming — doctor dismissed symptoms as 'eczema'", "tone": "Health scandal"},
        {"text": "Poisoned river: fake data, silenced workers, sick children", "tone": "Investigative"}
      ]
    }
  },
  {
    "id": "idrottsplanen",
    "title": "The Workers' Field",
    "description": "The factory sports field where workers play football is being sold for factory expansion.",
    "lead_text": "They're tearing up our football pitch. Bergström wants to build a new loading bay.",
    "preview": "Angry young apprentice corners you outside the library.",
    "source_type": "street",
    "difficulty": "easy",
    "base_value": 2,
    "category": "human_interest",
    "npc_id": "tommy_andersson_i",
    "npc_name": "Tommy Andersson",
    "npc_title": "Apprentice Welder",
    "town": "industristad",
    "interview": {
      "opening_line": "That field is the only good thing about working here. Every Wednesday and Saturday we play. Now they're turning it into concrete for trucks.",
      "q1_options": [
        {"archetype": "friendly", "text": "Sounds like the field means a lot to the workers. Tell me about it."},
        {"archetype": "direct", "text": "When was the decision made and who approved the sale?"},
        {"archetype": "pressure", "text": "Is it true the workers were never consulted about losing their sports field?"},
        {"archetype": "silence", "text": "..."}
      ],
      "branches": {
        "friendly": {
          "q1_response": "It's where the old-timers teach us youngsters. Where foremen forget they're foremen. We even got our rival match against the shipyard team. It's the one place at work where you're a person, not a number.",
          "expression_hint": "Animated, hands moving as he describes plays",
          "q2_options": [
            {"text": "Who decided to sell the field? Was it Bergström directly?"},
            {"text": "What do the older workers say about losing it?"},
            {"text": "Is there anywhere else the team could play?"}
          ],
          "outcomes": [
            {"tier": 2, "response": "Bergström said it at the quarterly meeting. Didn't even discuss it. Just said 'the sports field will be repurposed for operational expansion effective January'. Like it was nothing. Forty years of football — nothing.", "expression": "defiant", "feedback": "Unilateral decision, no discussion. Management dismissing workers' culture.", "note": "Bergström announced it at quarterly meeting, no discussion"},
            {"tier": 1, "response": "Old Lennart cried. First time I've ever seen that man show emotion. He said 'they're taking the last thing that makes this place bearable.'", "expression": "guarded", "feedback": "Emotional but not newsworthy beyond a feature.", "note": "Old worker cried — 'last thing that makes this place bearable'"},
            {"tier": 1, "response": "The municipal pitch is booked solid and costs money. We can't afford it on apprentice wages. Without the factory field, the team dies.", "expression": "nervous", "feedback": "No alternatives exist, but thin for a news story.", "note": "No affordable alternative venue exists"}
          ],
          "q1_note": "One place where you're a person, not a number"
        },
        "direct": {
          "q1_response": "The board decided in October. Nobody told the workers until last week. Bergström put up a notice on the canteen wall — 'field closing December 15'. That's how we found out.",
          "expression_hint": "Shows you a crumpled photocopy of the notice",
          "q2_options": [
            {"text": "Was the workers' council informed before the notice went up?"},
            {"text": "What's the land worth? Is this about real estate?"},
            {"text": "Is the loading bay expansion actually needed?"}
          ],
          "outcomes": [
            {"tier": 1, "response": "Workers' council? Nobody asked us anything. We found out from a piece of paper taped to a wall.", "expression": "defiant", "feedback": "Bypassed consultation but a familiar complaint.", "note": "Workers' council not consulted"},
            {"tier": 2, "response": "Funny you ask. The field is right next to the main road. A loading bay there? Makes no logistical sense. But a car dealership or a petrol station? That makes a lot of financial sense. Someone told me Bergström got an offer for the land.", "expression": "nervous", "feedback": "The loading bay might be a cover story. Real motive: land sale for profit.", "note": "Loading bay doesn't make logistic sense, Bergström may have received an offer for the land"},
            {"tier": 1, "response": "Do they need more loading capacity? Sure. But there's empty land on the south side of the factory. They chose the field because it's easier. Or cheaper. Or both.", "expression": "neutral", "feedback": "Alternative locations exist but you didn't uncover the real motive.", "note": "Empty land on south side could be used instead"}
          ],
          "q1_note": "Board decided in October, workers told last week"
        },
        "pressure": {
          "q1_response": "Consulted? Ha! When has this company ever consulted workers about anything? We're equipment to them. Interchangeable parts.",
          "expression_hint": "Fists clenched, face reddening",
          "q2_options": [
            {"text": "The union should have fought this. Where are they?"},
            {"text": "Are the workers going to do anything about it?"},
            {"text": "Is it true Bergström plans to sell the land commercially?"}
          ],
          "outcomes": [
            {"tier": 1, "response": "Pettersson at the union? He's useless. Shook his head, said 'it's management prerogative'. That's his answer to everything.", "expression": "hostile", "feedback": "Union abdicating responsibility but no unique angle.", "note": "Union boss said 'management prerogative'"},
            {"tier": 2, "response": "Some boys are talking about a work-to-rule protest. No overtime, no voluntary shifts, strict breaks. If they take our field, we take their flexibility.", "expression": "defiant", "feedback": "Workers planning collective action — potential followup story.", "note": "Workers planning work-to-rule protest"},
            {"tier": 1, "response": "Sell it? I wouldn't put it past him, but I don't know for sure. You'd have to check the land registry.", "expression": "guarded", "feedback": "Speculation only.", "note": "Doesn't know about commercial sale plans for certain"}
          ],
          "q1_note": "We're equipment to them, interchangeable parts"
        },
        "silence": {
          "q1_response": "...I'm nineteen. I started here because my dad worked here. He played on that field. And now they're killing it and nobody cares.",
          "expression_hint": "Voice breaking slightly, trying to hold it together",
          "q2_options": [
            {"text": "What would your dad say about this?"},
            {"text": "Why does nobody care? What's stopping people from fighting?"},
            {"text": "You care. That's why you're talking to me. What do you want people to know?"}
          ],
          "outcomes": [
            {"tier": 1, "response": "He'd say fight it. But he's not here anymore. Died in the mill two years ago. Heart attack on the factory floor. They sent flowers.", "expression": "guarded", "feedback": "Deeply personal but doesn't advance the field story.", "note": "Father died on the factory floor two years ago"},
            {"tier": 2, "response": "Because everyone's afraid. Afraid of losing shifts, afraid of being the troublemaker. Bergström doesn't fire you — he just gives you the worst assignments until you quit. That's how he works.", "expression": "nervous", "feedback": "Pattern of corporate intimidation. Strong context.", "note": "Bergström gives worst assignments to troublemakers until they quit"},
            {"tier": 3, "response": "I want them to know that this field was built by workers in 1935. With their own hands, on their own time. The company never paid for it. It's OUR field, not theirs. And I found the deed — it's registered to the Workers' Athletic Association, not to Ståhlbergs Stålverk. Bergström is selling land he doesn't own.", "expression": "open", "feedback": "Bombshell — the land is legally owned by the workers' association, not the company. Bergström has no right to sell it.", "note": "Deed shows field registered to Workers' Athletic Association, not the company"}
          ],
          "q1_note": "Nobody cares"
        }
      }
    },
    "headlines": {
      "tier_0": [
        {"text": "Workers' football field to close", "tone": "Factual"},
        {"text": "Factory expansion claims sports field", "tone": "Neutral"},
        {"text": "Apprentice upset about losing workers' pitch", "tone": "Personal"}
      ],
      "tier_1": [
        {"text": "Workers not consulted before field closure", "tone": "Questioning"},
        {"text": "Factory field: no overtime protest planned by workers", "tone": "Action"},
        {"text": "Father played here, now they're paving it — apprentice speaks out", "tone": "Personal"}
      ],
      "tier_2": [
        {"text": "Loading bay excuse? Real motive may be land sale", "tone": "Investigating"},
        {"text": "Workers fear retaliation if they protest field closure", "tone": "Labor rights"},
        {"text": "Bergström decides alone — workers learn from canteen wall", "tone": "Exposing"}
      ],
      "tier_3": [
        {"text": "LAND GRAB: Factory selling workers' field they don't legally own", "tone": "Sensational"},
        {"text": "Deed proves: sports field belongs to Workers' Athletic Association", "tone": "Evidence-based"},
        {"text": "Workers built it in 1935 — now Bergström claims it's his to sell", "tone": "Historical justice"}
      ]
    }
  },
  {
    "id": "veterandagen",
    "title": "The Veterans' Day",
    "description": "Retired factory workers' annual reunion reveals names that were erased from company history.",
    "lead_text": "They took our photos off the wall. Thirty years of service and now we don't exist.",
    "preview": "Handwritten letter from a retired worker, shaky handwriting.",
    "source_type": "letter",
    "difficulty": "easy",
    "base_value": 2,
    "category": "human_interest",
    "npc_id": "lennart_engstrom",
    "npc_name": "Lennart Engström",
    "npc_title": "Retired Mill Worker",
    "town": "industristad",
    "interview": {
      "opening_line": "Every year we meet at Folkets Hus. Fewer of us each time. But this year — they removed our photos from the factory hall. Thirty years of service portraits. Just gone.",
      "q1_options": [
        {"archetype": "friendly", "text": "That must hurt, Lennart. Those photos represent your life's work."},
        {"archetype": "direct", "text": "Who ordered the photos removed and why?"},
        {"archetype": "pressure", "text": "Is it true they're erasing workers who filed safety complaints?"},
        {"archetype": "silence", "text": "..."}
      ],
      "branches": {
        "friendly": {
          "q1_response": "Thirty-two years I gave to that mill. Started at sixteen. And now some new manager decides the entrance hall needs to be 'modernized'. Our faces don't fit the new image.",
          "expression_hint": "Holding a faded photograph of himself as a young worker",
          "q2_options": [
            {"text": "What happened to the photos? Were they destroyed?"},
            {"text": "How do the other retirees feel about this?"},
            {"text": "Did anyone from the company explain the decision?"}
          ],
          "outcomes": [
            {"tier": 2, "response": "I went to the factory to look. Found them in a skip behind the loading dock. Thirty years of portraits in a rubbish pile. I pulled mine out. And Göran's — he died last spring. His widow doesn't know yet. I can't tell her.", "expression": "open", "feedback": "Portraits literally trashed. Göran's widow angle adds devastating emotional weight.", "note": "Photos found in rubbish skip behind loading dock, including dead colleague's"},
            {"tier": 1, "response": "Åke is furious. Bengt won't stop talking about it. But we're old men. What are we going to do? Write an angry letter? We already did.", "expression": "guarded", "feedback": "Collective indignation but no news hook.", "note": "Retirees wrote angry letter, no response"},
            {"tier": 1, "response": "Nobody explained anything. I called the switchboard. They transferred me three times. Finally someone said 'the hall is being renovated'. Renovated. That's what they call throwing us away.", "expression": "defiant", "feedback": "Bureaucratic dismissal but no larger pattern.", "note": "Company said hall is being 'renovated'"}
          ],
          "q1_note": "Our faces don't fit the new image"
        },
        "direct": {
          "q1_response": "The new PR manager. Erika something. She's making the factory 'modern and forward-looking'. That's the actual quote from the newsletter.",
          "expression_hint": "Tapping the bench with his cane",
          "q2_options": [
            {"text": "Were all veteran photos removed, or only specific ones?"},
            {"text": "What's replacing the portraits?"},
            {"text": "Has the company acknowledged the veterans' service in any other way?"}
          ],
          "outcomes": [
            {"tier": 3, "response": "Only the ones from the union era. The old ones — from before the union was formed in '47 — those stayed. And the management portraits from every era. So workers who organized are erased. Workers who obeyed are kept. Managers forever. You see the pattern?", "expression": "defiant", "feedback": "Selective erasure — union-era workers removed, pre-union and management kept. Ideological purge of labor history.", "note": "Only union-era worker portraits removed, pre-union and management portraits kept"},
            {"tier": 1, "response": "Abstract art. Metal sculptures. 'Dynamic industry in motion' or some PR nonsense. Modern.", "expression": "hostile", "feedback": "Flavor detail but no news angle.", "note": "Replaced by abstract art and metal sculptures"},
            {"tier": 1, "response": "Acknowledged? They stopped the annual retirement dinner two years ago. No pension ceremony. No gold watch. You just... stop coming.", "expression": "guarded", "feedback": "Pattern of disrespect but thin for a story.", "note": "Annual retirement dinner cancelled two years ago"}
          ],
          "q1_note": "New PR manager making factory 'modern'"
        },
        "pressure": {
          "q1_response": "Safety complaints? I... I wouldn't know about that. I just know they took our pictures down. All of us. After decades.",
          "expression_hint": "Slightly rattled by the question",
          "q2_options": [
            {"text": "Lennart, I've heard that workers who challenged management are being erased from history. Is that what's happening?"},
            {"text": "Did you ever file a complaint during your years at the factory?"},
            {"text": "What happened to the workers who spoke up?"}
          ],
          "outcomes": [
            {"tier": 1, "response": "I don't know about 'erased'. They took down photos. It's disrespectful. That's all I know.", "expression": "guarded", "feedback": "He won't make the connection you're pushing for.", "note": "Doesn't connect photo removal to complaints"},
            {"tier": 2, "response": "I filed one. In 1961. About ventilation in the cutting room. They fixed it — took two years, but they fixed it. My photo was still up last year. Now it's gone.", "expression": "nervous", "feedback": "A complaint-filer whose portrait was removed. But he can't prove causation.", "note": "Filed safety complaint in 1961, photo removed"},
            {"tier": 1, "response": "Some got transferred. Some got the bad shifts. One man — Olle Falk — they promoted him to a job he didn't want, far from his family. He quit within a year. That was the point.", "expression": "neutral", "feedback": "Historical intimidation pattern but second-hand.", "note": "Workers who spoke up were transferred or promoted out"}
          ],
          "q1_note": "I wouldn't know about safety complaints"
        },
        "silence": {
          "q1_response": "...*looks down at his hands* These hands built that factory. Literally. I poured concrete for the eastern wing in '48. And now they throw my face in the rubbish.",
          "expression_hint": "Studying his weathered hands, profound sadness",
          "q2_options": [
            {"text": "What would you want young workers today to know?"},
            {"text": "What does this factory owe the people who built it?"},
            {"text": "Take your time, Lennart. I'm listening."}
          ],
          "outcomes": [
            {"tier": 1, "response": "That we existed. That real people, with real families, built every beam and poured every floor. We weren't just labor costs on a spreadsheet.", "expression": "open", "feedback": "Dignity statement. Moving but not news.", "note": "We existed, we weren't labor costs on a spreadsheet"},
            {"tier": 2, "response": "It owes us respect. And pensions that aren't being eroded by inflation while the directors get raises. Ingvar at the union — useless. He agreed to the pension freeze without telling us. We found out from the bank.", "expression": "defiant", "feedback": "Pension freeze agreed without worker consent — that's a story.", "note": "Union agreed to pension freeze without telling retirees"},
            {"tier": 3, "response": "*long silence* I brought something. *opens a worn folder* Every year-end bonus report from 1950 to 1972. The workers' share has gone from 12% of profits to 1.4%. In the same period, the board's share went from 3% to 18%. Every year they take more from us and give more to themselves. These photos? It's just the latest thing they've stolen.", "expression": "open", "feedback": "Twenty-two years of profit-sharing data showing systematic wealth transfer from workers to management. The photos are a symbol — the data is the story.", "note": "Year-end bonus: workers went from 12% to 1.4% of profits, board from 3% to 18%"}
          ],
          "q1_note": "These hands built that factory"
        }
      }
    },
    "headlines": {
      "tier_0": [
        {"text": "Retired workers upset over portrait removal", "tone": "Factual"},
        {"text": "Factory removes veteran portraits from hall", "tone": "Neutral"},
        {"text": "Retirees: 'Thirty years and now we don't exist'", "tone": "Quote-driven"}
      ],
      "tier_1": [
        {"text": "Factory throws veteran portraits in the skip", "tone": "Emotional"},
        {"text": "Retirement dinner cancelled, photos removed — veterans feel forgotten", "tone": "Pattern"},
        {"text": "Union agreed to pension freeze without asking retirees", "tone": "Revealing"}
      ],
      "tier_2": [
        {"text": "Only union-era workers erased — management portraits remain", "tone": "Exposing"},
        {"text": "Twenty years of declining worker bonuses while board pay rises", "tone": "Documented"},
        {"text": "Dead colleague's portrait found in rubbish skip", "tone": "Emotional impact"}
      ],
      "tier_3": [
        {"text": "DATA REVEALS: Worker profit share fell from 12% to 1.4% over 22 years", "tone": "Evidence-based"},
        {"text": "EXPOSED: Systematic wealth transfer — workers to boardroom, decade by decade", "tone": "Sensational"},
        {"text": "Retired worker's records prove: decades of shrinking worker rewards", "tone": "Investigative"}
      ]
    }
  },
  {
    "id": "strejkhotet",
    "title": "The Strike Threat",
    "description": "Paper mill workers threaten a symbolic one-day strike over broken overtime promises.",
    "lead_text": "They promised us time-and-a-half for weekend shifts. It's been six months. We got nothing.",
    "preview": "Anonymous letter from the paper mill union branch.",
    "source_type": "letter",
    "difficulty": "easy",
    "base_value": 3,
    "category": "labor",
    "npc_id": "folke_dahlberg",
    "npc_name": "Folke Dahlberg",
    "npc_title": "Senior Union Steward",
    "town": "industristad",
    "interview": {
      "opening_line": "Six months since the overtime agreement. Not a single extra krona. Management says 'administrative delays'. The boys are done waiting.",
      "q1_options": [
        {"archetype": "friendly", "text": "That's a long time to wait, Folke. How are the workers handling it?"},
        {"archetype": "direct", "text": "What exactly was agreed and do you have the signed agreement?"},
        {"archetype": "pressure", "text": "Some say the union leadership already took a deal and isn't telling the members. True?"},
        {"archetype": "silence", "text": "..."}
      ],
      "branches": {
        "friendly": {
          "q1_response": "They're angry. But quiet angry — the dangerous kind. Men with families who've been working every Saturday for six months without the pay they were promised.",
          "expression_hint": "Solid as a wall, controlled fury",
          "q2_options": [
            {"text": "What's the total unpaid overtime across all workers?"},
            {"text": "Have you confronted management about breaking the agreement?"},
            {"text": "What happens if the strike actually goes ahead?"}
          ],
          "outcomes": [
            {"tier": 2, "response": "I calculated it. 340 workers, average 4 unpaid weekend shifts each. At the agreed rate, the company owes roughly 680,000 kronor. That's money in workers' pockets that the company is sitting on.", "expression": "defiant", "feedback": "Hard number — 680,000 kronor owed. Concrete and publishable.", "note": "Company owes approximately 680,000 kronor in unpaid overtime"},
            {"tier": 1, "response": "Three times. Three meetings. Each time they say 'it's being processed'. Last time the HR director didn't even show up. Sent his secretary.", "expression": "hostile", "feedback": "Management contempt but no new angle.", "note": "Three meetings, HR director sent secretary"},
            {"tier": 1, "response": "If we strike, they'll bring in agency workers. They've done it before. We lose a day's pay and nothing changes.", "expression": "guarded", "feedback": "Strategic weakness admitted but not a news angle.", "note": "Strike risks replacement by agency workers"}
          ],
          "q1_note": "Quiet angry — the dangerous kind"
        },
        "direct": {
          "q1_response": "Signed agreement, March 15th. Time-and-a-half for all weekend and holiday shifts, effective April 1st. Signed by management and the union. I have my copy right here.",
          "expression_hint": "Pulls out a folded paper from his jacket",
          "q2_options": [
            {"text": "Can I photograph the agreement?"},
            {"text": "Who signed on behalf of management?"},
            {"text": "Has the union filed a formal dispute?"}
          ],
          "outcomes": [
            {"tier": 2, "response": "Here. Read it yourself. Clause 4, paragraph 2: 'All overtime hours worked on Saturdays, Sundays, and public holidays shall be compensated at 150% of the base hourly rate, effective April 1, 1974.' Crystal clear.", "expression": "defiant", "feedback": "Documentary proof of the broken agreement. The clause is unambiguous.", "note": "Clause 4, paragraph 2: 150% overtime rate effective April 1, 1974"},
            {"tier": 3, "response": "Rolf Bergström. Personally. His signature right there. And you know what I found out last week? Bergström sent a memo to payroll in June saying 'defer implementation until further notice'. He signed the agreement and then secretly told payroll not to honor it.", "expression": "open", "feedback": "Signed an agreement, then secretly blocked payment. Deliberate breach of contract with memo proof.", "note": "Bergström signed agreement then sent secret memo to payroll to 'defer implementation'"},
            {"tier": 1, "response": "Filed it two weeks ago. Central union says it could take months. That's why the boys want to strike — they can't wait for lawyers.", "expression": "neutral", "feedback": "Formal process underway but no dramatic revelation.", "note": "Formal dispute filed two weeks ago, could take months"}
          ],
          "q1_note": "Signed agreement, March 15th. Time-and-a-half"
        },
        "pressure": {
          "q1_response": "What? No. Absolutely not. I would never sell out my members. Where did you hear that?",
          "expression_hint": "Face darkens, steps closer",
          "q2_options": [
            {"text": "Workers I've spoken to say Pettersson at regional level made a side deal. Know anything about that?"},
            {"text": "If the union is clean, why has it taken this long to file a dispute?"},
            {"text": "I'm just asking the questions workers are asking, Folke. They need answers."}
          ],
          "outcomes": [
            {"tier": 2, "response": "*long pause* ...Pettersson told me to 'let it cool down'. Said that with the oil crisis, we can't push too hard. But that's not his decision. The agreement is signed. The law is on our side.", "expression": "defiant", "feedback": "Union leadership pressuring the local branch to back down. Internal conflict.", "note": "Regional union boss Pettersson told him to 'let it cool down'"},
            {"tier": 1, "response": "Because filing a dispute is a big step. You don't do it lightly. But we've done it now. And we're not backing down.", "expression": "hostile", "feedback": "Defensive answer. He's telling the truth but you rattled him for nothing.", "note": "Formal dispute now filed, not backing down"},
            {"tier": 1, "response": "Fine. Here's my answer: we fight for every krona, every time. That's what unions do. Anyone who says otherwise doesn't know me.", "expression": "hostile", "feedback": "A speech, not information.", "note": "Folke insists the union fights for every krona"}
          ],
          "q1_note": "I would never sell out my members"
        },
        "silence": {
          "q1_response": "...*studies you* You're new here, aren't you. Birgit's new reporter. Alright. I'll tell you what you need to know. But you have to understand something first — this isn't just about overtime.",
          "expression_hint": "Deciding whether to trust you",
          "q2_options": [
            {"text": "What is it about, then?"},
            {"text": "I'm listening. Take your time."},
            {"text": "What don't people understand about this dispute?"}
          ],
          "outcomes": [
            {"tier": 3, "response": "It's about whether agreements mean anything in this town. Bergström signs papers, shakes hands, takes photos for the newsletter. Then he does whatever he wants. The overtime is just the latest. Last year he promised safety equipment upgrades — nothing. Year before, he promised a daycare subsidy — nothing. I keep a list. Seventeen broken promises in five years. All documented.", "expression": "open", "feedback": "Seventeen documented broken promises in five years. This isn't about overtime — it's about institutional lying.", "note": "List of 17 broken management promises in 5 years, all documented"},
            {"tier": 2, "response": "Every time management breaks a promise and gets away with it, the workers lose a little more faith. In the company. In the union. In the system. This overtime fight — if we lose this one, the men will stop believing anything can change.", "expression": "open", "feedback": "The existential stakes for organized labor. Deep context but needs facts.", "note": "If workers lose this fight, they'll stop believing in the system"},
            {"tier": 1, "response": "People think unions are greedy. We're not greedy. We're asking for what was agreed. In writing. With signatures. That's not greed — that's contract law.", "expression": "defiant", "feedback": "Good quote but you already knew this.", "note": "Union asking for what was agreed in writing"}
          ],
          "q1_note": "This isn't just about overtime"
        }
      }
    },
    "headlines": {
      "tier_0": [
        {"text": "Paper mill workers threaten strike", "tone": "Factual"},
        {"text": "Overtime dispute at the paper mill", "tone": "Neutral"},
        {"text": "Workers say overtime pay not received", "tone": "Worker angle"}
      ],
      "tier_1": [
        {"text": "680,000 kronor owed — workers demand unpaid overtime", "tone": "Scale"},
        {"text": "Signed agreement ignored — strike looms at paper mill", "tone": "Tension"},
        {"text": "Regional union boss told local branch to stand down", "tone": "Revealing"}
      ],
      "tier_2": [
        {"text": "Management signed overtime deal — then secretly blocked payment", "tone": "Exposing"},
        {"text": "Director signed agreement, sent memo to payroll: 'defer'", "tone": "Documented"},
        {"text": "Workers calculate: company sitting on 680,000 kr of their wages", "tone": "Data-driven"}
      ],
      "tier_3": [
        {"text": "17 BROKEN PROMISES: Union steward's five-year record of management lies", "tone": "Sensational"},
        {"text": "EXPOSED: Director signed deals he never intended to honor — full list revealed", "tone": "Investigative"},
        {"text": "Five years, seventeen promises, zero kept — the Bergström pattern", "tone": "Pattern analysis"}
      ]
    }
  },
  {
    "id": "arbetarbostader",
    "title": "The Worker Housing",
    "description": "Families in the factory worker housing estate are getting sick from mold and damp.",
    "lead_text": "My two boys have had a cough since September. The walls in the bedroom are black with mold.",
    "preview": "Desperate letter from a mother, water stains on the paper.",
    "source_type": "letter",
    "difficulty": "easy",
    "base_value": 3,
    "category": "human_interest",
    "npc_id": "gunhild_persson_i",
    "npc_name": "Gunhild Persson",
    "npc_title": "Factory Worker's Wife",
    "town": "industristad",
    "interview": {
      "opening_line": "Come inside. See for yourself. I'm ashamed to show you but someone has to see what they make us live in.",
      "q1_options": [
        {"archetype": "friendly", "text": "You shouldn't be ashamed, Gunhild. How long has the mold been this bad?"},
        {"archetype": "direct", "text": "Who is responsible for maintaining these apartments?"},
        {"archetype": "pressure", "text": "These conditions are illegal. Has the housing company ever been inspected?"},
        {"archetype": "silence", "text": "..."}
      ],
      "branches": {
        "friendly": {
          "q1_response": "Since last winter. The pipes froze, something leaked inside the walls, and by spring the mold was everywhere. The bathroom. The bedroom. My boys' room. The doctor says it's making them sick.",
          "expression_hint": "Shows you the bedroom, black patches on walls",
          "q2_options": [
            {"text": "What did the doctor say exactly?"},
            {"text": "Have you reported it to the housing company?"},
            {"text": "Are other families in the building affected too?"}
          ],
          "outcomes": [
            {"tier": 1, "response": "Chronic bronchitis for both boys. The doctor said to 'improve ventilation'. How? The windows don't open properly and we can't afford to heat with them open.", "expression": "guarded", "feedback": "Medical confirmation but no accountability.", "note": "Both boys have chronic bronchitis, doctor said 'improve ventilation'"},
            {"tier": 2, "response": "Eleven times. I have carbon copies of every complaint. They sent a man once — he painted over the mold with white paint. It came back in two weeks. That was their 'repair'.", "expression": "defiant", "feedback": "Eleven documented complaints, cosmetic repair only. Pattern of neglect.", "note": "11 complaints, one repair: painted over mold, came back in 2 weeks"},
            {"tier": 3, "response": "The whole building. Fourteen apartments. Lena on the third floor — her daughter got asthma. Old Birger on the ground floor — he's been in hospital twice. And the new family, the Kovačevićs, they don't even know they can complain. They think this is normal. It's not normal.", "expression": "open", "feedback": "Building-wide health crisis. Hospital admissions. Immigrant family not knowing their rights. This is systemic.", "note": "14 apartments affected, child with asthma, elderly man hospitalized twice, immigrant family unaware of rights"}
          ],
          "q1_note": "Doctor says the mold is making the boys sick"
        },
        "direct": {
          "q1_response": "Industribostäder AB. A subsidiary of Ståhlbergs Stålverk. They own all the worker housing in Bruksgatan. My husband works at the steel mill — the apartment comes with the job.",
          "expression_hint": "Pulling apartment contract from a drawer",
          "q2_options": [
            {"text": "Can workers complain without risking their housing?"},
            {"text": "What does the lease say about maintenance responsibilities?"},
            {"text": "How much rent do you pay for these conditions?"}
          ],
          "outcomes": [
            {"tier": 2, "response": "That's the thing. If my husband makes trouble at the factory, we risk the apartment. They don't say it outright, but everyone knows. The housing IS the leash.", "expression": "nervous", "feedback": "Company housing as control mechanism. Workers can't complain without risking home AND job.", "note": "Housing used as control — complaining risks eviction"},
            {"tier": 1, "response": "The lease says 'landlord responsible for structural maintenance'. But there's a clause — 'tenant responsible for ventilation and surface condensation'. They use that clause to blame us for the mold.", "expression": "defiant", "feedback": "Contractual blame-shifting but expected.", "note": "Lease clause blames tenants for 'surface condensation'"},
            {"tier": 2, "response": "1,400 kronor a month. For a two-bedroom apartment with black mold, broken windows, and a bathroom where the tiles are falling off. Market rate for this area? Maybe 800. They overcharge us because we can't leave.", "expression": "defiant", "feedback": "Overcharging workers who can't leave. Captive market exploitation.", "note": "Paying 1,400 kr when market rate is 800, can't leave because housing tied to job"}
          ],
          "q1_note": "Housing company is subsidiary of Ståhlbergs Stålverk"
        },
        "pressure": {
          "q1_response": "Inspected? Nobody comes. We called the municipal health board once. They said they'd send someone. That was in March.",
          "expression_hint": "Clenching her coffee cup harder",
          "q2_options": [
            {"text": "Who at the health board did you speak to?"},
            {"text": "Would you let me bring a photographer to document the conditions?"},
            {"text": "What would happen if all fourteen families complained at once?"}
          ],
          "outcomes": [
            {"tier": 1, "response": "A woman named Ingrid. She sounded concerned on the phone. Then nothing. I called back in May — she'd been 'transferred to another department'.", "expression": "guarded", "feedback": "Municipal contact transferred. Possibly silenced. But speculative.", "note": "Health board contact transferred to another department"},
            {"tier": 2, "response": "You can photograph whatever you want. I have nothing to hide. Look at this wall. This ceiling. My boys' room. The world should see how Bergström's workers live.", "expression": "defiant", "feedback": "Open access for documentation. Photos would make this story visceral.", "note": "Open to full photo documentation of conditions"},
            {"tier": 1, "response": "Some are too scared. The Lindqvists just had a baby. They can't risk losing the apartment. We tried to organize — Ulla from the tenant association helped — but most people signed anonymously.", "expression": "nervous", "feedback": "Fear prevents collective action. The system working as designed.", "note": "Most families too scared to complain openly"}
          ],
          "q1_note": "Nobody inspects these apartments"
        },
        "silence": {
          "q1_response": "...*sets down the cup, walks you to the children's room* Look at this wall. My boys sleep here. Every night. In this. And I can't do anything about it.",
          "expression_hint": "Standing in the doorway, fists clenched",
          "q2_options": [
            {"text": "Why can't you do anything?"},
            {"text": "What would it take to fix this properly?"},
            {"text": "What do the boys say about their room?"}
          ],
          "outcomes": [
            {"tier": 2, "response": "Because if I push too hard, Erik loses his shifts. And if he loses shifts, we can't pay rent. And if we can't pay rent, we lose the apartment AND the job. The whole thing is a trap.", "expression": "nervous", "feedback": "The complete control system exposed: housing tied to job tied to silence.", "note": "Push too hard → lost shifts → can't pay rent → lose apartment AND job"},
            {"tier": 3, "response": "A plumber told me — in secret, because he works for Industribostäder — that the building needs complete pipe replacement. Cost: about 40,000 kronor per apartment. 14 apartments, that's 560,000. But last year the company's annual report showed 2.3 million in profit. They can afford it. They choose not to.", "expression": "open", "feedback": "The fix costs 560,000 kr. The company made 2.3 million profit. They choose to let children get sick. Devastating.", "note": "Pipe replacement costs 560,000 kr, company profit was 2.3 million — they choose not to fix it"},
            {"tier": 1, "response": "My youngest asks why they cough so much. He asks if he's sick. I say no, it's just the cold weather. I lie. Every night I lie to my children.", "expression": "open", "feedback": "Heartbreaking but not a news hook on its own.", "note": "Mother lies to children about why they're sick"}
          ],
          "q1_note": "I can't do anything about it"
        }
      }
    },
    "headlines": {
      "tier_0": [
        {"text": "Families report mold in worker housing", "tone": "Factual"},
        {"text": "Children sick in Bruksgatan apartments", "tone": "Human interest"},
        {"text": "Tenants complain about housing conditions", "tone": "Neutral"}
      ],
      "tier_1": [
        {"text": "11 complaints, one 'repair': housing company painted over mold", "tone": "Pattern"},
        {"text": "Health board contact transferred after housing complaint", "tone": "Questioning"},
        {"text": "Workers overcharged for substandard housing they can't leave", "tone": "Exploitation"}
      ],
      "tier_2": [
        {"text": "Company housing used as control — workers who complain risk eviction", "tone": "Exposing"},
        {"text": "14 apartments, mold everywhere — photos document the misery", "tone": "Visual evidence"},
        {"text": "Plumber reveals: building needs complete pipe replacement", "tone": "Expert source"}
      ],
      "tier_3": [
        {"text": "Children sick, 2.3M profit — company chooses not to fix worker housing", "tone": "Sensational"},
        {"text": "EXPOSED: 560,000 kr fix, 2.3 million profit — Industribostäder lets families suffer", "tone": "Data contrast"},
        {"text": "The trap: company housing ties workers to silence while children get sick", "tone": "Investigative"}
      ]
    }
  }
]

# Read existing stories and append
with open('data/stories.json', 'r') as f:
    all_stories = json.load(f)

# Remove existing Industristad stories (idempotent)
all_stories = [s for s in all_stories if s.get('town') != 'industristad']
all_stories.extend(stories)

with open('data/stories.json', 'w') as f:
    json.dump(all_stories, f, indent=2, ensure_ascii=False)

print(f"Batch 1 complete: {len(stories)} stories added")
print(f"Total stories: {len(all_stories)} (Småstad: {len([s for s in all_stories if s.get('town')=='smastad'])}, Industristad: {len([s for s in all_stories if s.get('town')=='industristad'])})")
