from random import randint
r_num1 = randint(1,10)
guess1 = eval(input("Guess the number: "))
if r_num1 == guess1:
    print("You have got it right!")
else:
    print("Wrong! The number is:",r_num1)