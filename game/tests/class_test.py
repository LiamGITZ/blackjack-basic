import unittest
from context import *
from deck import *

class TestDeckMethods(unittest.TestCase):
    def test_create52(self):
        deck1 = deck()
        deck2 = deck()

        deck1.emptyDeck()
        deck2.emptyDeck()

        deck1.create52()
        deck2.create52()
        self.assertEqual(deck1, deck2)

        deck1.create52(5)
        deck2.create52(5)
        self.assertEqual(deck1, deck2)

        deck1.create52(43135)
        deck2.create52(43135)
        self.assertEqual(deck1, deck2)
    
    
        self.assertRaises(ValueError, deck1.create52(), 0)
        self.assertRaises(ValueError, deck1.create52(), -213)
    
    def test_shuffle(self):
        deck1 = deck()
        deck2 = deck()
        
        self.assertEqual(deck1,deck2)
        deck1.shuffleDeck()
        self.assertNotEqual(deck1,deck2)
        deck1val = deck1.getDeck()
        deck2val = deck2.getDeck()
        self.assertEqual(sorted(deck1val),sorted(deck2val))

    def test_drawCard(self):
        deck1 = deck()
        deckList = deck1.getDeck()
        numberCards = 0
        while not (deck1.isEmpty()):
            c  = deck1.drawCard()
            assert(c in deckList)
            numberCards+=1
        self.assertEqual(numberCards, 52)

class TestCardMethods(unittest.TestCase):
    def test_randomize(self):
        for s in range(Card.MAX_SUIT):
            for v in range(Card.MAX_VALUE):
                c1 = Card(s+1,v+1)
                c2 = Card(s+1,v+1)
                self.assertEqual(c1,c2)
                while (c1 == c2):
                    c1.randomise()
                self.assertNotEqual(c1,c2)

    def test_changeSuit(self):
        c1 = Card(1,1)
        c1.changeSuit(2)
        c2 = Card(2,1)
        self.assertEqual(c1,c2)
        for s in range(Card.MAX_SUIT):
            c1.changeSuit(s+1)
            c2 = Card(s+1,1)
            self.assertEqual(c1,c2)

    def test_changeValue(self):
        c1 = Card(1,1)
        c1.changeValue(3)
        c2 = Card(1,3)
        self.assertEqual(c1,c2)
        for v in range(Card.MAX_VALUE):
            c1.changeValue(v+1)
            c2 = Card(1,v+1)
            self.assertEqual(c1,c2)


if __name__ == '__main__':
    unittest.main()
