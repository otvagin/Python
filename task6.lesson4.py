from itertools import count, cycle
print('part1:')
for el in count(3):
    if el > 10:
        break
    else:
        print(el)
print('part2:')
my_list = ['abc', 'dfg', 'hij']
c = 0
for el in cycle(my_list):
    print(el)
    c += 1

    if c > 30:
        break
    