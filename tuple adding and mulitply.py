# Adding tuples
this_tuple = ("apple", "grapes", "mango", "papaya")
that_tuple = ("brinjal", "potato", "tomato", "ginger")
v = this_tuple + that_tuple
print(v)

# multiplying tuples
yy = this_tuple*3
print(yy)

# Methods of tuple
# count() - 	Returns the number of times a specified value occurs in a tuple
# index() -     Searches the tuple for a specified value and,
#               returns the position of where it was found

thistuple = (1, 3, 7, 8, 7, 4, 5, 5, 4, 6, 8, 5, 4, 4)
print(thistuple.count(4))

print(thistuple.index(5))
