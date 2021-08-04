my_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
file_read = open("task5-4read.txt", "r", encoding="utf-8")
file_write = open("task5-4write.txt", "w", encoding="utf-8")
while True:
    line = file_read.readline()
    if not line:
        break
    a, _, b = line.split()
    print(f"{my_dict[a]} - {b}", file=file_write)

file_read.close()
file_write.close()