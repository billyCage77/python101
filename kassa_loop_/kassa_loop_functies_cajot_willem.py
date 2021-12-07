import pcinput

#FUNCTIE TERUGGAVE:
#waardes in eurocenten
TWEEHONDERD = 20000  
HONDERD = 10000 
VIJFTIG = 5000 
TWINTIG = 2000 
TIEN = 1000 
VIJF = 500
TWEE = 200 
EEN = 100 
VIJFT_C = 50 
TWINT_C = 20 
TIEN_C = 10 
VIJF_C = 5 
TWEE_C = 2 
EEN_C = 1


def totaal_terug_te_geven(ontv_bedrag, te_bet_bedrag):
    totaal_terug_te_geven = (ontv_bedrag*100 - te_bet_bedrag)

    briefje_200 = totaal_terug_te_geven // TWEEHONDERD
    rest = totaal_terug_te_geven % TWEEHONDERD
    briefje_100 = rest // HONDERD
    rest = rest % HONDERD
    briefje_50 =rest // VIJFTIG
    rest = (rest % VIJFTIG)
    briefje_20 = rest // TWINTIG
    rest = (rest % TWINTIG)
    briefje_10 = rest // TIEN
    rest = (rest % TIEN)
    briefje_5 = rest // VIJF
    rest = (rest % VIJF)
    stuk_2 = rest // TWEE
    rest = (rest % TWEE)
    stuk_1 = rest // EEN
    rest = (rest % EEN)
    stuk_50 = rest // VIJFT_C
    rest = (rest % VIJFT_C)
    stuk_20 = rest // TWINT_C
    rest = (rest % TWINT_C)
    stuk_10 = rest // TIEN_C
    rest = (rest % TIEN_C)
    stuk_5 = rest // VIJF_C
    rest = (rest % VIJF_C)
    stuk_2 = rest // TWEE_C
    rest = (rest % TWEE_C)
    stuk_01 = rest // EEN_C
    rest = (rest % EEN_C)

    if totaal_terug_te_geven != 0:
        print("Geef de volgende briefjes/munten terug:")
        print('*' * 27)
    if briefje_200 > 0:
        print("{:2} {:10} {:6} € ".format(briefje_200, "briefje(s) van", TWEEHONDERD//100))
    if briefje_100 > 0:
        print("{:2} {:10} {:6} € ".format(briefje_100, "briefje(s) van", HONDERD//100))
    if briefje_50 > 0:
        print("{:2} {:10} {:6} € ".format(briefje_50, "briefje(s) van", VIJFTIG//100))
    if briefje_20 > 0:
        print("{:2} {:10} {:6} € ".format(briefje_20, "briefje(s) van", TWINTIG//100))
    if briefje_10 > 0:
        print("{:2} {:10} {:6} € ".format(briefje_10, "briefje(s) van", TIEN//100))
    if briefje_5 > 0:
        print("{:2} {:10} {:6} € ".format(briefje_5, "briefje(s) van", VIJF//100))
    if stuk_2 > 0:
        print("{:2} {:10} {:6} € ".format(stuk_2, "stuk(ken) van", TWEE//100 ))
    if stuk_1 > 0:
        print("{:2} {:10} {:6} € ".format(stuk_1, "stuk(ken) van", EEN//100 ))
    if totaal_terug_te_geven != 0:
        print('*' * 27)

    return totaal_terug_te_geven//100


