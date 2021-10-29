number= float(input("1st number: "))
num= float(input("2nd number: "))
ask=input("what_arithmetic_operation?(/,*,+,-): ")
if ask == "*":
    operation= number*num
    print(operation)
elif ask == "/":
    operation= number/num
    print(operation)
elif ask == "-":
    operation= number-num
    print(operation)
elif ask =="+":
    operation=number+num
    print(operation)
else:
    print("not")


def week(i):
    switcher = {
        "+":
            number+num,
        "-": number-num,
    }
    return switcher.get(i, "Invalid operator")
#day= week(ask)
print(week(ask))
