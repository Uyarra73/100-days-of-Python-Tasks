from blackjack_art import logo
import random

# Lista de cartas posibles
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# Función para repartir cartas aleatoriamente
def deal_card():
    return random.choice(cards)


# Función para calcular el puntaje de una mano
def calculate_score(list_cards):
    total = sum(list_cards)

    # Verificar si hay un Blackjack (un As y una carta de valor 10)
    if total == 21 and len(list_cards) == 2:
        return 0  # Representa un Blackjack

    # Cambiar As (11) a 1 si el total supera 21
    if 11 in list_cards and total > 21:
        list_cards.remove(11)
        list_cards.append(1)
        total = sum(list_cards)

    return total


# Comienzo del juego
start_game = input("Do you want to play Blackjack? (y/n)\n").lower()

if start_game == "y":
    print(logo)

    user_cards = []
    computer_cards = []

    # Repartir dos cartas a cada uno
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Calcular puntajes iniciales
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    # Mostrar cartas y puntajes iniciales
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    # Verificar Blackjack
    if user_score == 0:
        print("Blackjack! User wins! ")
    elif computer_score == 0:
        print("Blackjack! Computer wins")
    elif user_score > 21:
        print("Bust! User loses!")
    else:
        should_continue = True

        # Bucle para permitir al usuario tomar más cartas
        while should_continue:
            draw_again = input("Do you want to draw another card? (y/n)\n").lower()

            if draw_again == "y":
                # El usuario saca una carta
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)

                # La computadora también saca carta si tiene menos de 17
                if computer_score < 17:
                    computer_cards.append(deal_card())
                    computer_score = calculate_score(computer_cards)

                # Mostrar cartas y puntajes después de cada turno
                print(f"Your cards: {user_cards}, current score: {user_score}")
                print(f"Computer's first card: {computer_cards[0]}")

                # Verificar si el usuario o la computadora han ganado o perdido
                if user_score > 21:
                    print(f"User busts with {user_score}! You lose.")
                    should_continue = False
                elif computer_score > 21:
                    print(f"Computer busts with {computer_score}! You win.")
                    should_continue = False
            else:
                # Si el usuario decide no tomar más cartas
                should_continue = False

                # La computadora debe seguir sacando cartas si su puntaje es menor a 17
                while computer_score < 17:
                    computer_cards.append(deal_card())
                    computer_score = calculate_score(computer_cards)

                # Mostrar las manos finales
                print(f"Your final hand: {user_cards}, final score: {user_score}")
                print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

                # Decidir el ganador final
                if user_score > 21:
                    print(f"User busts with {user_score}. Computer wins!")
                elif computer_score > 21:
                    print(f"Computer busts with {computer_score}. User wins!")
                elif user_score > computer_score:
                    print("User wins. Congratulations!")
                elif user_score == computer_score:
                    print("It's a draw!")
                else:
                    print("Computer wins! Better luck next time.")
else:
    print("Goodbye!")
