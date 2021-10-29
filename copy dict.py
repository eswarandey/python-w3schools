# we can't copy a dictionary into another variable,
# it will become a reference for the original dictionary
# the changes made in the original dictionary is automatically made in this variable

it_is_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict = it_is_dict.copy()
print(thisdict)

# to copy a dictionary using builtin _ dict() fuction:

mydist = dict(it_is_dict)
print(mydist)
