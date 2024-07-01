from logo_blackjack import logo  # Importa el logo del juego desde el módulo logo_blackjack
import os
import random  # Importa el módulo random para seleccionar cartas aleatorias

def deal_cards():
  """Devuelve una carta aleatoria del mazo"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # Define el mazo de cartas
  card = random.choice(cards)  # Selecciona una carta aleatoria
  return card

# Inicializa las manos del usuario y del ordenador
user_cards = []
computer_cards = []

# Reparte 2 cartas al usuario y al ordenador
for carta in range(2):
  user_cards.append(deal_cards())
  computer_cards.append(deal_cards())

def calculate_score(cards):
  """Toma una lista de cartas y devuelve el puntaje calculado"""
  if sum(cards) == 21 and len(cards) == 2:
      return 21  # Verifica si hay un blackjack (21 con 2 cartas)
  if 11 in cards and sum(cards) > 21:
      cards.remove(11)
      cards.append(1)  # Convierte un as (11) en 1 si el puntaje es mayor a 21
  return sum(cards)  # Devuelve la suma de las cartas

def play_game():
  print(logo)  # Imprime el logo del juego

  user_cards = []
  computer_cards = []
  for carta in range(2):
    user_cards.append(deal_cards())
    computer_cards.append(deal_cards())

  user_score = calculate_score(user_cards)
  computer_score = calculate_score(computer_cards)
  print(f"Your cards: {user_cards}, Your current score: {user_score}")
  print(f"Computer's first card: {computer_cards[0]}")

  while True:
    if user_score == 21 or computer_score == 21 or user_score > 21:
        break  # Verifica si alguien tiene un blackjack o si el usuario se ha pasado de 21
    else:
        another_deal = input("Type 'y' to get another card, type 'n' to pass: ").upper()
        if another_deal == "Y":
            user_cards.append(deal_cards())
            user_score = calculate_score(user_cards)
            print(f"Your cards: {user_cards}, Your current score: {user_score}")
            print(f"Computer's first card: {computer_cards[0]}")
        elif another_deal == "N":
            break
        else:
            print("Choose another option please!")

  while computer_score < 17:
    computer_cards.append(deal_cards())
    computer_score = calculate_score(computer_cards)

  print(f"Your final hand: {user_cards}, your final score: {user_score}")
  print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

  if user_score == computer_score:
    print("It's a Draw :|")
  elif user_score > 21 and computer_score > 21:
    print("It's a Bust :|")
  elif user_score > 21:
    print("You went over, You lose :c")
  elif computer_score > 21:
    print("Opponent went over, You win :D")
  elif user_score == 21:
    print("You got a blackjack :D")
  elif computer_score == 21:
    print("You lose, opponent has a Blackjack :C")
  elif user_score > computer_score:
    print("You win :D")
  elif computer_score > user_score:
    print("You lose :C")

while True:
  start_of_game = input("Do you want to play a game of Blackjack? Yes (Y) No (N) ").upper()
  if start_of_game == "Y":
    play_game()
  elif start_of_game == "N":
    print("See you soon!")
    break
  else:
    print("Choose another option please!")