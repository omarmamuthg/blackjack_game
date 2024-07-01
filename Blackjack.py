from logo_blackjack import logo
import os
import random 

def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card
#print(deal_cards())
#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
user_cards = []
computer_cards = []

for carta in range(2):
    user_cards.append(deal_cards())
    computer_cards.append(deal_cards())


#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.
def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""

  #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
  if sum(cards) == 21 and len(cards) == 2:
    return 21
  #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)
  


    


def play_game():
  print(logo)
  
  user_cards = []
  computer_cards = []
  for carta in range(2):
      #pass
      user_cards.append(deal_cards())
      computer_cards.append(deal_cards())
  #print(computer_cards)
  #print(user_cards)
  
  user_score= calculate_score(user_cards)
  computer_score=calculate_score(computer_cards)
  print(f"your cards: {user_cards},Your current score; {user_score}  ")
  print(f"Computer first cards: {computer_cards[0]} ")
  
  while True:
    if (user_cards == 21 or computer_cards== 21 or  user_score >21 ):
      break
    else:
      another_deal = input("Type 'y' to get another card, type 'n' to pass: ").upper()
      if another_deal=="Y":
        deal_cards()
        user_cards.append(deal_cards())
        user_score= calculate_score(user_cards)
        #print(user_cards)
        print(f"your cards: {user_cards},Your current score; {user_score}  ")
        print(f"Computer first card: {computer_cards[0]}")
        #break
      elif another_deal == "N":
        break
      else:
        print("Choose another option please!!")
  while computer_score < 17:
      computer_cards.append(deal_cards())
      computer_score= calculate_score(computer_cards)
  
  print(f"your final hand: {user_cards}, your final score; {user_score} ")
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
      print("you win :D")
  elif computer_score > user_score:
      print("You lose :C")


while True:
  start_of_game=input("Do you want to play a blackjack? Yes (Y) No (N) ").upper()
  if start_of_game== "Y":
    play_game()
  elif start_of_game== "N":
    print("see you soon!!")
    break
  else:
    print("Choose another option please!!")
