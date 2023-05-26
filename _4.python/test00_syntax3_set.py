set1 = {"green", "red", "blue", "red"} # Create a set
print(set1)

set2 = set([7, 1, 2, 23, 2, 4, 5]) # Create a set from a list
print(set2)

print("Is red in set1?", "red" in set1)

print("length is", len(set2)) # Use function len
print("max is", max(set2)) # Use max
print("min is", min(set2)) # Use min
print("sum is", sum(set2)) # Use sum

set3 = set1 | {"green", "yellow"} # Set union
print(set3)

set3 = set1 - {"green", "yellow"} # Set difference
print(set3)

set3 = set1 & {"green", "yellow"} # Set intersection
print(set3)

set3 = set1 ^ {"green", "yellow"} # Set exclusive or
print(set3)

list1 = list(set2) # Obtain a list from a set
print(set1 == {"green", "red", "blue"}) # Compare two sets

set1.add("yellow")
print(set1)

set1.remove("yellow")
print(set1)




import random
import time


print('set 和 list 速度比較')
NUMBER_OF_ELEMENTS = 50000

# Create a list
lst = list(range(NUMBER_OF_ELEMENTS))
random.shuffle(lst)

# Create a set from the list
s = set(lst)

# Test if an element is in the set
startTime = time.time() # Get start time
for i in range(NUMBER_OF_ELEMENTS):
    i in s
endTime = time.time() # Get end time
runTime = int((endTime - startTime) * 1000) # Get test time
print("To test if", NUMBER_OF_ELEMENTS, 
    "elements are in the set\n",
    "The runtime is", runTime, "milliseconds")

# Test if an element is in the list
startTime = time.time() # Get start time
for i in range(NUMBER_OF_ELEMENTS):
    i in lst
endTime = time.time() # Get end time
runTime = int((endTime - startTime) * 1000) # Get test time
print("\nTo test if", NUMBER_OF_ELEMENTS, 
    "elements are in the list\n",
    "The runtime is", runTime, "milliseconds")

# Remove elements from a set one at a time
startTime = time.time() # Get start time
for i in range(NUMBER_OF_ELEMENTS):
    s.remove(i)
endTime = time.time() # Get end time
runTime = int((endTime - startTime) * 1000) # Get test time
print("\nTo remove", NUMBER_OF_ELEMENTS, 
    "elements from the set\n",
    "The runtime is", runTime, "milliseconds")

# Remove elements from a list one at a time
startTime = time.time() # Get start time
for i in range(NUMBER_OF_ELEMENTS):
    lst.remove(i)
endTime = time.time() # Get end time
runTime = int((endTime - startTime) * 1000) # Get test time
print("\nTo remove", NUMBER_OF_ELEMENTS, 
    "elements from the list\n",
    "The runtime is", runTime, "milliseconds")
