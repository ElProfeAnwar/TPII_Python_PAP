# Función con argumentos predeterminados
def saludar(nombre="Usuario", edad=0):
    print(f"Hola, soy {nombre} y tengo {edad} años.")

# Llamada a la función sin proporcionar argumentos
saludar()

# Llamada a la función proporcionando solo un argumento
saludar("Ana")

# Llamada a la función proporcionando ambos argumentos
saludar("Pedro", 28)
