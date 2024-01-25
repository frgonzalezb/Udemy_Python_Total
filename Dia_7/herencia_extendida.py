'''
Ver video y pdf de la clase para más información.
'''

class Animal:
    '''
    Engloba a todos los animales, desde esponjas hasta humanos.
    '''
    def __init__(self, edad: int, color: str):
        self.edad = edad
        self.color = color

    def nacer(self):
        print('El animal ha nacido.')

    def hablar(self):
        print('El animal emite un sonido.')


class Pajaro(Animal):

    def __init__(self, edad, color, altura_vuelo):
        # Atributos edad y color pasan a ser sobrescritos
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo
    
    # Método heredado, pero sobrescrito
    def hablar(self):
        print('¡Pío!')

    # Método nuevo en subclase (no disponible en superclase)
    def volar(self, metros: int):
        print(f'El pájaro vuela {metros} metros.')


# Verificar herencia
print(Pajaro.__bases__)         # Acceder a las superclases de Pajaro
print(Animal.__subclasses__())  # Acceder a las subclases de Animal


# Ejemplo de uso
mi_animal = Animal(5, 'negro')
piolin = Pajaro(2, 'amarillo', 60)
piolin.nacer()
piolin.hablar()     # ¡Pío!
piolin.volar(50)    # El pájaro vuela 50 metros.


########################### HERENCIA MÚLTIPLE ###########################

print(('#' * 72) + '\n')

class Padre:
    def hablar(self):
        print('Hola')


class Madre:
    def reir(self):
        print('Jajaja')

    def hablar(self):
        print('Qué tal')


class Hijo(Padre, Madre):
    pass


class Nieto(Hijo):
    pass


# Ejemplo
mi_nieto = Nieto()
mi_nieto.hablar()       # Hola (ver explicación abajo)
mi_nieto.reir()

print(Nieto.__mro__)    # Orden herencia: Nieto > Hijo > Padre > Madre


'''
mi_nieto.hablar() dice 'Hola' porque la clase Padre está primero que 
la clase Madre entre los paréntesis. Vale decir, en aparente igualdad 
de condiciones, Python resuelve la jerarquía de manera posicional.

Si se invierte el orden de las clases entre los paréntesis, entonces 
mi_nieto.hablar() dirá 'Qué tal'.

El método __mro__ (Method Resolution Order) permite obtener el orden 
en el que Python buscará un método en la jerarquía de clases.
'''
