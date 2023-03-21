# Pencil-Game

## Introduction
This is a simple command-line game called "Pencils". It can be played by two players, or by one player against a bot. The objective of the game is to be the last player to remove the pencils from the pile. Players take turns removing one, two, or three pencils at a time.

## How to Play
Clone the repository to your local machine.
Navigate to the directory where the files are located.
Open the file pencils.py in a Python environment.
Run the file.
Follow the prompts to set the number of pencils and the players.
Choose the number of pencils to remove on your turn.
The game ends when there are no pencils left in the pile.
## Rules
The number of pencils in the pile must be a positive integer.
Players can only remove one, two, or three pencils at a time.
The player who removes the last pencil from the pile loses.
## How It Works
The game is implemented in Python using a simple command-line interface. The program prompts the user to enter the number of pencils to use and the names of the players. It then alternates between the players, prompting each player to choose the number of pencils to remove on their turn. If the player is a bot, it chooses the number of pencils to remove according to a strategy. If the player is a bot (named Jack), it chooses the number of pencils to remove according to the following strategy:
- If there is only one pencil left, Jack removes it.
- If the number of pencils left in the pile is divisible by 4, Jack removes 3 pencils.
- If the number of pencils left in the pile is odd, Jack removes 2 pencils.
- If the number of pencils left in the pile is such that n % 4 == 2, Jack removes 1 pencil.
- If none of the above conditions apply, Jack removes a random number of pencils between 1 and 3 inclusive.

The program checks after each turn to see if there are any pencils left in the pile. If not, the game ends and the program announces the winner.
