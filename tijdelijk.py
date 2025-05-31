smaken_ijs = ['aarbei', 'vanille', 'chocola']
prijzen = [3, 4, 5]
aanbieding = [prijs * 0.8 for prijs in prijzen]
for i in range(len(smaken_ijs)):
    print(f"{smaken_ijs[i]}: {aanbieding[i]} euro (aanbieding) of {prijzen[i]} euro (normaal)")
    Reclame_tekst = f"Vandaag in de aanbieding: {smaken_ijs[i]} 1 liter - slechts €{aanbieding[i]}!"
Reclame_tekst2 = [:0,]
print(Reclame_tekst2)

