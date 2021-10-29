# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

def my_function():
    print("hello world")


my_function() #this is how we call a function

# Arguments- the information can be passed into functions as arguments.
# specified after the function name inside the parantheses.
def the_function(first_name, lname=" andey"):
    print(first_name+lname)


the_function("Eswar")
the_function("rishi")
the_function("usha")
the_function("basava")
the_function("andey")


# in this the function expects 2 arguments if gave maore than 2 or
# less than 2 we get error
def function(firstname,lastname):
    print(firstname+ lastname)
function("eswar asish"," andey")

# arbitrary arguments *args shortned for arguments
def myfunction(*name):
    print("my name is " + name[1])


myfunction("eswar", "asish", "andey")

# Keywords arguments
# we can send arguments with keys ="values" syntax.
# this way the arguments doesnot matter
def num_function(child1, child2, child3):
    print("the youngest child is " + child1)


num_function(child1 ="darwin", child2 = "robert", child3="stantley")

# arbitrary keyword arguments, **kwargs
# If you do not know how many keyword arguments
# that will be passed into your function,
# Add two asterisk: ** before the parameter name in the function definition.

def jam_function(**kid):
    print("his last name is "+ kid["lname"])


jam_function(fname = "danny", lname = "african")

# default parameter value
# If we call the function without argument, it uses the default value
def add(num, num2 = 5):
    return num + num2


print(add(20))

# Passing a list as an argument
# we can pass any data types into the functions,
# [list],(tuple),{sets},{dict:""}

def data_type(name):
    for x in name:
        print(x)


names= ["thor", "tony", "falcon", "widow"]
data_type(names)

# Return values
# to let the function return a value

def rturn_function(x):
    print(5*x)# 5*x


rturn_function(5)
rturn_function(7)

# the pass statement
# the functions cant be empty but if need to keep an empty value,
# then we can keep pass statement to avoid error

def empty():
    pass


print(empty()) # simply returns none.

# recursion
# a function can call itself, that means we can loop through data
# to reach result.


def fibbonaci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibbonaci(n - 1)+ fibbonaci(n - 2)


for x in range(0, 15):
    print(x, "-", fibbonaci(x))

# simplyfied syntax

def recurrsive_fibonacci(n):
    if n <= 1:
        return n
    else:
        return (recurrsive_fibonacci(n-1)+ recurrsive_fibonacci(n-2))


num_range = int(input("give the range of fibonaci numbers:"))
if num_range <= 0:
    print("invalid number range")
else:
    print("fibonacci series:")
    for c in range(num_range):
        print(fibbonaci(c))
