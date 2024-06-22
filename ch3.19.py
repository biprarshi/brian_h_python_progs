height1 = eval(input("Enter height: "))
width1 = eval(input("Enter width: "))

num1 = 0
for i in range(height1):
    for j in range(width1):
        if num1 < 10:
            print(num1, end=' ')
            num1 += 1
        else:
            num1 = 0
            print(num1, end=' ')
            num1 += 1
    print()
