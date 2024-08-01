# Mover un archivo a un nuevo directorio
def mover_archivo(origen, destino):
    try:
        shutil.move(origen, destino)
        print("Archivo movido correctamente.")
    except FileNotFoundError:
        print("El archivo origen no existe.")
    except Exception as e:
        print("Error al mover el archivo:", str(e))

# Uso del método para mover un archivo
mover_archivo('archivo.txt', 'otro_directorio/archivo.txt')

 #archivo / otro_directorio 