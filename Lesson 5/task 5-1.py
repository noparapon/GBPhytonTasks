file = open("my_file.txt", "w")
lines = []
print("Введите строки (пустая строка для окончания):")
while True:
    line = input()
    if line == "":
        break
    file.write(line + "\n")
file.close()
