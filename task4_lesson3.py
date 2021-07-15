def my_funk(x, y):
    """
    Функция принимает действительное положительное число x
    и возводит его в степень y, которое является целм отрицательным числом. 
    """
    x = float(x)
    if y < 0:
        y = int(y)
    else:
        y = int(-y)
    print(x)
    print(y)
    rez1 = x ** y
    counter = -1
    xx = x * x
    while counter != y + 1:
        xx = xx * x
        counter -= 1
    return round(rez1, 2), round(1 / xx, 2)


print(my_funk(5.4, 2))
