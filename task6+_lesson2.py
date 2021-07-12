my_list_goods = []
range_number = 1
while True:
    product = input("Товар: ")
    price = input("Цена: ")
    quantity = input("Количество: ")
    unit = input("Единица учета товара: ")
    rec = {"название": product, "цена": price, "количество": quantity, "ед": unit}
    el = (range_number, rec)
    my_list_goods.append(el)
    range_number += 1
    request = input("Новый товар (да/нет)")
    if request == "нет":
        break
print(my_list_goods)
#Как из данной структуры можно получить статистику?
