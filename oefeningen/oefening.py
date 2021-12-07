from pcinput import getInteger

aantal = 0
totaal = 0
num = getInteger("geef een nummer (0 om te stoppen): ")
while num != 0:
    totaal += num
    num = getInteger("geef een nummer (0 om te stoppen): ")
    aantal += 1
print("Totaal is: ", totaal)
print(totaal / aantal)