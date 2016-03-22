__author__ = 'acpb968'
# Count occurrences of numbers
# Write a program that reads an unspecified number of integers and finds the ones that have the
# all of them should be reported. For example, since 9 and 3 appear twice in the list 9 30 3 9 3 2 4
# , both occurrences should be reported.

def main():
    line=input("Please enter a list fo numbers:")
    numCounts={}
    processNumbers(line,numCounts)

    pairs = list(numCounts.items()) # Get pairs from the dictionary

    items = [[x, y] for (y, x) in pairs] # Reverse pairs in the list

    items.sort() # Sort pairs in items
    print (items)
    dict={}
    for i in range(0, len(items)):
        print(i)
        print(str(list[i]))
        dict[list[i][0]]=list[i][1]

    print (dict)



def processNumbers(line,numCounts):

    numbers = line.split() # Get words from each line
    for number in numbers:
        if number in numCounts:
            numCounts[number] += 1
        else:
            numCounts[number] = 1


main()

