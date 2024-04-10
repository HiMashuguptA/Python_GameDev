import random

player_score = 0
computer_score = 0
options = ["rock", "paper", "scissor"]

while True:
    inp = input("Your turn: ").lower()
    if inp not in options:
        print("Invalid input. Please enter rock, paper, or scissor.")
        continue

    computer_option = random.choice(options)
    print("Computer turn:", computer_option)

    if inp == "rock" and computer_option == "paper":
        computer_score += 1
    elif inp == "paper" and computer_option == "scissor":
        computer_score += 1
    elif inp == "scissor" and computer_option == "rock":
        computer_score += 1
    elif inp == computer_option:
        player_score += 1
        computer_score += 1
    else:
        player_score += 1

    if player_score == 3 or computer_score == 3:
        break

if computer_score > player_score:
    print("Computer won the game")
elif player_score > computer_score:
    print("Player won the game")
else:
    print("Game tie")
