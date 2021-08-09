from itertools import count, cycle

# а) итератор, генерирующий целые числа, начиная с указанного
for i in count(10, 3):
    if i > 100:
        break
    print(i)

# б) итератор, повторяющий элементы некоторого списка, определенного заранее
year = 2019
for i, j in enumerate(cycle(["winter", "spring", "summer", "autumn"])):
    print(f"{j} of {year + i // 4}")
    if i == 10:
        break
