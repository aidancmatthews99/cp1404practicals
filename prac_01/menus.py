

MENU = """  MENU

E - Show even numbers
O - Show odd numbers
S - Show numbers squared
R - Show squared numbers
Q - Quit
"""

print("\n Kindergarten Number Maker \n")

print(MENU)
choice = input("Select: ").upper()

while choice != "Q":
    print()
    if choice == "E":
        x = int(input("Select lower value: "))
        y = int(input("Select higher value: "))
        x = (x + 1) // 2 * 2
        print()
        for i in range(x, y + 1, 2):
            print(i, end=' ')
        print()
    elif choice == "O":
        x = int(input("Select lower value: "))
        y = int(input("Select higher value: "))
        x = x // 2 * 2 + 1
        print()
        for i in range(x, y + 1, 2):
            print(i, end=' ')
        print()
    elif choice == "S":
        x = int(input("Select lower value: "))
        y = int(input("Select higher value: "))
        print()
        for i in range(x, y + 1):
            print(i * i, end=' ')
        print()
    elif choice == "R":
        x = int(input("Select lower value: "))
        y = int(input("Select higher value: "))
        print()
        for i in range(x, y + 1):
            if i ** (1 / 3.0) - int( i ** (1 / 3.0)) < 0.01 and i ** (1 / 3.0) - int( i ** (1 / 3.0)) > -0.01:
                print(i, end=' ')
        print()
    else:
         print("Invalid Option")

    print('\n', MENU, sep='')
    choice = input("Select: ").upper()

print("\nThank you and goodbye")




