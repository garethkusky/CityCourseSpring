#Write a test program that
#creates a Stock object with the stock symbol INTC, the name Intel Corporation, the previous
#closing price of 20.5, and the new current price of 20.35, and display the price­change
#percentage.

from stock import Stock

class main():
    myStock=Stock('INTC','Intel Corporation',20.5,20.35)
    print("Stock Informtion: Name=", myStock.getName(),", Symbol=", myStock.getSymbol())
    print("Day1: Previous Closing Price:",myStock.getClosePrice(),\
          ", Current Price: ", myStock.getCurPrice(),",Perc Change: ", str(int(myStock.getChangePercent()*100)/100)+ "%")
    # test update prices
    myStock.setClosePrice(20.35)
    myStock.setCurrentPrice(20.66)

    print("Day2: Previous Closing Price:",myStock.getClosePrice(),\
          ", Current Price: ", myStock.getCurPrice(),", Perc Change: ", str(int(myStock.getChangePercent()*100)/100)+ "%")

main()