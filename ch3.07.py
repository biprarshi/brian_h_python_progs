angle1 = eval(input("Enter an angle between 180◦ and -180◦: "))
if angle1>360:
    angle1 = angle1%360
elif 0<angle1<360:
    pass
elif -360<=angle1<0:
    angle1 = 360 - abs(angle1)
else:
    angle1 = 360 - (abs(angle1)%360)

print("Full angle is: ",angle1)