'''
Crea una función llamada verificar_email para comprobar si una dirección 
de email es correcta, que verifique si el email dado como argumento 
contiene "@" (entre el nombre de usuario y el dominio) y finaliza en 
".com" (aunque aceptando también casos que cuentan con un dominio 
adicional, tal como ".com.br" para el caso de un usuario de Brasil).

Si se encuentra el patrón, la función debe finalizar mostrando en pantalla 
el mensaje "Ok", pero si detecta que la frase no contiene los elementos 
indicados, debe informarle al usuario "La dirección de email es 
incorrecta" imprimiendo el mensaje.
'''

import re


def verificar_email(email):
    patron = r'(\w+)@(\w+)(\W\w+)(\W[a-z]+)?'
    if re.search(patron, email):
        print("Ok")
    else:
        print("La dirección de email es incorrecta")


emails = [
    'usuario@hostcom',
    'usuario@host.com',
    'usuario@host.com.br',
]

for email in emails:
    verificar_email(email)


'''
Crea una función llamada verificar_saludo para verificar si una frase 
entregada como argumento inicia con la palabra "Hola". Si se encuentra 
el patrón, la función debe finalizar mostrando el mensaje "Ok", pero 
si detecta que la frase no contiene "Hola", debe informarle al usuario 
"No has saludado" imprimiendo el mensaje en pantalla.
'''

def verificar_saludo(frase):
    patron = r'Hola'
    if re.search(patron, frase):
        print("Ok")
    else:
        print("No has saludado")


verificar_saludo('Hola, Python')
verificar_saludo('Ki ti pah longi')


'''
El código postal de una región determinada se forma a partir de dos 
caracteres alfanuméricos y cuatro numéricos a continuación 
(ejemplo: XX1234). 

Crea una función, llamada verificar_cp para comprobar si el código 
postal pasado como argumento sigue este patrón. Si el patrón es 
correcto, mostrar al usuario el mensaje "Ok", de lo contrario: 
"El código postal ingresado no es correcto".
'''

def verificar_cp(cp):
    patron = r'\w{2}\d{4}'
    if re.search(patron, cp):
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")


verificar_cp('XX1234')
verificar_cp('1234XX')
verificar_cp('X-1234')
