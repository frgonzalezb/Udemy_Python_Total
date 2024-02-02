'''
Remueve los caracteres a la izquierda de nuestro texto principal:

,

:

%

_

#

Utiliza el método lstrip(). Imprime el resultado en pantalla:

",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"

Busca en la documentación acerca del funcionamiento del método solicitado para saber cómo actúa. Puedes utilizar variables intermedias si las necesitas.
'''

texto_principal = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
print(texto_principal.lstrip(',:_#,,,,,,:::____##'))
