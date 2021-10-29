# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

x = 55
y = 155
if x > y:
    print("not possible")
else:
    print("true")
# ELIF
# elif is a command short for elseif it is used to tell python;
# if the previous conditions were not true, then try this condition

c = 50
d = 50
if c > d:
    print("no")
elif c == d:
    print("both are same")
# ELSE
# The else keyword catches anything,
# which isn't caught by the preceding conditions.

e = 100
f = 101
if e > f:
    print("true")
elif e < f:
    print("yes")
else:
    print("false")

# short hand IF statement
g = 55
h = 60
if g > h: print("g is greater than h")
else: print("not possible")

# if and else short hand
print("yes") if g < h else print("no")

# short hand syntax for multiple conditons in one line
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# And key word is used to combine conditional statements
u = 10
i = 8
o = 20
if u > i and o > u:
    print("both conditons are true")

# OR is a key word used to combine conditional statements
k = 25
l = 30
m = 50
if k > l or l < m:
    print("2nd conditon is correct")
else:
    print("l<m")

# Nested If statements
# we can write if statements within if statements
r = 100
if r > 10:
    print("greater that 10")
    if r > 50:
        print("and also greater than 50")
    else:
        print("not")

# the pass statement - to avoid a if statement or to return nothing
p= 200
q = 250
if p<q:
    pass # retuns nothing in run
