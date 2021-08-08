def devision(a, b):
    try:
        res = a / b
    except ZeroDivisionError:
        print("Деление на ноль detected!")
        return
    return res


try:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
except ValueError:
    print("Некорректный ввод!")
c = devision(a, b)
print(c)
