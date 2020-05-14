class Persona():
    """Clase que especifica las caracteristicas de una Persona
         Es la base para realizar herencia
    """

    def __init__(self, nombre):
        self._nombre = nombre

    def hablo(self):
        return "Soy una persona y puedo hablar"

    # def __str__(self):
    #    return f'Mi nombre es : {self._nombre}'

    # def __repr__(self):
    #    return f'Mi nombre es : {self._nombre}'


def main():
    javier = Persona("Javier")
    pedro = Persona("Pedro")
    print(javier)
    print(pedro)
    print(javier.hablo())
    # help(Persona)


if __name__ == '__main__':
    main()
