
import pcinput
from oxo_functies import speelveld, vragen


bord = [['-', "-", "-"], ['-', '-', '-'], ['-', '-', '-']]
speler = "X"
   
speelveld(bord)
#LOOP over programma, 9x herhaald
i=0
for i in range(9):
    print('Speler X :')
    i + 1
    while True:
        rij , kolom = vragen()

        #controle plaats bezet
        if bord[rij][kolom] == "O" or bord[rij][kolom] == "X":
            print("Dit vak is reeds gebruikt !")
            continue

        bord[rij][kolom] = speler
        speelveld(bord)
        #spelerwissel
        if speler == "X":
            speler = "O"
        else:
            speler = "X"

        #print wie aan de beurt
        if speler == 'X':
            print('Speler X : ')
        if speler == 'O': 
            print('Speler O : ')



#controle winnaar horizontaal
if bord[0][0] + bord[0][1] + bord[0][2] == 'OXO':
    winnaar = speler
if bord[1][0] + bord[1][1] + bord[1][2] == 'OXO':
    winnaar = speler
if bord[2][0] + bord[2][1] + bord[2][2] == 'OXO':
    winnaar = speler
#controle winnaar verticaal
if bord[0][0] + bord[1][0] + bord[2][0] == 'OXO':
    winnaar = speler
if bord[0][1] + bord[1][1] + bord[2][1] == 'OXO':
    winnaar = speler
if bord[0][2] + bord[1][2] + bord[2][2] == 'OXO':
    winnaar = speler
#controle winnaar diagonaal
if bord[0][0] + bord[1][1] + bord[2][2] == 'OXO':
    winnaar = speler
if bord[2][0] + bord[1][1] + bord[0][2] == 'OXO':
    winnaar = speler

winnaar = print("U hebt gewonnen !!")