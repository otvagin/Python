def dev_funk():
    """
    Функция принимает два числа и выполняет их деление.
    """
    try:
        dev1 = int(input("Введите делимое: "))
        dev2 = int(input("Введите делитель: "))
        rez = dev1 / dev2
    except ZeroDivisionError:
        print("Деление на ноль не выполняется!")
        return
    return rez


print("Результат деления: ", dev_funk())
