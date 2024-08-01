# Abrir el archivo en modo escritura
with open('nuevo.txt', 'w') as archivo:
    # Escribir líneas en el archivo
    archivo.write('Esta es una nueva línea.\n')
    archivo.write('Otra línea más.\n')
    archivo.write('Programación II\n')

with open('nuevo.txt', 'r') as archivo: #se nombra "archivo"
    # Leer el contenido completo del archivo
    contenido = archivo.read()
    # Imprimir el contenido
    print(contenido)