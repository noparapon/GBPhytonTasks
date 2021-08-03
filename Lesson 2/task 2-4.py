string = input("Введите строку: ")
str_list = string.split()
i = 1
for index, el in enumerate(str_list):
    print(f"{index + 1}. {el[0:10]}")