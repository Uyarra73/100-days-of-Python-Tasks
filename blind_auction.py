from blind_art import logo

print(logo)

bidder_exists = True
bidders = {}
best_bid = 0
winner = ""

while bidder_exists:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $ "))
    bidders[name] = bid

    another_bidder = input("Are there any other bidders? (yes/no) \n").lower()

    if another_bidder == "yes":
        print("\n" * 10)
    else:
        bidder_exists = False
        for key, value in bidders.items():
            if value > best_bid:
                best_bid = value
                winner = key
        print(f"The winner is {winner} with a bid of ${best_bid}")
