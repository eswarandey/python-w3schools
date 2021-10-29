# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*,
# changeable and does not allow duplicates.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(len(thisdict))

# Dictionaries cannot have two items with the same key
thatdict= {
  "name": "eswar",
  "age" : 22,
  "gender":"Male",
  "age": 25
}
print(thatdict)
# data types
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)

# Accessing dictionaries by printing the key item in the dictionaries

print(thisdict["colors"])
# or using get() command
x = thisdict.get("electric")
print(x)

# Get Keys
# The keys() method will return a list of all the keys in the dictionary
print(thisdict.keys())

# update an item in dictionary and keys list gets updated as well

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)
thisdict["country"]="India"
print(thisdict)

# Get values
# the value() method will return all the values in the dictionary
# The list of the values is a view of the dictionary, meaning that
# any changes done to the dictionary will be reflected in the values list.

x = thatdict.values()
print(x)

# Get items
# the items in the dictionary
# i.e keys and values are returned in the form of tuples in a list([],[])

# Check if Key Exists
# To determine if a specified key is present in a dictionary use the in keyword

thedict={
  "name":"harry",
  "type":"book",
  "year":"1990"
}
if "name" in thedict:
  print("Yes, it is present")
