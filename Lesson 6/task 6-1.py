from itertools import cycle
from time import sleep


class TrafficLight:

    tlight_dict = {"красный": 7, "желтый": 2, "зеленый": 4}

    def __init__(self, color):
        self.__color = color

    def running(self):
        color_cycle = cycle(self.tlight_dict.keys())
        for color in color_cycle:
            if self.__color == color:
                print(f"{color} ждем {self.tlight_dict[color]} секунд...")
                sleep(self.tlight_dict[color])
                self.__color = next(color_cycle)


my_tlight = TrafficLight("красный")
my_tlight.running()