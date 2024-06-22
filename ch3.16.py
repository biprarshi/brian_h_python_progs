# from math import floor, fmod

# Y1 = eval(input("Enter year: "))
# C1 = Y1//100
# m1 = fmod((15+C1-floor(C1/4)-floor((8*C1)/25)),30)
# n1 = fmod((4+C1-floor(C1/4)),7)
# a1 = fmod(Y1,4)
# b1 = fmod(Y1,7)
# c1 = fmod(Y1,19)
# d1 = fmod((19*c1+m1),30)
# e1 = fmod((2*a1+4*b1+6*d1+n1),7)

# if d1==29 and e1==6:
#     easter1 = "April 19"
# elif d1==28 and e1==6 and m in (2, 5, 10, 13, 16, 21, 24, 39):
#     easter1 = "April 18"
# elif 22+d1+e1 < 32:
#     easter1 = "March " + str(round(22+d1+e1))
# else:
#     easter1 = "April "+ str(round(d1+e1-9))

# print("In year",Y1,"easter is on",easter1)