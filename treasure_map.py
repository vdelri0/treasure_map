line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]

map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")

position = input() # Where do you want to put the treasure?
letter = position[0]
number = int(position[1])

if letter == 'A':
    letter = 0
elif letter == 'B':
    letter = 1
elif letter == 'C':
    letter = 2
else:
    print("Ingrese una letra valida.")

print(letter, number)
map[number-1][letter] = 'X'

print(f"{line1}\n{line2}\n{line3}")