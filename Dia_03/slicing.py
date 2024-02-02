texto = 'ABCDEFGHIJKLM'

fragmento = texto[2:5]    # REMEMBER: El valor final no es inclusivo
print(fragmento)          # Imprime 'CDE' 

fragmento = texto[2:]
print(fragmento)          # Imprime 'CDEFGHIJKLM'

fragmento = texto[:5]
print(fragmento)          # Imprime 'ABCDE'

fragmento = texto[2:10:2] # REMEMBER: El tercer valor es de salto
print(fragmento)          # Imprime 'CEGI'

fragmento = texto[::2]    # El valor de salto puede usarse sin índices
print(fragmento)          # Imprime 'ACEGIKM'

fragmento = texto[::-2]    # El valor de salto puede ser negativo
print(fragmento)          # Imprime 'MKIGECA'
