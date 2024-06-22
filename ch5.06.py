# from math import ceil


print("All four of the perfect numbers that are less than 10000 are: ", end='')
i = 1
for i in range(1, 10001):
    divisor1 = 0
    # for j in range(1, ceil(i/2)+1):
    for j in range(1,i//2+1):
        if i % j == 0:
            divisor1 += j
    if i == divisor1:
        print(i,end=' ')
