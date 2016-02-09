__author__ = 'acpb968'
#Number of days in a year
#Write a function that returns the number of days in a year using the following header:
#defnumberOfDaysInAYear(year):
#Write a test program that displays the number of days in the years from 2010 to 2020 .
#NB: You can use the following Boolean expressions to determine whether a year is a leap year:
# A leapyearisdivisibleby4
#isLeapYear=(year%4==0)
#Aleapyearisdivisibleby4butnotby100
#isLeapYear=isLeapYearand(year%100!=0)
##Aleapyearisdivisibleby4butnotby100ordivisibleby400
#isLeapYear=isLeapYearor(year%400==0)
#or you can combine all these expressions into one, like this:
#1 of 4
#City ?Short Courses
#isLeapYear=(year%4==0andyear%100!=0)or(year%400==0)

def daysInYear(year):
    isLeapYear=(year %4==0 and year %100!=0) or (year %400==0)
    if (isLeapYear):
        days=366
    else:
        days=365

    print ("Number of days in ", year, " is ", days)

def main():
    # call function for each of the years from 2010 up to and including 2020
    for i in range (2010,2021):
        daysInYear(i)

main()