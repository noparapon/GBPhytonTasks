def get_sum(s):
    res = sum([int(num) for num in s.split() if num.isdigit()])
    return res


whole_sum = 0
while True:
    string = input("Введите числа через пробел (для окончания '-'): ")
    str_sum = get_sum(string[: None if '-' not in string else string.find("-")])
    whole_sum += str_sum
    print(whole_sum)
    if '-' in string:
        break

