from math import pow
# num1 = eval(input("Enter the limit: "))
num1 = 2001
sum1 = 0
for i in range (1,num1):
    sum1 += pow(-1,i+1)*i
print("The sum of series (1 - 2 + 3 - 4 + · · · + 1999 - 2000) is: ",sum1)
