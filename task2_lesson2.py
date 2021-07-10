my_list = []
print('Введите элементы списка через Enter. Для окончания ввода - "q"')
range_number = 1
while True:
    el = input(f"Элемент №{range_number}: ")
    my_list.append(el)
    range_number += 1
    if el == "q":
        break
my_list.remove("q")
print("Исходный список: ", my_list)
argument = 0
while argument != range_number - 1:
    my_list.insert(argument + 1, my_list.pop(argument))
    argument += 2
print("Список после обмена значений соседних элементов: ", my_list)
