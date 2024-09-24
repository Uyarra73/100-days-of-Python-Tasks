from calculator_art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(logo)
    n1 = float(input("What's the first number? "))
    should_continue = True

    while should_continue:
        operation = input("Pick an operation: \n+\n-\n*\n/\n")
        n2 = float(input("What's the second number? "))
        total = operations[operation](n1, n2)
        print(f"{n1} {operation} {n2} = {total}")
        continue_calc = input(f"The result is {total}. Do you want to continue calculating from here? (y/n)\n").lower()
        if continue_calc == "y":
            n1 = total
        else:
            should_continue = False
            print("\n" * 20)
            calculator()

calculator()








