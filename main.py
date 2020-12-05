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

rps = [rock, paper, scissors]

import random

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
chosen = int(input())

print(rps[chosen])

print("Computer chose:")

computer = random.randint(0, 2)

print(rps[computer])

if computer == 0 and chosen == 2:
  print("You lose")

if computer == 0 and chosen == 1:
  print("You win")

if computer == 1 and chosen == 0:
  print("You lose")

if computer == 1 and chosen == 2:
  print("You win")

if computer == 2 and chosen == 0:
  print("You win")

if computer == 2 and chosen == 1:
  print("You lose")

if computer == chosen:
  print("It's a draw")