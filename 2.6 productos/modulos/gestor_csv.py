"""
Módulo Gestor CSV
Contiene funciones auxiliares para el manejo de archivos CSV de productos.
"""

import os
import csv

def crear_archivo_csv(nombre_archivo):
    """
    Crea un archivo CSV con encabezados si no existe.
    
    Args:
        nombre_archivo (str): Nombre del archivo CSV a crear
    
    Returns:
        bool: True si se creó exitosamente, False en caso contrario
    """
    try:
        # Verificar si el archivo ya existe
        if os.path.exists(nombre_archivo):
            return True
        
        # Crear el archivo con encabezados
        with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(['Nombre', 'Precio', 'Stock'])
        
        print(f" Archivo '{nombre_archivo}' creado exitosamente.")
        return True
    
    except PermissionError:
        print(f" Error: No se tienen permisos para crear '{nombre_archivo}'.")
        return False
    except Exception as e:
        print(f" Error al crear el archivo: {e}")
        return False

def agregar_producto_csv(nombre_archivo, nombre, precio, stock):
    """
    Agrega un nuevo producto al archivo CSV.
    
    Args:
        nombre_archivo (str): Nombre del archivo CSV
        nombre (str): Nombre del producto
        precio (float): Precio del producto
        stock (int): Stock disponible
    
    Returns:
        bool: True si se agregó exitosamente, False en caso contrario
    """
    try:
        # Verificar que el archivo existe, si no, crearlo
        if not os.path.exists(nombre_archivo):
            crear_archivo_csv(nombre_archivo)
        
        # Agregar el producto al archivo
        with open(nombre_archivo, 'a', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow([nombre, precio, stock])
        
        return True
    
    except PermissionError:
        print(f" Error: No se tienen permisos para escribir en '{nombre_archivo}'.")
        return False
    except Exception as e:
        print(f" Error al agregar producto: {e}")
        return False

def validar_precio_stock(valor):
    """
    Valida que un valor sea positivo (para precio y stock).
    
    Args:
        valor (float/int): Valor a validar
    
    Returns:
        bool: True si es válido (positivo), False en caso contrario
    """
    try:
        return float(valor) > 0
    except (ValueError, TypeError):
        return False

def leer_productos_csv(nombre_archivo):
    """
    Lee todos los productos del archivo CSV.
    
    Args:
        nombre_archivo (str): Nombre del archivo CSV
    
    Returns:
        list: Lista de diccionarios con los productos, o lista vacía si hay error
    """
    productos = []
    
    try:
        if not os.path.exists(nombre_archivo):
            return productos
        
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                productos.append({
                    'nombre': fila['Nombre'],
                    'precio': float(fila['Precio']),
                    'stock': int(fila['Stock'])
                })
    
    except Exception as e:
        print(f"Error al leer productos: {e}")
    
    return productos

def contar_productos(nombre_archivo):
    """
    Cuenta el número de productos en el archivo CSV.
    
    Args:
        nombre_archivo (str): Nombre del archivo CSV
    
    Returns:
        int: Número de productos (sin contar el encabezado)
    """
    try:
        if not os.path.exists(nombre_archivo):
            return 0
        
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            next(lector, None)  # Saltar encabezado
            return sum(1 for fila in lector if any(campo.strip() for campo in fila))
    
    except Exception as e:
        print(f" Error al contar productos: {e}")
        return 0