my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
num_list = [num for num in enumerate(my_list)]
new_list = [el for num, el in enumerate(my_list) if num > 0 and my_list[num - 1] < el]
print(num_list)
print(new_list)
