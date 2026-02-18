import json

with open('data/npcs.json', 'r') as f:
    npcs = json.load(f)

new_npcs = [
    {"id":"anders_vik","name":"Anders Vik","role":"Familjefar","age":38,"default_expression":"defiant","expressions":["defiant","open","nervous","guarded","neutral"],"unique_detail":"soot_stains","clothing_color":"#5a4a3a","initial_demeanor":"Bestämd men med djup sorg i ögonen"},
    {"id":"kerstin_alven","name":"Kerstin Alvén","role":"Journalist (fd)","age":55,"default_expression":"neutral","expressions":["neutral","guarded","open","defiant"],"unique_detail":"reading_glasses","clothing_color":"#7a5a4a","initial_demeanor":"Lugn, analytisk"},
    {"id":"arvid_magnusson","name":"Arvid Magnusson","role":"Chaufför","age":51,"default_expression":"guarded","expressions":["guarded","nervous","open","neutral","defiant"],"unique_detail":"flat_cap","clothing_color":"#5a5a6a","initial_demeanor":"Orolig, ser sig om ofta"},
    {"id":"arne_wikstrom","name":"Arne Wikström","role":"Handlare","age":47,"default_expression":"neutral","expressions":["neutral","guarded","open","hostile","defiant"],"unique_detail":"apron","clothing_color":"#6a6a5a","initial_demeanor":"Affärsmässig"},
    {"id":"rune_sjoberg","name":"Rune Sjöberg","role":"Byggnadsarbetare","age":44,"default_expression":"open","expressions":["open","guarded","nervous","defiant","neutral"],"unique_detail":"calloused_hands","clothing_color":"#5a6a5a","initial_demeanor":"Rakt på sak"},
    {"id":"bengt_ake_frid","name":"Bengt-Åke Frid","role":"Arkivarie","age":62,"default_expression":"nervous","expressions":["nervous","guarded","open","neutral"],"unique_detail":"bow_tie","clothing_color":"#4a4a5a","initial_demeanor":"Pedantisk och trevande"},
    {"id":"tommy_berg","name":"Tommy Berg","role":"Snickare","age":36,"default_expression":"guarded","expressions":["guarded","open","defiant","nervous","neutral"],"unique_detail":"pencil_ear","clothing_color":"#6a5a4a","initial_demeanor":"Fåordig"},
    {"id":"berit_holm","name":"Berit Holm","role":"Sjuksköterska","age":39,"default_expression":"open","expressions":["open","nervous","guarded","defiant","neutral"],"unique_detail":"nurse_pin","clothing_color":"#8a7a6a","initial_demeanor":"Varm men stressad"},
    {"id":"bo_lundgren","name":"Bo Lundgren","role":"Hamnarbetare","age":48,"default_expression":"hostile","expressions":["hostile","guarded","defiant","neutral","open"],"unique_detail":"anchor_tattoo","clothing_color":"#3a4a5a","initial_demeanor":"Misstänksam"},
    {"id":"maj_britt_olsson","name":"Maj-Britt Olsson","role":"Hembiträde","age":55,"default_expression":"nervous","expressions":["nervous","open","guarded","neutral"],"unique_detail":"kerchief","clothing_color":"#7a6a5a","initial_demeanor":"Tyst, vrider händerna"},
    {"id":"rune_karlsson","name":"Rune Karlsson","role":"Mekaniker","age":31,"default_expression":"neutral","expressions":["neutral","defiant","open","guarded","nervous"],"unique_detail":"oil_stains","clothing_color":"#4a5a4a","initial_demeanor":"Avspänd men skarp"},
    {"id":"astrid_nyberg","name":"Astrid Nyberg","role":"Pensionär","age":71,"default_expression":"open","expressions":["open","guarded","nervous","defiant","neutral"],"unique_detail":"crochet_shawl","clothing_color":"#8a6a7a","initial_demeanor":"Vänlig, bjuder kaffe"},
    {"id":"per_erik_johansson","name":"Per-Erik Johansson","role":"Bonde","age":53,"default_expression":"guarded","expressions":["guarded","defiant","open","hostile","neutral"],"unique_detail":"pipe","clothing_color":"#5a5a4a","initial_demeanor":"Tyst, tuggar pipskaft"},
    {"id":"tomas_falk","name":"Tomas Falk","role":"Kommunsekreterare","age":45,"default_expression":"nervous","expressions":["nervous","guarded","neutral","open"],"unique_detail":"briefcase","clothing_color":"#4a4a4a","initial_demeanor":"Tittar på klockan"},
    {"id":"margareta_holm","name":"Margareta Holm","role":"Vaktmästare","age":49,"default_expression":"neutral","expressions":["neutral","open","guarded","defiant","nervous"],"unique_detail":"key_ring","clothing_color":"#6a5a5a","initial_demeanor":"Praktisk, rakt på sak"},
    {"id":"maj_britt_hansson","name":"Maj-Britt Hansson","role":"Kassörska","age":33,"default_expression":"nervous","expressions":["nervous","open","guarded","defiant"],"unique_detail":"register_stain","clothing_color":"#7a5a6a","initial_demeanor":"Orolig, viskar"},
    {"id":"birgitta_lund","name":"Birgitta Lund","role":"Bibliotekarie","age":41,"default_expression":"open","expressions":["open","nervous","guarded","neutral","defiant"],"unique_detail":"bookmark","clothing_color":"#6a7a5a","initial_demeanor":"Hjälpsam, systematisk"},
    {"id":"olle_magnusson","name":"Olle Magnusson","role":"Brevbärare","age":56,"default_expression":"guarded","expressions":["guarded","open","nervous","defiant","neutral"],"unique_detail":"mailbag","clothing_color":"#5a6a7a","initial_demeanor":"Vet allt, balanserar försiktigt"}
]

npcs.extend(new_npcs)

with open('data/npcs.json', 'w') as f:
    json.dump(npcs, f, ensure_ascii=False, indent=2)

# Verify
with open('data/npcs.json') as f:
    verify = json.load(f)
print(f'NPCs written: {len(verify)}')
