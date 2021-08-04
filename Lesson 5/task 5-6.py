my_dict = {}
with open("task5-6.txt", encoding="utf-8") as file:
    lines = file.readlines()
    for line in lines:
        name, lessons = line.split(": ")
        lessons_list = lessons.split()
        counter = [int(lesson.rstrip("(л)(пр)(лаб)")) for lesson in lessons_list if lesson != "-"]
        my_dict.update({name: sum(counter)})
    print(my_dict)
