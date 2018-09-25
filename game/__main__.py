from classes.card import *
from classes.deck import *
import sys
import os


"""
function that takes in a list of cards and returns their integer value
counts aces as 11 if the resulting hand would be less than 21
and as 1 if the hand would otherwise bust
"""
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

"""
simple function to determine whether to prin a or an depening on if
the given string begins with an a, i, e, o, or u
"""
def AorAn(nstring):
    if nstring[0] == 'a' or nstring[0] =='e' or nstring[0] =='i' \
            or nstring[0] == 'o' or nstring[0] == 'u':
        return 'an'
    else:
        return 'a'

def handString(hand):
    handString = ''
    for card in hand:
        if card is hand[-1]:
            handString += 'and ' + AorAn(card.toString()) + ' ' + card.toString() + '.'
        elif len(hand) == 2:
            handString += AorAn(card.toString()) + ' ' + card.toString()+ ' '
        elif card is playerHand[-2]:
            handString += AorAn(card.toString()) + ' ' + card.toString() + ', '
        else:
            handString += AorAn(card.toString()) + ' ' + card.toString() + ', '
    return(handString)
   
"""
reading in the player's setting choices
"""
while True:
    try:
        numb = input('Enter the number of standard decks you would like to play with: ')
        number = int(numb)
    except (ValueError, SyntaxError, NameError) as error:
        print("Invalid number")
        continue
    if number <= 0:
        print("The number of decks must be greater than 0")
        continue
    else:
        break

while True:
    try:
        amnt = input('Enter the amount of money you would like to buy in with: $')
        money = int(amnt)
    except (ValueError, SyntaxError, NameError) as error:
        print("Invalid number must be int")
        continue
    if money <= 0:
        print("The amount must be greater than 0")
        continue
    else:
        break

#initializing our deck(s) to be randomized
theDeck = deck()
theDeck.create52(number)
theDeck.shuffleDeck()

startingMoney = money
wantToPlay = True
while wantToPlay:

    os.system('cls' if os.name == 'nt' else 'clear') #clears the screen
    print("You have $" + str(money) + " to bet")

    #take in bet
    moneyBet = 0
    while True:
        try:
            amntBet = input('Enter the amount of money you would like to buy in with: $')
            moneyBet = int(amntBet)
        except (ValueError, SyntaxError, NameError) as error:
            print("Invalid number must be int")
            continue
        if moneyBet <= 0:
            print("The amount must be greater than 0")
            continue
        if moneyBet > money:
            print("You only have $" + str(money) + " to bet")
        else:
            break


    print("Dealing cards ...")
    dealerHand = []
    playerHand = []

    dealerHand.extend(theDeck.drawCard(2))
    playerHand.extend(theDeck.drawCard(2))

    print("The dealer is showing " + AorAn(dealerHand[0].toString()) \
            + ' ' + dealerHand[0].toString())
    print()

    """
    player deciding whether they want to hit or stand
    """
    while True:       
        print("Your hand is " + handString(playerHand) + " Your hand's value is: " \
            + str(handValue(playerHand)))
        ans = ""
        if handValue(playerHand) >= 21:
            break
        try:
            ans = input('Would you like to hit or stand? ')
        except (ValueError, SyntaxError, NameError) as error:
            print(error)
        if ans.strip() == "":
            print("Invalid input ")
            continue
        ans = ans.strip().split()[0].lower()  #string formating to make input more lenient
        if ans == 'hit' or ans == 'h':
            playerHand.append(theDeck.drawCard())
            print()
            print('you hit ' + AorAn(playerHand[-1].toString()) + ' '\
                    + playerHand[-1].toString())
            continue
        elif ans == 'stand' or ans == 's' or ans == 'stnd':
            break
        else:
            print('Could not comprehend your answer')

    """
    dealer is automated to hit while under the value 17 and stop
    at or above the hand value of 17
    """
    os.system('cls' if os.name == 'nt' else 'clear') 
    while handValue(dealerHand) < 17:
        dealerHand.append(theDeck.drawCard())
   

    """
    deciding who won and the manner in which they won
    """   
    playerHandValue = handValue(playerHand)
    dealerHandValue = handValue(dealerHand)
    pbust = False
    dbust = False
    if playerHandValue > 21:
        print('You drew ' + AorAn(playerHand[-1].toString()) + ' ' \
                + playerHand[-1].toString() + ' and busted! fbm QQ ')
        pbust = True;
    elif playerHandValue == 21:
        print('Wow you somehow managed to get blackjack!')
    if dealerHandValue > 21:
        dbust = True

    winner = '?'
    ##winnner decide
    if pbust & (not dbust): 
        winner = 'dealer'
    elif (not pbust) & dbust:
        winner = 'player'
    elif pbust & dbust:
        winner = 'push'
    else:
        if playerHandValue > dealerHandValue:
            winner = 'player'
        elif dealerHandValue > playerHandValue:
            winner = 'dealer'
        else:
            winner = 'push'


    ############ formatting results ############

    print("The results are: ")
    print()

    # printing player's hand
    print('Your hand is ' + handString(playerHand))
    print('The value of your hand is ' + str(playerHandValue))
    print()


    # printing dealer's hand
    print("The Dealer's hand is " + handString(dealerHand))
    print("The value of the Dealer's hand is " + str(dealerHandValue))
    print()

    # print outcome
    if winner == 'player':
        print('Congrats you won the round and gained $' + str(moneyBet) + '!')
        money += moneyBet
    elif winner == 'dealer':
        print('Unfortunatley you did not win this round and lost $' + str(moneyBet)\
                + ' try again next time? ')
        money -= moneyBet
    elif winner == 'push':
        print('The good news is you didn t lose any money unfortunatley \
                you didnt gain any either good luck in the next round')
    else:
        print("Error winner undecided?")
    print()

        
    if theDeck.numCards() < 20:
        print('-'*50)
        print("Fewer than 20 cards game will now exit")
        wantToPlay = False
    elif money <= 0:
        print('-'*50)
        print("You are out of money come again another time!")
        wantToPlay = False
    else:
        while True:
            try:
                ans = input('Would you like to play another hand? (yes or no) ')
                ans = ans.strip().split()[0].lower()
            except (ValueError, SyntaxError, NameError) as error:
                continue
            if ans == 'yes' or ans == 'y':
                break
            elif ans == 'no' or ans == 'n':
                wantToPlay = False
                break
            else:
                print('could not comprehend your answer')

#######################################
print()
if (money-startingMoney >= 0):
    print("Your final results are you gained: $"+str(money-startingMoney))
else:
    print("Your final results are you lost: $"+str(startingMoney-money))
    print("How unfortunate !")

