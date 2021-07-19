from functools import reduce
my_list = [el for el in range(100, 1001) if el % 2 == 0]
#print(my_list)
def my_funk(prev_el, el):
    return prev_el * el
mult = reduce(my_funk, my_list)
print(mult)
