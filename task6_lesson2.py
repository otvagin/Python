product1 = input("Название продукта 1: ")
price1 = input("Цена 1: ")
quantity1 = input("Количество 1: ")
unit1 = input("Единица учета 1: ")
product2 = input("Название продукта 2: ")
price2 = input("Цена 2: ")
quantity2 = input("Количество 2: ")
unit2 = input("Единица учета 2: ")
product3 = input("Название продукта 3: ")
price3 = input("Цена 3: ")
quantity3 = input("Количество 3: ")
unit3 = input("Единица учета 3: ")
goods_dic1 = {"название": product1, "цена": price1, "количество": quantity1, "ед": unit1}
goods_dic2 = {"название": product2, "цена": price2, "количество": quantity2, "ед": unit2}
goods_dic3 = {"название": product3, "цена": price3, "количество": quantity3, "ед": unit3}
product_list = [product1, product2, product3]
price_list = [price1, price2, price3]
quantity_list = [quantity1, quantity2, quantity3]
unit_list = [unit1, unit2, unit3]
common_dic = {"название": product_list, "цена": price_list, "количество": quantity_list, "ед": unit_list}
print(common_dic)
print(type(common_dic))
