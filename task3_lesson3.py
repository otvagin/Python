def my_funk(arg1, arg2, arg3):
    """
    Функция принимает три аргумента 
    и возвращает сумму наибольших двух аргументов.
    """
    my_list = [arg1, arg2, arg3]
    my_list.sort()
    my_sum = my_list[1] + my_list[2]
    return my_sum


print(my_funk(2, 0, 11))

