from random import randint
right1 = 0

for i in range(10):
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    ans1 = eval(input(f'Question {i+1}: {num1} x {num2} = '))

    if ans1 == num1 * num2:
        print('Right!')
        right1 += 1
    else:
        print(f'Wrong! The answer is {num1*num2}')


print(f'You have got {right1} answers correct and {10-right1} answers wrong!')
