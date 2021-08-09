def my_gen(mother_list):
    prev = mother_list[0]
    for el in mother_list:
        if el > prev:
            yield el
        prev = el


my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
modified_list = list(my_gen(my_list))
print(modified_list)
