import pcinput

def speelveld(bord):
    print('  1 2 3')
    for rij in range(3):
        print(rij + 1, end=" ")
        for kol in range (3):
            print(bord[rij] [kol], end = " ")
        print()

def vragen():
    while True:
        try:
            rij = pcinput.getInteger("Geef een rij nummer in: ")
            if rij > 2:
                ValueError
            kolom = pcinput.getInteger ("Geef een kolom nummer in: ")
            if kolom > 2:
                ValueError
        except ValueError:
            print( "Probeer opnieuw" )
            continue
        return rij, kolom

