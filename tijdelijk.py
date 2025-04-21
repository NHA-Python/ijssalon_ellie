#Les 7
#1.2
prijzen = {
    "aardbei": 3,
    "vanille": 4,
    "chocolade": 5
}

#1.3
aanbieding = prijzen["aardbei"] * 0.8

#1.4
# Het is onduidelijk wat er nu echt gevraagd wordt.
# Volgens mij klopt de zin niet: "Daar waar nu <aanbieding> staat, plaatst u de variabele met de naam aanbieding. Dat doet u door het maken van een formatted string."
# Dit omdat een formatted string alleen in een print-statement gebruikt kan worden, tenminste zo begrijp ik het uit de lessen.
# Ik denk dat 1 van onderstaande gevraagd wordt.
reclame_tekst = "Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts € " + str(aanbieding)
#print(reclame_tekst)

reclame_tekst1 = "Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts €"
#print(f"{reclame_tekst1} {aanbieding}")

#1.5
reclame_tekst2 = reclame_tekst[:63]
#print(reclame_tekst2)

#1.6
reclame_tekst3 = reclame_tekst2.upper()
#print(reclame_tekst3)

#1.7
reclame_tekst4 = reclame_tekst3.split(" ")
#print(reclame_tekst4)

#1.8
for el in reclame_tekst4:
    if len(el) > 4:
        print(el.upper())
    else:
        print(el.lower())