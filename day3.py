
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
text = input("Do you want to go right or left? ")
upper_text = text.upper()
#print(upper_text)
if upper_text == "LEFT":
    choice1 = input("Ok! You have to get to next island. Do you want to swim or wait for the next boat? (wait/swim)? ")
    upper_choice1 = choice1.upper()
    if upper_choice1 == "WAIT":
        choice2 = input("You just found two doors. Red, Blue and Yellow. You have to pick one: ")
        upper_choice2 = choice2.upper()
        if upper_choice2 == "YELLOW":
            print("You win. You found the treasure!")
        elif upper_choice2 == "RED":
            print("You have been burned by fire. Game over!")
        elif upper_choice2 == "BLUE":
            print("You have been beaten by a sea beast. Game Over!")
        else:
            print("That door doesn\'t exist. Game Over!")
    else:
        print("You have been attacked by a giant trout. Game Over!")
elif upper_text == "RIGHT":
    print("So sorry! You felt into a hole. Game over. Try again!")
else:
    print("Wrong choice. Choose right or left!. Try again!")
