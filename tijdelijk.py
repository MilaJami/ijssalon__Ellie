# variablen
smaken_ijs = ['aarbei', 'vanille', 'chocola']
prijzen = [3, 4, 5]
#samenvoegen
aanbieding = [prijs * 0.8 for prijs in prijzen]
for i in range(len(smaken_ijs)):
    if smaken_ijs[i] == 'aardbei' or smaken_ijs[i] == 'chocola':
        continue
 #  print (f"{smaken_ijs[i]}: {aanbieding[i]} euro (aanbieding) of {prijzen[i]} euro (normaal)")
    reclame_tekst = (f"Vandaag in de aanbieding: {smaken_ijs[i]} 1 liter - slechts €{aanbieding[i]}!")
    print (reclame_tekst)