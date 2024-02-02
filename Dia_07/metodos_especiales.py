class CD:
    '''
    Compact Disc
    '''
    def __init__(self, autor: str, titulo: str, canciones: int):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    def __str__(self):
        '''
        Si se intenta imprimir en consola una instancia de la clase,
        sin sobrescribir este método, Python devolverá una cadena de 
        representación del objeto que no es muy legible a humanos.
        
        Por ende, es útil sobrescribir este método para obtener 
        información que sea más legible y útil.
        '''
        return f'Album "{self.titulo}" de {self.autor}'
    
    def __len__(self):
        '''
        Si se intenta obtener el largo de un objeto a secas con la
        función len() de Python, se devolverá un error.

        Sobrescribir este método permite que la función len() sí pueda
        ser aplicada a una instancia correctamente.
        '''
        return self.canciones
    
    def __del__(self):
        '''
        Si se ocupa la palabra clave "del" a secas, Python elimina la
        instancia, pero no informa al usuario de la acción realizada.

        Sobrescribir este método permite que "del" sí informe al usuario 
        de la eliminación de la instancia con un mensaje útil.
        '''
        print('El CD ha sido eliminado exitosamente.')


mi_cd = CD('Pink Floyd', 'The Wall', 24)

print(mi_cd)        # Devuelve lo definido en __str__
print(len(mi_cd))   # Devuelve lo definido en __len__

del mi_cd           # Devuelve lo definido en __del__
