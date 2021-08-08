def int_func(s):
    if s:
        return s[:1].upper() + s[1:]


string = input("Введите слова через пробел: ")
word_list = []
for word in string.split():
    word_list.append(int_func(word))
print(" ".join(word_list))
