string = input("Введите строку: ")
str_list = string.split()
i = 1
for index, el in enumerate(str_list, 1):
    print(f"{index}. {el[0:10]}")