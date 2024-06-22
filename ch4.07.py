from math import fabs
num1 = eval(input("Enter first number: "))
num2 = eval(input("Enter second number: "))
if fabs(num1-num2) < 0.001:
    print("Close", fabs(num1-num2))
else:
    print("Not Close", fabs(num1-num2))
