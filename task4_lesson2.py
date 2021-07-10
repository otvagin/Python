my_string = input("Введите любое количество слов через пробел: ")
for ind, el in enumerate(my_string.split(), 1):
    print(ind, el[:10])
