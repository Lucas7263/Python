import random


## Blackjack game notes 

# Create a list filled with the deck of cards

# Create a conditonal that will shuffle the deck of cards

# Have another conditional that deal cards and responds to the player/dealer input to draw another card or stay

# Create a loop that will repeat the last conditional until the game ends.

# After game ends ask player if they would like to play again or quit?


# deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Ace", "Jack", "King", "Queen"]


names = ["1","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
suits = ["Spades","Hearts","Clubs","Diamonds"]

dealer = []
player = []

game = input("Would you like to play?\n")


def create_deck():
  deck = []
  for s in suits:
    for v in names:
      deck.append((v,s))
      random.shuffle(deck)
  return deck
  
deck = create_deck()


def deal_cards(deck):
    for i in range(2): # This will draw two cards for the dealer and player
       dealer.append(draw_card())
       player.append(draw_card())
       print(dealer)
       print(player)
  
        
    # new_card = random.choice(deck)
    # dealer.append(new_card)
    # print(dealer)
    
def draw_card():
    new_card = random.choice(deck)
    return new_card



if game == 'yes':
   deal_cards(deck)
   
    



