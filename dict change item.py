# Change dictionary item
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2000
print(thisdict)

# Update dictionary

thisdict.update({"award": "piston cup"})
print(thisdict)

# Removing items from dictionary
# we can use pop(), popitem(), del(), clear();
thisdict.pop("year")
print(thisdict)
thisdict.popitem() #removes last updated item
print(thisdict)
del thisdict["model"]
print(thisdict)