revenue = int(input("Введите выручку: "))
costs = int(input("Введите издержки: "))
if revenue > costs:
    print("Прибыль!\n")
    profit = revenue - costs
    print(f"Рентабельность выручки: {profit / revenue:.2f}")
    num_staff = int(input("Введите количество персонала: "))
    print(f"Прибыль на одного работника: {profit / num_staff:.2f} усл. ед.")
elif revenue < costs:
    print("Работаем в убыток")
else:
    print("Работаем в ноль")
