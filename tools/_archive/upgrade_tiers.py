#!/usr/bin/env python3
"""
Upgrade one Q2 outcome per story to tier 3 for all 20 stories that lack one.
Each upgrade has hand-crafted tier-3 dialogue (dramatic revelation, specific details).
"""
import json

# Key: story title -> (archetype, q2_index, new_outcome_fields)
UPGRADES = {
    "The Dog Show in Småstad": ("friendly", 0, {
        "tier": 3,
        "response": "Related? They LIVE together! Ulla-Karin Persson moved in with the judge last March — I saw the moving van myself. And this isn't the first time: she won in Kisa last year with the same judge. Three shows, three wins. Bengt at the kennel club has a list — he was going to report it to the Swedish Kennel Club but somebody talked him out of it. Guess who.",
        "expression": "open",
        "feedback": "Cohabiting judges, a pattern across shows, and a suppressed complaint. Explosive for a dog show story.",
        "note": "They LIVE together — she won in Kisa last year with the same judge"
    }),
    "The Church Bells That Never Stop": ("friendly", 0, {
        "tier": 3,
        "response": "The Svensson family across the road — their three-year-old wakes up every single night. Mrs. Alm has written to the municipality THREE times. But here's the thing nobody talks about: the bell system was reprogrammed by the vicar's nephew — he's not even an electrician. He installed it wrong and now nobody knows how to fix it. The company that made the system went bankrupt. The diocese KNOWS but won't pay for a real technician because it would mean admitting the nephew botched it.",
        "expression": "open",
        "feedback": "Unqualified installation, cover-up by the diocese, and affected families. Full story.",
        "note": "The vicar's nephew reprogrammed it — he's not even an electrician"
    }),
    "The Shoplifting at ICA": ("friendly", 0, {
        "tier": 3,
        "response": "Everyone knows the Petterssons. The dad drinks. The mom works double shifts. But here's what nobody's saying — Tommy wasn't stealing for himself. He was taking food. Bread, milk, pasta. I checked the list of what he took. No candy, no soda. The family hasn't had a working fridge for two months. Social services were notified in September but NOTHING happened. I have the case number — the school reported it too. Two reports, zero action.",
        "expression": "open",
        "feedback": "Systemic failure — child poverty, social services failing, school reports ignored. This is much bigger than shoplifting.",
        "note": "Social services were notified in September but NOTHING happened"
    }),
    "The New Parking Lot by the Square": ("friendly", 1, {
        "tier": 3,
        "response": "800,000 on paper. But I work at the county administration — I've seen the REAL numbers. The demolition of the Alm villa alone costs 300,000. And the villa is listed as 'cultural heritage interest' in the county's own registry. They skipped the heritage assessment entirely. The municipal commissioner's brother-in-law owns the construction company that got the contract — WITHOUT a public tender. I can show you the procurement documents. It's all there in black and white.",
        "expression": "open",
        "feedback": "Skipped heritage assessment, nepotistic procurement, inflated costs. A corruption story hiding inside a parking lot.",
        "note": "The municipal commissioner's brother-in-law owns the construction company"
    }),
    "Christmas Bazaar at the Factory": ("friendly", 1, {
        "tier": 3,
        "response": "We're collecting for Erik's family — he injured his back in the spring. But what makes me furious is WHY. The forklift he was driving had a broken safety belt. We reported it to management in January. JANUARY! They said they'd fix it. Four months later Erik's in a hospital bed. And now the company says it was 'his own fault' and the insurance won't pay. We found the work order for the belt repair — it was never sent. Someone deleted it from the system.",
        "expression": "open",
        "feedback": "Deleted work order, ignored safety report, insurance fraud angle. The bazaar hides a workplace scandal.",
        "note": "The work order for the belt repair was never sent — someone deleted it"
    }),
    "The Water Leak on Storgatan": ("friendly", 1, {
        "tier": 3,
        "response": "Happened before? It leaked at the same intersection last summer! And here's what I found out — the pipe network is from the 1930s and the municipality commissioned a full inspection in 2019. The report said 40 percent of the pipes need IMMEDIATE replacement. Cost: 12 million. You know what happened to that report? The technical director classified it as 'internal working material' and buried it. Because the election was eight months away. I have a copy. A colleague saved one before they shredded the rest.",
        "expression": "open",
        "feedback": "Buried infrastructure report, classified to avoid election damage, documented evidence. Systematic cover-up.",
        "note": "The technical director classified the report as 'internal working material'"
    }),
    "The Power Outage": ("friendly", 0, {
        "tier": 3,
        "response": "*sighs* Fine. Thirty percent of the grid is from the '40s and '50s. But that's the official number. The REAL number — which I calculated myself last year — is closer to fifty percent. We submitted a risk assessment to the board in March. Category: 'critical.' The board chair said, and I quote, 'We can't alarm people before the rate negotiations.' So they reclassified it to 'elevated' and cut the replacement budget by half. I have the original assessment. They changed the cover page but forgot to update the appendix — it still says 'critical' on page 14.",
        "expression": "open",
        "feedback": "Falsified risk assessment, budget cuts despite critical infrastructure. Documentary evidence with the appendix discrepancy.",
        "note": "They reclassified 'critical' to 'elevated' — the appendix still says critical on page 14"
    }),
    "The Teacher Shortage": ("friendly", 2, {
        "tier": 3,
        "response": "Informed? The principal FORBADE us from telling parents. 'Say they're new colleagues,' she said. We lied at the parent meeting — on the principal's direct orders. But it gets worse. One of the substitutes — I won't say who — has a restraining order. Against a former student. At another school. The principal KNOWS. I saw the background check on her desk. She said, and I quote: 'We can't afford to lose another body.' A person with a restraining order, teaching children. And the parents have no idea.",
        "expression": "open",
        "feedback": "Substitute with restraining order, principal's knowledge, parents deliberately misled. Child safety story.",
        "note": "One substitute has a restraining order — the principal knows and said 'we can't afford to lose another body'"
    }),
    "The Land Deal": ("friendly", 1, {
        "tier": 3,
        "response": "They said 'industrial area' — but the internal planning documents say 'mixed use with municipal priority.' The land was valued at 1.2 million by an independent assessor in 2023. The municipality paid 600,000. And here's the kicker: the farmer who sold it? His daughter works at the planning office. SHE handled the zoning application. I checked the conflict-of-interest registry — she never declared it. The municipal auditor flagged it six months ago but the report was 'delayed' until after the council vote.",
        "expression": "open",
        "feedback": "Conflict of interest, suppressed audit, undervaluation with proof. Full corruption trail.",
        "note": "The farmer's daughter works at the planning office — she handled the zoning application"
    }),
    "The Road Project That Never Gets Finished": ("friendly", 1, {
        "tier": 3,
        "response": "The preliminary study? *dry laugh* It was done by Markgrund AB. The owner is Sven Björk's brother-in-law. That report was worth as much as toilet paper. But I dug deeper — Markgrund has done FOUR municipal contracts in three years. All awarded without competitive bidding. Every single one went over budget. The total overspend across all four? 8.2 million. And Björk sits on the procurement committee that approves these contracts. I filed a complaint with the county administrative board. They said they'd investigate. That was fourteen months ago.",
        "expression": "open",
        "feedback": "Pattern of rigged procurement across four contracts, 8.2 million in overspend, stalled investigation. Systemic corruption.",
        "note": "Markgrund has done FOUR contracts — all without bidding, all over budget, 8.2 million total overspend"
    }),
    "The School Food Nobody Wants to Eat": ("friendly", 1, {
        "tier": 3,
        "response": "YES! Matab — the cheapest option on the market. The food comes chilled from Norrköping, 200 kilometers away. But here's what the parents don't know: the municipal health inspector found bacteria levels ABOVE the limit in three samples last month. Three! The report went to the head of education. She told the inspector to 'retest with new samples' — which of course came back clean because they were taken on a day Matab knew about in advance. I have the original lab results. The inspector is furious but scared of losing her job.",
        "expression": "open",
        "feedback": "Failed health inspections, ordered retesting, supplier tipped off. Children's health at risk with a cover-up.",
        "note": "Bacteria levels ABOVE the limit — the inspector was told to retest after tipping off the supplier"
    }),
    "The Ice Rink Running Out of Money": ("pressure", 2, {
        "tier": 3,
        "response": "Fine, you want the truth? Ove Karlsson's kid plays football. The new football hall got OUR money — 1.4 million redirected. And Karlsson sits on the culture and leisure committee that made the decision. He didn't recuse himself. I have the meeting minutes — there's NO conflict-of-interest declaration. But it gets worse: the football hall's construction company? Småstad Bygg. Karlsson's wife is on their board. They got the contract at 30 percent above the next bid. So taxpayer money flows from the ice rink, through the committee Karlsson controls, to a company his wife profits from. It's all documented.",
        "expression": "open",
        "feedback": "Circular corruption — committee member redirects funds to company where his wife sits on the board. Fully documented chain.",
        "note": "Karlsson's wife is on the board of the construction company that got the contract"
    }),
    "The Library's Last Days": ("friendly", 2, {
        "tier": 3,
        "response": "They save 200,000 on the library. The conference trip to Båstad cost 230,000. But let me tell you what I found in the budget appendix that nobody reads: the building the library is in? The municipality owns it. When the library closes, the lease transfers to a PRIVATE company — Småstad Fastighets AB — at below market rate. Want to guess who's on the board? The municipal commissioner's husband. They're not just cutting a library — they're transferring a public asset to the commissioner's family. The deal was signed in June, three months BEFORE the budget vote.",
        "expression": "open",
        "feedback": "Property transfer to commissioner's family company, signed before the budget vote. The library closure is a front for asset stripping.",
        "note": "The building transfers to Småstad Fastighets AB — the commissioner's husband is on the board"
    }),
    "The Traffic Accident at the School": ("friendly", 1, {
        "tier": 3,
        "response": "Stopped? He braked after the intersection, looked in the rearview mirror and DROVE OFF! Hit and run! Gustavsson at the tobacco shop recognized the company — Fraktbolaget Svea. But here's what I found out after: that same company was involved in a near-miss at Parkskolan last spring. The driver — SAME driver — ran a stop sign. The school reported it. The transport authority did nothing. And the company's operating license was supposed to be reviewed in September — it was 'postponed.' My neighbor works at the transport authority. She says someone called from the municipality and asked them to delay the review. The truck shouldn't even have been on that route.",
        "expression": "open",
        "feedback": "Repeat offender, same driver, suppressed license review, municipal interference. Pattern of negligence with children at risk.",
        "note": "Same driver had a near-miss at Parkskolan — someone from the municipality asked the transport authority to delay the review"
    }),
    "The Bootleg Liquor": ("friendly", 1, {
        "tier": 3,
        "response": "Stig Lund ended up in the hospital last month. Methanol, the doctor said. But nobody reported it — Stig said he 'found the bottle.' But I talked to the nurse who treated him. She said there were TWO more methanol cases that same week. Two! Both claimed they 'found' bottles. The hospital reported it to the police but the cases were filed as 'individual alcohol poisoning' — not connected. And the market supervisor? Rolf Dahl. He takes a table fee from every seller. Cash. No receipts. He knows EXACTLY who's selling the moonshine. He's been confronted twice and both times said 'I can't control what people sell.' Three people poisoned and he's collecting fees from the poisoner.",
        "expression": "open",
        "feedback": "Three methanol cases in one week, cases deliberately not linked, market supervisor profiting from the seller. Public health emergency.",
        "note": "TWO more methanol cases that same week — the market supervisor collects fees and knows who's selling"
    }),
    "The Municipality's Christmas Party": ("friendly", 1, {
        "tier": 3,
        "response": "Three courses, karaoke, the works. But the council chairman also booked a 'separate lounge' for the management team. The invoice says 'conference room rental' — 45,000 kronor. For one evening. And I saw the real bill because my friend works at the restaurant. The 'lounge' included champagne, cigars, and a private chef. That's on TOP of the party budget. And here's the thing — the same restaurant has a catering contract with the municipality worth 800,000 a year. The contract was renewed in November. The Christmas party was December 8th. The chairman signed both. No tender. No comparison.",
        "expression": "open",
        "feedback": "Secret lounge party, disguised invoices, and quid pro quo with restaurant's municipal contract. Taxpayer-funded corruption.",
        "note": "The 'conference room' was champagne and cigars — 45,000 kr, same restaurant got an 800,000 contract renewed weeks earlier"
    }),
    "The Factory Closure": ("friendly", 0, {
        "tier": 3,
        "response": "Warning signs? The night shift was eliminated last summer. Then two machines disappeared — shipped to Lisbon, we found the freight documents. But what really stinks is this: the CEO applied for a RELOCATION GRANT from the EU three months ago. A grant for creating jobs in Portugal — using the same machines they took from us. And the municipality guaranteed a 4 million kronor loan to the company just last year. For 'local investment and expansion.' The money was used to BUY the factory in Lisbon. Our tax money funded our own job losses. The union found the EU application last week.",
        "expression": "open",
        "feedback": "Municipal loan used to fund relocation, EU grant application to create jobs elsewhere with stolen machines. Tax money financing the betrayal.",
        "note": "The municipality's 4 million loan was used to BUY the factory in Lisbon — EU relocation grant applied for"
    }),
    "The Municipal Storage": ("friendly", 1, {
        "tier": 3,
        "response": "Fifteen men in technical services have general access. But the copper room — that's where the expensive stuff vanishes from — only three have keys. Plus Björk. And the council chairman has a 'spare key that nobody uses.' Except somebody IS using it. I installed a camera — on my own, don't tell my boss — two weeks ago. The footage shows someone entering the copper room at 11 PM on a Tuesday. They used the chairman's spare key. I can't make out the face because the lighting is bad, but they loaded materials into a van with municipal plates. The van was logged as 'in service' that night — but the GPS shows it drove to an address in Karlstad. A construction site. I checked: the chairman's son has a renovation company in Karlstad.",
        "expression": "open",
        "feedback": "Camera evidence, GPS trail, chairman's key and son's company. A complete investigation chain.",
        "note": "Camera shows someone using the chairman's spare key at 11 PM — the van GPS went to the chairman's son's construction site in Karlstad"
    }),
    "The Fire in Eriksson's Barn": ("friendly", 1, {
        "tier": 3,
        "response": "That was the STRANGE thing. Eriksson came out after ten minutes — not until the neighbors had already called the department. And he wasn't in his pajamas. Fully dressed. Shoes on. At 2 AM. But here's what I haven't told anyone: I went back the next day to look around. Behind the barn — untouched by fire — I found two empty gasoline cans. New ones, from Byggmax, still had the price tag. And Eriksson's barn? He increased the insurance by 400 percent in September. SEPTEMBER. The fire was in November. The insurance company sent an investigator but somehow the report concluded 'electrical fault.' The investigator? He goes to Eriksson's church. Same congregation.",
        "expression": "open",
        "feedback": "Gasoline cans, 400% insurance increase two months before, biased investigator from same congregation. Arson with insurance fraud.",
        "note": "Two gasoline cans behind the barn — insurance increased 400% in September, investigator goes to Eriksson's church"
    }),
    "The Dead Cat with the Note": ("friendly", 2, {
        "tier": 3,
        "response": "Just me and Sonja at reception. But Björk himself saw it — and he was TERRIFIED. White as a sheet. He didn't call the police. He called a private number — I saw the area code, it was Stockholm. Then he locked himself in his office for an hour. When he came out, he told us to 'forget it happened.' But Sonja kept the note — she photographed it before Björk took it. The handwriting matches a letter that was sent to the building inspector last spring — another threat. Same block letters, same red ink. The building inspector quit two weeks later. Moved to Gothenburg. Nobody asked why. And now the same handwriting shows up with a dead cat. Someone is systematically threatening municipal officials who get in the way.",
        "expression": "open",
        "feedback": "Pattern of threats, matching handwriting, previous official forced out, Björk's terrified reaction and Stockholm call. Organized intimidation.",
        "note": "Sonja photographed the note — handwriting matches a threat letter to the building inspector who quit and fled to Gothenburg"
    }),
}

def main():
    with open("data/stories.json", "r", encoding="utf-8") as f:
        stories = json.load(f)
    
    updated = 0
    for story in stories:
        title = story["title"]
        if title not in UPGRADES:
            continue
        
        arch, q2_idx, new_fields = UPGRADES[title]
        interview = story.get("interview", {})
        branches = interview.get("branches", {})
        
        if arch not in branches:
            print(f"ERROR: {title} has no branch '{arch}'")
            continue
        
        outcomes = branches[arch].get("outcomes", [])
        if q2_idx >= len(outcomes):
            print(f"ERROR: {title} branch '{arch}' has no outcome index {q2_idx}")
            continue
        
        old_tier = outcomes[q2_idx].get("tier", 0)
        outcomes[q2_idx].update(new_fields)
        updated += 1
        print(f"OK: \"{title}\" — {arch} Q2[{q2_idx}]: tier {old_tier} -> 3")
    
    with open("data/stories.json", "w", encoding="utf-8") as f:
        json.dump(stories, f, indent=2, ensure_ascii=False)
    
    print(f"\nDone: {updated} stories upgraded to include tier 3.")

if __name__ == "__main__":
    main()
