from random import shuffle
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7 ,'Eight':8, 'Nine':9, 'Ten':10
,'Jack':10, 'Queen':10, 'King':10, 'Ace':11} #These are the global values of cards
game_on=  True
class Card:
    """Card(suit,rank)
       here, suit and rank are str type"""

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} of {self.suit}'

class Deck:

    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))

    def __len__(self):
        #This returns How many card objects are in a deckß
        return len(self.all_cards)

    def __str__(self):
        deck_composition = ""
        for card in self.all_cards:
            deck_composition += "\n"+ card.__str__()
        return 'The Deck has ' + deck_composition

    def shuffle(self):
        shuffle(self.all_cards)

    def deal_card(self,card_amount):
        cards = []
        if card_amount <= len(self.all_cards):
            for _ in range(card_amount):
                cards.append(self.all_cards.pop())
        else:
            print('You don\'t have enough cards in deck')
        return cards

class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0


    def __str__(self):
        card_str = ''
        for x in self.cards:
            card_str += "\n"+ x.__str__()
        return card_str

    def add_cards(self,added_cards):
        if isinstance(added_cards,list): # checking if added_cards is a list so to avoid a nested list
            self.cards.extend(added_cards)
            for card in added_cards:
                self.value += values[card.rank] # For each card object i
        else:
            self.cards.append(added_cards)
            self.value += values[added_cards.rank]

        for card in added_cards:
            if card.rank == 'Ace':
                self.aces += 1

    def adjusting_ace(self):
        #If Value > 21 change the  ace value from 11 to 1 so we don't bust
        while self.value > 21 and self.aces: # Using self.aces as a bool
            self.value -= 10
            self.aces -= 1

class Chips:

    def __init__(self,total_chips=100):
        self.total_chips = total_chips
        self.bet=0

    def win_bet(self):
        self.total_chips += self.bet

    def lose_bet(self):
        self.total_chips -= self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How much do you want to bet this round : '))
        except:
            print('Bets must be a integer!')
        else:
            if chips.bet > chips.total_chips:
                print(f'Sorry You don\'t have enough chips! You have {chips.total_chips} chips')
            else:
                break

def hit(deck,hand,add=1):
    hand.add_cards(deck.deal_card(add))
    hand.adjusting_ace()

def hit_or_stand(deck,hand):

    while True:
        choice = input('Hit or Stand. input H for Hit and S for stand : ')
        if choice[0].lower() not in ['h','s']:
            print('Sorry I Did not get that. Try Again! ')
            continue
        else:
            if choice[0].lower() == 'h':
                hit(deck,hand)
                return True

            elif choice[0].lower() == 's':
                return False

def continue_playing():

    while True:
        choice = input('Continue Playing? , Yes or No : ')
        if choice[0].lower() not in ['y','n']:
            print('Sorry I Did not get that. Try Again! ')
            continue
        else:
            if choice[0].lower() == 'y':
                return True

            elif choice[0].lower() == 'n':
                return False
# DISPLAYING CARDS
def display_some(dealer,player):

    print('\n| Dealer\'s Hand |')
    print('REDACTED CARD')
    print(dealer.cards[-1])

    print('\n| Player\'s Hand |')
    print(player)

def display_all(dealer,player):

    print('\n| Dealer\'s Hand |')
    print(dealer)
    print(f'\nValue of Dealer\'s Hand is {dealer.value}')

    print('\n| Player\'s Hand |')
    print(player)
    print(f'\nValue of Player\'s Hand is {player.value}')
#END GAME CONDITIONS
def player_busts(chips):

    print('Player Busts!!')
    chips.lose_bet()

def dealer_busts(chips):

    print('Player Wins! Dealer Busts!')
    chips.win_bet()

def player_wins(chips):

    print('Player Wins!!')
    chips.win_bet()

def dealer_wins(chips):

    print('Dealer Wins!!')
    chips.lose_bet()
def push():

    print('Player and Dealer Tie! Its a push!!')
#GAME LOGIC
if __name__ == '__main__':
    player_chips = Chips()#This is here so that it doesn't reset if player continues to play after a single round
    while True:
        #Setting the game up
        print('Welcome To BlackJack!\nDealer can hit until he reaches 17 in card value')
        game_on = True
        game_deck = Deck()
        game_deck.shuffle()

        player_hand = Hand()
        player_hand.add_cards(game_deck.deal_card(2))#This adds 2 cards from deck to player hand

        dealer_hand =  Hand()
        dealer_hand.add_cards(game_deck.deal_card(2))#this adds 2 cards from deck to dealer hand


        take_bet(player_chips) # Taking the bets

        display_some(dealer_hand,player_hand)

        while game_on:

            game_on = hit_or_stand(game_deck,player_hand)
            display_some(dealer_hand,player_hand)

            if player_hand.value > 21:
                player_busts(player_chips)
                break
        if player_hand.value <= 21:

            while dealer_hand.value < 17:
                hit(game_deck,dealer_hand)

            display_all(dealer_hand,player_hand)
            if dealer_hand.value > 21:
                dealer_busts(player_chips)
                game_on = False
            elif player_hand.value > dealer_hand.value:
                player_wins(player_chips)
                game_on = False
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_chips)
                game_on = False
            else:
                push()
                game_on = False

        print(f'Player\'s Winnings stand at {player_chips.total_chips} chips.')
        if continue_playing() is True:
            continue
        else:
            break
