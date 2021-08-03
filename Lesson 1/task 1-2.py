seconds = int(input("Введите кол-во секунд:"))
hour = seconds // 3600
minutes = (seconds % 3600) // 60
sec = seconds % 60
print(f'{hour:02}:{minutes:02}:{sec:02}')
