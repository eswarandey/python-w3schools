def adding(x):
    cal = lambda a: a + x
    print(cal(int(input("2nd number :"))))


def sub(x):
    subtract = lambda a: x - a
    print(subtract(int(input("2nd number :"))))


def multiple(x):
    multi = lambda a: a * x
    print(multi(int(input("2nd number :"))))

first_number = int(input("give a number :"))
operation = input("""+, -, *, / :""")
if operation == "+":
    adding(first_number)
elif operation == "-":
    sub(first_number)
elif operation == "*":
    multiple(first_number)
else:
    print("not defined")
