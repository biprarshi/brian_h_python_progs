from math import ceil, sqrt


num1 = eval(input("Enter a number: "))

flag1 = 1
for i in range(2, ceil(num1//2)+1):
    if num1 % i == 0:
        if sqrt(i) == round(sqrt(i)):
            flag1 = 0
            break

if  num1 != 1 and (flag1 == 0 or sqrt(num1) == round(sqrt(num1))):
    print(f'{num1} is not squarefree.')
else:
    print(f'{num1} is squarefree.')
