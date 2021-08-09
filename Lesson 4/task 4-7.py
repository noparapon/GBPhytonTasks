def fact(n):
    factorial = k = 1
    while k <= n:
        factorial *= k
        k += 1
        yield factorial


for el in fact(15):
    print(el)
