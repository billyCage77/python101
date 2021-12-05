
import pcinput
from oxo_functies import speelveld, vragen


bord = [['-', "-", "-"], ['-', '-', '-'], ['-', '-', '-']]
speler = "X"
   
speelveld(bord)


while True:
    rij , kolom = vragen()
    bord[rij][kolom] = speler
    speelveld(bord)

    if speler == "X":
        speler = "O"
    else:
        speler = "X"



