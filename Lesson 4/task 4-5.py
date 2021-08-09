from functools import reduce

my_list = [a for a in range(100, 1001) if a % 2 == 0]
print(reduce(lambda x, y: x * y, my_list))
