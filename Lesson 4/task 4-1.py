from sys import argv

script_name, *list_params = argv

int_list = [int(num) for num in list_params if num.isdigit()]
print(int(int_list[0]) * int(int_list[1]) + int(int_list[2])) \
    if len(int_list) == len(list_params) == 3 else print("ввели что-то не то...")

