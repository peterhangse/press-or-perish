#!/usr/bin/env python3
"""
Redistribute tier 3 paths from friendly to the archetype that fits each NPC.
Each placement is based on who the interviewee IS and what approach cracks them.

Steps per story:
1. Restore the friendly outcome to its original (pre-upgrade) state
2. Promote the target archetype's Q2 outcome to tier 3 with new dialogue

NPC logic:
- direct:    practical people, witnesses, reps who respect factual questions
- pressure:  officials, politicians, guilty parties who crack under confrontation
- silence:   nervous whistleblowers, guilt-ridden, emotional, scared sources
"""
import json, copy

# ─── Load both versions ───
with open("/tmp/stories_before_upgrade.json", "r", encoding="utf-8") as f:
    originals = {s["title"]: s for s in json.load(f)}

with open("data/stories.json", "r", encoding="utf-8") as f:
    stories = json.load(f)

# ─── Moves: (old_arch, old_q2_idx) -> (new_arch, new_q2_idx, new_outcome) ───
# Ice Rink stays on pressure — not in this dict.
MOVES = {
    # ──── DIRECT (7) ────
    # Witnesses, practical workers, union reps who respect factual questions

    "The Dog Show in Småstad": {
        # Maj-Britt Olsson (Kennel Club Treasurer) — knows the admin process
        # "How was Rolf Danielsson chosen as judge?" breaks open the rigged selection
        "old": ("friendly", 0),
        "new": ("direct", 1, {
            "tier": 3,
            "response": "Chosen? Ha! Nobody 'chose' him. Ulla-Karin SUGGESTED him — to her own sister on the board. They didn't even ask the kennel club. And this isn't the first time: Rolf judged in Kisa last year, same breed class, same winner. I have the protocols from THREE shows. Bengt was going to report it to the Swedish Kennel Club — but Ulla-Karin's sister got him voted off the board first. The whole selection process is a sham. I can show you the minutes.",
            "expression": "open",
            "feedback": "Rigged selection process, pattern across multiple shows, whistleblower silenced. Full story.",
            "note": "Same judge, same winner across THREE shows — Bengt was voted off the board to silence him"
        }),
    },

    "Christmas Bazaar at the Factory": {
        # Berit Holm (Union representative) — union reps respond to numbers and facts
        # "What kind of budget are we talking about?" triggers her real anger
        "old": ("friendly", 1),
        "new": ("direct", 0, {
            "tier": 3,
            "response": "Budget? We raised 14,000 last year. All of it was supposed to go to Erik's family — he broke his back on a forklift with a broken safety belt. But here's what I found in the books: management took 3,000 as 'administrative overhead.' For a CHARITY bazaar! And that forklift? We reported the belt in January. JANUARY! The work order was filed, then someone deleted it from the system. Four months later Erik's in the hospital, and the company says it was 'his own fault.' The insurance won't pay because there's no work order. Because somebody erased it.",
            "expression": "open",
            "feedback": "Deleted work order, management skimming charity funds, falsified safety records. The bazaar hides a workplace scandal.",
            "note": "The work order for the belt repair was deleted — management took 3,000 from the charity fund"
        }),
    },

    "The Water Leak on Storgatan": {
        # Rune Karlsson (Caretaker) — practical man, responds to practical questions
        # "One single excavator for the whole municipality?" gets him going
        "old": ("friendly", 1),
        "new": ("direct", 0, {
            "tier": 3,
            "response": "One excavator — that's right! And it's from 1978! But that's not even the real problem. The pipe network is from the 1930s and the municipality commissioned an inspection in 2019. The report said 40 percent needs IMMEDIATE replacement. Cost: 12 million. You know what happened? The technical director classified it as 'internal working material' and buried it — because the election was eight months away. I have a copy. A colleague saved one before they shredded the rest. One excavator, one old pipe network, and one buried report. That's Småstad for you.",
            "expression": "open",
            "feedback": "Buried infrastructure report, classified to avoid election damage. Systematic cover-up behind a 'simple' water leak.",
            "note": "The technical director classified the inspection report as 'internal working material' and shredded copies"
        }),
    },

    "The Land Deal": {
        # Erik Persson (Farmer) — straightforward, responds to direct comparisons
        # "Why was the price so much lower than Olsson's?" hits the nerve
        "old": ("friendly", 1),
        "new": ("direct", 2, {
            "tier": 3,
            "response": "Lower? Let me tell you why. Olsson's land was zoned 'residential' — mine was kept as 'agricultural' right up until the sale. But the INTERNAL planning documents say 'mixed use with municipal priority.' An independent assessor valued my land at 1.2 million in 2023. The municipality paid 600,000. And here's the kicker: the farmer who — well, that's me — my daughter works at the planning office. No wait, I mean the COUNCIL'S daughter. Björk's girl. SHE handled the zoning application. She never declared the conflict. The municipal auditor flagged it six months ago but the report was delayed until after the council voted.",
            "expression": "open",
            "feedback": "Conflict of interest, suppressed audit, undervaluation with proof. The farmer connects the dots when asked directly.",
            "note": "Björk's daughter handled the zoning — the auditor's report was delayed until after the vote"
        }),
    },

    "The School Food Nobody Wants to Eat": {
        # Birgitta Lund (School Board Member) — angry, wants to point fingers
        # "Who decided to switch to Matab?" lets her name names
        "old": ("friendly", 1),
        "new": ("direct", 0, {
            "tier": 3,
            "response": "WHO decided? The head of education, Annika Ström. She pushed it through in June — no board vote, no consultation. Matab was the cheapest bid by far. The food comes chilled from Norrköping, 200 kilometers away. But here's what the parents don't know: the municipal health inspector found bacteria levels ABOVE the limit in three samples last month. Three! The report went straight to Ström. She told the inspector to 'retest with new samples' — and tipped off Matab about the date. Of course the retest came back clean. I have the original lab results. The inspector is furious but scared for her job.",
            "expression": "open",
            "feedback": "Named the decision-maker, failed health inspections, ordered retesting with supplier tipped off. Children's health at risk.",
            "note": "Annika Ström pushed Matab through without a board vote — bacteria levels above the limit, retesting rigged"
        }),
    },

    "The Traffic Accident at the School": {
        # Maj-Britt Hansson (Witness) — saw it happen, responds to specific questions
        # "Did you see the truck's logo or license plate?" gets the facts
        "old": ("friendly", 1),
        "new": ("direct", 0, {
            "tier": 3,
            "response": "Yes! Fraktbolaget Svea — big red letters on the side. And I got the last three digits of the plate: 847. But here's what I found out after: that same company was involved in a near-miss at Parkskolan last spring. The driver — SAME driver, I recognized the beard — ran a stop sign. The school reported it. The transport authority did nothing. And the company's license was supposed to be reviewed in September — it was 'postponed.' My neighbor works at the transport authority. She says someone called from the municipality and asked them to delay. The truck shouldn't even have been on that route — it's a school zone.",
            "expression": "open",
            "feedback": "Plate number, company ID, repeat offender, same driver, suppressed license review. Rock-solid witness testimony.",
            "note": "Fraktbolaget Svea, plate ending 847 — same driver had a near-miss at Parkskolan, license review was postponed"
        }),
    },

    "The Municipal Storage": {
        # Karl Lindström (Worker) — proactive, installed his own camera
        # "Who among the municipal leadership is renovating right now?" aligns with his investigation
        "old": ("friendly", 1),
        "new": ("direct", 1, {
            "tier": 3,
            "response": "Renovating? *leans in* The council chairman's son. Big renovation in Karlstad. And guess what I did — I installed a camera two weeks ago. My own camera. Don't tell my boss. The footage shows someone entering the copper room at 11 PM on a Tuesday. They used the chairman's spare key — the one 'nobody uses.' Loaded materials into a van with municipal plates. The van was logged as 'in service' that night, but the GPS shows it drove straight to Karlstad. To a construction site. The chairman's son's site. Copper pipes, fittings, insulation. Thousands of kronor. All on camera.",
            "expression": "open",
            "feedback": "Camera evidence, GPS trail, chairman's key, son's construction site. A complete investigation chain from one direct question.",
            "note": "Camera shows chairman's key used at 11 PM — van GPS went to the chairman's son's construction site in Karlstad"
        }),
    },

    # ──── PRESSURE (7) ────
    # Politicians, officials, guilty parties who crack under confrontation

    "The Church Bells That Never Stop": {
        # Gunnar Ek (Farmer, church neighbor) — frustrated, cracks HARDER under pressure
        # "Has the nighttime ringing been going on since the new mechanism was installed?" connects the dots
        "old": ("friendly", 0),
        "new": ("pressure", 2, {
            "tier": 3,
            "response": "Since the new mechanism? YES! That's exactly when it started! The vicar's nephew installed it — kid's not even an electrician! He did it for free, and now nobody knows how to fix it. The company that made the system went bankrupt. The diocese KNOWS but won't pay for a real technician because it means admitting the nephew botched it. Meanwhile, the Svenssons' three-year-old wakes up every night and Mrs. Alm has written to the municipality three times. You put that in the paper. Every word.",
            "expression": "open",
            "feedback": "Unqualified installation, diocese cover-up, affected families. The frustrated farmer gave you everything when you pressed the right button.",
            "note": "The vicar's nephew installed it — not an electrician — the diocese won't pay to fix his mistake"
        }),
    },

    "The New Parking Lot by the Square": {
        # Rune Sjöberg (Politician, Social Democrats) — politicians crack under specific allegations
        # "Is it true that Björk owns land adjacent to the square?" is the confrontation
        "old": ("friendly", 1),
        "new": ("pressure", 2, {
            "tier": 3,
            "response": "*long pause* Who told you that? *shifts in chair* Fine. Yes, the Alm villa demolition — it wasn't in the original plan. It was added AFTER the land survey. And the survey was done by Björk's brother-in-law's company. Without a public tender. The demolition alone costs 300,000 but the villa is listed as 'cultural heritage interest' in the county's registry. They skipped the heritage assessment entirely. And yes — Björk's wife owns the adjacent plot. When the parking lot goes in, that plot doubles in value. But you didn't hear that from me.",
            "expression": "guarded",
            "feedback": "Pressed the politician on the specific allegation — he cracked and revealed nepotistic procurement, skipped heritage assessment, and Björk's wife's land profit.",
            "note": "Björk's wife owns adjacent land — his brother-in-law did the survey without tender"
        }),
    },

    "The Road Project That Never Gets Finished": {
        # Bengt-Åke Frid (Project Manager) — bureaucrat who cracks when confronted with the allegation
        # "Is it true that Markgrund AB got the contract despite lacking experience?" is the key
        "old": ("friendly", 1),
        "new": ("pressure", 1, {
            "tier": 3,
            "response": "*tight-lipped* Where did you... Fine. Markgrund AB. Owned by Sven Björk's brother-in-law. That preliminary study was garbage — I TOLD them. But it gets worse. Markgrund has done FOUR municipal contracts in three years. All without competitive bidding. Every single one went over budget. Total overspend: 8.2 million. And Björk sits on the procurement committee. I filed a complaint with the county administrative board fourteen months ago. They said they'd investigate. Nothing. You want to know why nobody talks? Because Björk controls who gets contracts in this town. And everyone knows it.",
            "expression": "open",
            "feedback": "Confronted the project manager — he confirmed the rigged procurement pattern. Four contracts, 8.2 million overspend, stalled investigation.",
            "note": "Markgrund AB — four no-bid contracts, 8.2 million overspend, Björk controls procurement"
        }),
    },

    "The Bootleg Liquor": {
        # Lars Björk (Innkeeper) — pressing on police inaction enrages him
        # "What do you mean the police do nothing?" makes him explode
        "old": ("friendly", 1),
        "new": ("pressure", 1, {
            "tier": 3,
            "response": "NOTHING! I've called three times! Constable Hedlund says 'we can't control what people sell at a market.' But I talked to the nurse who treated Stig Lund — methanol poisoning. And she said there were TWO more cases that same week! Two! Both claimed they 'found' bottles. The hospital reported it but the police filed them as separate 'individual alcohol poisoning' cases — deliberately unconnected. And Rolf Dahl — the market supervisor — he takes a table fee from every seller. Cash. No receipts. He knows EXACTLY who's selling. Three people poisoned and he collects from the poisoner while the police look the other way.",
            "expression": "open",
            "feedback": "Pressed about police inaction — the innkeeper exploded with three methanol cases, deliberate case separation, and the market supervisor's complicity.",
            "note": "THREE methanol cases in one week — police deliberately filed them separately, market supervisor profits"
        }),
    },

    "The Factory Closure": {
        # Sven-Erik Berg (Union rep, IF Metall) — confronting about the secret CEO dinner
        # "The CEO invited the union chairman to dinner in September. What was that about?"
        "old": ("friendly", 0),
        "new": ("pressure", 0, {
            "tier": 3,
            "response": "*goes quiet, then angry* How do you know about that dinner? Fine. The CEO wanted Holm to keep quiet about the plan — offered him a 'consulting role' at the Portugal factory. Holm turned him down but he didn't TELL us about the offer until last week. Meanwhile, two machines disappeared — shipped to Lisbon, we found the freight documents. And the municipality guaranteed a 4 million kronor loan last year for 'local investment and expansion.' That money was used to BUY the Lisbon factory. Our tax money funded our own job losses. The CEO also applied for an EU RELOCATION GRANT — for creating jobs in Portugal. With OUR machines.",
            "expression": "open",
            "feedback": "Confrontation about the dinner cracked it open — bribe attempt, municipal loan misused, EU grant fraud. The union rep couldn't hold back once pressed.",
            "note": "CEO tried to bribe union chairman — 4 million municipal loan used to buy the Portugal factory"
        }),
    },

    "The Fire in Eriksson's Barn": {
        # Astrid Nyberg (Neighbor) — pressing with THE question makes her blurt it out
        # "Is there any reason Eriksson would want the barn to burn?" shows you've figured it out
        "old": ("friendly", 1),
        "new": ("pressure", 2, {
            "tier": 3,
            "response": "*whispers* You've figured it out too? I went back the next day. Behind the barn — untouched by fire — I found two gasoline cans. New ones, from Byggmax, price tags still on. And Eriksson? He increased the insurance by FOUR HUNDRED percent in September. The fire was in November. The insurance company sent an investigator, but the report says 'electrical fault.' The investigator goes to Eriksson's church. Same congregation. Same prayer group. And Eriksson wasn't in his pajamas at 2 AM — he was fully dressed. Shoes on. He was WAITING for it.",
            "expression": "open",
            "feedback": "You named the suspicion — and the scared neighbor confirmed everything. Gasoline cans, 400% insurance increase, biased investigator from same church.",
            "note": "Gasoline cans behind the barn, insurance increased 400% two months before, investigator is in Eriksson's congregation"
        }),
    },

    # ──── SILENCE (6) ────
    # Nervous whistleblowers, guilt-ridden, emotional, scared sources

    "The Shoplifting at ICA": {
        # Per-Erik Johansson (Shopkeeper) — feels guilty, silence lets him unburden
        # "How is the boy doing now?" — silence + care = confession
        "old": ("friendly", 0),
        "new": ("silence", 2, {
            "tier": 3,
            "response": "*long silence, then quietly* He's... not doing well. *rubs eyes* The thing is — Tommy wasn't stealing for himself. I checked the list. Bread, milk, pasta. No candy. No soda. The family hasn't had a working fridge for two months. The dad drinks everything away. Social services were notified in September — the school sent a report too. Two reports. Zero action. *voice breaks* I've been giving him day-old bread for weeks. Pretending we're throwing it away. But he needs real help. Not bread from a guilty shopkeeper.",
            "expression": "open",
            "feedback": "Silence let the guilt pour out — child poverty, social services failing, school reports ignored. Much bigger than shoplifting.",
            "note": "Tommy was stealing food — social services got two reports and did nothing"
        }),
    },

    "The Power Outage": {
        # Bo Lundgren (Utility chief) — bureaucrat who wants to talk but can't officially
        # "The press release was pretty short. What was left out?" — silence gives him permission
        "old": ("friendly", 0),
        "new": ("silence", 1, {
            "tier": 3,
            "response": "*looks around, lowers voice* What was left out? Everything. Thirty percent old cables — that's the official number. The real number is closer to fifty. I wrote a risk assessment in March. Category: 'critical.' The board chair said — and I can quote him because I wrote it down — 'We can't alarm people before the rate negotiations.' So they reclassified it to 'elevated' and cut the replacement budget by half. I kept the original. They changed the cover page but forgot to update the appendix — it still says 'critical' on page 14. I've been waiting for someone to ask the right question.",
            "expression": "open",
            "feedback": "Silence gave the bureaucrat space to reveal what he couldn't say officially — falsified risk assessment, the appendix still proves it.",
            "note": "Risk assessment reclassified from 'critical' to 'elevated' — the appendix on page 14 still says critical"
        }),
    },

    "The Teacher Shortage": {
        # Margareta Lund (Teacher) — burdened by guilt, needs space to confess
        # "Is there documentation of the substitute status?" — silence draws out the secret
        "old": ("friendly", 2),
        "new": ("silence", 2, {
            "tier": 3,
            "response": "*very long pause* ...Yes. There's documentation. I've seen the files on the principal's desk. The background checks. *whispers* One of the substitutes — I can't say who — has a restraining order. Against a former student. At another school. The principal KNOWS. I SAW the background check. She said: 'We can't afford to lose another body.' Those were her exact words. A person with a restraining order against a child, teaching children. And the parents think they're just 'new colleagues.' We lied to them. On the principal's direct orders.",
            "expression": "open",
            "feedback": "Silence let the teacher confess what she couldn't say outright — a substitute with a restraining order, principal's knowledge, parents deliberately misled.",
            "note": "One substitute has a restraining order against a student — the principal said 'we can't afford to lose another body'"
        }),
    },

    "The Library's Last Days": {
        # Margareta Holm (Librarian since 1962) — emotional, 30+ years of observation
        # "Is there any hope?" — silence draws out what she's pieced together over decades
        "old": ("friendly", 2),
        "new": ("silence", 2, {
            "tier": 3,
            "response": "*quiet for a long time* Hope? No. Because it was never about saving money. *takes out a folder* I've worked here for 32 years. I read every budget document. The library costs 200,000. The conference trip to Båstad cost 230,000. But listen to this: when the library closes, this building — which the municipality owns — transfers to a private company. Småstad Fastighets AB. Below market rate. And the commissioner's husband sits on that company's board. The transfer agreement was signed in June. Three months BEFORE the budget vote. They're not closing a library. They're handing a building to the commissioner's family.",
            "expression": "open",
            "feedback": "Silence let the librarian reveal 32 years of careful observation — the closure is a front for transferring public property to the commissioner's family.",
            "note": "The building transfers to Småstad Fastighets AB — commissioner's husband on the board, deal signed before the vote"
        }),
    },

    "The Municipality's Christmas Party": {
        # Kerstin Alvén (Municipal secretary) — nervous, needs safe space
        # "I'm listening, Kerstin. Tell me what you think people should know."
        "old": ("friendly", 1),
        "new": ("silence", 0, {
            "tier": 3,
            "response": "*fidgets, then slowly* My friend works at the restaurant. She showed me the REAL bill. The 'separate lounge' the council chairman ordered? The invoice to the municipality says 'conference room rental' — 45,000 kronor. But the real bill shows champagne, cigars, a private chef. All on top of the party budget. And... *looks at door* ...the same restaurant has a catering contract with the municipality. 800,000 a year. Renewed in November. The party was December 8th. The chairman signed both. No tender. No comparison. It's... it's not right. I see this paperwork every day and nobody asks.",
            "expression": "open",
            "feedback": "Silence gave the nervous secretary courage — disguised invoices, champagne lounge, quid pro quo with the restaurant's contract. She'd been waiting for someone to listen.",
            "note": "The 'conference room' was champagne and cigars — 45,000 kr, same restaurant got an 800,000 contract renewed weeks earlier"
        }),
    },

    "The Dead Cat with the Note": {
        # Olle Magnusson (Town messenger) — scared, needs trust and patience
        # "Why did Björk want you to stay quiet?" shows you believe him
        "old": ("friendly", 2),
        "new": ("silence", 1, {
            "tier": 3,
            "response": "*looks around nervously* Because he knows who did it. He called a private number — Stockholm area code — not the police. Locked himself in for an hour. And Sonja at reception — she photographed the note before Björk took it. The handwriting... *swallows* ...it matches a letter that was sent to the building inspector last spring. Same block letters, same red ink. Another threat. The building inspector quit two weeks later. Moved to Gothenburg. Nobody asked why. And now the same handwriting shows up with a dead cat. Someone is systematically threatening municipal officials who get in the way. And Björk knows who.",
            "expression": "open",
            "feedback": "Patience and silence unlocked the scared messenger — matching handwriting, previous threat, building inspector fled. Organized intimidation.",
            "note": "Sonja photographed the note — handwriting matches a threat to the building inspector who quit and fled"
        }),
    },
}


def main():
    updated = 0
    for story in stories:
        title = story["title"]
        if title not in MOVES:
            continue

        move = MOVES[title]
        old_arch, old_idx = move["old"]
        new_arch, new_idx, new_outcome = move["new"]
        
        branches = story["interview"]["branches"]
        
        # 1. Restore old path to its original state
        orig = originals[title]
        orig_outcome = orig["interview"]["branches"][old_arch]["outcomes"][old_idx]
        branches[old_arch]["outcomes"][old_idx] = copy.deepcopy(orig_outcome)
        old_tier = orig_outcome.get("tier", 0)
        
        # 2. Promote new path to tier 3
        branches[new_arch]["outcomes"][new_idx].update(new_outcome)
        
        updated += 1
        print(f"OK: \"{title}\" — restored {old_arch}[{old_idx}] to tier {old_tier}, promoted {new_arch}[{new_idx}] to tier 3")

    with open("data/stories.json", "w", encoding="utf-8") as f:
        json.dump(stories, f, indent=2, ensure_ascii=False)
    
    print(f"\nDone: {updated} stories redistributed.")


if __name__ == "__main__":
    main()
