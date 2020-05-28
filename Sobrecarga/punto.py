import math


class Punto:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def _distancia(self):
        return math.sqrt(self._x ** 2 + self._y ** 2)

    def __str__(self):
        return f'( {self._x} , {self._y} )'

    def __add__(self, other):
        return Punto(self._x + other._x, self._y + other._y)

    def __gt__(self, other):
        return self._distancia() > other._distancia()


p1 = Punto(4, 5)
p2 = Punto(3, 3)
print(p1)
print(p2)
print(p1 + p2)
print(p1 > p2)
