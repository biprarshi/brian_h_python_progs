tempr1 = eval(input("Enter temperature in Celsius: "))
if tempr1 < -273.15:
    print('The temperature is invalid because it is below absolute zero!')
elif tempr1 == -273.15:
    print('The temperature is absolute 0.')
elif -273.15 < tempr1 < 0:
    print('The temperature is below freezing.')
elif tempr1 == 0:
    print('The temperature is at the freezing point.')
elif 0 < tempr1 < 100:
    print('The temperature is in the normal range.')
elif tempr1 == 100:
    print('The temperature is at the boiling point.')
else:
    print('The temperature is above the boiling point.')
