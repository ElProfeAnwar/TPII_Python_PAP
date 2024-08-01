# Abrir el archivo en modo lectura
with open('datos.txt', 'r') as archivo:
    # Leer línea por línea y mostrarlas
    for linea in archivo:
        print(linea.strip())  # El método strip() elimina el salto de línea al final de cada línea
