import random
print("Welcome to Rock, Paper, Scissors!\n")
print("Press 0 for Rock, 1 for Paper, 2 for Scissors.\n")

rock = """
    ROCK
    _______
---'   ____ )
      (_____
      (_____
      (____
---.__(___)
"""

paper = """
    PAPER
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
scissors = """
    SCISSORS
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
choice = [rock, paper, scissors]
print("Welcome to the Rock, Paper & Scissors Game!\n")
print("Press 0 for 'Rock', 1 for 'Paper' and 2 for 'Scissors'")
#users input

users_choice = int(input("What do you choose? "))

if users_choice < 0 or users_choice >2:
    print("Invalid choice. You lost the game!")
    exit()
print ("You chose:", choice[users_choice])

#computer turn


computers_choice = random.randint(0, 2)
print("Computer chose:", choice[computers_choice])

#gfame logic
if users_choice == computers_choice:
    print("It's a tie!")
elif (users_choice == 0 and computers_choice == 2) or \
     (users_choice == 1 and computers_choice == 0)  or \
     (users_choice == 2 and computers_choice == 1):
    print("You WInnnn!!")
else:
    print("You lose!")



#input validations

