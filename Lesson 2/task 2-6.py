my_tuples = []
i = 1
while True:
    name = input("Введите название товара: ")
    price = int(input("Введите цену: "))
    number = int(input("Введите количество: "))
    unit = input("Введите единицу измерения: ")
    my_tuples.append((i, {"название": name, "цена": price, "количество": number, "eд": unit}))
    answer = input("[добавлено]\n\nДобавить еще? [+/-]")
    if answer == '-':
        break
    i += 1
print("Структура (товары):\n",my_tuples)
my_dict = {}
names, prices, nums, units = [], [], [], []
units = set()
for one_tuple in my_tuples:
    names.append(one_tuple[1]["название"])
    prices.append(one_tuple[1]["цена"])
    nums.append(one_tuple[1]["количество"])
    units.add(one_tuple[1]["eд"])
my_dict.update({"название": names, "цена": prices, "количество": nums, "eд": list(units)})
print(my_dict)
