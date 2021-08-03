my_list = [18, 16, 16, 15, 13, 13, 13, 8, 6, 6]
print(my_list)
n = int(input("Введите новый элемент: "))

for i in range(0, len(my_list)):
    if n > my_list[i]:
        my_list.insert(i, n)
        break
if n < my_list[-1]:
    my_list.append(n)
print("Результат:", my_list)
