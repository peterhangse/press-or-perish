#!/usr/bin/env python3
"""Generate Industristad stories batch 2: 1×bv3 + 9×bv4 (medium-easy)"""
import json, os

STORIES = [
{
  "id": "kontorsfesten",
  "title": "The Office Party",
  "description": "The steel mill's annual Christmas party cost more than workers earn in a month.",
  "lead_text": "Someone left the party receipt on the canteen table. Three thousand kronor on champagne alone.",
  "preview": "A factory clerk catches your eye near the post office, holding something.",
  "source_type": "document",
  "difficulty": "easy",
  "base_value": 3,
  "category": "corruption",
  "npc_id": "per_olov_strand",
  "npc_name": "Per-Olov Strand",
  "npc_title": "Assistant Accountant, Ståhlbergs Stålverk",
  "town": "industristad",
  "interview": {
    "opening_line": "I found this on my desk. I think it was left there by mistake. The numbers... look at the numbers.",
    "q1_options": [
      {"archetype": "friendly", "text": "That must have been quite a shock, Per-Olov. Walk me through what you see."},
      {"archetype": "direct", "text": "What's the total? Who signed off on it?"},
      {"archetype": "pressure", "text": "Is the company laundering money through these parties?"},
      {"archetype": "silence", "text": "..."}
    ],
    "branches": {
      "friendly": {
        "q1_response": "I've worked here nine years. Our Christmas bonus was canceled this year. 'Austerity,' they said. Then they spent more on a single party than I make in a month.",
        "expression_hint": "Shaking his head, bitter disbelief",
        "q2_options": [
          {"text": "What exactly was on the receipt? Can you list the items?"},
          {"text": "Who attended this party? Was it management only?"},
          {"text": "Has this happened before, or is this the first time?"}
        ],
        "outcomes": [
          {"tier": 1, "response": "Champagne, imported cheese, cigars. It was a management dinner at Hotel Strandberg. Maybe twenty people.", "expression": "guarded", "feedback": "Basic party details confirmed but nothing specifically damning.", "note": "Management dinner at Hotel Strandberg"},
          {"tier": 2, "response": "Three thousand kronor on champagne. Seven hundred on cigars. They rented a private dining room at Hotel Strandberg. The same month they cut the workers' Christmas bonus of 200 kronor — 'too expensive,' they said.", "expression": "open", "feedback": "Specific contrast between executive spending and worker austerity. Publishable comparison.", "note": "3000 kr champagne vs 200 kr bonus cut"},
          {"tier": 3, "response": "Here's the thing — the receipt was coded as 'equipment maintenance.' I checked the ledger. The last three quarters, 'equipment maintenance' has doubled. I think they've been hiding entertainment costs in the maintenance budget.", "expression": "open", "feedback": "Accounting fraud — entertainment disguised as equipment costs. This is bigger than a party.", "note": "Entertainment hidden as 'equipment maintenance'"}
        ],
        "q1_note": "Bonus canceled same year as lavish party"
      },
      "direct": {
        "q1_response": "Twelve thousand kronor total. Director Bergström signed it. But here's the strange part — it's coded as 'equipment inspection dinner.' There was no inspection.",
        "expression_hint": "Tapping the paper nervously",
        "q2_options": [
          {"text": "Can I see the receipt? I need to verify the figures."},
          {"text": "How does a twelve-thousand-kronor dinner get coded as equipment inspection?"},
          {"text": "Are there more receipts like this? Is this a pattern?"}
        ],
        "outcomes": [
          {"tier": 1, "response": "I can't give it to you — they'd know it was me. But the total was twelve thousand, signed by Bergström on December 8th.", "expression": "guarded", "feedback": "Verbal confirmation only — no document. Hard to publish without proof.", "note": "12,000 kr signed by Bergström, Dec 8"},
          {"tier": 2, "response": "Here, look — 'Equipment Inspection Dinner, 12,340 kr.' The inspection line doesn't exist in the schedule. I checked. They invented a reason to expense it.", "expression": "open", "feedback": "Document with fabricated justification. Clear paper trail.", "note": "Fictitious inspection used to justify expense"},
          {"tier": 3, "response": "I pulled four more. Same pattern every quarter — 'equipment inspection,' 'safety review dinner,' 'board consultation.' If you add them up, that's almost 50,000 kronor in fake dinners this year alone. While 300 workers lost their bonus.", "expression": "open", "feedback": "Systematic fraud with multiple documents. Front-page material.", "note": "50,000 kr in fake dinners across four quarters"}
        ],
        "q1_note": "12,000 kr coded as 'equipment inspection'"
      },
      "pressure": {
        "q1_response": "Laundering? I didn't say — I mean, it's creative accounting, not... Look, I just thought someone should know.",
        "expression_hint": "Pulling back, alarmed",
        "q2_options": [
          {"text": "I'm sorry. Let's slow down. What does the receipt actually show?"},
          {"text": "Creative accounting is a crime too, Per-Olov. What are you afraid of?"},
          {"text": "If this goes deeper, wouldn't you want someone to expose it?"}
        ],
        "outcomes": [
          {"tier": 1, "response": "It shows a party. An expensive party. That's all I know for certain.", "expression": "guarded", "feedback": "He retreated. You got the minimum — an expensive party exists.", "note": "Expensive party confirmed, no details"},
          {"tier": 2, "response": "Fine. Yes, I think there's something wrong. The receipt is coded as equipment maintenance. There was no maintenance. Bergström signs these every quarter.", "expression": "guarded", "feedback": "Pressure rattled him but he cracked. You got the miscoding angle.", "note": "Quarterly miscoded expenses, Bergström signs"},
          {"tier": 3, "response": "I'll tell you what I'm afraid of — that I'll end up like Sjögren in accounts. He asked too many questions and was 'restructured' out. But yes, it's a pattern. Every quarter. And it's not just parties — there are supplier invoices from companies that don't seem to exist.", "expression": "open", "feedback": "Ghost suppliers and retribution — this is systematic fraud. He broke through the fear.", "note": "Non-existent supplier invoices, previous questioner fired"}
        ],
        "q1_note": "He got scared — may be bigger than a party"
      },
      "silence": {
        "q1_response": "... You're not going to say anything? Fine. Maybe I was stupid to come here. It's just... twelve thousand kronor. We lost our bonuses, you know.",
        "expression_hint": "Shuffling the paper, talking to himself as much as you",
        "q2_options": [
          {"text": "Twelve thousand. That's a lot of bonuses."},
          {"text": "You came here for a reason, Per-Olov."},
          {"text": "What would happen if Bergström knew you had this?"}
        ],
        "outcomes": [
          {"tier": 1, "response": "Sixty bonuses. Sixty families. They could have had Christmas money instead of this party. That's the story, isn't it?", "expression": "open", "feedback": "Emotional angle but no evidence of wrongdoing beyond bad taste.", "note": "12,000 kr = 60 worker bonuses"},
          {"tier": 2, "response": "I came because it's wrong. And because this receipt says 'equipment maintenance' but it was a party. If that's not lying, what is?", "expression": "open", "feedback": "He found his conviction. The miscoding angle gives you something concrete.", "note": "Receipt miscoded — party as 'equipment maintenance'"},
          {"tier": 3, "response": "He'd fire me. Like he fired Sjögren. But you know what? Sjögren was right to ask questions. There are more receipts. Supplier invoices to addresses that are just empty lots. I've been keeping copies.", "expression": "open", "feedback": "He trusts the silence. Copies of fraudulent invoices — documentary evidence.", "note": "Copies of fraudulent supplier invoices kept"}
        ],
        "q1_note": "Twelve thousand kronor, sixty lost bonuses"
      }
    }
  },
  "headlines": [
    {"text": "Steel Mill Christmas Party Exceeds Worker Bonuses", "tone": "Factual"},
    {"text": "Champagne for Bosses While Workers Lose Bonus", "tone": "Confrontational"},
    {"text": "HIDDEN RECEIPTS: Mill's Party Budget Coded as 'Equipment'", "tone": "Exposing"}
  ]
},

{
  "id": "nattskiftet",
  "title": "The Night Shift",
  "description": "Night shift workers at the rolling mill say safety lights have been off for weeks.",
  "lead_text": "We work in the dark. One guy slipped on the grating last week. Foreman says it's a 'temporary situation.'",
  "preview": "A steelworker flags you down at the bus stop, still in overalls.",
  "source_type": "street",
  "difficulty": "medium",
  "base_value": 4,
  "category": "labor",
  "npc_id": "erik_svensson_i",
  "npc_name": "Erik Svensson",
  "npc_title": "Rolling Mill Operator",
  "town": "industristad",
  "interview": {
    "opening_line": "You from the paper? Good. Someone needs to write about this before someone dies.",
    "q1_options": [
      {"archetype": "friendly", "text": "I appreciate you speaking up, Erik. Tell me what's happening on the night shift."},
      {"archetype": "direct", "text": "How long have the safety lights been out? Which sections?"},
      {"archetype": "pressure", "text": "If someone gets killed, the company will say you never reported it. Did you?"},
      {"archetype": "silence", "text": "..."}
    ],
    "branches": {
      "friendly": {
        "q1_response": "Three weeks. The overhead lights in sections C and D went out. We reported it. Nothing happened. Then Krister Holm slipped on the grating Tuesday — fell two meters onto concrete.",
        "expression_hint": "Clenching his jaw, looking down",
        "q2_options": [
          {"text": "Is Krister okay? What happened after the fall?"},
          {"text": "Did anyone document the reports you made?"},
          {"text": "What did the foreman say when you reported it?"}
        ],
        "outcomes": [
          {"tier": 1, "response": "Krister bruised his ribs. Foreman told him to take a couple days off — but not to file a workplace injury report. Said it was 'Krister's own carelessness.'", "expression": "open", "feedback": "Victim exists but you only got the verbal cover-up angle.", "note": "Foreman blocked injury report, blamed worker"},
          {"tier": 2, "response": "Krister cracked two ribs. He went to Dr. Lindqvist at the health center — there's a medical record. But the foreman told him not to file a workplace injury claim. And we have a logbook entry from two weeks ago reporting the lights.", "expression": "open", "feedback": "Medical record plus written safety complaint — two documents that contradict the cover-up.", "note": "Medical record + logbook entry from 2 weeks ago"},
          {"tier": 3, "response": "Here's what you need to know — Krister isn't the first. Nils Forsberg fell in September. Same section, same darkness. His injury report was filed but then disappeared from the records. And the lights were reported broken in August. Three months, nothing done.", "expression": "open", "feedback": "Pattern of injuries plus vanishing reports. Systematic negligence.", "note": "Second worker fell in Sept, report disappeared, lights broken since Aug"}
        ],
        "q1_note": "Krister Holm fell two meters in the dark"
      },
      "direct": {
        "q1_response": "Sections C and D of the rolling mill. Three weeks now. We put in a maintenance request on October 28th. Reference number 74-382. Nothing happened.",
        "expression_hint": "Steady eye contact, counting on fingers",
        "q2_options": [
          {"text": "Who handles maintenance requests? Where does 74-382 go?"},
          {"text": "Have there been any injuries in those sections since the lights went out?"},
          {"text": "Is there a safety inspector assigned to the rolling mill?"}
        ],
        "outcomes": [
          {"tier": 1, "response": "Goes to the maintenance department, then to the production manager for approval. Ours is Henriksson. He approves or rejects. We never heard back.", "expression": "guarded", "feedback": "You know the chain of command but not why it stalled.", "note": "Maintenance request to Henriksson, no response"},
          {"tier": 2, "response": "Henriksson is the production manager. He rejected the request — marked it 'non-critical.' I have a copy. And yes, Krister Holm fell Tuesday. Cracked ribs. Medical record exists at the health center.", "expression": "open", "feedback": "The rejection document plus medical evidence. Strong factual case.", "note": "Request rejected as 'non-critical', injury documented"},
          {"tier": 3, "response": "Henriksson rejected it as 'non-critical.' But I checked — the budget line for safety maintenance was diverted to production targets last quarter. The money for lights went to keeping the furnace running an extra shift. And the safety inspector? He hasn't visited since June. I have the visitors' log.", "expression": "open", "feedback": "Budget diversion from safety to production plus absent inspectors. Systemic.", "note": "Safety budget diverted to production, no inspector visit since June"}
        ],
        "q1_note": "Request 74-382, sections C and D"
      },
      "pressure": {
        "q1_response": "Reported it? Of course we reported it! I have the damn reference number memorized — 74-382. Filed October 28th. What more do you want?",
        "expression_hint": "Angry, stabbing finger toward factory",
        "q2_options": [
          {"text": "Good — you did the right thing. What happened after you filed it?"},
          {"text": "So if you reported it, why is the company pretending you didn't?"},
          {"text": "Who specifically ignored request 74-382?"}
        ],
        "outcomes": [
          {"tier": 1, "response": "Nothing happened. That's the point. Three weeks, nothing. And then Krister fell.", "expression": "guarded", "feedback": "Clear timeline but no documentation of the cover-up.", "note": "Three weeks ignored, then injury"},
          {"tier": 2, "response": "Because Henriksson rejected it. Stamped it 'non-critical.' A rolling mill in the dark — 'non-critical.' One week later, Krister Holm cracks his ribs. And Henriksson tells him not to file an injury report.", "expression": "open", "feedback": "Named decision-maker plus injury suppression. Good story.", "note": "Henriksson stamped 'non-critical', then blocked injury report"},
          {"tier": 3, "response": "Henriksson. But he's following orders. The production targets went up 15% last quarter. Safety budget got raided to fund overtime. They're literally spending the light money on keeping the furnace hot. And the county safety inspector? Bergström plays golf with him. Last inspection was a phone call.", "expression": "open", "feedback": "Systemic — production over safety, inspector corruption. Major story.", "note": "Safety budget raided for production, inspector compromised"}
        ],
        "q1_note": "Filed report, reference 74-382"
      },
      "silence": {
        "q1_response": "... You're just going to stand there? Fine. I'll tell you anyway. Krister Holm fell two meters in the dark on Tuesday. Cracked ribs. Nobody cares.",
        "expression_hint": "Searching your face, then looking away",
        "q2_options": [
          {"text": "Tell me about Krister."},
          {"text": "You said nobody cares. Who specifically should care?"},
          {"text": "..."}
        ],
        "outcomes": [
          {"tier": 1, "response": "Good man. Twenty years at the mill. Slipped on the grating because you can't see your own feet in sections C and D. Foreman blamed him.", "expression": "open", "feedback": "Human story but thin on evidence.", "note": "Twenty-year veteran, foreman blamed him"},
          {"tier": 2, "response": "Krister's at home now. Wife says he can barely breathe. Doctor documented cracked ribs. But the company won't file an injury report because then the safety statistics look bad before the county review.", "expression": "open", "feedback": "Connected the cover-up to the county review — motive established.", "note": "Injury suppressed before county safety review"},
          {"tier": 3, "response": "It's not just Krister. Nils Forsberg fell in September. Same spot. Same darkness. His report was filed — and then it vanished. I started keeping copies after that. I have three months of maintenance requests that went nowhere. All stamped 'non-critical' by Henriksson.", "expression": "open", "feedback": "Pattern of vanishing reports plus copies of evidence. He's been building a file.", "note": "Multiple vanishing reports, worker keeping copies"}
        ],
        "q1_note": "Krister Holm fell, nobody cares"
      }
    }
  },
  "headlines": [
    {"text": "Night Shift Workers Report Safety Light Failures", "tone": "Factual"},
    {"text": "Worker Falls in Darkened Mill — Company Blocks Injury Report", "tone": "Confrontational"},
    {"text": "SAFETY BUDGET RAIDED: Mill Spent Light Money on Production", "tone": "Exposing"}
  ]
},

{
  "id": "fackavgiften",
  "title": "The Union Dues",
  "description": "A union member questions where the local chapter's fees are actually going.",
  "lead_text": "Fifty kronor a month. Four hundred members. That's a lot of money with nothing to show for it.",
  "preview": "An anonymous letter left at the newspaper office, handwritten on lined paper.",
  "source_type": "letter",
  "difficulty": "medium",
  "base_value": 4,
  "category": "corruption",
  "npc_id": "maj_britt_karlsson",
  "npc_name": "Maj-Britt Karlsson",
  "npc_title": "Shop Steward, Paper Mill",
  "town": "industristad",
  "interview": {
    "opening_line": "I wrote to you because I've tried everything else. The local chapter won't answer my questions about the money.",
    "q1_options": [
      {"archetype": "friendly", "text": "That's frustrating, Maj-Britt. What questions are they refusing to answer?"},
      {"archetype": "direct", "text": "How much are we talking about? Where should the money be going?"},
      {"archetype": "pressure", "text": "Is the chapter chairman stealing from the members?"},
      {"archetype": "silence", "text": "..."}
    ],
    "branches": {
      "friendly": {
        "q1_response": "The solidarity fund. Every member pays fifty kronor a month. Four hundred members. That's twenty thousand a month, two hundred forty thousand a year. Where does it go? I asked at the last meeting. Göransson told me to 'trust the process.'",
        "expression_hint": "Leaning forward, hands on the table",
        "q2_options": [
          {"text": "Have you seen any financial statements or annual reports from the chapter?"},
          {"text": "What should the solidarity fund be paying for?"},
          {"text": "How did other members react when you asked?"}
        ],
        "outcomes": [
          {"tier": 1, "response": "No financial statements. They say they file them with the regional office. I called the regional office — they said the local chapter handles its own reporting. Everyone points somewhere else.", "expression": "open", "feedback": "Classic runaround but no concrete evidence of misuse.", "note": "No financial statements available, circular accountability"},
          {"tier": 2, "response": "The fund is supposed to cover strike support, legal aid, and member education. But there hasn't been a training session in two years. No strike fund has been paid out. And Göransson just bought a summer cottage on Öland. On a shop floor salary.", "expression": "open", "feedback": "The chairman's new property versus frozen fund activities. Circumstantial but newsworthy.", "note": "No fund activity in 2 years, chairman bought summer cottage"},
          {"tier": 3, "response": "I got a look at the bank statements. A friend at Handelsbanken. There are regular withdrawals — cash — by Göransson himself. Three, four thousand at a time. And the 'conference expenses' line? The last three conferences were at a resort hotel. Göransson went alone.", "expression": "open", "feedback": "Bank records showing cash withdrawals plus fake conference expenses. Documentary proof.", "note": "Cash withdrawals by chairman, fake conference expenses"}
        ],
        "q1_note": "240,000 kr/year, no accounting"
      },
      "direct": {
        "q1_response": "Two hundred forty thousand kronor a year. Fifty per member, four hundred members. It's supposed to go to the solidarity fund — strike support, legal aid, training. Nothing's been spent on any of that since '72.",
        "expression_hint": "Counting on fingers with precision",
        "q2_options": [
          {"text": "That's almost half a million in two years with no spending. Where's the money sitting?"},
          {"text": "Who controls the fund? Is there a board or just one person?"},
          {"text": "Have you requested an audit from the regional office?"}
        ],
        "outcomes": [
          {"tier": 1, "response": "Göransson controls it. He's chairman, treasurer, and signatory. Nobody else has access. I asked for an audit and was told 'the books are in order.'", "expression": "guarded", "feedback": "One-man control with no oversight. Structural problem confirmed.", "note": "Göransson sole controller, no audit allowed"},
          {"tier": 2, "response": "I requested an audit. Göransson said the regional office handles it. The regional office said they don't audit local funds. So I went to Handelsbanken myself. The account balance doesn't match what it should be. It's about 180,000 kronor short.", "expression": "open", "feedback": "180,000 kronor gap in the fund. That's embezzlement territory.", "note": "180,000 kr missing from solidarity fund"},
          {"tier": 3, "response": "Here's what I found — the account balance is 58,000 kronor. After two years of collecting 240,000 annually with zero legitimate expenses, it should be close to half a million. And the withdrawals are all in Göransson's name. Cash. No receipts filed.", "expression": "open", "feedback": "Documented gap of ~400,000 kr with cash withdrawals traced to one person. Iron-clad.", "note": "58,000 in account vs ~480,000 expected, all cash withdrawals by Göransson"}
        ],
        "q1_note": "240,000/year, nothing spent since '72"
      },
      "pressure": {
        "q1_response": "Stealing? That's... I mean, I don't want to say that. But something is very wrong. The numbers don't add up. And Göransson gets very angry when anyone asks.",
        "expression_hint": "Struggling between loyalty and honesty",
        "q2_options": [
          {"text": "I understand the hesitation. What specifically doesn't add up?"},
          {"text": "What happens when someone asks? Has anyone been retaliated against?"},
          {"text": "Göransson's anger — is it because the answer would be damaging?"}
        ],
        "outcomes": [
          {"tier": 1, "response": "Four hundred members paying fifty kronor. No workshops, no strike fund payouts, no legal aid. The money goes in. Nothing comes out. That's what doesn't add up.", "expression": "guarded", "feedback": "The math problem is clear but she pulled back from the accusation.", "note": "Money flows in, nothing visible comes out"},
          {"tier": 2, "response": "Lena Forsberg asked at the September meeting. Next week, her shift was changed to nights. Her husband works days. Now they never see each other. Göransson didn't say it was punishment. He didn't have to.", "expression": "open", "feedback": "Retaliation against a questioner. The fear is part of the story.", "note": "Member's shift changed after questioning finances"},
          {"tier": 3, "response": "Two people have asked. Both got their shifts changed. And I heard from someone at Handelsbanken — the account is nearly empty. Almost half a million should be in there. It's not. You do the math.", "expression": "open", "feedback": "Retaliation pattern plus a near-empty account. The union is being robbed.", "note": "Account nearly empty, two questioners retaliated against"}
        ],
        "q1_note": "Something very wrong with the money"
      },
      "silence": {
        "q1_response": "... I know what you're thinking. Why would a union member go to the press? Because the union won't listen. My own union.",
        "expression_hint": "Voice cracking slightly",
        "q2_options": [
          {"text": "That must feel like a betrayal."},
          {"text": "What did you try before coming here?"},
          {"text": "..."}
        ],
        "outcomes": [
          {"tier": 1, "response": "I wrote to the regional office. They said to take it up at the local meeting. I did. Göransson told me I was 'undermining solidarity.' The irony, right?", "expression": "open", "feedback": "She's been stonewalled but only has the runaround story.", "note": "Regional office deflected, chairman called her disloyal"},
          {"tier": 2, "response": "I asked at meetings. I wrote to the region. I even tried to look at the books. Göransson keeps them in a locked drawer in his office. But his neighbor told me about the summer cottage. And the boat. On a paper mill worker's salary.", "expression": "open", "feedback": "Lifestyle doesn't match income. The circumstantial case builds.", "note": "Chairman has summer cottage and boat on factory salary"},
          {"tier": 3, "response": "I went to everyone. Nobody wanted to hear it. So I started keeping records myself. Every month's dues, every member's payment. Compare that to the bank balance — a friend checked for me. Almost 400,000 kronor has vanished. I have it all written down.", "expression": "open", "feedback": "She built her own audit. Hand-written evidence of 400,000 kr missing.", "note": "Self-conducted audit shows ~400,000 kr missing, documented"}
        ],
        "q1_note": "Union won't listen, went to the press"
      }
    }
  },
  "headlines": [
    {"text": "Union Members Question Solidarity Fund Spending", "tone": "Cautious"},
    {"text": "240,000 Kronor a Year — No Accounting, No Answers", "tone": "Fact-based"},
    {"text": "UNION BOSS'S COTTAGE: Where Did the Dues Go?", "tone": "Exposing"}
  ]
},

{
  "id": "skolgarden",
  "title": "The Schoolyard",
  "description": "Parents near the Ståhlberg steel mill worry about dust settling on the school playground.",
  "lead_text": "My daughter comes home with grey dust in her hair every day. The school is 200 meters from the slag heap.",
  "preview": "A concerned woman approaches you outside the school gates, holding a child's hand.",
  "source_type": "street",
  "difficulty": "medium",
  "base_value": 4,
  "category": "environment",
  "npc_id": "astrid_lindkvist",
  "npc_name": "Astrid Lindkvist",
  "npc_title": "Parent, Bruksskolan PTA",
  "town": "industristad",
  "interview": {
    "opening_line": "Look at her hair. See the grey? That's not dirt. That's from the factory. And they play outside every day.",
    "q1_options": [
      {"archetype": "friendly", "text": "That's alarming, Astrid. How long has this been going on?"},
      {"archetype": "direct", "text": "Is it metal dust? Has anyone tested it?"},
      {"archetype": "pressure", "text": "Are the children getting sick? Is the school covering it up?"},
      {"archetype": "silence", "text": "..."}
    ],
    "branches": {
      "friendly": {
        "q1_response": "Since they expanded the slag heap in the spring. The wind carries it right over. Little Maja coughs every night now. And she's not the only one — half the kids in her class have the same cough.",
        "expression_hint": "Stroking her daughter's hair protectively",
        "q2_options": [
          {"text": "Have other parents complained? What does the school say?"},
          {"text": "Has a doctor looked at the coughing children?"},
          {"text": "How close is the slag heap to the playground exactly?"}
        ],
        "outcomes": [
          {"tier": 1, "response": "The school says it's autumn colds. Normal, they say. But it's not normal. It started when the slag heap got bigger. We all see it.", "expression": "open", "feedback": "Concerned parent testimony but no medical or environmental evidence.", "note": "School dismisses coughing as autumn colds"},
          {"tier": 2, "response": "Dr. Lindqvist at the health center has seen seven children this month with 'respiratory irritation.' Same class, same school. She won't say it's the dust on the record, but she told me privately it's not normal.", "expression": "open", "feedback": "Doctor sees the pattern. Off-the-record medical opinion strengthens the case.", "note": "7 children with respiratory issues, Dr. Lindqvist sees pattern"},
          {"tier": 3, "response": "I collected dust from the playground in a jar. Brought it to the pharmacy — the pharmacist said it looks like it contains heavy metals. And the headmaster? He got a letter from Ståhlbergs last month asking him not to 'alarm parents unnecessarily.' I saw a copy.", "expression": "open", "feedback": "Physical evidence plus corporate pressure on the school. The company knew.", "note": "Dust contains heavy metals, Ståhlbergs pressured headmaster to stay quiet"}
        ],
        "q1_note": "Slag heap expanded, children coughing"
      },
      "direct": {
        "q1_response": "Nobody's tested it. That's the problem. The slag heap is 200 meters from the school. The wind blows from the west — straight over the playground — about three days a week. And the dust settles on everything.",
        "expression_hint": "Pointing toward the factory stack visible above rooftops",
        "q2_options": [
          {"text": "Has the school or the municipality measured air quality?"},
          {"text": "What's in a slag heap? Could it be toxic?"},
          {"text": "Who owns the land between the school and the factory?"}
        ],
        "outcomes": [
          {"tier": 1, "response": "No measurements. The municipality says the factory has all required permits. End of discussion, as far as they're concerned.", "expression": "guarded", "feedback": "Municipality hiding behind permits. Bureaucratic deflection.", "note": "Municipality says factory has permits, no measurements done"},
          {"tier": 2, "response": "The municipality hasn't measured anything. But I found out the school was built in 1962 — before the slag heap existed. The heap started in '68, expanded in '73. No environmental review was done when they expanded it. I checked.", "expression": "open", "feedback": "The school came first. No review when slag heap expanded. Procedural failure.", "note": "No environmental review when slag heap expanded near school"},
          {"tier": 3, "response": "No review was done. And here's why — the land between the school and the slag heap belongs to Ståhlbergs. They donated it to the municipality in '61 to build the school. Then they built the slag heap 200 meters away. The municipality can't complain about their biggest taxpayer.", "expression": "open", "feedback": "The school is on company land. The municipality is trapped. Structural corruption.", "note": "School on donated Ståhlbergs land, municipality can't challenge them"}
        ],
        "q1_note": "Slag heap 200m from school, no testing"
      },
      "pressure": {
        "q1_response": "Sick? My Maja coughs every night. But covering it up? The school isn't evil — they're scared. Ståhlbergs employs half the parents. Nobody wants to make a fuss.",
        "expression_hint": "Lowering her voice, glancing at other parents",
        "q2_options": [
          {"text": "What are the parents afraid of specifically?"},
          {"text": "Has the school been told not to raise concerns?"},
          {"text": "If the factory employs the parents, who protects the children?"}
        ],
        "outcomes": [
          {"tier": 1, "response": "Afraid of rocking the boat. My husband works at the mill. If I make noise, what happens to his job? That's what everyone thinks.", "expression": "guarded", "feedback": "The fear is real but it's just a parent's worry, not evidence.", "note": "Parents afraid for jobs at the mill"},
          {"tier": 2, "response": "The headmaster got a call from Bergström's office. 'Don't create unnecessary alarm.' I know because I was in the office when it happened. The headmaster went white.", "expression": "open", "feedback": "Direct corporate pressure on a public school. That's the story.", "note": "Bergström's office called headmaster: 'don't create alarm'"},
          {"tier": 3, "response": "Bergström's office called the headmaster AND the health center. 'Don't create alarm.' Dr. Lindqvist was told not to link the children's symptoms to the factory. I know because she told me — off the record. She's terrified too. Everyone is.", "expression": "open", "feedback": "Coordinated suppression of both school and medical professionals. Explosive.", "note": "Company pressured both school and health center to suppress concerns"}
        ],
        "q1_note": "Children coughing, parents afraid to complain"
      },
      "silence": {
        "q1_response": "... You see that grey on the climbing frame? That's not paint. Touch it. Feel it. My daughter plays on that every day.",
        "expression_hint": "Walking to the fence, scraping dust with her finger",
        "q2_options": [
          {"text": "How many children play here every day?"},
          {"text": "Has anyone tried to get the dust analyzed?"},
          {"text": "..."}
        ],
        "outcomes": [
          {"tier": 1, "response": "Eighty-five children. Kindergarten through sixth grade. They eat lunch and then they go outside. Into this. Every. Single. Day.", "expression": "open", "feedback": "The scale is clear but you need more than a worried parent.", "note": "85 children exposed daily"},
          {"tier": 2, "response": "I scraped some into a jar. Brought it to Ekström at the pharmacy. He said it's not ordinary dust — it's metallic. Could contain chromium, iron oxide, maybe worse. But he can't do a proper analysis. You'd need a lab.", "expression": "open", "feedback": "Pharmacist confirms metallic content. A lab test away from proof.", "note": "Pharmacist says metallic dust, possible chromium"},
          {"tier": 3, "response": "I kept a jar of it. Ekström at the pharmacy says it's metallic. And last week I found something else — a letter in the school office waste bin. From Ståhlbergs to the headmaster. 'We appreciate your discretion regarding the expansion. The dust levels are within our internal targets.' They knew. They knew and they said nothing.", "expression": "open", "feedback": "Company letter acknowledging dust and requesting silence. This is the smoking gun.", "note": "Company letter: 'We appreciate your discretion, dust within our targets'"}
        ],
        "q1_note": "Grey dust on the climbing frame"
      }
    }
  },
  "headlines": [
    {"text": "Parents Concerned About Dust Near Bruksskolan", "tone": "Cautious"},
    {"text": "Children Cough as Factory Dust Coats Playground", "tone": "Narrative"},
    {"text": "SILENCED: Mill Told School to Hide Dust Danger", "tone": "Exposing"}
  ]
},

{
  "id": "brukets_vatten",
  "title": "The Mill Water",
  "description": "A retired worker says the factory's been dumping waste in the river since the sixties.",
  "lead_text": "The fish died ten years ago. We used to swim there as boys. Now it smells like chemicals.",
  "preview": "A wheezing old man at the local café insists on buying you coffee.",
  "source_type": "street",
  "difficulty": "medium",
  "base_value": 4,
  "category": "environment",
  "npc_id": "gosta_fredriksson",
  "npc_name": "Gösta Fredriksson",
  "npc_title": "Retired Steelworker",
  "town": "industristad",
  "interview": {
    "opening_line": "I worked there thirty-two years. I've seen what they put in the river. Sit down — I'll tell you everything.",
    "q1_options": [
      {"archetype": "friendly", "text": "Thirty-two years — you must have seen a lot, Gösta. I'm listening."},
      {"archetype": "direct", "text": "What specific substances are they dumping? When did it start?"},
      {"archetype": "pressure", "text": "If you knew they were poisoning the river, why didn't you say something sooner?"},
      {"archetype": "silence", "text": "..."}
    ],
    "branches": {
      "friendly": {
        "q1_response": "Started in '62 when they built the new acid bath. The runoff goes straight into Svartån. No treatment, no filter. Just a pipe into the river. Everyone knew.",
        "expression_hint": "Settling into his chair, glad someone's finally listening",
        "q2_options": [
          {"text": "What kind of acid? Is the pipe still there?"},
          {"text": "When you say 'everyone knew' — does that include management?"},
          {"text": "Have you noticed any health effects in the people living near the river?"}
        ],
        "outcomes": [
          {"tier": 1, "response": "Hydrochloric acid from the pickling process. The pipe's behind the loading dock — you can see it from the bridge if you know where to look. It runs at night, mostly.", "expression": "open", "feedback": "The pipe exists and you know where it is. A good start.", "note": "Hydrochloric acid pipe behind loading dock, runs at night"},
          {"tier": 2, "response": "Hydrochloric acid, chromium rinse, and the cooling water from the furnace. The pipe runs into the river at night. And management knows — I was there when Bergström's father ordered it installed. 'Cheaper than treatment,' he said. I remember because my foreman laughed.", "expression": "open", "feedback": "Three pollutants, a management order, and a direct quote. Strong sourcing.", "note": "Three pollutants, Bergström Sr ordered pipe: 'cheaper than treatment'"},
          {"tier": 3, "response": "In '71, the county did a water test downstream. The results were bad — heavy metals, pH levels way off. Bergström sent his lawyer to meet with the county inspector. After that meeting, the report was 'revised.' The final version said 'within acceptable parameters.' I know because the original inspector quit over it. He's still alive. Name's Holmgren.", "expression": "open", "feedback": "Falsified county report plus a named whistleblower. Massive story.", "note": "1971 water report falsified after Bergström's lawyer intervened, inspector Holmgren quit"}
        ],
        "q1_note": "Acid runoff into Svartån since '62"
      },
      "direct": {
        "q1_response": "Hydrochloric acid from the pickling line. Chromium from the plating wash. And whatever comes out of the cooling system — metals, oils, who knows what. Since 1962, through a 15-centimeter pipe into Svartån.",
        "expression_hint": "Drawing a map on a napkin",
        "q2_options": [
          {"text": "Is the pipe still active? Does anyone regulate it?"},
          {"text": "Have there been any official inspections of the discharge?"},
          {"text": "What volume are we talking about? How much goes in daily?"}
        ],
        "outcomes": [
          {"tier": 1, "response": "Still active. They run it at night. The county is supposed to inspect annually but I haven't seen an inspector at that pipe in years. They inspect the front gate — not the back.", "expression": "open", "feedback": "Pipe is active, inspections are superficial. But it's his word.", "note": "Pipe active, night discharge, inspections miss it"},
          {"tier": 2, "response": "Still pumping every night. About 2,000 liters goes through between midnight and four AM. The county inspected in '71 — found violations. Then Bergström's lawyer showed up and the report was 'adjusted.' The violations disappeared from the final version.", "expression": "open", "feedback": "Volume estimate plus a falsified inspection report. Documentary angle.", "note": "2,000 liters nightly, 1971 inspection report falsified"},
          {"tier": 3, "response": "Two thousand liters a night, twelve years straight. Do the math — that's almost nine million liters of contaminated water. In '71 the county found violations and Bergström had the report changed. The inspector who filed it — Stig Holmgren — was pressured to resign. He lives in Karlstad now. I have his address if you want to talk to him.", "expression": "open", "feedback": "Nine million liters, falsified report, and a named witness. This could bring the factory down.", "note": "9 million liters over 12 years, fired inspector in Karlstad"}
        ],
        "q1_note": "HCl, chromium, oils — 15cm pipe into Svartån"
      },
      "pressure": {
        "q1_response": "Why didn't I? Because I had a family to feed! You try being a whistleblower when the factory is the only employer in town. I waited until I retired. Are you going to listen or judge?",
        "expression_hint": "Slapping the table, wheezing harder",
        "q2_options": [
          {"text": "You're right. I'm sorry. Tell me what you saw."},
          {"text": "You're safe now though. What exactly did they dump?"},
          {"text": "Other workers must have seen it too. Who else knows?"}
        ],
        "outcomes": [
          {"tier": 1, "response": "Acid and metal wash. Through a pipe into the river. Everyone on the night shift knew. We just... didn't talk about it.", "expression": "guarded", "feedback": "Basic facts confirmed but he's holding back after the aggressive start.", "note": "Night shift knew about the dumping"},
          {"tier": 2, "response": "Fine. Hydrochloric acid and chromium waste. A pipe behind the dock. Two thousand liters a night. I know because I maintained the pump for seven years. And every time there was an inspection, we'd shut it off the day before. Someone always tipped us off.", "expression": "open", "feedback": "Inside knowledge of the concealment system. He maintained the pump.", "note": "Pump shut off before inspections, someone tipped them off"},
          {"tier": 3, "response": "I maintained that pump for seven years. I know exactly what went through it. And I kept a logbook — dates, volumes, what they ran. My own record, hidden at home. Because I knew this day would come. I also know the inspector who tried to report it and was forced out. Holmgren. He'll talk.", "expression": "open", "feedback": "Seven years of personal logbooks plus a willing second source. Explosive investigative material.", "note": "Personal logbook of 7 years of dumping data, plus second source"}
        ],
        "q1_note": "Waited until retirement to speak"
      },
      "silence": {
        "q1_response": "... Smart. You wait. Like I waited. Thirty-two years I waited. The river turned grey. The fish died. My grandchildren can't swim where I swam. And the factory keeps pumping.",
        "expression_hint": "Staring at his coffee, then at the window toward the river",
        "q2_options": [
          {"text": "The river turned grey."},
          {"text": "What changed that made you want to talk now?"},
          {"text": "..."}
        ],
        "outcomes": [
          {"tier": 1, "response": "Grey and sometimes green. Depends on what they're running. The acid turns it grey. The chromium gives it a shimmer. You can still see it from the bridge on a moonlit night.", "expression": "open", "feedback": "Vivid description but it's an old man's memory. You need more.", "note": "Grey and green river, visible from the bridge"},
          {"tier": 2, "response": "My grandson asked me why the river smells. I couldn't lie to him. So I'll tell you instead. Two thousand liters a night. Acid and metals. And the county knew — they tested it in '71. The results disappeared.", "expression": "open", "feedback": "The grandson triggered it. Emotional and factual — the disappeared results give it weight.", "note": "2,000 liters nightly, 1971 test results disappeared"},
          {"tier": 3, "response": "I'm dying. Doctor says the lungs. Thirty-two years of breathing what they put in the water and the air. I kept a logbook. Seven years of dates and volumes. And I know who else can confirm it — Stig Holmgren, the county inspector they pushed out. Here. Take this.", "expression": "open", "feedback": "A dying man's logbook and a second source. This is the biggest environmental story in the county.", "note": "Terminally ill, 7-year logbook, corroborating witness Holmgren"}
        ],
        "q1_note": "Waited thirty-two years to speak"
      }
    }
  },
  "headlines": [
    {"text": "Retired Worker Claims Mill Dumps Acid in River", "tone": "Cautious"},
    {"text": "Thirty-Two Years of Poison: Inside the Mill's Hidden Pipe", "tone": "Narrative"},
    {"text": "NINE MILLION LITERS: The Pipe Ståhlbergs Doesn't Want You to See", "tone": "Exposing"}
  ]
},

{
  "id": "loneforhandlingen",
  "title": "The Wage Slip",
  "description": "A leaked document shows management planned to reject the wage increase before negotiations even started.",
  "lead_text": "They had the answer ready before we even sat down. The whole negotiation was a show.",
  "preview": "An envelope slipped under the office door overnight, containing a photocopied memo.",
  "source_type": "document",
  "difficulty": "medium",
  "base_value": 4,
  "category": "labor",
  "npc_id": "kerstin_holmberg",
  "npc_name": "Kerstin Holmberg",
  "npc_title": "Secretary, Ståhlbergs Administration",
  "town": "industristad",
  "interview": {
    "opening_line": "I typed that memo. I know what it says. They decided the outcome before the union even entered the room.",
    "q1_options": [
      {"archetype": "friendly", "text": "That took courage, Kerstin. What exactly did the memo say?"},
      {"archetype": "direct", "text": "When was the memo dated? Who wrote it and who received it?"},
      {"archetype": "pressure", "text": "This looks like bad-faith bargaining. Is that what you're saying?"},
      {"archetype": "silence", "text": "..."}
    ],
    "branches": {
      "friendly": {
        "q1_response": "Two weeks before the wage negotiations. Director Bergström to the board: 'The request will be denied regardless of presentation. Prepare conciliatory language for the press release.' They had the press release written before the meeting.",
        "expression_hint": "Speaking quietly, checking the door",
        "q2_options": [
          {"text": "A press release already written? Can you describe it?"},
          {"text": "What was the union asking for? Was it unreasonable?"},
          {"text": "Were there other memos like this? Is it a pattern?"}
        ],
        "outcomes": [
          {"tier": 1, "response": "The press release said management had 'carefully considered the proposal' and found it 'incompatible with current market conditions.' Word for word what they said after the meeting. They didn't consider anything.", "expression": "open", "feedback": "Pre-written rejection language. Embarrassing but not illegal.", "note": "Press release drafted before negotiations — identical language used"},
          {"tier": 2, "response": "The union asked for a 4% raise. Industry standard. The memo said: 'Offer 1.5% with improved canteen facilities as compromise. Cost of canteen improvements: negligible. Optics: positive.' They planned the whole kabuki.", "expression": "open", "feedback": "Scripted negotiation with calculated optics. Shows contempt for the process.", "note": "4% requested, pre-planned 1.5% offer, canteen 'improvement' as cover"},
          {"tier": 3, "response": "The memo included a line I'll never forget: 'Union leadership will accept 1.5% — Göransson has been briefed and will recommend acceptance.' The union chairman was in on it. They fixed the negotiation from both sides.", "expression": "open", "feedback": "Collusion between management and union leadership. Both sides betrayed the workers.", "note": "Union chairman Göransson pre-briefed, agreed to accept 1.5%"}
        ],
        "q1_note": "Memo: rejection decided before negotiation"
      },
      "direct": {
        "q1_response": "October 14th. From Bergström to the board — Lundgren, Ståhl, and Franzén. CC'd to the company lawyer. Marked 'strictly confidential.' I have the carbon copy.",
        "expression_hint": "Tapping a plain brown envelope on the table",
        "q2_options": [
          {"text": "Can I see the carbon copy?"},
          {"text": "What specifically does the memo instruct the board to do?"},
          {"text": "Why was the company lawyer CC'd?"}
        ],
        "outcomes": [
          {"tier": 1, "response": "The memo says to reject any increase above 1.5%. The rest is strategy language — 'maintain firm position,' 'express sympathy for worker concerns.' Standard manipulation.", "expression": "guarded", "feedback": "Clear rejection strategy but could be defended as normal negotiation prep.", "note": "Reject above 1.5%, 'express sympathy' strategy"},
          {"tier": 2, "response": "Here — read it yourself. 'Reject any increase above 1.5%. If union threatens action, remind them of the oil crisis and potential layoffs. Layoffs are not planned but the threat is useful.' They weaponized job insecurity.", "expression": "open", "feedback": "Written admission of using false layoff threats as leverage. This is the story.", "note": "Memo admits fake layoff threats as negotiation weapon"},
          {"tier": 3, "response": "Read it. The last paragraph: 'Union chairman has indicated willingness to settle at 1.5% provided management supports his re-election bid at the April meeting.' Bergström and Göransson made a deal. The workers never had a chance.", "expression": "open", "feedback": "Management-union chairman pact. Corruption on both sides of the table.", "note": "Göransson traded 1.5% acceptance for re-election support from management"}
        ],
        "q1_note": "Oct 14 memo, Bergström to board, CC lawyer"
      },
      "pressure": {
        "q1_response": "Bad-faith? That's exactly what it is. But try proving it. The original memo is in Bergström's safe. I only have the carbon copy. And if they find out I gave it to you, I'm finished.",
        "expression_hint": "Hands trembling slightly",
        "q2_options": [
          {"text": "I'll protect your identity. What does the carbon copy say?"},
          {"text": "If you're this scared, why come forward at all?"},
          {"text": "Would anyone else corroborate what you're telling me?"}
        ],
        "outcomes": [
          {"tier": 1, "response": "It says to reject anything above 1.5%. 'Express regret, cite market conditions.' The usual corporate script. But the fact that they wrote it two weeks before the meeting — that's the point.", "expression": "guarded", "feedback": "The timing is the story, but it's thin without more context.", "note": "Rejection scripted two weeks before meeting"},
          {"tier": 2, "response": "Because 340 workers deserved a fair negotiation. The memo tells the board to threaten layoffs if the union pushes back. But there are no planned layoffs — it says so right there. 'Layoffs are not planned but the threat is useful.' I typed those words.", "expression": "open", "feedback": "The false layoff threat in writing. She typed it — she's a direct witness.", "note": "She typed the memo with false layoff threat, 340 workers affected"},
          {"tier": 3, "response": "Because I also typed the follow-up memo — where Bergström thanks Göransson for his 'cooperation' and promises to 'ensure his continued leadership position.' The union chairman sold out his own members for a handshake deal with the boss.", "expression": "open", "feedback": "Two memos proving collusion. The secretary typed them both. Devastating.", "note": "Second memo: Bergström thanks Göransson for cooperation, promises support"}
        ],
        "q1_note": "Carbon copy of confidential memo"
      },
      "silence": {
        "q1_response": "... I thought you'd have more questions. Most people do. But I suppose the document speaks for itself. I'll just say this: I type everything in that office. Everything.",
        "expression_hint": "Sliding the envelope across the table",
        "q2_options": [
          {"text": "Everything. What else have you typed?"},
          {"text": "This document — when was it written relative to the negotiations?"},
          {"text": "..."}
        ],
        "outcomes": [
          {"tier": 1, "response": "The memo is dated October 14th. The negotiations were October 28th. Fourteen days. They knew exactly what they'd say.", "expression": "open", "feedback": "Clean timeline. Pre-planned rejection.", "note": "14-day gap between memo and negotiations"},
          {"tier": 2, "response": "Termination lists. Two sets. One real — for the oil crisis contingency. One fake — designed to scare the union during negotiations. 'Show them the list but don't file it.' Bergström's instructions.", "expression": "open", "feedback": "Fake termination lists as intimidation. Written evidence of deception.", "note": "Fake termination list used as union intimidation tool"},
          {"tier": 3, "response": "I type everything. Including the letter from Göransson to Bergström — the union chairman writing to the factory director, asking for 'mutual understanding on the wage question.' Dated October 10th. Four days before the rejection memo. They coordinated. And I have carbons of both.", "expression": "open", "feedback": "The union chairman initiated the collusion. Carbon copies of both sides. Nuclear.", "note": "Göransson wrote to Bergström first, Oct 10 — union chairman initiated collusion"}
        ],
        "q1_note": "She types everything in that office"
      }
    }
  },
  "headlines": [
    {"text": "Internal Memo Shows Pre-Planned Wage Rejection", "tone": "Fact-based"},
    {"text": "Workers Never Had a Chance: Negotiation Scripted in Advance", "tone": "Narrative"},
    {"text": "FIXED DEAL: Union Boss and Director Agreed Before Workers Sat Down", "tone": "Exposing"}
  ]
},

{
  "id": "brandovningen",
  "title": "The Fire Drill",
  "description": "A fire drill at the paper mill revealed emergency exits blocked by stored materials.",
  "lead_text": "We couldn't get out. Three exits, all blocked. The fire chief was furious.",
  "preview": "A mill worker approaches you outside the library, looking over his shoulder.",
  "source_type": "street",
  "difficulty": "medium",
  "base_value": 4,
  "category": "labor",
  "npc_id": "rune_hellstrom",
  "npc_name": "Rune Hellström",
  "npc_title": "Paper Mill Shift Supervisor",
  "town": "industristad",
  "interview": {
    "opening_line": "Last Thursday's fire drill. It was a disaster. But nobody's talking about it because the company 'resolved it internally.'",
    "q1_options": [
      {"archetype": "friendly", "text": "That sounds serious, Rune. Tell me what happened during the drill."},
      {"archetype": "direct", "text": "Which exits were blocked? What was blocking them?"},
      {"archetype": "pressure", "text": "If there had been a real fire, how many people would have died?"},
      {"archetype": "silence", "text": "..."}
    ],
    "branches": {
      "friendly": {
        "q1_response": "Fire bell rings at 14:00. My section — forty-three men — start moving to the exits. Exit B: pallets of raw paper stacked floor to ceiling. Exit C: a forklift parked across the door. Exit D: chained shut. We had to go all the way back to the main entrance.",
        "expression_hint": "Counting exits on his fingers, getting agitated",
        "q2_options": [
          {"text": "What did the fire chief say when he saw this?"},
          {"text": "How long did it take everyone to get out?"},
          {"text": "Who authorized storing materials in front of the exits?"}
        ],
        "outcomes": [
          {"tier": 1, "response": "Twelve minutes for full evacuation. Standard should be under four. The fire chief told the production manager it was 'unacceptable.' Next day, the pallets were moved. Problem solved, they said.", "expression": "open", "feedback": "Three times the evacuation standard. Quick fix but no accountability.", "note": "12-minute evacuation vs 4-minute standard"},
          {"tier": 2, "response": "Fire chief Bengtsson was livid. He wrote a formal violation report. I saw him hand it to the production manager. But here's the thing — when I asked about it this week, the production manager said 'no formal report was filed.' It vanished.", "expression": "open", "feedback": "Disappeared violation report. The cover-up is the story.", "note": "Fire chief's violation report disappeared"},
          {"tier": 3, "response": "Bengtsson filed a violation report. It disappeared. But what they don't know is that I was there when he filed it, and I wrote down the reference number — FV-74-019. You can call the fire department and ask for it. If it's not in their files either, then someone in the municipality is covering for the factory.", "expression": "open", "feedback": "Reference number you can verify independently. If it's missing from fire department records too, it's a conspiracy.", "note": "Violation report FV-74-019 — verifiable, may have been purged from fire dept too"}
        ],
        "q1_note": "Three exits blocked, 43 men trapped"
      },
      "direct": {
        "q1_response": "Exit B: raw paper pallets, about three meters high. Exit C: forklift parked sideways, keys removed. Exit D: padlocked. A padlock on a fire exit. The fire code is very clear about that.",
        "expression_hint": "Speaking precisely, a supervisor's attention to detail",
        "q2_options": [
          {"text": "Who has the key to Exit D? Why was it locked?"},
          {"text": "Does the fire department know about this? Was it reported?"},
          {"text": "Is the fire code violation still ongoing, or did they fix it?"}
        ],
        "outcomes": [
          {"tier": 1, "response": "They moved the pallets and the forklift the next day. Exit D was unlocked. The production manager called it a 'temporary storage solution' that 'unfortunately coincided with the drill.'", "expression": "guarded", "feedback": "Quick fix with corporate language. No accountability trail.", "note": "Fixed after drill, called 'temporary storage solution'"},
          {"tier": 2, "response": "Exit D was locked because of theft. Someone was stealing paper stock. Instead of hiring a guard, they chained the exit. The fire chief filed a violation — number FV-74-019. When I checked this week, the production manager denied any report was filed.", "expression": "open", "feedback": "Locked exit to prevent theft, disappeared violation report.", "note": "Exit locked to prevent theft, violation FV-74-019 denied"},
          {"tier": 3, "response": "I checked all four sections this morning. Exit D is unlocked now — but Exit B has pallets again. Already. One week later. And the violation report? Gone from both the factory and the fire department records. Someone made it disappear. I took a photo of the exits with my own camera. Want to see?", "expression": "open", "feedback": "Exits re-blocked already, violation report erased from two agencies, photographic evidence.", "note": "Exits re-blocked after one week, report erased, worker has photos"}
        ],
        "q1_note": "Exit B: pallets, C: forklift, D: padlocked"
      },
      "pressure": {
        "q1_response": "Dead? In a real fire? All forty-three of us in section four. Maybe more. You can do the math — three exits blocked, one entrance, twelve minutes to evacuate.",
        "expression_hint": "Dead serious, jaw tight",
        "q2_options": [
          {"text": "Has anyone done the math officially? What do fire safety standards say?"},
          {"text": "Are the exits still blocked right now?"},
          {"text": "If this is as dangerous as you say, why hasn't the fire department shut the mill down?"}
        ],
        "outcomes": [
          {"tier": 1, "response": "Standards say under four minutes for full evacuation. We took twelve. The fire department can order a shutdown but they need to file a violation report first. And that report seems to have disappeared.", "expression": "open", "feedback": "The gap between standard and reality, plus the missing report.", "note": "4-min standard vs 12-min actual, report missing"},
          {"tier": 2, "response": "The fire department should have shut us down. Fire chief Bengtsson wanted to. But his report — FV-74-019 — never made it into the system. I asked at the fire station yesterday. They have no record of it. Bengtsson is on leave. 'Personal reasons.'", "expression": "open", "feedback": "Missing report, fire chief on sudden leave. Looks like suppression.", "note": "Fire chief Bengtsson on sudden leave, report vanished from system"},
          {"tier": 3, "response": "Because someone killed the report. And Bengtsson — who filed it — was told to take leave. 'Stress,' they said. But I talked to him at home. He says his supervisor was called by someone at the municipality. And I have photos of the exits — taken two days ago. They're already blocked again.", "expression": "open", "feedback": "Municipal-level cover-up, intimidated fire chief, photographic proof of ongoing violation.", "note": "Municipality called fire chief's boss, exits re-blocked, photos exist"}
        ],
        "q1_note": "Forty-three men would have died"
      },
      "silence": {
        "q1_response": "... Forty-three men in my section. One working exit. Paper everywhere — a paper mill, for God's sake. The most flammable workplace in Sweden, and they block the fire exits.",
        "expression_hint": "Shaking his head slowly, gripping the edge of the table",
        "q2_options": [
          {"text": "A paper mill with blocked fire exits."},
          {"text": "You're a supervisor. What would you do if it caught fire?"},
          {"text": "..."}
        ],
        "outcomes": [
          {"tier": 1, "response": "I'd try to get my men to the main entrance. A hundred meters through the production floor. Past the drying ovens. With burning paper falling from the ceiling. You see the problem.", "expression": "open", "feedback": "Vivid horror scenario but only his assessment.", "note": "Only escape route passes drying ovens and burning paper"},
          {"tier": 2, "response": "I've thought about it every night this week. And then I thought — there's a fire drill record. The fire chief filed a violation. But the company says it was never filed. So I went to the fire station myself. They have no record either. Someone erased it.", "expression": "open", "feedback": "Records erased from both factory and fire department. Concerted cover-up.", "note": "Violation erased from both factory and fire department records"},
          {"tier": 3, "response": "I'd watch my men die. That's the truth. And the worst part? They 'fixed' the exits after the drill. I checked yesterday — Exit B is blocked again. With paper. In a paper mill. And the fire chief who reported it is on 'sick leave.' I'm done being quiet. Here — I brought photos.", "expression": "open", "feedback": "Re-blocked exit one week later, intimidated fire chief, photographic evidence. Front page.", "note": "Exit re-blocked in one week, fire chief forced on leave, photos taken"}
        ],
        "q1_note": "Most flammable workplace, exits blocked"
      }
    }
  },
  "headlines": [
    {"text": "Fire Drill Reveals Blocked Exits at Paper Mill", "tone": "Factual"},
    {"text": "43 Workers Trapped During Fire Drill — Violation Report Vanishes", "tone": "Confrontational"},
    {"text": "BURNED EVIDENCE: Mill Erased Fire Safety Violation from Records", "tone": "Exposing"}
  ]
},

{
  "id": "soptippen",
  "title": "The Dump",
  "description": "Residents near the old gravel pit say the factory is dumping waste there at night.",
  "lead_text": "Trucks come at midnight. They back up to the pit and dump barrels. The smell lasts for days.",
  "preview": "A woman in a house near the gravel pit waves you over, pointing at tire tracks.",
  "source_type": "street",
  "difficulty": "medium",
  "base_value": 4,
  "category": "environment",
  "npc_id": "ulla_bjork",
  "npc_name": "Ulla Björk",
  "npc_title": "Resident, Gruvvägen 14",
  "town": "industristad",
  "interview": {
    "opening_line": "They think nobody notices because they come at midnight. But I don't sleep well. And I see the trucks.",
    "q1_options": [
      {"archetype": "friendly", "text": "That must be unsettling, Ulla. How long have you been seeing the trucks?"},
      {"archetype": "direct", "text": "What kind of trucks? How often? Can you identify the company?"},
      {"archetype": "pressure", "text": "Are they dumping toxic waste? Do you have proof?"},
      {"archetype": "silence", "text": "..."}
    ],
    "branches": {
      "friendly": {
        "q1_response": "Since August. Every Thursday and sometimes Saturday. Big flatbed trucks with covered loads. They back up to the edge of the old gravel pit and dump barrels. Last week the smell was so bad I had to close all the windows.",
        "expression_hint": "Leading you to the kitchen window with a view of the pit",
        "q2_options": [
          {"text": "Can you see any markings on the trucks or the barrels?"},
          {"text": "Have you or your neighbors reported this to the municipality?"},
          {"text": "What does the smell remind you of? Chemicals? Something else?"}
        ],
        "outcomes": [
          {"tier": 1, "response": "The smell is like... rotten eggs and something metallic. My throat itches for days after. And the dog won't go near that end of the garden anymore. Animals know.", "expression": "open", "feedback": "Sensory description suggesting chemical waste but no hard evidence.", "note": "Sulfur + metallic smell, dog avoids the area"},
          {"tier": 2, "response": "Last Thursday I got close enough to see — blue barrels with a white label. I couldn't read it in the dark, but the truck had 'Industrifrakt AB' on the side. That's Ståhlbergs' transport company. And I reported it to the municipality in September. They said they'd investigate. Nothing happened.", "expression": "open", "feedback": "Identified the transport company linked to Ståhlbergs. Municipality ignored complaint.", "note": "Industrifrakt AB trucks (Ståhlbergs), municipality ignored Sept complaint"},
          {"tier": 3, "response": "I went down there last Sunday with my camera. There are at least forty barrels in the pit. Some are leaking — there's a brown sludge running into the drainage ditch that goes to Svartån. The barrels say 'CHROMIUM WASTE — HANDLE WITH CARE.' I have the photos.", "expression": "open", "feedback": "Photographic evidence of labeled toxic waste leaking toward the river. Devastating.", "note": "40+ barrels labeled 'CHROMIUM WASTE', leaking into drainage to Svartån, photos"}
        ],
        "q1_note": "Thursday midnight trucks since August"
      },
      "direct": {
        "q1_response": "Flatbed trucks, covered loads. License plates start with 'O' — Örebro county registration. They come between midnight and two AM, Thursdays primarily. The truck sides say 'Industrifrakt' when the tarp shifts.",
        "expression_hint": "Reading from a notebook she's been keeping",
        "q2_options": [
          {"text": "You've been keeping notes. What else is in your log?"},
          {"text": "Industrifrakt — is that connected to Ståhlbergs?"},
          {"text": "What are they dumping? Have you gone down to look?"}
        ],
        "outcomes": [
          {"tier": 1, "response": "Twelve visits since August. Always between midnight and two. Industrifrakt is Ståhlbergs' in-house transport operation. They handle all the factory's outbound freight.", "expression": "open", "feedback": "Solid log linking Ståhlbergs' transport company. But what's being dumped?", "note": "12 documented visits, Industrifrakt = Ståhlbergs transport"},
          {"tier": 2, "response": "Twelve visits logged. Industrifrakt is wholly owned by Ståhlbergs — I checked at the company registry. And yes, I went down there. Blue barrels with hazard labels. Some cracked open. The ground around them is discolored and nothing grows within twenty meters.", "expression": "open", "feedback": "Ownership confirmation plus visual evidence of contamination.", "note": "Ståhlbergs owns Industrifrakt, barrels leaking, ground dead within 20m"},
          {"tier": 3, "response": "Here's my log — twelve visits, dates, times, plate numbers. Industrifrakt is owned by Ståhlbergs, registered at the same address. The barrels say 'chromium waste' and some are leaking into the drainage ditch toward Svartån. And the gravel pit? The municipality approved it for 'inert fill material only.' What's in those barrels is anything but inert.", "expression": "open", "feedback": "Complete evidence package: log, ownership trail, labeled toxic waste, permit violation, river contamination.", "note": "Full log, ownership proof, chromium waste violates pit permit, drains to river"}
        ],
        "q1_note": "Industrifrakt trucks, O-plates, Thursday nights"
      },
      "pressure": {
        "q1_response": "Toxic? What do you think makes my eyes water and my throat burn? Of course it's toxic. But proof? I'm a retired schoolteacher. I don't have a laboratory.",
        "expression_hint": "Frustrated, pointing at red-rimmed eyes",
        "q2_options": [
          {"text": "Your observations are valuable. What exactly have you noticed about the dump site?"},
          {"text": "Have you tried to get anyone to test the soil or water?"},
          {"text": "What do you think would happen if the factory found out you were watching?"}
        ],
        "outcomes": [
          {"tier": 1, "response": "Brown sludge running from cracked barrels. Dead grass in a circle around the pit. The drainage ditch has a sheen on top of the water. I'm not a chemist but I know what poison looks like.", "expression": "open", "feedback": "Strong observational evidence but needs expert confirmation.", "note": "Brown sludge, dead grass, chemical sheen in drainage ditch"},
          {"tier": 2, "response": "I asked the municipality to test the water in the drainage ditch. They sent someone who took a sample in September. I called last week for results — they said the sample was 'lost in processing.' Lost. After six weeks.", "expression": "open", "feedback": "Municipality 'lost' a water sample. Cover-up by negligence or design.", "note": "Municipality 'lost' water sample taken in September"},
          {"tier": 3, "response": "The municipality 'lost' my water sample. So I saved one myself. Filled a bottle from the drainage ditch. And I went to the pit with my camera. The barrels are labeled. 'Chromium waste.' And the permit for the fill site? I looked it up — it only allows 'clean soil and rock.' I am a retired schoolteacher, and even I can see this is illegal.", "expression": "open", "feedback": "Self-collected water sample, photographic evidence, permit violation documented. Solid.", "note": "Self-collected water sample, photos of labeled barrels, permit violation proven"}
        ],
        "q1_note": "Eyes burn, throat burns — obvious toxicity"
      },
      "silence": {
        "q1_response": "... You can smell it from here on Fridays. After the Thursday night dump. Open the window if you don't believe me.",
        "expression_hint": "Opening the kitchen window, winter air carries a faint chemical tang",
        "q2_options": [
          {"text": "I can smell it. What is that?"},
          {"text": "How long have you lived here?"},
          {"text": "..."}
        ],
        "outcomes": [
          {"tier": 1, "response": "Thirty-one years. The pit was just gravel when we moved in. Now it's a dump. And nobody cares because it's just us — the old houses by the pit. We don't matter to the municipality.", "expression": "open", "feedback": "The human story is there but you need more than testimony.", "note": "31-year resident, neighborhood marginalized"},
          {"tier": 2, "response": "Thirty-one years. I've watched this neighborhood change. The pit used to be gravel — clean gravel. Now there are barrels down there. I've counted over forty. Some are cracked. The drainage ditch runs brown after rain. And the municipality won't test the water.", "expression": "open", "feedback": "Long-term observation, barrel count, drainage contamination, municipality inaction.", "note": "40+ barrels, brown drainage water, municipality refuses testing"},
          {"tier": 3, "response": "Thirty-one years. I raised my children here. Now my grandchildren can't play in the garden because of the smell. I've kept a log since August. Twelve truck visits. And I went down there myself. The barrels say 'chromium waste.' I took pictures. And I saved a water sample from the ditch because the municipality 'lost' theirs. I'm old, not stupid.", "expression": "open", "feedback": "Log, photos, label evidence, self-collected sample. A retired teacher built a better case than the authorities.", "note": "Full evidence kit: log, photos, labeled barrels, water sample, 30-year resident"}
        ],
        "q1_note": "You can smell it from the kitchen"
      }
    }
  },
  "headlines": [
    {"text": "Residents Report Late-Night Dumping Near Gravel Pit", "tone": "Cautious"},
    {"text": "Midnight Trucks: Ståhlbergs Linked to Illegal Waste Site", "tone": "Confrontational"},
    {"text": "CHROMIUM IN THE DITCH: Factory Dumps Toxic Barrels by Night", "tone": "Exposing"}
  ]
},

{
  "id": "bygglovet",
  "title": "The Building Permit",
  "description": "A new factory extension got approved in record time, bypassing the usual environmental review.",
  "lead_text": "The permit was approved in three days. Normal process takes six months. Someone made a phone call.",
  "preview": "A manila folder left on the newspaper's front step, marked 'For the editor.'",
  "source_type": "document",
  "difficulty": "medium",
  "base_value": 4,
  "category": "corruption",
  "npc_id": "bo_fredriksson_i",
  "npc_name": "Bo Fredriksson",
  "npc_title": "Municipal Planning Clerk",
  "town": "industristad",
  "interview": {
    "opening_line": "I process building permits. I've never seen one approved in three days. Not once in fourteen years. Someone called my boss.",
    "q1_options": [
      {"archetype": "friendly", "text": "Fourteen years of experience — you know when something's wrong. Tell me about this permit."},
      {"archetype": "direct", "text": "Which permit? What's the reference number and the applicant?"},
      {"archetype": "pressure", "text": "Did your boss take a bribe to fast-track this?"},
      {"archetype": "silence", "text": "..."}
    ],
    "branches": {
      "friendly": {
        "q1_response": "Ståhlbergs applied for an extension to their acid pickling facility on October 21st. Approved October 24th. The environmental review alone should take eight weeks. This one had no environmental review at all.",
        "expression_hint": "Adjusting his glasses, speaking with bureaucratic precision",
        "q2_options": [
          {"text": "No environmental review for an acid facility? Is that legal?"},
          {"text": "Who approved it? Who has the authority to skip the review?"},
          {"text": "What's the normal timeline for a permit like this?"}
        ],
        "outcomes": [
          {"tier": 1, "response": "It's not legal for a chemical processing extension. Environmental review is mandatory under the 1969 Environment Protection Act. But the box was checked as 'not applicable' on the form. Someone ticked the wrong box — or the right one, depending on your perspective.", "expression": "guarded", "feedback": "Legal violation identified but could be called a clerical error.", "note": "Mandatory environmental review skipped, marked 'not applicable'"},
          {"tier": 2, "response": "Chief planner Nilsson approved it. He has the authority to waive reviews for 'minor modifications.' But an acid pickling extension is not minor — it's Category B under the EPA. Nilsson reclassified it as Category D: 'cosmetic alterations.' An acid facility as 'cosmetic.' You can't make this up.", "expression": "open", "feedback": "Deliberate misclassification to bypass environmental law. Named decision-maker.", "note": "Nilsson reclassified acid facility as 'cosmetic alterations' (Cat D vs Cat B)"},
          {"tier": 3, "response": "Nilsson reclassified it. But here's what you really need to know — on October 22nd, the day after the application, Nilsson drove to Stockholm with Bergström. I know because they used the municipal car. The mileage log is in our records. When they came back, the permit was approved. And Nilsson's son started a new job at Ståhlbergs the following Monday.", "expression": "open", "feedback": "Trip with factory director, permit approved, son hired. Classic quid pro quo.", "note": "Nilsson traveled with Bergström to Stockholm, son hired at Ståhlbergs next week"}
        ],
        "q1_note": "3-day approval, no environmental review"
      },
      "direct": {
        "q1_response": "Reference BP-74-2341. Applicant: Ståhlbergs Stålverk AB. Extension of acid pickling facility, Building 7. Applied October 21st, approved October 24th. Category reclassified from B to D to skip environmental review.",
        "expression_hint": "Reading from memory, precise as a filing cabinet",
        "q2_options": [
          {"text": "Who changed the category classification?"},
          {"text": "What's the difference between Category B and D in practice?"},
          {"text": "Is there a paper trail showing the reclassification?"}
        ],
        "outcomes": [
          {"tier": 1, "response": "Chief planner Nilsson. His signature is on the reclassification. Category B requires full environmental review — eight weeks minimum. Category D is for paint jobs and new windows. Make of that what you will.", "expression": "guarded", "feedback": "Named official, clear misclassification. Solid municipal story.", "note": "Nilsson signed reclassification, acid facility = 'paint job' category"},
          {"tier": 2, "response": "Nilsson signed the reclassification. But the original form — the one Ståhlbergs submitted — correctly listed it as Category B. Someone overwrote it in pen. I have a photocopy of the original and the amended version. They don't match.", "expression": "open", "feedback": "Two versions of the form — original and altered. Documentary proof of tampering.", "note": "Original form altered in pen, photocopies of both versions exist"},
          {"tier": 3, "response": "I have both versions — original and altered. The original was Category B. Nilsson changed it to D in pen. And the day between application and approval? Nilsson took the municipal car to Stockholm. With Bergström. The mileage log proves it. And his son was hired at Ståhlbergs five days later. I have all the paperwork.", "expression": "open", "feedback": "Altered documents, travel records, nepotistic hiring. Complete corruption case.", "note": "Altered permit + mileage log + son hired at Ståhlbergs = full corruption chain"}
        ],
        "q1_note": "BP-74-2341, Cat B→D reclassification"
      },
      "pressure": {
        "q1_response": "A bribe? I wouldn't say that. But something happened between October 21st and 24th that made my boss change a legal classification from B to D. You can call that what you want.",
        "expression_hint": "Very careful with his words, civil service caution",
        "q2_options": [
          {"text": "What do YOU think happened?"},
          {"text": "If it wasn't a bribe, what could make a career official break the rules?"},
          {"text": "Are there other permits that were fast-tracked like this?"}
        ],
        "outcomes": [
          {"tier": 1, "response": "I think he got a phone call from someone important. And he decided the easy path was compliance. Nilsson is two years from retirement. He doesn't want trouble.", "expression": "guarded", "feedback": "Plausible but speculative. A phone call theory isn't evidence.", "note": "Theory: pressure call, Nilsson close to retirement"},
          {"tier": 2, "response": "Other permits? Let me check... Actually, I already checked. In '72, Ståhlbergs got a warehouse extension approved in four days. Category C reclassified as D. Same signature. Nilsson. It's a pattern.", "expression": "open", "feedback": "Pattern of fast-tracked permits for Ståhlbergs. This isn't a one-off.", "note": "Same pattern in 1972 — warehouse extension fast-tracked by Nilsson"},
          {"tier": 3, "response": "I checked three years of Ståhlbergs permits. Four fast-tracked. All reclassified by Nilsson. And this year, Nilsson's son got a management trainee position at the factory. No interview. No other candidates. I have the permit records and the employment notice. Connect the dots.", "expression": "open", "feedback": "Four permits, systematic corruption, and a nepotism trail. This is a municipal scandal.", "note": "4 fast-tracked permits over 3 years, Nilsson's son hired without interview"}
        ],
        "q1_note": "Something happened in those three days"
      },
      "silence": {
        "q1_response": "... I've worked at the planning office fourteen years. I've seen permits come and go. This one... this one was different. Three days. For an acid facility.",
        "expression_hint": "Folding and unfolding his hands, wrestling with duty",
        "q2_options": [
          {"text": "What made it different?"},
          {"text": "You've been at this a long time. Have you seen this before?"},
          {"text": "..."}
        ],
        "outcomes": [
          {"tier": 1, "response": "An acid pickling extension normally takes six months. Environmental review, public comment period, building inspection. This one had none of that. Three days from application to approval.", "expression": "open", "feedback": "The timeline tells the story but no explanation of why.", "note": "6-month process compressed to 3 days, no reviews"},
          {"tier": 2, "response": "Once before. In '72. Same applicant. Same chief planner. Same reclassification trick. And both times, Nilsson seemed nervous after. Like he'd done something he shouldn't have.", "expression": "open", "feedback": "Pattern confirmed. Nilsson's behavior changed both times.", "note": "Same pattern in '72, Nilsson visibly nervous both times"},
          {"tier": 3, "response": "I've been sitting on this for two weeks. Because I know what it means. Nilsson is my boss. But I've made copies. The original application — Category B. The approved version — Category D, in Nilsson's handwriting. The mileage log showing the car trip. And the letter from Ståhlbergs welcoming Nilsson's son to the company. If I give you these, there's no going back.", "expression": "open", "feedback": "He brought the full package. Copies that prove everything. He's burning his career for this.", "note": "Full document package: original, altered permit, mileage log, hiring letter"}
        ],
        "q1_note": "Fourteen years, never seen anything like it"
      }
    }
  },
  "headlines": [
    {"text": "Acid Facility Permit Approved in Three Days — No Review", "tone": "Fact-based"},
    {"text": "Fast-Tracked and Reclassified: How Ståhlbergs Skipped the Rules", "tone": "Analytical"},
    {"text": "PERMIT FOR HIRE: Planner's Son Got Factory Job After Fast-Track", "tone": "Exposing"}
  ]
},

{
  "id": "julbonusen",
  "title": "The Christmas Bonus",
  "description": "Workers' Christmas bonus was canceled — but management received theirs doubled.",
  "lead_text": "No bonus this year. 'Tough times,' they said. Then we found out the managers got double.",
  "preview": "A neatly folded notice pinned to the break room bulletin board, photographed and mailed to you.",
  "source_type": "letter",
  "difficulty": "medium",
  "base_value": 4,
  "category": "labor",
  "npc_id": "margareta_olsson_i",
  "npc_name": "Margareta Olsson",
  "npc_title": "Administrative Assistant, HR Department",
  "town": "industristad",
  "interview": {
    "opening_line": "I process the payroll. I see everything. And what I saw this month made me sick.",
    "q1_options": [
      {"archetype": "friendly", "text": "That's a heavy thing to carry, Margareta. What did you find?"},
      {"archetype": "direct", "text": "What are the exact figures? How much did workers lose and managers gain?"},
      {"archetype": "pressure", "text": "Is the company stealing from its workers to pay its managers?"},
      {"archetype": "silence", "text": "..."}
    ],
    "branches": {
      "friendly": {
        "q1_response": "Every November, workers get a Christmas bonus — 500 kronor. Three hundred and forty workers. This year: canceled. 'Economic climate,' the memo said. Then I processed the management payroll. Their bonus doubled. From 5,000 to 10,000 kronor.",
        "expression_hint": "Removing her glasses, rubbing her eyes",
        "q2_options": [
          {"text": "How many managers received the doubled bonus?"},
          {"text": "Was there any explanation for why management got more while workers got nothing?"},
          {"text": "Do you have any documentation — payroll records, memos?"}
        ],
        "outcomes": [
          {"tier": 1, "response": "Twelve managers. 10,000 each. That's 120,000 kronor in management bonuses. The worker bonuses would have cost 170,000. They 'saved' 170,000 and spent 120,000. The net saving is 50,000. For a factory that turns over forty million.", "expression": "open", "feedback": "The math is damning. Saved 170k, spent 120k on managers. Revealing priorities.", "note": "340 workers × 500 kr cut = 170k saved; 12 managers × 10k = 120k spent"},
          {"tier": 2, "response": "The memo canceling worker bonuses was signed by Bergström and dated November 1st. The memo approving doubled management bonuses was signed by Bergström on October 28th. He approved the raises before he canceled the workers' pay. I have copies of both memos.", "expression": "open", "feedback": "Timeline proves management bonuses came first. The 'economic climate' was a lie.", "note": "Management bonus approved Oct 28, worker bonus cut Nov 1 — raises came first"},
          {"tier": 3, "response": "I have both memos. And here's what really got me — the management bonus memo says: 'To ensure retention of key personnel during the restructuring period.' Restructuring. There are layoff plans I've seen on Bergström's desk. They're going to cut fifty jobs in January. And the managers who decided that? They just got 10,000 kronor each.", "expression": "open", "feedback": "Bonuses for managers who are planning mass layoffs. The cruelty is structural.", "note": "Manager bonuses tied to 'restructuring' = 50 planned layoffs in January"}
        ],
        "q1_note": "Workers: 0 kr. Managers: 10,000 kr each"
      },
      "direct": {
        "q1_response": "Worker bonus: 500 kronor per person, 340 eligible. Canceled November 1st. Management bonus: 10,000 kronor per person, 12 eligible. Approved October 28th. Total worker savings: 170,000. Total management payout: 120,000.",
        "expression_hint": "Precise, controlled anger",
        "q2_options": [
          {"text": "Both memos were signed by Bergström?"},
          {"text": "Is there a formal justification for the management bonus increase?"},
          {"text": "Are there other expenses that were increased while worker costs were cut?"}
        ],
        "outcomes": [
          {"tier": 1, "response": "Both signed by Bergström. The worker memo cites 'challenging economic conditions.' The management memo cites 'retention of critical leadership talent.' Same economy, two different stories.", "expression": "open", "feedback": "Two contradictory narratives from the same person. Hypocrisy exposed.", "note": "Same signer, 'tough economy' for workers, 'retention' for managers"},
          {"tier": 2, "response": "Same signature, same week. And the management memo was backdated — I know because I typed it on November 3rd, but it's dated October 28th. Bergström told me to change the date so it wouldn't look like the two decisions were connected.", "expression": "open", "feedback": "Deliberately backdated to hide the connection. Active cover-up.", "note": "Management memo backdated from Nov 3 to Oct 28 to hide link"},
          {"tier": 3, "response": "Backdated memo, same signer. And the 'retention' justification? Three of those twelve managers are Bergström's relatives. His brother-in-law, his nephew, and his wife's cousin. Family members getting doubled bonuses while the factory cuts worker pay. I have the payroll list and the family connections documented.", "expression": "open", "feedback": "Nepotism and self-enrichment disguised as retention. Complete corruption case.", "note": "3 of 12 bonus managers are Bergström's relatives, documented"}
        ],
        "q1_note": "170k saved on workers, 120k spent on managers"
      },
      "pressure": {
        "q1_response": "Stealing? It's... it's redistributing, isn't it? Taking from 340 people and giving to 12. You tell me what that's called.",
        "expression_hint": "Struggling with the word, then finding her resolve",
        "q2_options": [
          {"text": "You're right to be angry. What evidence can you share?"},
          {"text": "Does anyone else in HR know about this disparity?"},
          {"text": "What would happen to you if Bergström found out you told me this?"}
        ],
        "outcomes": [
          {"tier": 1, "response": "I'd be fired. Immediately. But 340 families won't have Christmas money this year. And twelve managers will have twice as much. That's not right.", "expression": "guarded", "feedback": "The moral weight is clear but she's holding back evidence.", "note": "340 families lose Christmas money, 12 managers doubled"},
          {"tier": 2, "response": "I'd be fired. But I made copies. The cancellation memo and the bonus memo. Look at the dates — the management bonus was approved three days before the worker bonus was cut. It was planned.", "expression": "open", "feedback": "Documents with dates that prove the sequence. Planned redistribution.", "note": "Copies of both memos, management bonus approved first"},
          {"tier": 3, "response": "Fired? I'm already looking for another job. Because I also saw the January plans. Fifty layoffs. And the twelve managers getting bonuses? They're the ones deciding who gets laid off. They're being rewarded for firing people. I have the layoff list and the bonus list. Three names appear on both — they're getting bonuses and laying off their own workers.", "expression": "open", "feedback": "Managers bonused for planning layoffs. Three are on both lists. This is devastating.", "note": "Managers bonused for planning 50 layoffs, 3 names on both bonus and layoff lists"}
        ],
        "q1_note": "Redistributing from 340 to 12"
      },
      "silence": {
        "q1_response": "... I process payroll. Every month I see the numbers. Usually it's just numbers. This month... the numbers told a story. And it's an ugly one.",
        "expression_hint": "Staring at her hands, the hands that typed the numbers",
        "q2_options": [
          {"text": "Tell me the story the numbers told."},
          {"text": "How long have you been processing payroll here?"},
          {"text": "..."}
        ],
        "outcomes": [
          {"tier": 1, "response": "Eight years. And this is the first time I felt ashamed to hand out the pay slips. Zero for the workers. Ten thousand for the bosses. In the same month. How do you explain that?", "expression": "open", "feedback": "Emotional testimony from someone who processes the money. Human angle.", "note": "8-year payroll clerk ashamed of the disparity"},
          {"tier": 2, "response": "The numbers said: worker bonus line — zero. Management bonus line — doubled. Same budget, same quarter, same signature. And the management memo was backdated so it wouldn't look like they were connected. But I typed them both. I know the real dates.", "expression": "open", "feedback": "She's the witness who typed both memos. Backdating confirmed by the source.", "note": "Typed both memos, knows management memo was backdated"},
          {"tier": 3, "response": "I process everything. Including the January restructuring plan. Fifty names. People I eat lunch with. People whose children go to school with mine. And the managers who put those names on the list? They just got ten thousand kronor each. I can't un-see that. Here — take these. Before I change my mind.", "expression": "open", "feedback": "She's handing over the full package — bonus memos and the layoff list. Breaking point.", "note": "Bonus memos + January layoff list of 50 names, handed over in full"}
        ],
        "q1_note": "The numbers told an ugly story"
      }
    }
  },
  "headlines": [
    {"text": "Steel Mill Cancels Worker Bonus, Doubles Management Pay", "tone": "Factual"},
    {"text": "340 Workers Get Nothing — 12 Managers Get 10,000 Each", "tone": "Confrontational"},
    {"text": "BONUS FOR LAYOFFS: Managers Rewarded for Cutting 50 Jobs", "tone": "Exposing"}
  ]
}
]

def main():
    with open('data/stories.json', 'r') as f:
        existing = json.load(f)
    
    existing_ids = {s['id'] for s in existing}
    added = 0
    for s in STORIES:
        if s['id'] not in existing_ids:
            existing.append(s)
            added += 1
            print(f"  Added: {s['id']} (bv{s['base_value']})")
        else:
            print(f"  Skipped (exists): {s['id']}")
    
    with open('data/stories.json', 'w') as f:
        json.dump(existing, f, indent=2, ensure_ascii=False)
    
    print(f"\nAdded {added} stories. Total: {len(existing)}")

if __name__ == '__main__':
    main()
