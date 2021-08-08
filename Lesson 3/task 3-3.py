def my_func(*args):
    minimal = min(args)
    my_list = list(args)
    my_list[args.index(minimal)] = 0
    res = 0
    for el in my_list:
        res += el
    return res


print(my_func(2, 6, 4))
print(my_func(12, 3, 15))
print(my_func(21, 12, 10))
