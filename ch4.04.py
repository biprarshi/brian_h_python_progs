credits1 = eval(input("Enter no of credits taken: "))
if credits1 <24:
    print('Student is a freshman.')
elif 23<credits1 <54:
    print('Student is a sophomore.')
elif 53 <credits1<84:
    print('Student is a junior.')
elif 83< credits1:
    print('Student is a senior.')
