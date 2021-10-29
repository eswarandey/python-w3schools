class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def print_name(self):
        print(self.firstname, self.lastname)


class Child(Person):
    def __init__(self, firstname, lastname):
        super().__init__( firstname, lastname)
        self.birthdate = 1999

    def welcome(self):
        print("welcome ", self.firstname,self.lastname, "to the family")


# or we can use super() to inherit properties
# from the parent class
# def __init__(self,fname,lname):
# super().__init__(fname,lname)

x = Child("John", "wick")
x.welcome()
