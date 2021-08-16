class MyException(Exception):
    def __str__(self):
        return "Вы ввели не число!"


def add(lst, input_str):
    if input_str.isdigit():
        lst.append(int(input_str))
    else:
        raise MyException


my_lst = []
while True:
    try:
        in_str = input("Введите число (для окончания '-')")
        if "-" == in_str:
            break
        add(my_lst, in_str)
    except MyException as e:
        print("Ошибка:", e)
print(my_lst)
