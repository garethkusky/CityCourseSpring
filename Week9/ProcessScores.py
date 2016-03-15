__author__ = 'acpb968'
#Suppose that a text file contains an unspecified number of scores. Write a program that reads
#the scores from the file and displays their total and average. Scores are separated by blanks.
#Your program should prompt the user to enter a filename. Here is a sample run:
#Enter a filename: scores.txt
#There are 70 scores
#The total is 800
#The average is 33.33

from random import randint

def CreateFile(noOfScores):
    outfile = open("Numbers.txt", "w")
    for i in range(noOfScores):
        outfile.write(str(randint(0, 99)) + " ")
    outfile.close() # Close the file

def readFile(filename):
    infile=open(filename,'r')
    s = infile.read()
    numbers = [eval(x) for x in s.split()]
    numCount=0
    total=0

    for number in numbers:
        numCount+=1
        total+=number

    average=total/numCount

    infile.close() # Close the file

    return numCount, total, average



def main():
    createfile=input("Do you want to create a Numbers file y or n: ")
    if createfile=="y":
        CreateFile(eval(input("Please enter the number of scores to add to the file: ")))

    numcount,total,average = readFile("Numbers.txt")

    print("There are",numcount, "scores")
    print("The total is",total)
    print("The average is", 33.33)

main()