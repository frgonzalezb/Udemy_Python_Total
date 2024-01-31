import os
import shutil
import zipfile

from pathlib import Path


CWD = os.getcwd()

texto_A = Path(CWD, 'Files', 'mi_texto_A.txt')
texto_B = Path(CWD, 'Files', 'mi_texto_B.txt')
comprimido = Path(CWD, 'Files', 'archivo_comprimido.zip')

# Comprimir
mi_zip = zipfile.ZipFile(comprimido, 'w') # Genera archivo zip vacío
mi_zip.write(texto_A)
mi_zip.write(texto_B)
mi_zip.close()

# Descomprimir
zip_abierto = zipfile.ZipFile(comprimido, 'r')
zip_abierto.extract()
zip_abierto.close()

# Comprimir con shutil
destino = Path(CWD, 'Files', 'comprimido')
directorio = Path(CWD, 'Files')
desempacar = Path(CWD, 'Files', 'comprimido_shutil')
shutil.make_archive(destino, 'zip', directorio)

# Descomprimir con shutil
shutil.unpack_archive(str(destino) + '.zip', desempacar, 'zip')
