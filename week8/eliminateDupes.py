__author__ = 'acpb968'
#Write a function that returns a new list by eliminating the duplicate values in the list. Use the
#following function header:
#def eliminateDuplicates(lst):
#Write a test program that reads in a list of integers, invokes the function, and displays the result.
#Here is the sample run of the program:
#Enter ten numbers: 1 2 3 2 1 6 3 4 5 2
#The distinct numbers are: 1 2 3 6 4 5

def main():
    list=[int(x) for x in input("Enter ten Numbers: ").split()]
    distinct=eliminateDuplicates(list)
    print("the distinct Numbers are: ", distinct)

def eliminateDuplicates(lst):
    list2=[]
    for x in range (0,len(lst)):
        if list2.index(lst(x))==False:
            list2.append[lst(x)]

    return list2

main()