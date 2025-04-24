from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    prijs_na_korting = prijs * (1 - korting)
    uitvoer = f'''Vandaag in de aanbieding: Emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {format(prijs_na_korting, '.2f')} euro.'''
    return uitvoer

def inkomsten_totaal(inkomsten, btw):
    totaal = 0
    for day in inkomsten:
        totaal += day
    
    uitvoer = f'''Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {totaal * btw} euro btw betaald dient te worden.'''
    return uitvoer

# print(inkomsten_totaal([220, 43, 125, 160, 205, 90, 345],0.09))

def laag_en_hoog(mijn_lijst):
    minmax = []
    minmax.append(min(mijn_lijst))
    minmax.append(max(mijn_lijst))
    return minmax

# print(laag_en_hoog([220, 43, 125, 160, 205, 90, 345]))

def gemiddelde(mijn_lijst):
    totaal = 0
    for day in mijn_lijst:
        totaal += day
    uitvoer = f'''De gemiddelde inkomsten deze week zijn {totaal/len(mijn_lijst)} euro.'''
    return uitvoer

# print(gemiddelde([220, 43, 125, 160, 205, 90, 345]))

def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)

# print(meervoudig([10,5,3,2,1,2,9]))

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0],korte_lijst[1])
    return uitvoer

print(combinatie([10,5,3,2,1,2,9]))