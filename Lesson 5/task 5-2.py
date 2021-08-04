with open("file_task5-2", "r") as file:
    lines = file.readlines()
    print("Количество строк: ", len(lines))
    ind = 1
    for line in lines:
        print(f"слов в {ind}-й строке: ", len(line.split()))
        ind += 1
