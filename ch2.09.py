# Fibonacci
num1 = eval(input('How many Fibonacci numbers to print? '))
item1 = 1
item2 = 1
for i in range(num1):
    if i == 0:
        item3 = 1
    elif i == 1:
        item3 = 1
    else:
        item3 = item2 + item1
        item1 = item2
        item2 = item3

    print(item3, end=' ')