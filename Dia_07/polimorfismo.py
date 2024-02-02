'''
POLIMORFISMO, según profe:

Dos o más objetos de clases distintas pueden ejecutar métodos que 
comparten el mismo nombre y, aunque hagan cosas totalmente distintas, 
no hay conflictos (ni errores, ni sobrescrituras, etc.) en su ejecución, 
todo funciona bien.
'''

class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + ' dice muuuuu.')


class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + ' dice beeeee.')


# Ejemplo simple
vaca_1 = Vaca('Aurora')
oveja_1 = Oveja('Nube')

vaca_1.hablar()
oveja_1.hablar()


# Ejemplo con ciclo for
animales = [vaca_1, oveja_1]

for animal in animales:
    animal.hablar()


# Ejemplo con función
def hacer_hablar_al_animal(animal):
    animal.hablar()


hacer_hablar_al_animal(vaca_1)
hacer_hablar_al_animal(oveja_1)
