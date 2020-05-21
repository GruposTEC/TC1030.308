from envio import Envio


class Paquete(Envio):
    def calculaCosto(self):
        print("calculacosto desde paquete")

    def __str__(self):
        return "Paquete"
