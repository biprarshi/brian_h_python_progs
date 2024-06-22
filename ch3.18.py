amount1 = eval(input("Enter amount in cents: "))
quarters1 = dimes1 = nickels1 = cents1 = 0
while amount1 > 0:
    if amount1 > 25:
        quarters1 = quarters1 + amount1//25
        amount1 = amount1 % 25
    elif amount1 > 10:
        dimes1 = dimes1 + amount1//10
        amount1 = amount1 % 10
    elif amount1 > 5:
        nickels1 = nickels1 + amount1//5
        amount1 = amount1 % 5
    else:
        cents1 = round(amount1)
        amount1 = 0

print("You will need", quarters1, "quarters,", dimes1,
      "dimes,", nickels1, "nickels, and", cents1, "cents.")
