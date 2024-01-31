'''
Descomprimir el proyecto sin trampa (sin WinRAR, WinZIP, 7-Zip, etc.), 
según instrucciones en video/pdf.
'''


import os
import zipfile

from pathlib import Path


CWD = os.getcwd()

directorio = Path(CWD, 'Dia_9', 'Proyecto')
comprimido = Path(directorio, 'Proyecto+Dia+9.zip')

zip_abierto = zipfile.ZipFile(comprimido, 'r')
zip_abierto.extractall(directorio)
zip_abierto.close()
