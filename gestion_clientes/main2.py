from modulos.gestor_clientes import (
    crear_archivo,
    agregar_clientes,
    leer_csv,
    filtrar_por_columna,
    calcular_promedio_columna,
    escribir_csv
)

ruta_csv = 'data/clientes.csv'
encabezados = ['Nombre', 'Edad', 'Ciudad']

# Crea el archivo si no existe
crear_archivo(ruta_csv, encabezados)

def menu():
    print("\n--- MENÚ DE CLIENTES ---")
    print("1. Agregar cliente")
    print("2. Mostrar todos los clientes")
    print("3. Filtrar clientes por ciudad")
    print("4. Calcular promedio de edad")
    print("5. Guardar filtro en nuevo archivo")
    print("6. Salir")
    return input("Elige una opción: ")

while True:
    opcion = menu()

    if opcion == "1":
        nombre = input("Nombre: ")
        edad = input("Edad: ")
        ciudad = input("Ciudad: ")
        agregar_clientes(ruta_csv, [nombre, edad, ciudad])

    elif opcion == "2":
        datos = leer_csv(ruta_csv)
        print("Lista de clientes:")
        for fila in datos[1:]:
            print(f"Nombre: {fila[0]} - Edad: {fila[1]} - Ciudad: {fila[2]}")

    elif opcion == "3":
        datos = leer_csv(ruta_csv)
        ciudad = input("Ciudad para filtrar: ")
        filtrados = filtrar_por_columna(datos, "Ciudad", ciudad)
        print("Clientes filtrados:")
        for fila in filtrados[1:]:
            print(f"Nombre: {fila[0]} - Edad: {fila[1]} - Ciudad: {fila[2]}")
    
    elif opcion == "4":
        datos = leer_csv(ruta_csv)
        promedio = calcular_promedio_columna(datos, "Edad")
        print(f"El promedio de edad es: {promedio}")

    elif opcion == "5":
        datos = leer_csv(ruta_csv)
        ciudad = input("Ciudad para filtrar y guardar: ")
        filtrados = filtrar_por_columna(datos, "Ciudad", ciudad)
        nombre_archivo = input("Nombre del archivo para guardar (ej. clientes_filtrados.csv): ")
        escribir_csv(nombre_archivo, filtrados)

    elif opcion == "6":
        print("¡Hasta luego!")
        break

    else:
        print("Opción no válida, intenta de nuevo.")

