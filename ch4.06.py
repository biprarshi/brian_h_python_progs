no_items1 = eval(input("Enter no of item syou are buying: "))
if no_items1 < 10:
    print('Total cost is $', no_items1*12, sep='')
elif 9 < no_items1 < 100:
    print('Total cost is $', no_items1*10, sep='')
if no_items1 > 99:
    print('Total cost is $', no_items1*7, sep='')
