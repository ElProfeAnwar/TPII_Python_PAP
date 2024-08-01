# Abrir el archivo de origen en modo lectura
with open('nuevo.txt', 'r') as archivo_origen:
    # Leer el contenido del archivo de origen
    contenido = archivo_origen.read()

# Abrir el archivo de copia en modo escritura
with open('copia.txt', 'w') as archivo_copia:
    # Escribir el contenido en el archivo de copia
    archivo_copia.write(contenido)

# Abrir el archivo en modo lectura
with open('copia.txt', 'r') as archivo:
    # Leer el contenido completo del archivo
    cont_copia = archivo.read()
    # Imprimir el contenido
    print(cont_copia)
