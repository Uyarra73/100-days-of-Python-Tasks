from tabnanny import check
from game_data import data
import random
from art import logo, vs

def random_pick(empty_pick=None):
    """ Makes a random choice from the data list"""
    pick = random.choice(data)
    while pick == empty_pick:
        pick = random.choice(data)
    return pick

def print_picks(pick_a, pick_b):
    """ Prints the two different options to compare """
    print(f"Compare {pick_a['name']}, a {pick_a['description']} from {pick_a['country']}")
    print(vs)
    print(f"Compare {pick_b['name']}, a {pick_b['description']} from {pick_b['country']}")

def check_winner(option, pick_a, pick_b):
    """ Checks for a winner among the options """
    if option == "a":
        return pick_a['follower_count'] > pick_b['follower_count']
    elif option == "b":
        return pick_b['follower_count'] > pick_a['follower_count']
    return False

def higher_or_lower():
    score = 0
    pick_a = random_pick()  # Random choice
    pick_b = random_pick(pick_a)  # A choice different from pick_a
    print(logo)
    while True:
        print_picks(pick_a, pick_b)
        option = input("Who has more followers? (A/B) \n").lower()
        if check_winner(option, pick_a, pick_b):
            score += 1
            print(f"Correct! Your score is {score}")
            pick_a = pick_b  # pick_a becomes pick_b
            pick_b = random_pick(pick_a)  # Random choice different from pick_a
        else:
            print(f"Wrong! Final score is {score}")
            break  # Stops the program

higher_or_lower()




