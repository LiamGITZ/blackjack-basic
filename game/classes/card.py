import random
from enum import Enum


Suit = Enum('Suit', 'hearts diamonds clubs spades')
Value = Enum('Value', 'ace two three four five six seven eight nine ten \
            jack queen king joker')


class Card (object):
    MIN_SUIT = 1
    MAX_SUIT = 4
    MIN_VALUE = 1
    MAX_VALUE = 14

    """
    generates a card with a given suit and value 
    if none specified generates a random card
    """
    def __init__(self, gsuit=None, gvalue=None):
        if gsuit == None:
            self.suit = Suit(random.randint(Card.MIN_SUIT,Card.MAX_SUIT))
        else:
            try:
                self.suit = Suit(gsuit)
            except ValueError:
                print("suit out of range! -see Suit Enum in card.py-")
                self.suit = Suit(random.randint(Card.MIN_SUIT,Card.MAX_SUIT))
        
        if gvalue == None:
            self.value = Value(random.randint(Card.MIN_VALUE,Card.MAX_VALUE))
        else:
            try:
                self.value = Value(gvalue)
            except ValueError:
                print("value out of range! -see Value Enum in card.py-")
                self.value = Value(random.randint(Card.MIN_VALUE,Card.MAX_VALUE))
    
    """
    randomize suit and value
    """
    def randomise(self):
        self.suit = Suit(random.randint(Card.MIN_SUIT,Card.MAX_SUIT))
        self.value = Value(random.randint(Card.MIN_VALUE,Card.MAX_VALUE))


    """
    changes suit to specified value or random if none specified
    """
    def changeSuit(self, gsuit=None):
        if gsuit == None:
            self.suit = Suit(random.randint(Card.MIN_SUIT,Card.MAX_SUIT))
        else:
            try:
                self.suit = Suit(gsuit)
            except ValueError:
                print("suit out of range! -see Suit Enum in card.py-")
                self.suit = Suit(random.randint(Card.MIN_SUIT,Card.MAX_SUIT))


    """
    changes value to specified value or random if none specified
    """
    def changeValue(self, gvalue=None):
        if gvalue == None:
            self.value = Value(random.randint(Card.MIN_VALUE,Card.MAX_VALUE))
        else:
            try:
                self.value = Value(gvalue)
            except ValueError:
                print("value out of range! -see Value Enum in card.py-")
                self.value = Value(random.randint(Card.MIN_VALUE,Card.MAX_VALUE))
    
    """
    returns a printable string of the given card
    """
    def toString(self):
        return (self.value.name + " of " + self.suit.name)

    def __eq__(self, otherCard):
        return (self.value == otherCard.value) & (self.suit == otherCard.suit)
        
    def __gt__(self, otherCard):
        return (self.value.value*5 + self.suit.value) > (otherCard.value.value*5 + otherCard.suit.value)

