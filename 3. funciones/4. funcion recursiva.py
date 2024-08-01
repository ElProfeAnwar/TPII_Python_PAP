# Función recursiva para calcular el factorial de un número
def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n<0:
        print("No se aceptan negativos")
    else:
        return n * factorial(n - 1)

# Llamada a la función recursiva
numero = -5
resultado_factorial = factorial(numero)
if numero >= 0:
    print(f"El factorial de {numero} es: {resultado_factorial}")
