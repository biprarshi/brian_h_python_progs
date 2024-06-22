tempr1 = eval(input("Enter temperature: "))
unit1 = eval(input('''Enter unit:
                   1. Celsius
                   2. Fahrenheit '''))
if unit1 == 1:
    print(tempr1, "degrees Celsius is", tempr1*9/5+32, "degrees Fahrenheit.")
elif unit1 == 2:
    print(tempr1, "degrees Fahrenheit is", (tempr1-32)*5/9, "degrees Celsius.")
else:
    print("Invalid unit!")
