from envio import Envio
from sobre import Sobre
from paquete import Paquete


class Paqueteria:

    # Puede recibir cualquier objeto donde su superClase es Envio
    def mandarPorPaqueteria(self, unenvio):
        unenvio.calcula_costo()


class Fondita:
    def calcula_costo(self):
        print("La comida cuesta $")


env1 = Envio()
paq1 = Paquete()
sob1 = Sobre()

dhl = Paqueteria()


dhl.mandarPorPaqueteria(env1)
dhl.mandarPorPaqueteria(paq1)
dhl.mandarPorPaqueteria(sob1)

casadetono = Fondita()

dhl.mandarPorPaqueteria(casadetono)

print(isinstance(env1, Envio))
print(isinstance(paq1, Envio))
print(isinstance(sob1, Envio))
print(isinstance(casadetono, Envio))
