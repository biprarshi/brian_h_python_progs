num1 = eval(input("Enter a number: "))
fact1 = 1
for i in range(2, num1+1):
    fact1 *= i
print(f"The factorial of {num1} is: {fact1}.")
