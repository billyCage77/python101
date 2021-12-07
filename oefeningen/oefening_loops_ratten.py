
date = 2021
aantal_ratten = 2000000
groei_per_jaar = 15

while aantal_ratten < 10000000:
    aantal_ratten += ((aantal_ratten / 100) * groei_per_jaar)
    date += 1

print(date)
