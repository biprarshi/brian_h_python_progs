price1 = eval(input("Enter the price of meal: "))
tip1 = eval(input("Enter the percent tip you want to leave: "))
tip1 = tip1*price1/100
print("Tip amount: ",tip1)
print("Total bill with the tip included: ",price1+tip1)
