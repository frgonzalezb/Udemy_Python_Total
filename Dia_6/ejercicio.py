registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

for index, elemento in enumerate(registro_ultima_sesion):
    registro_ultima_sesion[index] = elemento + '\t'

archivo = open('registro.txt', 'a')
archivo.writelines(registro_ultima_sesion)
archivo.close()

archivo = open('registro.txt', 'r')
print(archivo.read())
archivo.close()
