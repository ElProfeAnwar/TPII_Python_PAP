import os

# Listar archivos en un directorio
def listar_archivos(directorio):
    try:
        archivos = os.listdir(directorio)
        print("Archivos en el directorio:", archivos)
    except FileNotFoundError:
        print("El directorio especificado no existe.")
    except Exception as e:
        print("Error al listar archivos:", str(e))

# Uso del método para listar archivos en un directorio
listar_archivos('D:\Onedrive\directorio')

# Verificar si un archivo existe en la misma carpeta del archivo py
def verificar_existencia_archivo(archivo):
    if os.path.exists(archivo):
        print(f"El archivo {archivo} existe.")
    else:
        print(f"El archivo {archivo} no existe.")

# Uso del método para verificar existencia de un archivo
verificar_existencia_archivo('archivo.txt')

#para buscar en otra carpeta
# verificar_existencia_archivo('D:\Onedrive\directorio')
