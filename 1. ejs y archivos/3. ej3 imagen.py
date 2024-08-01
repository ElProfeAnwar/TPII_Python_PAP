# Abrir el archivo binario en modo lectura
with open('perro.jpg', 'rb') as foto:
    # Leer los primeros 10 bytes del archivo
    primeros_bytes = foto.read(10)
    # Imprimir los primeros bytes en formato hexadecimal
    print(primeros_bytes.hex())
