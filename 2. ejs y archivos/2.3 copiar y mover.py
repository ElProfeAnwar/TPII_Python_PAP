import shutil
# Copiar un archivo a un nuevo destino
def copiar_archivo(origen, destino):
    try:
        shutil.copy(origen, destino)
        print("Archivo copiado correctamente.")
    except FileNotFoundError:
        print("El archivo origen no existe.")
    except Exception as e:
        print("Error al copiar el archivo:", str(e))

# Uso del método para copiar un archivo
# la carpeta dirnuevo, debe ser creada previamente
#\a \n en la ruta del archivo, da errores, evitar nombrar carpeta y archivos con esas letras
copiar_archivo('E:\Directorio\origen.txt', 'E:\Directorio\dirnuevo\destino.txt')

