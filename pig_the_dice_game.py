print('pig the dice game')
import random
score1 = 0
score2 = 0
while True:
    current1 = 0
    current2 = 0
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
    score1 += current1
    print(f'user 총합은{score1}입니다.')

    a = 'yes'
    while a == 'yes':
        roll2 = random.randint(1,6)
        print(roll2)
        if roll2 == 1:
            current2 = 0
            break
        else:
            current2 += roll2
            a = random.choice(['yes', 'no'])

    score2 += current2
    print(f'컴퓨터 총합은{score2}입니다.')
