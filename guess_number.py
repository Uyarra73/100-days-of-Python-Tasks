import random
from guess_number_art import logo

def guess_number():
    continue_playing = True
    count = 0
    computer_guess = int(random.randrange(1, 101))
    print(logo)
    print("Welcome to the number guessing game!")
    level = ""
    while level not in ["easy", "hard"]:
        level = input("Choose a difficulty level: (easy/hard) \n").lower()
        if level == "easy":
            count = 10
        elif level == "hard":
            count = 5
        else:
            print("Please, you have to choose 'easy' or 'hard'.")
    print(f"You have {count} time to guess th number I'm thinking")
    while continue_playing:
        my_guess = int(input("Make your guess: \n"))
        if my_guess == computer_guess:
            print("You guessed it. You win")
            continue_playing = False
        elif my_guess > computer_guess:
            count -= 1
            print(f"Too high. {count} times left. Try again")
        else:
            count -= 1
            print(f"Too low. {count} times left.Try again")

        if count == 0:
            continue_playing = False
            print("You run out of chances. See you next time")

guess_number()
