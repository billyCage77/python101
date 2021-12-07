

print("Welkom bij de BTW-nummer checker")

def getBTW():
    while True:
        try:
            btw_invoer = str(input("Geef uw BTW nr in aub: (BE 0xxx.xxx.xxx)" ))
        except ValueError:
            print( "Dit is geen geldig nummer, probeer opnieuw")
            continue
        btw_nummers = btw_invoer.upper()
        btw_nummers_twee = btw_nummers.replace(".", "")
        btw_nummers_drie = btw_nummers_twee[4:15]
    
        return btw_nummers_drie

btw = getBTW()

laatste_2_calc = btw[7:9]
controle_reeks_calc = btw[0:7]

controle = 97 - (int(controle_reeks_calc) % 97)

print(controle)
if controle == int(laatste_2_calc):
    resultaat = print('dit is een correct BTW nummer')
else:
    print('Dit is een fout BTW nummer !!')

