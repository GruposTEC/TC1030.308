from abc import ABC, abstractmethod
import dibujopol as pol


class Poligono(ABC):
    def __init__(self, num):
        self.num = num

    @abstractmethod
    def dibujo(self):
        pass


class Triangulo(Poligono):
    def __init__(self):
        super().__init__(3)

        # implementando el método abstracto
    def dibujo(self):
        pol.dibuja3()

class Hexagono(Poligono):

    def __init__(self):
        super().__init__(6)

    # sobreescritura abstract method
    def dibujo(self):
        pol.dibuja6()


def dibujarPoligonos(poligono):
    poligono.dibujo()


tri = Triangulo()
hexa = Hexagono()

dibujarPoligonos(tri)
dibujarPoligonos(hexa)
