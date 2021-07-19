def fact(arg):
    c = 1
    for el in range(1, arg + 1):
        c *= el
        yield c
for el in fact(5):
    print(el)
