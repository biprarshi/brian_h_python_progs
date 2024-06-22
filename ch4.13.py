from random import choice
u_count1 = 0
c_count1 = 0
# u_choice1 = ''
# c_choice1 = ''
choice1 = (1, 2, 3)
choice2 = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
print(f"{'':=^25}")
print('Rock-Paper-Scissors game!')
print(f"{'':+^25}")
i = 0
while i < 5:
    print(f"Round {i+1}!")
    u_choice1 = eval(input('''1. (Rock)
2. (Paper)
3. (Scissors)
Enter your choice(1, 2 or 3): '''))
    c_choice1 = choice(choice1)
    if 0 < u_choice1 < 4:
        i += 1
        if u_choice1 == c_choice1:
            print(f'Both User and Computer chose {
                  choice2[u_choice1]}. Its a tie!')
        elif (u_choice1 == 2 and c_choice1 == 1) or (u_choice1 == 3 and c_choice1 == 2) or (u_choice1 == 1 and c_choice1 == 3):
            print(f'User chose {choice2[u_choice1]} and Computer chose {
                  choice2[c_choice1]}. User Wins!')
            u_count1 += 1
        else:
            print(f'User chose {choice2[u_choice1]} and Computer chose {
                  choice2[c_choice1]}. Computer Wins!')
            c_count1 += 1
    else:
        print(f"{'Invalid User Input! try again':!^50}")
print("User score:", u_count1)
print("Computer score:", c_count1)
if u_count1 == c_count1:
    print("Its a tie!")
elif u_count1 > c_count1:
    print("User Wins!!!")
else:
    print("Computer Wins!!!")
