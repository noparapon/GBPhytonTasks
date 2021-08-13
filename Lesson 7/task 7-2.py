from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def fabric(self):
        pass


class Coat(Clothes):
    def __init__(self, param):
        super().__init__(param)
        print(f"Новое пальто с размером: {param}")

    @property
    def fabric(self):
        return round(self.param / 6.5 + 0.5, 2)


class Suit(Clothes):
    def __init__(self, param):
        super().__init__(param)
        print(f"Новый костюм, рост: {param}")

    @property
    def fabric(self):
        return round(self.param * 2 + 0.3, 2)


my_coat = Coat(52)
my_suit = Suit(1.82)
print(f"На пальто нужно ткани: {my_coat.fabric}")
print(f"На костюм нужно ткани: {my_suit.fabric}")
print(f"Всего нужно ткани: {my_coat.fabric + my_suit.fabric}")
