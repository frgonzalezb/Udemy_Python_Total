'''
Escribe una función que requiera una cantidad indefinida de argumentos. 
Lo que hará esta función es devolver True si en algún momento se ha ingresado 
al numero cero repetido dos veces consecutivas.

Por ejemplo:

(5, 6, 1, 0, 0, 9, 3, 5) >>> True
(6, 0, 5, 1, 0, 3, 0, 1) >>> False
'''

def verificar_ceros_consecutivos(*args):
    args = iter(args)

    for arg in args:
        if arg == 0 and next(args) == 0:
            return True
    
    return False


print(verificar_ceros_consecutivos(5, 6, 1, 0, 0, 9, 3, 5))
print(verificar_ceros_consecutivos(6, 0, 5, 1, 0, 3, 0, 1))
