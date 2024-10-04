MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Función para actualizar los recursos después de servir un café
def update_resources(selection):
    """ Updates resources after executing the payment function and prints a report of them """
    for n in resources:
        resources[n] -= MENU[selection]["ingredients"].get(n, 0)  # Evitar KeyError
    print(f"You have these resources left: \n"
          f"{resources['water']} ml \n"
          f"{resources['milk']} ml \n"
          f"{resources['coffee']} gr \n")


# Función para manejar el pago
def payment(amount):
    """Manages the payment of the selected type of coffee"""
    coins = {"dollars": 0, "quarters": 0, "dimes": 0, "nickles": 0, "pennies": 0}
    for n in coins:
        coins[n] = int(input(f"Add {n}: "))
    total = round(coins["pennies"] * 0.01 + coins["nickles"] * 0.05 + coins["dimes"] * 0.1 + coins["quarters"] * 0.25 + coins["dollars"], 2)

    print(f"Total inserted: ${total:.2f}")
    if total == amount:
        print("Here is your coffee. Thanks!")
    elif total > amount:
        change = total - amount
        print(f"Here is your coffee and your change: ${change:.2f}. Thanks!")
    else:
        print(f"Not enough credit. You inserted ${total:.2f}, but the price is ${amount:.2f}. Money refunded.")
        return False  # Indicar que no se pudo realizar el pago

    return True  # Indicar que el pago fue exitoso


# Función para verificar si hay recursos suficientes
def check_resources(coffee):
    """ Compares the resources remaining with those required to make the selected coffee"""
    for ingredient, amount in MENU[coffee]["ingredients"].items():
        if resources[ingredient] < amount:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    price = MENU[coffee]["cost"]
    print(f"Price: ${price}")
    
    if payment(price):
        update_resources(coffee)
        return True
    return False


# Función para seleccionar el tipo de café
def type_of_coffee():
    """ Gives the user the chance to choose a type of coffee """
    selection = ""
    while selection not in ["espresso", "latte", "cappuccino"]:
        selection = input("What kind of coffee would you like today? (Espresso/Latte/Cappuccino): ").lower()
        if selection in MENU:
            if check_resources(selection):
                print("Enjoy your coffee!")
            else:
                print("Sorry, we couldn't process your request.")
        else:
            print("Please select a valid coffee option!")


# Función para imprimir los recursos restantes
def print_resources():
    """ Prints the remaining resources once executed """
    print(f"Your current resources are: \n"
          f"{resources['water']} ml of water \n"
          f"{resources['milk']} ml of milk \n"
          f"{resources['coffee']} g of coffee \n")


# Función para seleccionar una acción
def select_action():
    """ Selects an action to be executed by the user """
    while True:
        action = input("Select one of the following: OFF/REPORT/COFFEE: \n").lower()
        if action == "off":
            print("The machine is now OFF. Proceed with maintenance procedure")
            break
        elif action == "report":
            print_resources()
        elif action == "coffee":
            type_of_coffee()
        else:
            print("Please, select a valid action!")

# Ejecutar la función principal
select_action()
