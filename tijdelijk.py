# variablen
smaken_ijs = ['aarbei', 'vanille', 'chocola']
prijzen = [3, 4, 5]
#samenvoegen
aanbieding = [prijs * 0.8 for prijs in prijzen]
for i in range(len(smaken_ijs)):
    if smaken_ijs[i] == 'vanille':	 
        reclame_tekst = (f"vandaag in de aanbieding: {smaken_ijs[i]} 1 liter - slechts €{aanbieding[i]}!")
        print (reclame_tekst)
        punt_index = reclame_tekst.find('.')
        index_nul = reclame_tekst.find('0', punt_index)
        reclame_tekst2 = reclame_tekst[:punt_index]
        reclame_tekst3 = (reclame_tekst2.swapcase() + reclame_tekst[index_nul:])
        reclame_tekst4 = list = "" + reclame_tekst3 + "!"
        for el in reclame_tekst4:
            print(el)
        reclame_tekst4 = (reclame_tekst3.lower() + reclame_tekst[index_nul:])
        woorden = reclame_tekst4.split()
        for el in woorden:
            if len(el) > 5:
                print (el.upper())
            else:
                print(el.lower())