__author__ = 'acpb968'
#Write a program that removes all the occurrences of a specified string from a text file. Your
#program should prompt the user to enter a filename and a string to be removed. Here is a
#sample run:
#Enter a filename: test.txt
#Enter the string to be removed: morning
#Done
import pickle

def createTestFile():
    outfile = open("testFile.txt", "w")

    # Write data to the file
    outfile.write("Wales are Amazing\n")
    outfile.write("Wales are great\n")
    outfile.write("Wales are Euro 2016 Champions")
    outfile.close()

def fileContents(fileName):
    infile=open(fileName,"r")
    inline=infile.readlines()
    for x in range(0,len(inline)):
        print(inline[x], end="")

    infile.close()

def main ():
    filename = input("Enter a filename: ").strip()
    #filename = "testFile.txt"
    removeText = input("Enter the text to remove: ").strip()
    print ("File contents before removing text: ")
    fileContents(filename)

    infile = open(filename, 'r')# Open the file
    outline=infile.readlines()
    for x in range(0, len(outline)):
        outline[x]=outline[x].replace(removeText,"")

    infile.close()

    outfile=open(filename, 'w')
    outfile.writelines(outline)
    outfile.close()
    print ("File contents after removing text: ")
    fileContents(filename)


createTestFile()
main()