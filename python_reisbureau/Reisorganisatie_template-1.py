# opvragen aantal volwassenen en aantal kinderen
#
# berekenen vervoer                                             --> functie
# berekenen standaard_kamerprijs per nacht afh van hotelkeuze   --> functie
# bereken supplement_kamerprijs afhankelijk van type kamer      --> functie
# berekenen van aantal_nachten  8,9,10,11 = -1, vanaf 12 = -2   --> functie
# bereken kostprijs eten * aantal_nachten * aantal_personen     --> functie
#
# berekenen kostprijs voor volwassenen =  supplement_kamerprijs * aantal_volw * aantal_nachten
# berekenen kostprijs voor de kinderen = (supplement_kamerprijs * aantal_kind * aantal_nachten) * 50% korting
# berekenen totale kostprijs = kostprijs vervoer + kostprijs volw + kostprijs kind + kostprijs eten

from pcinput import getInteger
from pcinput import getLetter

# 7 + 1 gratis en 10 + 2 gratis
# vanaf 12 dagen heb je recht op 2 dagen gratis (10 + 2)
# stel je wenst maar 11 dagen te blijven, dan heb je maar recht op 1 gratis dag (10+1gratis)
# die 1 gratis dag blijft geldig op alle boekingen vanaf 8 dagen (dus groter dan 7)
def get_aantal_nachten():
    pass
    # return nachten,gratis_nachten

def get_vervoer():
    pass
    # return type_vervoer,naam_vervoer,kost_vervoer

def get_hotel():
    pass
    # return type_hotel,naam_hotel,kost_hotel

# afh van type kamer komt er al dan niet een supplement of korting bij
# parameter is standaard_kamerprijs van hotel
def get_kamer(hotel_kamerkost):
    pass
    # return type_kamer,naam_kamer,kost_kamer

# type maaltijd
def get_maaltijd():
    pass
    # return type_maaltijd,naam_maaltijd,kost_maaltijd


# *******************************
# * H O O F D P R O G R A M M A *
# *******************************

# *******************************
# * 1 Opvragen input
# *******************************
# aantal personen opvragen

# --> print("aantal_personen: ", aantal_volwassenen,"volwassenen +",aantal_kinderen,"kinderen")
# aantal_nachten, berekenen gratis nachten (7+1, 10+2)

# --> print("aantal nachten: ", aantal_nachten,"met", gratis_nachten,"gratis")
#type vervoer?

# --> print("vervoer: ",vervoer_type,vervoer_kost, vervoer_naam)
#type hotel?

# --> print("hotel: ", hotel_type, hotel_naam, hotel_kost)
# type kamer?

# --> print("kamer: ", kamer_type,kamer_naam,kamer_kost)
# type maaltijd?

# --> print("maaltijd: ", maaltijd_type,maaltijd_naam,maaltijd_kost)

# *******************************
# * 2 berekeningen maken
# *******************************
## aantal_personen = 
## te_betalen_nachten= 
#berekenen kosten voor vervoer (opletten : prijs is enkele reis)
## kosten_vervoer=
# berekenen kosten kamer voor de volwassenen en de kinderen (-50%)
## kosten_kamer_volw = 
## kosten_kamer_kind = 
# berekenen kosten maaltijden
## kosten_maaltijden=
# berekenen van de totale kostprijs
## kosten_totaal = 

# *******************************
# * 3. Afdrukken
# *******************************

