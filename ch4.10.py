from random import randint
for i in range(10):
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    ans1 = eval(input(f'Question {i+1}: {num1} x {num2} = '))
    if ans1 == num1 * num2:
        print('Right!')
    else:
        print(f'Wrong! The answer is {num1*num2}')
