a = float(input("Введите результат первого дня (а): "))
b = float(input("Введите желаемый результат(b): "))
res = 1
while a < b:
    a *= 1.1
    res += 1
print(f"На {res}-й день результат превзойдет {b} километров")

