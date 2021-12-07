
import pcinput
from oxo_functies import speelveld, vragen


bord = [['-', "-", "-"], ['-', '-', '-'], ['-', '-', '-']]
speler = "X"
   
speelveld(bord)

print('Speler X :')
while True:
    rij , kolom = vragen()
    bord[rij][kolom] = speler
    speelveld(bord)

    if speler == "X":
        speler = "O"
    else:
        speler = "X"

    if speler == 'X':
        print('Speler X : ')
    if speler == 'O':
        print('Speler O : ')


#controle plaats bezet

#controle winnaar horizontaal
if bord[0:0] [0:1] [0:2] == ['O'] ['X'] ['O']:
if bord[1:0] [1:1] [1:2] == ['O'] ['X'] ['O']:
if bord[2:0] [2:1] [2:2] == ['O'] ['X'] ['O']:
#controle winnaar verticaal
if bord[0:0] [1:0] [2:0] == ['O'] ['X'] ['O']:
if bord[0:1] [1:1] [2:1] == ['O'] ['X'] ['O']:
if bord[0:2] [1:2] [2:2] == ['O'] ['X'] ['O']:
#controle winnaar diagonaal
if bord[0:0] [1:1] [2:2] == ['O'] ['X'] ['O']:
if bord[2:0] [1:1] [0:2] == ['O'] ['X'] ['O']:
