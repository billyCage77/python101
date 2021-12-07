from kassa_loop_functies_cajot_willem import totaal_terug_te_geven
import pcinput
pcinput.getInteger
pcinput.getString

#user input
naam_bediende = pcinput.getString("Voer uw naam in aub: ")
totaal_kassa = pcinput.getInteger("Geef het huidige kassa totaal in: ")


#LOOP 
stoppen = "nee"
while stoppen != 'ja':
    totaal_mosselen = 0
    totaal_koning = 0
    totaal_ijsje = 0
    totaal_drank = 0
    totaal_mosselen = pcinput.getInteger("Hoeveel porties mosselen-friet? ")
    totaal_koning = pcinput.getInteger("Hoeveel porties koninginnehapjes? ")
    totaal_ijsje = pcinput.getInteger("Hoeveel ijsjes? ")
    totaal_drank = pcinput.getInteger("Hoeveel drankjes? ")

    #korting
    korting = 0
    te_bet_bedrag = 0
    totaal = (totaal_mosselen * 2000 + totaal_koning * 1000 + totaal_ijsje * 300 + totaal_drank * 200) 

    if totaal_mosselen >= 2:
        if 5000 < totaal < 10000:
            korting = 500
            te_bet_bedrag = totaal - korting
        if 10000 < totaal < 15000 and totaal_mosselen >= 2:
            korting = 1000
            te_bet_bedrag = totaal - korting
        if totaal >= 15000 and totaal_mosselen >= 2:
            korting = 2000
            te_bet_bedrag = totaal - korting
    else:
        te_bet_bedrag = totaal

    #terug te geven
    print('Te betalen bedrag is: ', te_bet_bedrag//100, '€')
    ontv_bedrag = pcinput.getInteger("Vul hier het ontvangen bedrag in: ")
    totaal_terug_te_geven(ontv_bedrag, te_bet_bedrag) 

    #kasticket
   
    rekening = pcinput.getString('Wenst u de rekening af te drukken? ja/nee ')
    if rekening == 'ja':
        print("*" * 50)
        print(" " * 19, "REKENING", " " * 21)
        print("*" * 50)
        print("*{:4} {:30}*{:9} € *".format(totaal_mosselen, "portie(s) mosselen", totaal_mosselen * 20))
        print("*{:4} {:30}*{:9} € *".format(totaal_koning, "portie(s) koninginnehapje(s)", totaal_koning * 10))
        print("*{:4} {:30}*{:9} € *".format(totaal_ijsje, "portie(s) ijs", totaal_ijsje * 3))
        print("*{:4} {:30}*{:9} € *".format(totaal_drank, "portie(s) drank", totaal_drank * 2))

        print("*" * 50)
        print("*{:10} {:20} {:14}€ *".format(" ", "totaal: ", totaal//100), " €")

        if korting != 0:            
            print("*{:10} {:20} {:14}€ *".format(" ", "uw korting is: ", korting//100), " €")
            print("*{:10} {:20} {:14}€ *".format(" ", "totaal te betalen: ", te_bet_bedrag//100), " €")
        
        print("*" * 50)
        print("*{:10} {:20} {:14}€ *".format(" ", "ontvangen: ", ontv_bedrag, " €"))
        print("*{:10} {:20} {:14}€ *".format(" ", "terug: ", ontv_bedrag - te_bet_bedrag//100), " €")

        print("*" * 50)
        if totaal_mosselen == 0 and totaal_koning == 0:
            print("*{:18} {:28} *".format(" ", "Gezondheid !"))
        else:
            print("*{:18} {:28} *".format(" ", "Smakelijk !"))
        print("*" * 50)
    else:
        print('Er wordt geen rekening afgedrukt ')
    
    stoppen = pcinput.getString('Wenst u de kassa te sluiten? ja/nee ')
    totaal_kassa = totaal_kassa + te_bet_bedrag//100

else: 
    print("*" * 27)
    print("{:3} {:5} {:5} ".format(' ', "Naam bediende: ", naam_bediende))
    print("{:1} {:5} {:4} € ".format(' ', 'kassatotaal is: ', totaal_kassa,))
    print("*" * 27)
    exit



