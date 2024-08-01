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
copiar_archivo('archivo_origen.txt', 'nuevo_directorio/archivo_destino.txt')

#crear archivo_origen / nuevo_directorio /

