__author__ = 'acpb968'
#Conversion from kilograms to pounds
#Write a program that displays the following table (note that 1 kilogram is 2.2 pounds)
#1 2.2
#3 6.6
#...
#197 433.4
#199 437.8

print ("Kilograms", end='  ')
print ("Pounds")

for i in range (1,200,2):
    print (i, end="   ")
    print (str(int((i*2.2)*100)/100))

