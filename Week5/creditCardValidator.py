__author__ = 'acpb968'
#Write a program that prompts the user to enter a credit card number as an integer.
#Display whether the number is valid or invalid. Design your program to use the following
#functions:
#Returntrueifthecardnumberisvalid
#defisValid(number):
#GettheresultfromStep2
#defsumOfDoubleEvenPlace(number):
#Returnthisnumberifitisasingledigit,otherwise,return
#thesumofthetwodigits
#defgetDigit(number):
#Returnsumofoddplacedigitsinnumber
#defsumOfOddPlace(number):
#Returntrueifthedigitdisaprefixfornumber
#defprefixMatched(number,d):
#Returnthenumberofdigitsind
#defgetSize(d):
#Returnthefirstknumberofdigitsfromnumber.Ifthe
#numberofdigitsinnumberislessthank,returnnumber.
#defgetPrefix(number,k):

#Return true if the cardnumber is valid
def isValid(number):

#Get the result from Step 2
def sumOfDoubleEvenPlace(number):

#Return this number if it is a singledigit, otherwise, return
#the sum of the two digits
def getDigit(number):

#Return sum of odd place digits in number
def sumOfOddPlace(number):

#Return true if the digit d is a prefix for number
def prefixMatched(number,d):

#Return thenumber of digits in d
def getSize(d):

#Return the first k number of digits from number. If the
#number of digits in number is less than k, returnnumber.
def getPrefix(number,k):


def main():
    print(isValid(eval(input("Please enter a credit card number: "))))


main()