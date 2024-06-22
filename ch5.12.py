from random import randint

points1 =0
for i in range(5):
    random_no1 = randint(1,10)
    guess1 = eval(input("Enter your guess(1-10): "))
    if random_no1 == guess1:
        points1+=10
        print("Hurray!")
    else:
        points1-=1
print(f"Your score is: {points1}.")