__author__ = 'acpb968'
#Count positive and negative numbers and compute the average of numbers
#Write a program that reads an unspecified number of integers, determines how many positive
#and negative values have been read, and computes the total and average of the input values
#(not counting zeros). Your program ends with the input 0 . Display the average as a floatingpoint
#number

# set inital values
positiveCount=0
negativeCount=0
total=0
sum=0
num=-1 # set to negative to allow initial entry to while loop

while num != 0:
    num=eval(input("please enter an integer, will exit on 0: "))

    if num > 0: # if value is positive
        positiveCount +=1
        sum=sum+num
        total +=1
    elif num < 0: # if value is negative
        negativeCount +=1
        sum=sum+num
        total +=1
    elif total==0 and num ==0: # if value is 0 and first run
        print("you didnt enter a number")

if total>0: # only output results when first value is not 0
    average = sum/total
    print (sum, average, total)
    print("the number of positives is " + str(positiveCount),
      "\nthe number of negatives is " + str(negativeCount),
      "\nthe total is " + str(sum),
      "\nthe average is " + str(average))
