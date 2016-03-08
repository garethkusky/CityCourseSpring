__author__ = 'acpb968'
import random
def main():
    deck = list(range(0,52))

    random.shuffle(deck)
    for element in deck[0:4]:
        print (getCard(element))


def getCard(cardNumber):

    if cardNumber//13 == 0:
        suit="Spades"
    elif cardNumber//13 == 1:
        suit="Hearts"
    elif cardNumber //13 == 2:
        suit="Diamonds"
    elif cardNumber //13 == 3:
        suit="Clubs"
    else:
        print("there has been an error getting suit")

    if (cardNumber % 13)==0:
        card ="A"
    elif (cardNumber % 13)==1:
        card="2"
    elif (cardNumber % 13)==2:
        card="3"
    elif (cardNumber % 13)==3:
        card="4"
    elif (cardNumber % 13)==4:
        card="5"
    elif (cardNumber % 13)==5:
        card="6"
    elif (cardNumber % 13)==6:
        card="7"
    elif (cardNumber % 13)==7:
        card="8"
    elif (cardNumber % 13)==8:
        card="9"
    elif (cardNumber % 13)==9:
        card="10"
    elif (cardNumber % 13)==10:
        card="J"
    elif (cardNumber % 13)==11:
        card="Q"
    elif (cardNumber % 13)==12:
        card="K"
    else:
        print ("Error getting card")


    return card + " " + suit

main()