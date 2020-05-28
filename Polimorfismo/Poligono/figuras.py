import dibujopol as pol

# pip install pillow


class Poligono:
    def __init__(self, num):
        self.num = num

    def dibujo(self):
        pass


class Triangulo(Poligono):
    def __init__(self):
        super().__init__(3)

    def dibujo(self):
        pol.dibuja3()


class Hexagono(Poligono):
    def __init__(self):
        super().__init__(6)

    def dibujo(self):
        pol.dibuja6()

# puedo Dibujar cualquier tipo de poligono
# porque cumplen con la interface de ener un método que se llama dibujo


def dibujoPoligono(poligono):
    poligono.dibujo()


tri = Triangulo()
hexa = Hexagono()

print("Triangulo instancia de Poligono : " + str(isinstance(tri, Poligono)))
print("Hexagono instancia de Poligono : " + str(isinstance(hexa, Poligono)))

dibujoPoligono(tri)
dibujoPoligono(hexa)


#uno = Linea()
# dibujoPoligono(uno)

#print("Linea instancia de Poligono : " + str(isinstance(uno, Poligono)))
