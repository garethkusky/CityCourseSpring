__author__ = 'acpb968'
#Display leap years
#Write a program that displays, ten per line, all the leap years in the twenty-first century
#(from year 2001 to 2100). The years are separated by exactly one space.

count=0
for i in range (2001,2100):
    if i %4 ==0 or i %400 ==0: # check if year is a leap year
       print(i, end=" ")
       count +=1

    if count==10: # every 10 leap years add a new line and reset count
        count=0
        print()