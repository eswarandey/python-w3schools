# class is an blueprint for creating an objects in python
# this simplest form of class but we need the init() function
# to assign values into the class or object
class Tyrant:
    x = 9


print(Tyrant)

p1 = Tyrant()
print(p1.x)

# new class example with init function


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


h1 = Human("eswar", 22)
print(h1.name)
print(h1.age)

# another example of class


class Human2:
    def __init__(self, phno, instaid):
        self.phno = phno
        self.instaid = instaid

    def function(self):
        print("hi ra edava " + self.phno)


h1 = Human2("eswar", 8888)
h1.function()
print(h1.instaid)

