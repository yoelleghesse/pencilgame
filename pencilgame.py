import random

# Prompts the user to enter the number of pencils they want to use.
print("How many pencils would you like to use:")

# Loops until the user enters a valid number of pencils (a positive integer).
while True:
    # Reads the user's input.
    n_pencils = input()

    # Checks if the input is numeric.
    if not n_pencils.isdigit():
        print("The number of pencils should be numeric")
    # Checks if the input is positive.
    elif int(n_pencils) < 1:
        print("The number of pencils should be positive")
    # If the input is valid, sets the number of pencils to the integer value of the input and breaks the loop.
    else:
        n_pencils = int(n_pencils)
        break

# Asks the user who will go first.
player = input("Who will be the first (John, Jack):")

# Loops until the user enters a valid player name.
while player not in ("John", "Jack"):
    print("Choose between John and Jack")
    player = input()

# Loops until there are no pencils left.
while True:
    # Checks if there are no pencils left, and if so, prints the name of the winner and breaks the loop.
    if n_pencils < 1:
        print(f"{player} won!")
        break

    # Prints the remaining pencils as vertical bars.
    print("|" * n_pencils)

    # If it's not the bot's turn, prints the player's name.
    if player != "Jack":
        print(f"{player}'s turn!")
    # If it's the bot's turn, prints the bot's name.
    else:
        print(f"{player}'s turn:")

    # If it's not the bot's turn, loops until the player enters a valid choice.
    if player != "Jack":
        while True:
            choice = input()
            if choice not in ("1", "2", "3"):
                print("Possible values: '1', '2' or '3'")
            elif int(choice) > n_pencils:
                print("Too many pencils were taken")
            else:
                break

        # Removes the chosen number of pencils from the pile.
        n_pencils -= int(choice)

    # If it's the bot's turn, chooses how many pencils to remove according to a strategy.
    if player == "Jack":
        if n_pencils == 1:
            print(1)
            n_pencils -= 1
        elif n_pencils % 4 == 0:
            print(3)
            n_pencils -= 3
        elif n_pencils % 2 == 1:
            print(2)
            n_pencils -= 2
        elif n_pencils % 4 == 2:
            print(1)
            n_pencils -= 1
        else:
            rand = random.randint(1, 3)
            n_pencils -= rand
            print(rand)

    # Switches the player for the next turn.
    player = "John" if player == "Jack" else "Jack"
