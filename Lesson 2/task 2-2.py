my_list = []
while True:
    el = input("Добавьте элемент (Enter для окончания): ")
    if el == "":
        break
    my_list.append(el)
print(my_list)

for i in range(0, len(my_list)-1, 2):
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
print(my_list)
