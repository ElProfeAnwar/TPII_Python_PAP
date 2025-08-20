from modulos.gestor_clientes import (
    crear_archivo,
    agregar_clientes,
    leer_csv,
    filtrar_por_columna,
    calcular_promedio_columna,
    escribir_csv
)
#Definir la ruta del archivo csv
ruta_csv = 'data/clientes.csv'
#Lista con los nombres de los encabezados
encabezados = ['Nombre', 'Edad', 'Ciudad']
#LLamamos a la f(x) que crea el archivo sino existe
crear_archivo(ruta_csv, encabezados)
#Agregamos clientes a través de inputs
print("Ingreso de clientes::")
nombre = input("Ingrese el nombre del cliente: ")
edad = input("Ingrese la edad del cliente: ")
ciudad = input("Ingrese ciudad del cliente: ")
#Guardamos al cliente con funcion
agregar_clientes(ruta_csv, [nombre, edad, ciudad])
#Leer archivo de clientes
datos = leer_csv(ruta_csv)
#Mostrar los clientes
print("Lista de clientes")
for fila in datos[1:]:
    print(f"Nombre: {fila[0]} - Edad:{fila[1]} - Ciudad:{fila[2]}")