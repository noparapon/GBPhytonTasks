class Road:
    _length = None
    _width = None

    def __init__(self, length, width):
        self._width = width
        self._length = length

    def asphalt_calculate(self, mass, height):
        return self._width * self._length * mass * height


my_road = Road(5000, 20)
print(f"Масса асфальта для дороги 800 м х 20 м х 5 см - {my_road.asphalt_calculate(25, 5) / 1000} тонн")
