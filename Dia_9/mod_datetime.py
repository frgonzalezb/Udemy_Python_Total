'''
Uso del módulo datetime
'''


from datetime import date, time, datetime


'''
EJERCICIO 1
Crea un objeto fecha llamado mi_fecha que almacene el día 3 de febrero 
de 1999
'''

mi_fecha = date(1999, 2, 3)
print(mi_fecha)


'''
EJERCICIO 2
Crea un objeto en la variable hoy que siempre almacene la fecha actual 
cuando sea invocada.
'''

hoy = date.today()
print(hoy)


'''
EJERCICIO 3
En una variable llamada minutos, almacena únicamente los minutos de 
la hora actual.

Por ejemplo, si se ejecutara a las 20:43:17 de la noche, la variable 
minutos debe almacenar el valor 43
'''

minutos = datetime.now().minute
print(minutos)
