set1 = {"green", "red", "blue", "red"} # Create a set
print("1",set1)

set2 = set([7, 1, 2, 23, 2, 4, 5]) # Create a set from a list
print("2",set2)

print("3 Is red in set1?", "red" in set1)

print("4 length is", len(set2)) # Use function len
print("5 max is", max(set2)) # Use max
print("6 min is", min(set2)) # Use min
print("7 sum is", sum(set2)) # Use sum

set3 = set1 | {"green", "yellow"} # Set union
print("8",set3)

set3 = set1 - {"green", "yellow"} # Set difference
print("9",set3)

set3 = set1 & {"green", "yellow"} # Set intersection
print("10",set3)

set3 = set1 ^ {"green", "yellow"} # Set exclusive or
print("11",set3)

list1 = list(set2) # Obtain a list from a set
print("12",set1 == {"green", "red", "blue"}) # Compare two sets

set1.add("yellow")
print("13",set1)

set1.remove("yellow")
print("14",set1)
