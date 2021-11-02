from random import shuffle
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7 ,'Eight':8, 'Nine':9, 'Ten':10
,'Jack':11, 'Queen':12, 'King':13, 'Ace':14} #These are the global values of cards


class Card :
    """Card(suit,rank)
       where suit and rank are a str
       """

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank.capitalize()
        self.value = values[rank.capitalize()] #To Access the values dictionary with capitalized strings
    def __str__(self):
        return self.rank + ' Of ' + self.suit


class Deck:
    """Deck Gives a List of 52 Card Objects
       You can Shuffle these Cards"""

    def __init__(self):
        self.all_cards = []

        for suit in suits:# Four suits
            for rank in ranks:#13 Cards for each suit
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)

    def shuffle_cards(self):
        shuffle(self.all_cards)
    def deal_card(self):
        return self.all_cards.pop()


class Player:
    """Player takes in name of player.
       We can remove or add cards to the player hand"""
    def __init__(self,name):
        self.name = name
        self.hand = []# The hand of a Player starts out empty.

    def __str__(self):
        return f'Player {self.name} has {len(self.hand)} cards. '

    def __len__(self):
        """len(player) returns the amount of cards they currently have."""
        return len(self.hand)

    def add_cards(self,added_cards): #This adds a card to the bottom of a deck ie the right side of  list
        if type(added_cards) ==  type([]): #This is to check for a list with multiple Card objects
            self.hand.extend(added_cards)
        else:
            self.hand.append(added_cards) #This appends a single Card object to a Player hand

    def remove_card(self): #This is to remove a card from the top of a deck ie the left side of  list
        return self.hand.pop(0)


#Game Setup
player_one = Player('Balkrishan')
player_two = Player('Harsh')

game_deck = Deck()
game_deck.shuffle_cards()
for i in range(26):
    player_one.add_cards(game_deck.deal_card())#adding one card to both players at a time in a single for loop iteration
    player_two.add_cards(game_deck.deal_card())

game_on =  True

round_count = 0
while game_on:
    round_count += 1
    print(f'round is {round_count}.')
    if len(player_one) == 0: #To check if player one has no cards
        print(f'Player {player_one.name} has run out of cards! Player {player_two.name} Wins ')
        game_on = False
        break
    elif len(player_two) == 0:# for player two
        print(f'Player {player_two.name} has run out of cards! Player {player_one.name} Wins ')
        game_on = False
        break
    #Start New Round
    player_one_cards = []
    player_one_cards.append(player_one.remove_card())

    player_two_cards = []
    player_two_cards.append(player_two.remove_card())

    at_war = True
    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:

            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            at_war = False
        elif player_two_cards[-1].value > player_one_cards[-1].value:

            player_two.add_cards(player_two_cards)
            player_two.add_cards(player_one_cards)
            at_war = False
        else:
            print('THERE IS WAR!!')
            if len(player_one) < 3:
                print( f"Player {player_one.name} unable to declare war. Player {player_two.name} has won!")
                game_on =  False
                break
            elif len(player_two) < 3:
                print( f"Player {player_two.name} unable to declare war. Player {player_one.name} has won!")
                game_on = False
                break
            else:
                for x in range(3):
                    player_one_cards.append(player_one.remove_card())
                    player_two_cards.append(player_two.remove_card())
