class Cell:
    def __init__(self, num):
        if num <= 0:
            print("Неверные данные, количество клеток приведено к 1!")
            num = 1
        self.num = num

    def __add__(self, other):
        return Cell(self.num + other.num)

    def __sub__(self, other):
        if self.num > other.num:
            return Cell(self.num - other.num)
        else:
            print("Невозможно произвести вычитание!")
            return None

    def __mul__(self, other):
        return Cell(self.num * other.num)

    def __truediv__(self, other):
        return Cell(self.num // other.num)

    def make_order(self, n):
        res = ((("*" * n) + "\n") * (self.num // n)) + ("*" * (self.num % n))
        return res


my_cell1 = Cell(16)
my_cell2 = Cell(12)
print(my_cell1.make_order(3))
print(my_cell2.make_order(5))
new_cell = my_cell2 * (my_cell1 - my_cell2)
print(new_cell.make_order(10))
