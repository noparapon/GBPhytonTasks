my_tuples = []
i = 1
keys = ["название", "цена", "количество", "eд"]
while True:
    name = input("Введите название товара: ")
    price = int(input("Введите цену: "))
    number = int(input("Введите количество: "))
    unit = input("Введите единицу измерения: ")
    my_tuples.append((i, {keys[0]: name, keys[1]: price, keys[2]: number, keys[3]: unit}))
    answer = input("[Ok]\n\nДобавить еще? [+/-]")
    if answer == '-':
        break
    i += 1
print("Структура (товары):\n",my_tuples)
my_dict = {}
names, prices, nums = [], [], []
units = set()
for _, one_dict in my_tuples:
    names.append(one_dict[keys[0]])
    prices.append(one_dict[keys[1]])
    nums.append(one_dict[keys[2]])
    units.add(one_dict[keys[3]])
my_dict.update({keys[0]: names, keys[1]: prices, keys[2]: nums, keys[3]: list(units)})
print(my_dict)
