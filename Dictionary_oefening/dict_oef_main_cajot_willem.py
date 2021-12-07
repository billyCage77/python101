
tekst= '\
appel,peer,banaan,kers,appel,kers,\
kers,mango,appel,appel,kers,tomaat,\
banaan,appel,appel,appel,appel,kers,\
banaan,appel,banaan,kers,tomaat,mango'

tekst_lijst = tekst.split(",")

fruit_count = {}

for fruit in tekst_lijst:
    fruit_count[fruit] = tekst_lijst.count(fruit)

fruit_count_list = list(fruit_count.keys())
fruit_count_list.sort()
for fruit in fruit_count_list:
    print("{0:6} : {1:3}".format(fruit, fruit_count[fruit]))


 
 
