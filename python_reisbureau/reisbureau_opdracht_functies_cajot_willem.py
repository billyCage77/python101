from pcinput import getString, getInteger
from reisbureau_opdracht import aantal_kind, aantal_volw
# kost vervoer ENKELE REIS !!!!!
ENKELE_REIS_VLIEGTUIG = 200
ENKELE_REIS_BUS = 50
EIGEN_WAGEN = 0

# prijs PER NACHT !!!
PRIJS_HOTEL_ZEEZICHT = 30
PRIJS_HOTEL_DUINENZICHT = 25

# optie zeezicht : supplement 10% PER NACHT  !!!!
# optie balkon : 20€ extra PER NACHT !!!!
BALKON = 20
# optie luxesuite : 40€ extra PER NACHT !!!!
SUITE = 40
# optie eten PER NACHT !!!!
ONTBIJT = 10
HALF_PENSION = 30
VOL_PENSION = 40

# kortingen: kind 50% korting op kamer en op kamer opties

#vervoer
def kosten_vervoer(aantal_volw, aantal_kind):    
    vervoer = getString("Hoe zal u naar de bestemming reizen? Met de auto, bus of met het vliegtuig? ")
    if vervoer == "auto":
        kosten_vervoer = EIGEN_WAGEN
    if vervoer == "bus":
        kosten_vervoer = (ENKELE_REIS_BUS * 2) * (aantal_kind + aantal_volw)
    if vervoer == "vliegtuig":
        kosten_vervoer = (ENKELE_REIS_VLIEGTUIG * 2) * (aantal_kind + aantal_volw)
    return kosten_vervoer, vervoer

#verblijf
def kosten_verblijf(aantal_nachten, aantal_volw, aantal_kind, welk_hotel):
    aantal_nachten = getInteger("Aan hoeveel overnachtingen had u gedacht? (minstens 1) ")
    welk_hotel = getString("In welk hotel gaat u verblijven? Hotel Zeezicht of hotel Duinenzicht? zee/duin ")
    if aantal_volw > 0 and welk_hotel == "zee":
        kosten_volw = (aantal_nachten * PRIJS_HOTEL_ZEEZICHT)
    else:
        kosten_volw = (aantal_nachten * PRIJS_HOTEL_DUINENZICHT)
    
    if aantal_kind > 0 and welk_hotel == "zee":
        kosten_kind = (aantal_nachten * PRIJS_HOTEL_ZEEZICHT) * 0.5
    else:
        kosten_kind = (aantal_nachten * PRIJS_HOTEL_DUINENZICHT) * 0.5
    kosten_verblijf = kosten_volw + kosten_kind
    return kosten_verblijf, kosten_volw, kosten_kind

#opties
def opties(optie_suite, optie_zeezicht, optie_balkon, aantal_nachten, kosten_volw):
    optie_suite = getString("Wenst u een luxesuite? ja/nee ")
    optie_zeezicht = getString("Wenst u een kamer met zicht op zee? ja/nee ")
    optie_balkon = getString("Zou u graag een balkon hebben? ja/nee ")
    if optie_suite == "ja":
        luxe = aantal_nachten * SUITE
    if optie_balkon == "ja":
        balkon_optie = aantal_nachten * BALKON
    if optie_zeezicht == "ja":
        zeezicht_optie = kosten_volw * 1.1
    opties = luxe + balkon_optie + zeezicht_optie
    return opties, luxe, balkon_optie, zeezicht_optie
