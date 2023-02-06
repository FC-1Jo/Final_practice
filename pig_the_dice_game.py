print('pig the dice game')
import random
current = 0
dice = random.randint(1,6)
if dice != 1:
    current += dice
else:
    current = 0
print(current)
input("roll the dice? yes / no : ")
