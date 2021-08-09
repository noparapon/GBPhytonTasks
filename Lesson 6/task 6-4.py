class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f"{self.name} на связи")

    def go(self):
        print(f"Машина {self.name} поехала")

    def stop(self):
        print(f"Машина {self.name} остановилась")

    def turn(self, direction):
        print(f"Машина {self.name} поворачивает {direction}")

    def show_speed(self):
        print(f"Текущая скорость {self.name}: ", self.speed)


class TownCar(Car):
    def show_speed(self):
        print(f"Текущая скорость {self.name}: ", self.speed) if self.speed <= 60 else \
            print(f"!!!Превышение скорости ({self.name})")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f"Текущая скорость {self.name}: ", self.speed) if self.speed <= 40 else \
            print(f"!!!Превышение скорости ({self.name})")


class PoliceCar(Car):
    pass

car1 = PoliceCar(60, "black", "skoda", True)
car2 = WorkCar(50, "white", "lada", False)
car3 = SportCar(120, "red", "Lamborgini", False)
car1.go()
car2.go()
car3.go()
car1.turn("налево")
car2.turn("направо")
car3.stop()
car1.show_speed()
car2.show_speed()
