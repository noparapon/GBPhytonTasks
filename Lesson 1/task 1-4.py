n = int(input("Введите целое положительное n: "))
max_digit = 0
while n > 0:
    digit = n % 10
    if digit > max_digit:
        max_digit = digit
    if max_digit == 9:
        break
    n = n // 10
print("Самая большая цифра числа: ", max_digit)
