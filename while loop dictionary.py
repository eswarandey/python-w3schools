# we can execute a set of statements as long as condition is true
i = 0
while i < 5:
    print(i*"hi")
    i += 1
    # remember to increment i, or else the loop will continue forever.

# continue statement which used to stop the current iteration and continue with rest
i = 1
while i<10:
    i += 1
    if i ==5:
        continue
    print(i)

# Else statement
#we can run the code when the conditon is no longer true
i = 1
while i<5:
    print(i)
    i += 1
else:
    print('not longer than 5')

