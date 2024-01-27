'''
El desafío de hoy, es que crees un software que funcione como el turnero 
de una farmacia (en mi país le llamamos así a esa máquina que se encuentra 
en la entrada de muchos comercios o bancos inclusive, que te pregunta qué 
trámite vienes a realizar y te asigna un número de turno según el área a 
la que deseas dirigirte.

Más detalles en el video y/o el pdf.

Aquí se encuentra el desarrollo de las funciones principales del programa.
'''


import numeros
import utilidades


AREAS = [
    'Perfumería',
    'Farmacia',
    'Cosmética',
]


def mostrar_menu():
    salir = False
    while not salir:
        utilidades.limpiar_consola()
        utilidades.mostrar_titulo('Farmacia Matasanos')
        utilidades.mostrar_opciones(AREAS)

        opcion = utilidades.escoger_opcion()

        if opcion == 1:
            numeros.obtener_numero('P')
            utilidades.esperar_usuario()
        elif opcion == 2:
            numeros.obtener_numero('F')
        elif opcion == 3:
            numeros.obtener_numero('C')
        else:
            continue


if __name__ == '__main__':
    mostrar_menu()
