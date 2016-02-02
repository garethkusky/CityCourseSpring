__author__ = 'acpb968'
#Write a program that displays the following
#table (note that 1 mile is 1.609 kilometres):
#Miles Kilometres
#1 1.609
#2 3.218
#...
#9 15.481
#10 16.090

print ("Miles", end='  ')
print ("Kilometers")

for i in range (1,11):
    print (format(i,'<5d' ), end='')
    print (str(int((i*1.609)*1000)/1000))