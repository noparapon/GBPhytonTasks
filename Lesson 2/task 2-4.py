string = input("Введите строку: ")
str_list = string.split()
i = 1
for el in str_list:
    print(f"{i}. {el[0:10]}")
    i += 1