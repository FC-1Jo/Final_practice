print('pig the dice game')
import random
score = 0
current = 0
a = 'yes'
while a =='yes':
    roll=random.randint(1,6)
    print(roll)
    if roll == 1:
        current = 0
        break
    else:
        current += roll
        a = input("주사위를 굴리시겠습니까? yes/no:")
score += current
print(f'user 총합은{score}입니다.')
