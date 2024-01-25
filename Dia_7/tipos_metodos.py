'''
Tipos de métodos:

- Métodos de INSTANCIA (MI):
    - Se declaran sin decoradores.
    - Pueden acceder a los atributos de la instancia.
    - Pueden acceder a otros métodos.
    - Pueden modificar el estado de la clase.

- Métodos de CLASE (MC):
    - Se declaran con el decorador "@classmethod".
    - No están asociados a las instancias sino a la clase misma.
    - Por ende, usan "cls" en vez de "self" como parametro inicial.
    - Pueden ser llamados directamente desde la clase.
    - No pueden acceder a los atributos de instancia, pero sí a
      los de clase.

- Métodos ESTÁTICOS (ME):
    - Se declaran con el decorador "@staticmethod".
    - No aceptan parámetros iniciales, ni "self" ni "cls".
    - No pueden modificar el estado de la clase ni de la instancia.
    - Sin embargo, pueden aceptar otros parámetros de entrada.
'''

class Pajaro:
    '''
    Define cualquier pájaro según especie y color.
    '''
    alas = True

    def __init__(self, especie, color):
        self.especie = especie
        self.color = color

    def piar(self):
        print('Pío')

    def volar(self, metros):
        print(f'El pájaro ha volado {metros} metros.')

    def hablar(self):
        print(f'Mi color es {self.color}')

    def pintar_negro(self):
        self.color = 'negro'
        print(f'Ahora el pájaro es {self.color}.')

    def volar_y_piar(self, metros):
        self.volar(metros)
        self.piar()

    def quitar_alas(self):
        self.alas = False
        print(f'El pájaro ya no tiene alas.')

    @classmethod
    def poner_huevos(cls, cantidad):
        print('Los pájaros pusieron {} huevos.'.format(cantidad))

    @staticmethod
    def mirar():
        print('Los pájaros están mirando.')


piolin = Pajaro('Canario', 'amarillo')
print(f'Mi pájaro es un {piolin.especie} y es de color {piolin.color}.')

piolin.piar()
piolin.volar(50)
piolin.hablar()
piolin.pintar_negro()
piolin.volar_y_piar(25)
piolin.quitar_alas()

Pajaro.poner_huevos(3)
# Pajaro.piar() # Levanta TypeError
Pajaro.mirar()
