# Abrir el archivo en modo lectura
with open('nuevo.txt', 'r') as archivo: #se nombra "archivo"
    # Leer el contenido completo del archivo
    contenido = archivo.read()
    # Imprimir el contenido
    print(contenido)