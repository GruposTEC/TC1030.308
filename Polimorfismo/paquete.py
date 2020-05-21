from envio import Envio


class Paquete(Envio):
    def calcula_costo(self):
        print("calculacosto desde paquete")

    def __str__(self):
        return "Paquete"
