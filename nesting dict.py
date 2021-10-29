# A dictionary can contain dictionaries, this is called nested dictionaries
myfamily = {
"child1" : {
  "name":"Radha",
  "age":22
},
"child2":{
  "name":"santhosh",
  "age":20
},
  "child3":{
    "name":"mounica",
    "age":22
  },
  "child4":{
    "name":"mohit",
  "age":21
  }
  }


for x,y in myfamily.items():
  print(x,y)


# create 3 dicts and save them in one dictionaries;

child1={
  "name":"jack",
  "year":"2000"
}
child2={
  "name":"dani",
  "year":"2001"
}
child3={
  "name":"nick",
  "year":"2002"
}
child4={
  "name":"mike",
  "year":"2003"
}
family={
  "child1": child1,
  "child2": child2,
  "child3": child3,
  "child4": child4
}
for v in family:
  print(v)



