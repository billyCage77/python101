for getal in range(2, 101):
    priem = True
    for deler in range(2, getal):
        if getal % deler == 0:
            priem = False
            continue
    if priem:
        print(getal)