num1 = eval(input('Enter a number: '))
divisors1 = ''
if num1 ==1:
    print("The only divisor of 1 is 1.")
else:
    for i in range(1, num1//2+1):
        if num1 % i == 0:
            divisors1 += str(i)+' '
    print(f"The divisors of {num1} are:", divisors1+f'and {num1}.')
