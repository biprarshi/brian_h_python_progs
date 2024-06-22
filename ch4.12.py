candy1 = ''
for i in range(1, 201):
    if i % 5 == 2 and i % 6 == 3 and i % 7 == 2:
        candy1 += str(i)+' '
print(f"There are {candy1} pieces of Halloween candy in the jar!")
