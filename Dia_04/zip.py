nombres = ['Ana', 'Hugo', 'Valeria']
edades = [65, 29, 42]
ciudades = ['Lima', 'Madrid', 'México']

combinados = zip(nombres, edades, ciudades)
print(combinados)
print(list(combinados))

for nombre, edad, ciudad in list(combinados):
    print(f'{nombre} tiene {edad} años y vive en {ciudad}.')

'''
Crea el zip con las traducciones los números del 1 al 5 en español, portugués e inglés (en el mismo orden), y convierte el objeto generado en una lista almacenada en la variable numeros:

uno / um / one

dos / dois / two

tres / três / three

cuatro / quatro / four

cinco / cinco / five

El resultado deberá seguir la estructura:

[('uno', 'um', 'one'), ('dos', 'dois', 'two'), ... ]
'''

espanol = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
portugues = ['um', 'dois', 'três', 'quatro', 'cinco']
ingles = ['one', 'two', 'three', 'four', 'five']

numeros = list(zip(espanol, portugues, ingles))
print(numeros)
