"""
Este ejercicio requiere que se importe la libreria matplotlib y numpy
Esto se realiza desde la terminal conel comando
pip install matplotlib
"""

from calculadora import CalculadoraMaizoro
from calgrafica import CalculadoraGrafica
import numpy as np


def main():
    print("Usemos una calculadora basica")
    maizoro = CalculadoraMaizoro()
    print(maizoro.suma(5, 7))
    print(maizoro.resta(5, 7))
    print(maizoro.multiplicacion(5, 7))
    print(maizoro.division(5, 7))
    print("Ahora usemos una calculadora grafica")
    casio = CalculadoraGrafica()
    print(casio.suma(5, 7))
    print(casio.resta(5, 7))
    print(casio.multiplicacion(5, 7))
    print(casio.division(5, 7))
    valores = np.linspace(0, 20, 50)
    print(valores)
    casio.grafica(valores)


if __name__ == "__main__":
    main()
