# variablen
smaken_ijs = ['aarbei', 'vanille', 'chocola']
prijzen = [3, 4, 5]
#samenvoegen
aanbieding = [prijs * 0.8 for prijs in prijzen]
for i in range(len(smaken_ijs)):
    if smaken_ijs[i] == 'vanille':	 
        reclame_tekst = (f"Vandaag in de aanbieding: {smaken_ijs[i]} 1 liter - slechts €{aanbieding[i]}!")
        print (reclame_tekst)
        punt_index = reclame_tekst.find('.')
        index_nul = reclame_tekst.find('0', punt_index)
        reclame_tekst2 = reclame_tekst[:punt_index]
        print("Volledige tekst:", reclame_tekst) 
        print("Tot aan de 0:", reclame_tekst2)