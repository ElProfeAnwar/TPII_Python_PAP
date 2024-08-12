# Función con número variable de argumentos posicionales
def suma_numeros(*args):
    suma = sum(args)
    print("La suma de los números es:", suma)

# Llamada a la función con diferentes cantidades de argumentos
suma_numeros(2, 4, 6)
suma_numeros(1, 3, 5, 7, 9)

# Función con número variable de argumentos con nombre
def datos_personales(kwargs):
    print("Datos personales:")
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

# Llamada a la función con diferentes argumentos con nombre
#datos_personales(nombre="Juan", edad=30, ciudad="Madrid")
datos_personales(nombre="María", edad=25, ciudad="Barcelona", profesion="Ingeniera")

