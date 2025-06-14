Naam_bestand = '"bestand tijdelijk.py gecodeerd"'
woorden = Naam_bestand.split()
for el in woorden:
    if len(el) > 8:
        print (el.upper())
    else:
        print(el.lower())