# iterator is a object that contains a countable no of value, we can traverse
# through all the values. we can use __iter__() &
# we use __next__() to get the next value for iteration

my_tuple1 = ["eswar", "asish", "andey"]

cable = iter(my_tuple1)
print(next(cable))
print(next(cable))
print(next(cable))

# looping through a iterator

my_tuple = ["nsp", "hyd", "kkd", "nd", "madras", "kanchi"]
for i in my_tuple:
    print(i)


# iteration for a sequence of numbers using classes and iterations

class Nums:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


classes = Nums()
sequence = iter(classes)

print(next(sequence))
print(next(sequence))
print(next(sequence))

# to stop iteration for go on forever we use Stopiteration function

class Numbers:
    def __iter__(self):
        self.a = 0
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 2
            return x
        else:
            raise StopIteration

numbersss = Numbers()
iteration = iter(numbersss)

for i in iteration:
    print(i)
