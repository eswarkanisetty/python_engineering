import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
computer = [rock, paper, scissors]
computer_random = random.choice(computer)

print("Welcome to the rock, paper, scissors Game.")
user_choice=int(input("What do you choose ? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))

if user_choice == 0:
    play = rock
    print(f" You have chosen rock: {play}\n Computer Choice is {computer_random}")
elif user_choice == 1:
    play = paper
    print(f" You have chosen paper: {play}\n Computer Choice is {computer_random}")
elif user_choice == 2:
    play = scissors
    print(f" You have chosen scissors: {play}\n Computer Choice is {computer_random}")
else :
    print("Choose the Options that are available among 0,1,2 !!!")

if play  == computer_random :
    print("Game Draw")
elif play == rock and computer_random == scissors :
    print("You win Rock crushes Scissors")
elif play == scissors and computer_random == paper :
    print("You win Scissors cuts Paper")
else :
    print("You win Paper Covers Rock")





