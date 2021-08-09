class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return " ".join([self.name, self.surname])

    def get_full_income(self):
        return self._income["wage"] + self._income["bonus"]


vasja = Position("Вася", "Пупкин", "директор", 50000, 25000)
print(f"Полная зарплата сотрудника {vasja.get_full_name()} составляет {vasja.get_full_income()}")
