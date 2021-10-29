tuple1 = ("This", "is", "an", "unchangeable", "data", "collection")
print(tuple1)
print(len(tuple1))

# data types in tuples are
tuple10 = ("ferrari", "morris", "Bmw", "ford")
tuple2 = (1, 2, 3, 4)
tuple3 = (True, True, False)
print(tuple10, tuple2, tuple3)

# tuple can contains various data types like integer, string, boolean
# From Python's perspective, tuples are defined as objects with the data type 'tuple'

python_tuple = tuple(("high", "grade", "of", "quality"))
print(type(python_tuple))

# accessing tuple items
print(python_tuple[0:4])
print(python_tuple[-1])

# checking a value exists in tuple
if "grade" in python_tuple:
    print("Yes, it is in tuple")

# Update tuple values
# we can convert a tuple into list and insert a value,
# then after we can convert it into tuple
# hence we can add a value into tuple
# there are 2 types to add items to tuple
# 1st converting it to list
# 2nd adding one tuple to other tuple

# 1st conversion
x = ("time", "space", "reality", "soul", "mind", "power")
y = list(x)
y[-1] = "stones"
x = tuple(y)
print(x)

# 2nd adding a tuple to another
# when there is an single item in the tuple a comma have to be placed
# after the item, so that the python can identify that as an tuple.

z = ("_Its MCU_",)
print(x + z)

# removing items from tuple
# by 2 methods 1st by converting it into list and removing the required item from list
# and converting back to tuple

c = list(x)
print(c)
c.remove("stones")
x = tuple(c)
print(x)

# or delete whole tuple
h = ("game of thrones", "lost in space", "vikings")
del h
# the tuple was deleted
