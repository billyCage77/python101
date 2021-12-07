##################################################
# code bij de presentatie Dictionaries H13
##################################################
# 13 Wat zijn dictionaries
# dict1 = {'mossel': 20, 'videe': 10, 'ijs': 3, 'drank': 2 }
# print(type(dict1))
# print(dict1)
#
# # 13.1 De basis van dictionaries - nieuwe dict
# dictleeg = {}
# print(type(dictleeg))
# print(dictleeg)
# dict1 = {'mossel': 20, 'videe': 10, 'ijs': 3, 'drank': 2 }
# print(dict1)
#
# # 13.1 De basis van dictionaries - waarde opvragen
# fruitmand = {'appel': 3, 'banaan': 5, 'kers': 50}
# waarde = fruitmand['banaan']
# print(waarde)
# waarde = fruitmand['tomaat']
#
# 13.1 De basis van dictionaries - waarde toevoegen
# fruitmand = {'appel': 3, 'banaan': 5, 'kers': 50}
# print(fruitmand)
# fruitmand['mango'] = 2
# print(fruitmand)
#
# 13.1 De basis van dictionaries - waarde aanpassen
# fruitmand = {'appel': 3, 'banaan': 5, 'kers': 50}
# print(fruitmand)
# fruitmand['banaan'] = 1
# print(fruitmand)
#
# 13.1 De basis van dictionaries - waarde verwijderen
# fruitmand = {'appel': 3, 'banaan': 5, 'kers': 50}
# print(fruitmand)
# del fruitmand['banaan']
# print(fruitmand)
#
# 13.1 De basis van dictionaries - lengte
# fruitmand = {'appel': 3, 'banaan': 5, 'kers': 50}
# dictLengte = len(fruitmand)
# print(dictLengte)
#
# 13.1 De basis van dictionaries - afdrukken
# fruitmand = {'appel': 3, 'banaan': 5, 'kers': 50}
# print(fruitmand)
# print(fruitmand['banaan'])
# print(fruitmand.get('mango'))
# for x in fruitmand:
#     print('{}:\t{}'.format(x, fruitmand[x]))
#
# 13.2.1 <dict>.copy()
# from copy import deepcopy
#
# fruitmand = {'appel': 3, 'kers': 50, 'banaan': 5, 'druiven': {'wit': 50, 'rood': 50}, 'mango':'heel lekker', 'pruimen':50,'mandarijn': 5,'noten': 5,}
# fruitmandAlias = fruitmand
# fruitmandKopie = fruitmand.copy()
# fruitmandDKopie = deepcopy(fruitmand)
# print(id(fruitmand), id(fruitmand['druiven']))
# print(id(fruitmandAlias), id(fruitmandAlias['druiven']))
# print(id(fruitmandKopie), id(fruitmandKopie['druiven']))
# print(id(fruitmandDKopie), id(fruitmandDKopie['druiven']))
#
# 13.2.2 <dict>.keys(), .values() & .items()
# fruitmand = {'appel': 3, 'banaan': 5, 'kers': 50}
# print(list(fruitmand.keys()))
# print(list(fruitmand.values()))
# print(list(fruitmand.items()))
# print(sum(fruitmand.values()))
# print(max(fruitmand.values()))
# # max() en min() kunnen ook op strings toegepast worden
# print(max(fruitmand.keys()))

# # 13.2.3 <dict>.get(<key>)
# fruitmand = {'appel': 3, 'banaan': 5, 'kers': 50}
# print(fruitmand.get('appel'))
# if fruitmand.get('appel'):      # none of nul waarde levert False op
#     print(fruitmand.get('appel'),'appel(s) in de mand')
# else:
#     print('geen appel in de mand')
# # verkorte notatie
# print('appel is in de mand') if fruitmand.get('appel') else print('geen appel in de mand')
# aardbei = fruitmand.get('aardbei')
# print('aardbei is in de mand') if aardbei else print('geen aardbei in de mand')

# 13.2.3 <dict>.get(<key>,"0")
# fruitmand = {'appel': 3, 'banaan': 5, 'kers': 50}
# banaan = fruitmand.get('banaan', 0)
# print('aantal bananen in de mand:', banaan)
# mango = fruitmand.get('mango', 0)
# print('aantal mango\'s in de mand:', mango)

# 13.2.3 in om bestaan van key te controleren
# fruitmand = {'appel': 3, 'banaan': 5, 'kers': 50}
# if 'appel' in fruitmand:
#     print('appel is in de mand')
# else:
#     print('geen appel in de mand')
# # verkorte notatie
# print('druif is in de mand') if 'druif' in fruitmand else print('geen druif in de mand')

# Probleemstelling oplossing
# dictFruitmand = {'kers': 50, 'appel': 3, 'peer': 2}
# print('Ongesorteerd:')
# for fruit, aantal in dictFruitmand.items():
#     print('\t', fruit, ':', '\t', aantal)
# # for item in dictFruitmand:
# #     print(type(item),item)
# print('Gesorteerd:')
# lstKeysInFruitmand = list(dictFruitmand.keys())
# lstKeysInFruitmand.sort()
# print(lstKeysInFruitmand)
# for fruit in lstKeysInFruitmand:
#     print('\t', fruit, ':', '\t', dictFruitmand[fruit])
#
# Oefening
# tekst= '\
# appel,peer,banaan,kers,appel,kers,\
# kers,mango,appel,appel,kers,tomaat,\
# banaan,appel,appel,appel,appel,kers,\
# banaan,appel,banaan,kers,tomaat,mango'
# print(tekst)
#


