class Humano:
    def __init__(self, edad):
        self.edad = edad

    def hablar(self, mensaje):
        print(self.edad)
        print(mensaje)

class IngSistemas(Humano):
    def programar(self, lenguaje):
        print("voy aprograr en ", lenguaje)

class LicDerecho(Humano):
    def estudiarCasa(self, de):
        print("debo estudias el caso de", de)



