# imports the random module from the python library
import random

# get user input by prompting for their choice
user_choice = input("Choose: Rock, Paper, or Scissors? ").lower()

# gets computer choice by randomly selecting from a list of the choices possible (rock, paper, or scissors)
comp_choice = random.choice(["rock", "paper", "scissors"])

# series of if and elif statements that helps determine the winner based on the user's choice and the computer's choice
if user_choice == comp_choice:
    print(f"You chose {user_choice} and the computer chose {comp_choice}. It's a tie!")
elif user_choice == "rock" and comp_choice == "paper":
    print(f"You chose {user_choice} and the computer chose {comp_choice}. The computer wins!")
elif user_choice == "rock" and comp_choice == "scissors":
    print(f"You chose {user_choice} and the computer chose {comp_choice}. You win!")
elif user_choice == "paper" and comp_choice == "rock":
    print(f"You chose {user_choice} and the computer chose {comp_choice}. You win!")
elif user_choice == "paper" and comp_choice == "scissors":
    print(f"You chose {user_choice} and the computer chose {comp_choice}. The computer wins!")
elif user_choice == "scissors" and comp_choice == "rock":
    print(f"You chose {user_choice} and the computer chose {comp_choice}. The computer wins!")
elif user_choice == "scissors" and comp_choice == "paper":
    print(f"You chose {user_choice} and the computer chose {comp_choice}. You win!")
# outputs a message if the user inputs something other than rock, paper, or scissors
else:
    print("You an entered an invalid option.")



