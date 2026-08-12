#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gestor de Archivos
Archivo principal (main.py)
"""

import os
import sys

# Agregar la carpeta MODULOS al path para importar
sys.path.append(os.path.join(os.path.dirname(__file__), 'MODULOS'))

from MODULOS.gestor_funciones import *

def mostrar_menu():
    """Muestra el menú principal del gestor de archivos"""
    print("\n" + "="*50)
    print("           GESTOR DE ARCHIVOS")
    print("="*50)
    print("1. Listar archivos")
    print("2. Agregar nuevo archivo")
    print("3. Editar archivo existente")
    print("4. Ver contenido de archivo")
    print("5. Eliminar archivo")
    print("0. Salir")
    print("="*50)

def main():
    """Función principal del programa"""
    print("¡Bienvenido al Gestor de Archivos!")
    
    # Crear las carpetas necesarias si no existen
    crear_estructura_carpetas()
    
    while True:
        mostrar_menu()
        
        try:
            opcion = input("\nSeleccione una opción (0-5): ").strip()
            
            if opcion == "0":
                print("\nGracias por usar el Gestor de Archivos")
                print("Hasta luego 👋")
                break
                
            elif opcion == "1":
                print("\n📁 LISTA DE ARCHIVOS:")
                listar_archivos()
                
            elif opcion == "2":
                print("\n📝 AGREGAR NUEVO ARCHIVO:")
                nombre = input("Ingrese el nombre del archivo (sin extensión): ").strip()
                if nombre:
                    contenido = input("Ingrese el contenido inicial del archivo: ")
                    if agregar_archivo(nombre, contenido):
                        print(f"✅ Archivo '{nombre}.txt' creado exitosamente!")
                    else:
                        print(f"❌ Error: El archivo '{nombre}.txt' ya existe.")
                else:
                    print("❌ Error: Debe ingresar un nombre válido.")
                    
            elif opcion == "3":
                print("\n✏️ EDITAR ARCHIVO:")
                listar_archivos()
                nombre = input("\nIngrese el nombre del archivo a editar (sin extensión): ").strip()
                if nombre:
                    if verificar_archivo_existe(nombre):
                        print(f"\n📄 Contenido actual de '{nombre}.txt':")
                        contenido_actual = ver_contenido_archivo(nombre)
                        if contenido_actual is not None:
                            print("-" * 40)
                            print(contenido_actual)
                            print("-" * 40)
                            
                            print("\nOpciones de edición:")
                            print("1. Reemplazar todo el contenido")
                            print("2. Agregar contenido al final")
                            
                            modo = input("Seleccione modo de edición (1-2): ").strip()
                            nuevo_contenido = input("Ingrese el nuevo contenido: ")
                            
                            if editar_archivo(nombre, nuevo_contenido, modo == "2"):
                                print(f"✅ Archivo '{nombre}.txt' editado exitosamente!")
                            else:
                                print(f"❌ Error al editar el archivo '{nombre}.txt'.")
                    else:
                        print(f"❌ Error: El archivo '{nombre}.txt' no existe.")
                else:
                    print("❌ Error: Debe ingresar un nombre válido.")
                    
            elif opcion == "4":
                print("\n👁️ VER CONTENIDO DE ARCHIVO:")
                listar_archivos()
                nombre = input("\nIngrese el nombre del archivo a ver (sin extensión): ").strip()
                if nombre:
                    contenido = ver_contenido_archivo(nombre)
                    if contenido is not None:
                        print(f"\n📄 Contenido de '{nombre}.txt':")
                        print("-" * 40)
                        print(contenido)
                        print("-" * 40)
                    else:
                        print(f"❌ Error: El archivo '{nombre}.txt' no existe.")
                else:
                    print("❌ Error: Debe ingresar un nombre válido.")
                    
            elif opcion == "5":
                print("\n🗑️ ELIMINAR ARCHIVO:")
                listar_archivos()
                nombre = input("\nIngrese el nombre del archivo a eliminar (sin extensión): ").strip()
                if nombre:
                    if verificar_archivo_existe(nombre):
                        confirmacion = input(f"¿Está seguro de eliminar '{nombre}.txt'? (s/N): ").strip().lower()
                        if confirmacion in ['s', 'si', 'sí', 'yes', 'y']:
                            if eliminar_archivo(nombre):
                                print(f"✅ Archivo '{nombre}.txt' eliminado exitosamente!")
                            else:
                                print(f"❌ Error al eliminar el archivo '{nombre}.txt'.")
                        else:
                            print("❌ Operación cancelada.")
                    else:
                        print(f"❌ Error: El archivo '{nombre}.txt' no existe.")
                else:
                    print("❌ Error: Debe ingresar un nombre válido.")
                    
            else:
                print("❌ Opción no válida. Por favor seleccione una opción del 0 al 5.")
                
        except KeyboardInterrupt:# Manejo de interrupción por Ctrl+C
            print("\n\n🛑 Programa interrumpido por el usuario.")
            print("¡Hasta luego! 👋")
            break
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
            
        # Pausa para que el usuario pueda ver el resultado
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()