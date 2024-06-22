year1 = eval(input("Enter Year: "))
if year1 % 4 == 0 and year1 % 100 != 0:
    print("yes")
elif year1 % 100 == 0 and year1 % 400 == 0:
    print("yes")
else:
    print("no")
str1 = ''
count1 = 0
for i in range(1601, year1):
    if i % 4 == 0 and i % 100 != 0:
        count1 += 1
        str1 = str1 + str(i) + " "
    elif i % 100 == 0 and i % 400 == 0:
        count1 += 1
        str1 = str1 + str(i) + " "

print(count1, str1)
