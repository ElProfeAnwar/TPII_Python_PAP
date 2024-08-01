# Copiar contenido de un archivo binario a otro 
def copiar_archivo_binario(origen, destino):
    try:
        with open(origen, 'rb') as archivo_origen:
            with open(destino, 'wb') as archivo_destino:
                # Copiar el contenido del archivo origen al archivo destino en bloques
                for bloque in iter(lambda: archivo_origen.read(4096), b''):
                    archivo_destino.write(bloque)
        print("Archivo binario copiado correctamente.")
    except FileNotFoundError:
        print("El archivo origen no existe.")
    except Exception as e:
        print("Error al copiar el archivo:", str(e))

# Uso del método para copiar una imagen binaria
copiar_archivo_binario('imagen_origen.jpg', 'imagen_destino.jpg')
