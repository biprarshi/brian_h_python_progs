num1 = eval(input("Enter a number: "))
divisor_sum1 = 0
for i in range(1, num1//2+1):
    if num1 % i == 0:
        divisor_sum1 += i
divisor_sum1 += num1
print(f'The sum of the divisors of {num1} =', divisor_sum1)
