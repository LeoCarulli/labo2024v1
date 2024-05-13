import os
from kaggle.api.kaggle_api_extended import KaggleApi

# Configurar la API de Kaggle
api = KaggleApi()
api.authenticate()

# Ruta de la carpeta con los archivos a subir
carpeta_archivos = r'C:\Users\RYZEN\Desktop\Maestria_Austral\7-LabDeImplementación\ArchivosKaggle'

# Obtener la lista de archivos en la carpeta
archivos = os.listdir(carpeta_archivos)

# Iterar sobre cada archivo y subirlo a la competencia
for archivo in archivos:
    ruta_completa = os.path.join(carpeta_archivos, archivo)
    # Subir archivo a la competencia
    api.competition_submit(ruta_completa, "Exp Final Versión 2 - semillerío", competition="labo-i-2024-virtual")
    print(f"Archivo '{archivo}' subido con éxito.")
