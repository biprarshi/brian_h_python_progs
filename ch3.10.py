exponent_val1 = eval(input("Enter the exponent: "))
result1 = 2**exponent_val1%10
print("Last digit:",result1)
result2 = (2**exponent_val1)%100
print("Last two digits:",result2)
digits1 = eval(input("Enter the no of digits you want: "))
result3 = (2**exponent_val1)%(10**digits1)
print("Last",digits1,"digits are:",result3)