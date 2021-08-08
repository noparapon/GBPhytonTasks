def my_func1(a, b):
    """
    Возводит a в степень b через **

    :param a: основание степени
    :param b: показатель степени
    :return: а в степени b
    """
    return a ** b


def my_func2(a, b):
    """
    Возводит a в степень b через цикл

    :param a: основание степени
    :param b: показатель степени
    :return: а в степени b
    """
    res = 1
    for _ in range(abs(b)):
        res *= a
    if b < 0:
        res = 1 / res
    return res


x = float(input("Введите положительное x: "))
y = int(input("Введите отрицательное целое y: "))
print("x^y через **: ", my_func1(x, y))
print("x^y через цикл: ", my_func2(x, y))
