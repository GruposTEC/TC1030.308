"""Modulos."""

from persona import Persona


class Alumno(Persona):
    """
    Clase Alumno.

    Representa la información de un alumno del TEC
    """

    matricula = 430000

    def __init__(self,  nombre, carrera):
        """Uso de super() para reutilizar el código en la superclase."""
        super().__init__(nombre)
        self.matricula = Alumno.matricula
        self.carrera = carrera
        Alumno.matricula = Alumno.matricula + 1

    def hablo(self):
        """Overrindig del método hablo, modifico el comportamiento."""
        return f'Soy un alumno y estudio {self.carrera}'

    def __str__(self):
        """Método mágico."""
        return super().__str__() + f'  y mi matricula es : {self.matricula}'


antonio = Alumno("Antonio", "IEC")
juan = Alumno("juan", "ISC")
print(antonio)
print(juan)
print(antonio.hablo())
