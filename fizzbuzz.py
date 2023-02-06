user_num = int(input("Hello! positive integer : "))

for i in range(1, user_num+1):
    if i%3==0:
        print('fizz')
    else:
        print(f'{i}')

