import random
import os
import sys
from os import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../classes')))
from card import *


"""
class to create a deck of card objects to simulate card games
"""
class deck (object):
    __cardCollection = [];
    def __init__(self):
        self.create52()


    """
ised ...
    adds a full 52 standard deck of cards into the deck 
    specified number of times or once by defualt
    """
    def create52(self, numDecks = None):
        self.__cardCollection = []
        if numDecks == None:
            numDecks = 1 
        elif  numDecks < 1:
            raise ValueError('what are negative decks?')
        for s in Suit:
            for v in Value:
                if v != Value.joker:
                    self.__cardCollection.append(Card(s,v))
        tempList = list(self.__cardCollection)
        for i in range(numDecks-1):
            self.__cardCollection.extend(tempList)

    """
    randomizes all cards in deck
    """
    def shuffleDeck(self):
        random.shuffle(self.__cardCollection)

    """
    removes and returns specified number of cards from the deck in a list
    by default a singluar card object
    """
    def drawCard(self, numCards = None):
        if numCards == None:
            drawnCard = self.__cardCollection.pop()
            return drawnCard
        else:
            drawnCards = []
            for i in range(numCards):
                drawnCards.append(self.__cardCollection.pop())
            return drawnCards


    def getDeck(self):
        deckCopy = self.__cardCollection.copy()
        return deckCopy


    def addCard(self, gcard):
        self.__cardCollection.append(gcard)

    def isEmpty(self):
        if not self.__cardCollection:
            return True
        else:
            return False


    def numCards(self):
        return len(self.__cardCollection)


    def emptyDeck(self):
        self.__cardCollection = []


    def __eq__(self, otherDeck):  
        return self.__cardCollection == otherDeck.getDeck()

