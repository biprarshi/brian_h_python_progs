count4 = 0
count9 = 0
for i in range(1, 101):
    if (i*i) % 10 == 4:
        count4 += 1
    if (i*i) % 10 == 9:
        count9 += 1

print("No of the squares of the numbers from 1 to 100 that end in a 4 =", count4)
print("No of the squares of the numbers from 1 to 100 that end in a 9 =", count9)
