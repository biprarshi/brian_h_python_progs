hour1 = eval(input("Enter an hour between 1 and 12: "))
hour2 = eval(input("Enter how many hours in the future you want to go? "))
hour3 = ((hour1%12)+hour2)%12
print(hour2,"hours into the future is",hour3,"o' clock.")
