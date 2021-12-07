

print("Welkom bij de Falco quiz")

meespelen = input('Wil je meespelen? ja/nee ')
if meespelen.lower() != "ja":
    print('Prettige dag nog!')
    quit()
print('OK! Dan zullen we starten!')

name = input('Wat is uw naam? ')

score = 0



antw_1 = input("vraag 1: welk ras is Falco? ")
if antw_1.lower() == "whippet":
    print('Dat is juist ',name, '!')
    score += 1
else:
    print('Dat is fout ',name, '!')

antw_2 = input("Vraag 2: welke kleur heeft Falco, officieel? ")
if antw_2.lower() == "blauw":
    print('Juist ',name,'!')
    score += 1
else:
    print('Fout!')

antw_3 = input("Hoe oud is Falco? ")
if antw_3 == "5":
    print('Juist!')
    score += 1
else:
    print('Fout!')

antw_4 = input("Wat snoept Falco het liefst aan tafel? ")
if antw_4.lower() == "kaas":
    print('Juist!')
    score += 1
else:
    print('Fout!')

print("U hebt " + str(score) + " vragen juist van de vier!" )