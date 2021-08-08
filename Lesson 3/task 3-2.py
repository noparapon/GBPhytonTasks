# имя, фамилия, год рождения, город проживания, email, телефон


def show_info(name, surname, year, city, email, tel):
    print(f"ФИО: {surname} {name} из города {city}, год рождения: {year}, эл. почта: {email}, тел. {tel}")


show_info(name="Иван", surname="Иванов", year=1980, email="ivanov@mail.ru", tel="88005553535", city="Москва")
