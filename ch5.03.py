from math import log

num1 = eval(input("Enter the limit: "))
sum1 = 0
sum2 = 0
for i in range(1, num1+1):
    sum1 += 1/i

print("(1 + 1/2 + 1/3 + · · · + 1/n ) - ln(n) =", sum1 - log(num1))
