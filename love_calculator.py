# Love calculator

def calculate_love_score(name1, name2):
    names = (name1 + name2).upper()
    total_true = 0
    total_love = 0

    for letter in "TRUE":
        count_letter = names.count(letter)
        print(f"{letter} occurs {count_letter} times")
        total_true += count_letter
    print(f"Total = {total_true}")

    for letter in "LOVE":
        count_letter = names.count(letter)
        print(f"{letter} occurs {count_letter} times")
        total_love += count_letter
    print(f"Total = {total_love}")

    love_score = str(total_true) + str(total_love)
    print(f"Love Score = {love_score}")

calculate_love_score("Angela Yu", "Jack Bauer")


















