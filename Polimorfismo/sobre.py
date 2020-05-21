from envio import Envio


class Sobre(Envio):
    def calcula_costo(self):
        print("calcula_costo desde sobre")

    def __str__(self):
        return "Sobre"
