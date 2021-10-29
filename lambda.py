# lambda
# it is a small anonymous function.
# takes no. of arguments, gives single expression.

# adding 5 to an argument (g)
e = lambda g: g + 5
print(e(5))

# we can give 2 arguments but it returns a single value.


e = lambda g, h: g*h
print(e(4, 5))

# with 3 arguments
e = lambda h, i, j: (h + i) * j
print(e(2, 2, 2))

# we can use lambda within function
# in this we double a number we send in


def number(n):
    return lambda a: a * n


value = number(2)
print(value(10))

# triple the number we send in


def number(x):
    return lambda c: c * x


thrice = number(5)
print(thrice(3))

#  we can use both the lambda functions in one statements


def number(x):
    return lambda c: c * x


twice = number(2)
thrice = number(3)
fourth = number(4)

print(twice(2))
print(thrice(2))
print(fourth(2))

def even_number(v):
    if v % 2  == 0: print("it is even")
    else: print("not even")


even_number(int(input("give me number:")))


def greet(x):
    print("hi ra ")
    for f in x:
        print(f)




c = input("give me a name:")
print(greet(c))

if c == "vijay":
    print("hi ra eswar")
else:
    print("hi ra edava")



