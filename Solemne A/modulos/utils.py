
import csv
import os

def validar_archivo_existe(ruta_archivo):
    """
    Valida si existe el archivo en la ruta especificada
    """
    return os.path.exists(ruta_archivo)

def leer_archivo_txt(ruta_archivo):
    """
    Lee el archivo de texto y devuelve las líneas
    """
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
        return lineas
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ruta_archivo}")
        return None
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None

def limpiar_datos(lineas):
    """
    Limpia los datos del archivo txt y los convierte en una lista de diccionarios
    """
    datos_limpios = []
    
    for linea in lineas:
        # Limpiar espacios en blanco al inicio y final
        linea = linea.strip()
        
        # Saltar líneas vacías
        if not linea:
            continue
            
        # Dividir la línea por ' - '
        partes = linea.split(' - ')
        
        if len(partes) == 3:  # Debe tener exactamente 3 partes
            # Extraer magnitud (eliminar "Magnitud: ")
            magnitud_str = partes[0].replace("Magnitud: ", "").strip()
            
            # Extraer región (eliminar "Región: ")
            region = partes[1].replace("Región: ", "").strip()
            
            # Extraer estado (eliminar "Estado: ")
            estado = partes[2].replace("Estado: ", "").strip()
            
            # Convertir magnitud a float
            try:
                magnitud = float(magnitud_str)
                
                # Agregar a la lista de datos limpios
                datos_limpios.append({
                    'magnitud': magnitud,
                    'region': region,
                    'estado': estado
                })
            except ValueError:
                print(f"Error: No se pudo convertir la magnitud '{magnitud_str}' a número")
                continue
    
    return datos_limpios

def generar_csv(datos, ruta_csv):
    """
    Genera el archivo CSV con los datos limpios
    """
    try:
        with open(ruta_csv, 'w', newline='', encoding='utf-8') as archivo_csv:
            # Crear el escritor CSV
            escritor = csv.writer(archivo_csv)
            
            # Escribir encabezados
            escritor.writerow(['Magnitud', 'Region', 'Estado'])
            
            # Escribir los datos
            for dato in datos:
                escritor.writerow([dato['magnitud'], dato['region'], dato['estado']])
        
        print(f"Archivo CSV generado exitosamente: {ruta_csv}")
        return True
    except Exception as e:
        print(f"Error al generar el archivo CSV: {e}")
        return False

def leer_csv_para_estadisticas(ruta_csv):
    """
    Lee el archivo CSV y devuelve los datos para calcular estadísticas
    """
    datos = []
    try:
        with open(ruta_csv, 'r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                datos.append({
                    'magnitud': float(fila['Magnitud']),
                    'region': fila['Region'],
                    'estado': fila['Estado']
                })
        return datos
    except Exception as e:
        print(f"Error al leer el CSV: {e}")
        return None

def calcular_estadisticas(datos):
    """
    Calcula todas las estadísticas requeridas
    """
    if not datos:
        return None
    
    # Total de eventos
    total_eventos = len(datos)
    
    # Contar perceptibles y no perceptibles
    perceptibles = 0
    no_perceptibles = 0
    
    # Suma de magnitudes para el promedio
    suma_magnitudes = 0
    
    # Contador de eventos por región
    eventos_por_region = {}
    
    for evento in datos:
        # Contar magnitudes
        suma_magnitudes += evento['magnitud']
        
        # Contar por estado
        if evento['estado'] == 'perceptible':
            perceptibles += 1
        elif evento['estado'] == 'no perceptible':
            no_perceptibles += 1
        
        # Contar por región
        region = evento['region']
        if region in eventos_por_region:
            eventos_por_region[region] += 1
        else:
            eventos_por_region[region] = 1
    
    # Calcular promedio de magnitudes
    promedio_magnitudes = suma_magnitudes / total_eventos if total_eventos > 0 else 0
    
    # Encontrar región con más eventos
    region_max_eventos = ""
    max_eventos = 0
    for region, cantidad in eventos_por_region.items():
        if cantidad > max_eventos:
            max_eventos = cantidad
            region_max_eventos = region
    
    return {
        'total_eventos': total_eventos,
        'perceptibles': perceptibles,
        'no_perceptibles': no_perceptibles,
        'promedio_magnitudes': promedio_magnitudes,
        'region_max_eventos': region_max_eventos,
        'max_eventos': max_eventos
    }

def mostrar_estadisticas(estadisticas):
    """
    Muestra las estadísticas en consola
    """
    print("\n" + "="*50)
    print("ESTADÍSTICAS DE EVENTOS SÍSMICOS")
    print("="*50)
    print(f"Total de eventos sísmicos registrados: {estadisticas['total_eventos']}")
    print(f"Eventos perceptibles: {estadisticas['perceptibles']}")
    print(f"Eventos no perceptibles: {estadisticas['no_perceptibles']}")
    print(f"Promedio de magnitudes: {estadisticas['promedio_magnitudes']:.2f}")
    print(f"Región con mayor cantidad de eventos: {estadisticas['region_max_eventos']} ({estadisticas['max_eventos']} eventos)")
    print("="*50)