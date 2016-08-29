import random

class Deck:
    Value = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13}
    suits = ['Hearts','Spades','Clubs','Diamonds']
    numbers = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
    """ This class has a single inner class.  For the sake of compartmentalization I have put it here instead of its own file."""
class card:
    def __init__(self, suit, face_or_number):
        self.suit = suit
        self.face_or_number = face_or_number

    # representaion when printed, javas toString override
    def __repr__(self):
        self.str_rep = self.face_or_number + ' of ' + self.suit
        return self.str_rep


def __init__(self):
    self.deck = []
    # For every thing in the lists make a deck
    for suit in self.suits:
        i = suit
        for numberFace in self.numbers:
            j = numberFace
            self.deck.append(Deck.card(i, j))
    random.shuffle(self.deck)


def print_whole_deck(self):
    for cards in self.deck:
        print(cards)


def deal_card(self):
    # this method deals from the bottom of the deck ( I know that's not legal technically but whatever)
    try:
        one_card = self.deck.pop()
        return one_card
    except IndexError:
        "The game experienced an unexpected error! There were no cards left!"