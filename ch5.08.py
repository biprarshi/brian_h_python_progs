num1, num2, num3 = input("Enter three values: ").split()

num1, num2, num3 = int(num1), int(num2), int(num3)

print(f"x={num1}, y={num2}, z={num3}")
num1 = num1 + num2 + num3
num3 = num1 - (num2 + num3)
num2 = num1 - (num2 + num3)
num1 = num1 - (num2 + num3)
print(f"x={num1}, y={num2}, z={num3}")