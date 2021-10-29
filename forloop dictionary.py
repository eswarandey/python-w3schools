# A for loop is used for iterating over a sequence
# (that is either a list, a tuple, a dictionary, a set, or a string).
# With the for loop we can execute a set of statements,
# once for each item in a list, tuple, set etc

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# it does not require an indexing variable before the seqeunce like while loop
# looping through a string
for v in "lapping":
    print(v)

# break statement used to stop the iteration at a specific item
names = ["garry", "larry", "suri", "barry", "jerry"]
for z in names:
    print(z)
    if z == "suri":
        break
# Exit the loop when x is "banana", but this time the break comes before the print:
names = ["garry", "larry", "suri", "barry", "jerry"]
for z in names:
    if z == "suri":
        break
    print(z)
# continue command used to skip the current iteration and continue with other
names = ["ganesh", "vinay", "suri", "balaji", "jagadheesh"]
for b in names:
    if b=="balaji":
        continue
    print(b)

# range function used to iterate over a specified number of times
for h in range(0,100,20):
    print(h)

#else in for loop
for g in range(0,8):
    print(g)
else:
    print("completed")

# breaking for looping by a specific value does not exceute else statement
for y in range(0,5):
    if y == 3:
        break
    print(y)
else:
    print(";)")

# nested loops
list1= ["high", "hill", "low"]
list2= ["tower", "top", "river"]
for s in list1:
    for t in list2:
        print(s,t)

# pass statement
for b in range(0,10,2):
    pass
#noting returns
