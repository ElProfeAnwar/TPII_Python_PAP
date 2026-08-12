#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gestor de Archivos - Módulo de Funciones
MODULOS/gestor_funciones.py

Este módulo contiene todas las funciones necesarias para el gestor de archivos:
- Crear estructura de carpetas
- Agregar archivos
- Editar archivos
- Listar archivos
- Ver contenido de archivos
- Eliminar archivos
"""

import os
import datetime

# Ruta de la carpeta DATA
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'DATA')

def crear_estructura_carpetas():
    """
    Crea las carpetas necesarias para el funcionamiento del gestor
    """
    try:
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)
            print(f"📁 Carpeta DATA creada en: {DATA_DIR}")
        return True
    except Exception as e:
        print(f"❌ Error al crear la estructura de carpetas: {e}")
        return False

def obtener_ruta_archivo(nombre_archivo):
    """
    Genera la ruta completa del archivo en la carpeta DATA
    
    Args:
        nombre_archivo (str): Nombre del archivo sin extensión
        
    Returns:
        str: Ruta completa del archivo
    """
    return os.path.join(DATA_DIR, f"{nombre_archivo}.txt")

def verificar_archivo_existe(nombre_archivo):
    """
    Verifica si un archivo existe en la carpeta DATA
    
    Args:
        nombre_archivo (str): Nombre del archivo sin extensión
        
    Returns:
        bool: True si existe, False si no existe
    """
    ruta_archivo = obtener_ruta_archivo(nombre_archivo)
    return os.path.exists(ruta_archivo)

def agregar_archivo(nombre_archivo, contenido=""):
    """
    Crea un nuevo archivo con el contenido especificado
    
    Args:
        nombre_archivo (str): Nombre del archivo sin extensión
        contenido (str): Contenido inicial del archivo
        
    Returns:
        bool: True si se creó exitosamente, False si ya existe o hay error
    """
    try:
        if verificar_archivo_existe(nombre_archivo):
            return False
        
        ruta_archivo = obtener_ruta_archivo(nombre_archivo)
        
        # Crear el archivo con el contenido y metadata
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        contenido_completo = f"# Archivo: {nombre_archivo}.txt\n"
        contenido_completo += f"# Creado: {timestamp}\n"
        contenido_completo += f"# Última modificación: {timestamp}\n"
        contenido_completo += "\n" + contenido
        
        with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write(contenido_completo)
            
        return True
    except Exception as e:
        print(f"❌ Error al crear el archivo: {e}")
        return False

def editar_archivo(nombre_archivo, nuevo_contenido, agregar=False):
    """
    Edita un archivo existente
    
    Args:
        nombre_archivo (str): Nombre del archivo sin extensión
        nuevo_contenido (str): Nuevo contenido o contenido a agregar
        agregar (bool): Si True, agrega al final. Si False, reemplaza todo
        
    Returns:
        bool: True si se editó exitosamente, False si hay error
    """
    try:
        if not verificar_archivo_existe(nombre_archivo):
            return False
            
        ruta_archivo = obtener_ruta_archivo(nombre_archivo)
        
        if agregar:
            # Leer contenido actual y agregar el nuevo
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                contenido_actual = archivo.read()
            
            # Actualizar la fecha de modificación en los metadatos
            lines = contenido_actual.split('\n')
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Buscar y actualizar la línea de última modificación
            for i, line in enumerate(lines):
                if line.startswith('# Última modificación:'):
                    lines[i] = f"# Última modificación: {timestamp}"
                    break
            
            contenido_actualizado = '\n'.join(lines) + '\n\n' + nuevo_contenido
        else:
            # Reemplazar todo el contenido manteniendo los metadatos
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Leer metadatos existentes
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                lines = archivo.readlines()
            
            creado = "Desconocido"
            for line in lines:
                if line.startswith('# Creado:'):
                    creado = line.strip().replace('# Creado: ', '')
                    break
            
            contenido_actualizado = f"# Archivo: {nombre_archivo}.txt\n"
            contenido_actualizado += f"# Creado: {creado}\n"
            contenido_actualizado += f"# Última modificación: {timestamp}\n"
            contenido_actualizado += "\n" + nuevo_contenido
        
        with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write(contenido_actualizado)
            
        return True
    except Exception as e:
        print(f"❌ Error al editar el archivo: {e}")
        return False

def ver_contenido_archivo(nombre_archivo):
    """
    Lee y retorna el contenido de un archivo
    
    Args:
        nombre_archivo (str): Nombre del archivo sin extensión
        
    Returns:
        str: Contenido del archivo sin metadatos, None si hay error
    """
    try:
        if not verificar_archivo_existe(nombre_archivo):
            return None
            
        ruta_archivo = obtener_ruta_archivo(nombre_archivo)
        
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            contenido_completo = archivo.read()
        
        # Separar metadatos del contenido real
        lines = contenido_completo.split('\n')
        contenido_sin_metadatos = []
        saltear_metadatos = True
        
        for line in lines:
            if saltear_metadatos and line.startswith('#'):
                continue
            elif saltear_metadatos and line.strip() == "":
                saltear_metadatos = False
                continue
            else:
                saltear_metadatos = False
                contenido_sin_metadatos.append(line)
        
        return '\n'.join(contenido_sin_metadatos)
    except Exception as e:
        print(f"❌ Error al leer el archivo: {e}")
        return None

def obtener_info_archivo(nombre_archivo):
    """
    Obtiene información detallada de un archivo
    
    Args:
        nombre_archivo (str): Nombre del archivo sin extensión
        
    Returns:
        dict: Información del archivo (nombre, tamaño, fechas, etc.)
    """
    try:
        if not verificar_archivo_existe(nombre_archivo):
            return None
            
        ruta_archivo = obtener_ruta_archivo(nombre_archivo)
        stat_info = os.stat(ruta_archivo)
        
        # Leer metadatos del archivo
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            lines = archivo.readlines()
        
        creado = "Desconocido"
        modificado = "Desconocido"
        
        for line in lines:
            if line.startswith('# Creado:'):
                creado = line.strip().replace('# Creado: ', '')
            elif line.startswith('# Última modificación:'):
                modificado = line.strip().replace('# Última modificación: ', '')
        
        return {
            'nombre': f"{nombre_archivo}.txt",
            'tamaño': stat_info.st_size,
            'creado': creado,
            'modificado': modificado,
            'ruta': ruta_archivo
        }
    except Exception as e:
        print(f"❌ Error al obtener información del archivo: {e}")
        return None

def listar_archivos():
    """
    Lista todos los archivos en la carpeta DATA con información detallada
    """
    try:
        if not os.path.exists(DATA_DIR):
            print("📁 La carpeta DATA no existe. Se creará automáticamente.")
            crear_estructura_carpetas()
            return
        
        archivos = [f for f in os.listdir(DATA_DIR) if f.endswith('.txt')]
        
        if not archivos:
            print("📭 No hay archivos guardados.")
            return
        
        print(f"\n📚 Se encontraron {len(archivos)} archivo(s):")
        print("-" * 80)
        print(f"{'Nombre':<25} {'Tamaño':<10} {'Creado':<20} {'Modificado':<20}")
        print("-" * 80)
        
        for archivo in sorted(archivos):
            nombre_sin_ext = archivo.replace('.txt', '')
            info = obtener_info_archivo(nombre_sin_ext)
            
            if info:
                tamaño_str = f"{info['tamaño']} bytes"
                print(f"{info['nombre']:<25} {tamaño_str:<10} {info['creado']:<20} {info['modificado']:<20}")
            else:
                print(f"{archivo:<25} {'Error':<10} {'Error':<20} {'Error':<20}")
                
        print("-" * 80)
    except Exception as e:
        print(f"❌ Error al listar archivos: {e}")

def eliminar_archivo(nombre_archivo):
    """
    Elimina un archivo de la carpeta DATA
    
    Args:
        nombre_archivo (str): Nombre del archivo sin extensión
        
    Returns:
        bool: True si se eliminó exitosamente, False si hay error
    """
    try:
        if not verificar_archivo_existe(nombre_archivo):
            return False
            
        ruta_archivo = obtener_ruta_archivo(nombre_archivo)
        os.remove(ruta_archivo)
        return True
    except Exception as e:
        print(f"❌ Error al eliminar el archivo: {e}")
        return False

def obtener_estadisticas():
    """
    Obtiene estadísticas generales de los archivos
    
    Returns:
        dict: Estadísticas (cantidad de archivos, tamaño total, etc.)
    """
    try:
        if not os.path.exists(DATA_DIR):
            return {
                'cantidad_archivos': 0,
                'tamaño_total': 0,
                'archivos_detalle': []
            }
        
        archivos = [f for f in os.listdir(DATA_DIR) if f.endswith('.txt')]
        tamaño_total = 0
        archivos_detalle = []
        
        for archivo in archivos:
            nombre_sin_ext = archivo.replace('.txt', '')
            info = obtener_info_archivo(nombre_sin_ext)
            if info:
                tamaño_total += info['tamaño']
                archivos_detalle.append(info)
        
        return {
            'cantidad_archivos': len(archivos),
            'tamaño_total': tamaño_total,
            'archivos_detalle': archivos_detalle
        }
    except Exception as e:
        print(f"❌ Error al obtener estadísticas: {e}")
        return {
            'cantidad_archivos': 0,
            'tamaño_total': 0,
            'archivos_detalle': []
        }