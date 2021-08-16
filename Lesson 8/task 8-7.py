class cmplx:

    def __init__(self, x, y):
        try:
            self.x = int(x)
            self.y = int(y)
        except ValueError as v:
            print("ввели некорректные данные!")

    def __str__(self):
        return f"{self.x} + {self.y}i"

    def __add__(self, other):
        return cmplx(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return cmplx(self.x * other.x - self.y * other.y, self.x * other.y + self.y * other.x)


cx= input('Введите действительную часть комплексного числа:"):')
cy= input('Введите мнимую часть комплексного числа:"):')
c = cmplx(cx, cy)
print(c)

dx= input('Введите действительную часть комплексного числа:"):')
dy= input('Введите мнимую часть комплексного числа:"):')
d = cmplx(dx, dy)
print(d)

print("c + d = ", c + d)
print("c * d = ", c * d)

