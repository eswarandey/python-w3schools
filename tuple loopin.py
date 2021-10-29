# we use for loop for iterate items in tuple

this_tuple = ("apple", "banana", "cherry", "mango")
for x in this_tuple:
    print(x)

# looping through index numbers of items in tuple by using range and len functions
for i in range(len(this_tuple)):
    print(this_tuple[i])

# While loop is also used to iterate items in tuple

game = ("assassins creed", "black flag", "brotherhood", "liberation")
y = 0
while y < len(game):
    print(game[y])
    y += 1
