__author__ = 'acpb968'
#Display matrix of 0s and 1s
#write a fucntion that displays an n-by-n matrix using the following header:
#def printMatrix(n):
#Each element is 0 or 1, which is generated randomly. Write a test program that
# prompts the user to enter n and displays an n-by-n matrix. here is a sample run:
#Entern:3
#010
#000
#111
import random
def printMatrix(n):
    i=0
    for i in range (n):
        for i in range (n):
            print(random.randint(0, 1),end='')

        print()


def main():
    matrixSize=eval(input("please enter the number of elements in the matrix: "))
    printMatrix(matrixSize)
main()