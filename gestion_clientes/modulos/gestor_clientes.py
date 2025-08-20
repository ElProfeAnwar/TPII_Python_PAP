import os
import csv


#Función que va a crear detro de la carpeta data
# el archivo clientes.csv sino existe
def crear_archivo(ruta_archivo, encabezados):
    if not os.path.exists("data"):
        os.makedirs("data")#solo si no existe
    if not os.path.exists(ruta_archivo):
        with open(ruta_archivo, 'w', newline='', encoding='utf-8') as archivo:
            writer = csv.writer(archivo)#Se crea el escritor
            writer.writerow(encabezados)#Se escriben los encabezados como primera linea
        print(f"Archivo '{ruta_archivo}' creado con encabezados")
    else:
        print(f"Archivo '{ruta_archivo}' ya existe!")

#Función para agregar un nuevo client al archivo csv
def agregar_clientes(ruta_archivo, cliente):
    with open(ruta_archivo, 'a', newline='', encoding='utf-8') as archivo:
        writer = csv.writer(archivo)
        writer.writerow(cliente) #Se agrega la nueva fila con los datos del cliente
    print("Cliente agregado exitosamente!")

#Función que pueda leer el contenido de mi archivo csv
def leer_csv(ruta_archivo):
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        return list(lector)#Convertir el lector a una lista de filas

#Función que filtra los datos de una columna especifica (ciudad)
def filtrar_por_columna(datos, columna, valor):
    indice = datos[0].index(columna)#Obtenemos el indice de la columna buscada
    return [datos[0]] + [fila for fila in datos[1:] if fila[indice]==valor]

#función que permite calcular el promedio de una columna como "edad"
def calcular_promedio_columna(datos, columna):
    indice = datos[0].index(columna)#indice de la columna que se requiere analizar
    total = 0
    for fila in datos[1:]: #Saltamos el encabezado
        total += int(fila[indice])#Sumamos cada valor de edad ya convertido a int
    return total / (len(datos) - 1)#retorno el promedio de las edades

#función para guardar los datos filtrados en un nuevo archivo csv
def escribir_csv(nombre_archivo, datos):
    with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo:
        writer = csv.writer(archivo)
        writer.writerows(datos)#Escribimos todas las filas obtenidas
    print(f"Archivo '{nombre_archivo}' creado con éxito!")


