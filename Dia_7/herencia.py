class Animal:
    '''
    Engloba a todos los animales, desde esponjas hasta humanos.
    '''
    def __init__(self, edad: int, color: str):
        self.edad = edad
        self.color = color

    def nacer(self):
        print('El animal ha nacido.')


class Pajaro(Animal):
    pass


# Verificar herencia
print(Pajaro.__bases__)         # Acceder a las superclases de Pajaro
print(Animal.__subclasses__())  # Acceder a las subclases de Animal


# Ejemplo de uso
piolin = Pajaro(2, 'amarillo')
piolin.nacer()
