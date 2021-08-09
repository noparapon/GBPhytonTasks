class Stationery:

    def __init__(self, name):
        self.name = name

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):

    def draw(self):
        print("Запуск отрисовки ручкой.")


class Pencil(Stationery):

    def draw(self):
        print("Запуск отрисовки карандашом.")


class Handle(Stationery):

    def draw(self):
        print("Запуск отрисовки маркером.")


my_stationary = Stationery("Канцелярия")
my_stationary.draw()

my_pen = Pen("Ручка")
my_pen.draw()

my_pencil = Pencil("Карандаш")
my_pencil.draw()

my_handle = Handle("Ручка")
my_handle.draw()
