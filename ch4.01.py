length1 = eval(input("Enter length in cm: "))
if length1 < 0:
    print("Invalid input!")
else:
    print(length1, "cms is", length1/2.54, "inches.")
