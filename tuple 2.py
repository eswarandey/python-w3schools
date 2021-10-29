# Assigning items to tuple is also called packing
# and removing items is called as unpacking
fruits = ("apple", "banana", "cherry")
print(fruits)

(you, can, do) = fruits
print(can)

# asterisk "*" is used to store more than one item in the single variable,
# while unpacking the tuple
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(one, two, *three) = fruits
print(three)

# If the asterisk is added to another variable name than the last,
# Python will assign values to the variable until
# the number of values left matches the number of variables right.

fruits = ("apple", "mango", "papaya", "pineapple", "cherry", "grape")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)
