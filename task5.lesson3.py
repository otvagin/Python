summa = 0
while True:
    try:
        my_string = input("Введите строку чисел, разделенных пробелом: ")
        my_list = list(my_string.split())
        my_num_list = []
        for el in my_list:
            summa += int(el)
    except ValueError:
        break       
    print("Сумма представленных чисел: ", summa)
print("Готово! Итоговая сумма чисел: ", summa)    