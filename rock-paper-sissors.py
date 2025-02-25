import random

game_elements = ['rock', 'paper', 'scissors']

player_input = input('Tell me, rock, paper, or scissors?: ')
computer = random.choice(game_elements)
if player_input in game_elements:
    print(f"Computers choice is... {computer}")

if player_input == "rock":
    if computer == "rock":
        print("It's a tie!")
    elif computer == "paper":
        print("Paper beats the rock! Computer wins.")
    elif computer == "scissors":
        print("Rock beats the scissors! You win.")
elif player_input == "paper":
    if computer == "paper":
        print("It's a tie!")
    elif computer == "rock":
        print("Paper beats the rock! You win.")
    elif computer == "scissors":
        print("Scissors beats the paper! Computer win.")
elif player_input == "scissors":
    if computer == "scissors":
        print("It's a tie!")
    elif computer == "rock":
        print("Rock beats the scissors! Computer win.")
    elif computer == "paper":
        print("Scissors beats the paper! You win.")
else:
    print("Invalid input.")
