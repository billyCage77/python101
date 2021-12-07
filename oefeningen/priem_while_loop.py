getal = 2

while getal <101:
    getal += 1
    priem = True
    for deler in range(2, getal):
        if getal % deler == 0:
            priem = False
            break
    if priem:
        print(getal)