#Design a class named Stock to represent a company’s stock that contains:
#■ A private string data field named symbol for the stock’s symbol.
#■ A private string data field named name for the stock’s name.
#■ A private float data field named previousClosingPrice that stores the stock
#price for the previous day.
#■ A private float data field named currentPrice that stores the stock price for
#the current time.
#■ A constructor that creates a stock with the specified symbol, name, previous
#price, and current price.
#■ A get method for returning the stock name.
#■ A get method for returning the stock symbol.
#■ Get and set methods forgetting/setting the stock’s previous price.
#■ Get and set methods for getting/setting the stock’s current price.
#■ A method named getChangePercent() that returns the percentage changed
#from previousClosingPrice to currentPrice.
#Draw the UML diagram for the class, and then implement the class.

class Stock:
        # Construct a stock object with default sizes
        def __init__(self, symbol, name, closePrice=0.00, curPrice=0.00):
            self.__symbol=symbol
            self.__name=name
            self.__closePrice=closePrice
            self.__curPrice=curPrice

        def getName(self):
            return self.__name

        def getSymbol(self):
            return self.__symbol

        def getClosePrice(self):
            return self.__closePrice

        def getCurPrice(self):
            return self.__curPrice

        def setClosePrice(self, newClosePrice):
            self.__closePrice=newClosePrice

        def setCurrentPrice(self,newCurPrice):
            self.__curPrice=newCurPrice

        def getChangePercent(self):
            return ((self.__curPrice/self.__closePrice) * 100)-100