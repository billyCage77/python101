
import pcinput
import random

teller = 0
score = 0

for teller in range(5):
    num1 = random.randint(1,1000)
    num2 = random.randint(1,1000)
    som = num1 + num2
    answ = pcinput.getInteger(f"{num1} + {num2} = ")    
    teller += 1
    if answ == som:
        score += 1
    
print("score is: ", score*20, "%")