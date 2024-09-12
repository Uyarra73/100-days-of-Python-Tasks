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
your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors. \n"))
computer_choice = random.randint(0, 2)

if your_choice > 2:
    print("You chose an invalid number")
elif your_choice == 0:
    if computer_choice == 0:
        print(your_choice, rock, "Computer chose: ", computer_choice, rock, "It is a draw!", sep="\n")
    elif computer_choice == 1:
        print(your_choice, rock, "Computer chose: ", computer_choice, paper, "You lose!", sep="\n")
    else:
        print(your_choice, rock, "Computer chose: ", computer_choice, scissors, "You win!", sep="\n")
elif your_choice == 1:
    if computer_choice == 0:
        print(your_choice, paper, "Computer chose: ", computer_choice, rock, "You win!", sep="\n")
    elif computer_choice == 1:
        print(your_choice, paper, "Computer chose: ", computer_choice, paper, "It is a draw!", sep="\n")
    else:
        print(your_choice, paper, "Computer chose: ", computer_choice, scissors, "You lose!", sep="\n")
else:
    if computer_choice == 0:
        print(your_choice, scissors, "Computer chose: ", computer_choice, rock, "You lose!", sep="\n")
    elif computer_choice == 1:
        print(your_choice, scissors, "Computer chose: ", computer_choice, paper, "You win!", sep="\n")
    else:
        print(your_choice, scissors, "Computer chose: ", computer_choice, scissors, "It is a draw!", sep="\n")








