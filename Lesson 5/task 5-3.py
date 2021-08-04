with open("task5-3.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    summ = 0.0
    print("Оклады меньше 20 тыс. руб.:")
    for line in lines:
        surname, salary = line.split()
        summ += float(salary)
        if float(salary) < 20000:
            print(surname)
    print(f"Средний оклад: {summ/len(lines):.2f}")