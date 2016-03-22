tuple1 = ("green", "red", "blue") # Create a tuple
print("1",tuple1)

tuple2 = tuple([7, 1, 2, 23, 4, 5]) # Create a tuple from a list
print("2",tuple2)

print("3 length is", len(tuple2)) # Use function len
print("4 max is", max(tuple2)) # Use max
print("5 min is", min(tuple2)) # Use min
print("6 sum is", sum(tuple2)) # Use sum

print("7 The first element is", tuple2[0]) # Use indexer

tuple3 = tuple1 + tuple2 # Combine 2 tuples
print("8",tuple3)

tuple3 = 2 * tuple1 # Multiple a tuple
print("9",tuple3)

print("10",tuple2[2 : 4]) # Slicing operator
print("11",tuple1[-1])

print("12",2 in tuple2) # in operator

for v in tuple1:
    print("13",v, end = " ")
print()
    
list1 = list(tuple2) # Obtain a list from a tuple
list1.sort()
tuple4 = tuple(list1)
tuple5 = tuple(list1)
print("14",tuple4)
print("15",tuple4 == tuple5) # Compare two tuples
