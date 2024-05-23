# create a rock paper scissors game using python with GitHub Copilot

# import random module
import random

# create a list of play options
options = ["rock", "paper", "scissors"]

# create the score and round played variables
player_score = 0
computer_score = 0

# create the loop to play the game
while True:
    # assign a random play to the computer
    computer = random.choice(options)

    # ask the player for their play
    player = input("rock, paper, scissors?")

    # if the player selected "rock"
    if player == "rock":
        if computer == "rock":
            print("Tie!")
        elif computer == "paper":
            print("You lose!", computer, "covers", player)
            computer_score += 1
        elif computer == "scissors":
            print("You win!", player, "smashes", computer)
            player_score += 1        
        
    # if the player selected "paper"
    elif player == "paper":
        if computer == "rock":
            print("You win!", player, "covers", computer)
            player_score += 1
        elif computer == "paper":
            print("Tie!")
        elif computer == "scissors":
            print("You lose!", computer, "cut", player)
            computer_score += 1

    # if the player selected "scissors"
    elif player == "scissors":
        if computer == "rock":
            print("You lose...", computer, "smashes", player)
            computer_score += 1
        elif computer == "paper":
            print("You win!", player, "cut", computer)
            player_score += 1
        elif computer == "scissors":
            print("Tie!")

    # if the player selected an invalid option
    else:
        print("That's not a valid play. Check your spelling!")
    
    # ask the player if they want to play again
    repeat = input("Do you want to play again? (yes/no)")
    if repeat == "no":
        break

# print the final score
print("Player score:", player_score)
print("Computer score:", computer_score)
