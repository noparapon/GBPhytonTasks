with open("task5-5.txt","w") as file_w:
    file_w.write(input("Введите числа через пробел: "))

with open("task5-5.txt") as file_r:
    my_list = file_r.read().split()
    number_list = [int(num) for num in my_list if num.isdecimal()]
    print(f"Сумма: {sum(number_list)}")
