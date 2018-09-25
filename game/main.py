from classes.card import *
from classes.deck import *
class blackJackEval:
    
    def handValue(hand):
        handValue = 0;
        numAces = 0;
        if not hand:
            return 0
        for card in hand:
            if card.value.value == 1:
                numAces+= 1
            elif card.value.value > 10:
                    handValue += 10
            else:
                handValue += card.value.value
        for i in range(numAces):
            if (handValue+11) > 21:
                handValue += 1
            else:
                handValue += 11
        return handValue

