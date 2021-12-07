from collections import Counter


tekst= '\
appel,peer,banaan,kers,appel,kers,\
kers,mango,appel,appel,kers,tomaat,\
banaan,appel,appel,appel,appel,kers,\
banaan,appel,banaan,kers,tomaat,mango'

tekst_lijst = tekst.split(",")





print(Counter(tekst_lijst).items())
