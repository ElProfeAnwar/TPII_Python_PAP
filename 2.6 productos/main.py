# proyecto_csv/main.py
"""
Sistema de Gestión de Productos - Archivo Principal
Permite al usuario ingresar datos de productos y guardarlos en un archivo CSV.
"""

import os
import sys

# Agregar la carpeta modulos al path para poder importar
sys.path.append(os.path.join(os.path.dirname(__file__), 'C:/Users/anwyu/OneDrive - Corporación Santo Tomas/USS/2025 USS/2do Semestre/Taller de Prog II/Ejercicios 1 CSV/2.6 productos/modulos'))

from gestor_csv import crear_archivo_csv, agregar_producto_csv, validar_precio_stock

def mostrar_menu():
    """Muestra el menú principal de opciones"""
    print("\n" + "="*50)
    print("    SISTEMA DE GESTIÓN DE PRODUCTOS")
    print("="*50)
    print("1. Agregar producto")
    print("2. Ver productos guardados")
    print("3. Salir")
    print("-"*50)

def solicitar_datos_producto():
    """
    Solicita al usuario los datos del producto con validaciones
    Returns:
        tuple: (nombre, precio, stock) o None si se cancela
    """
    try:
        nombre = input("Ingrese el nombre del producto: ").strip()
        if not nombre:
            print("❌ El nombre no puede estar vacío.")
            return None
        
        # Validar precio
        while True:
            try:
                precio_str = input("Ingrese el precio: $").strip()
                precio = float(precio_str)
                if not validar_precio_stock(precio):
                    print("❌ El precio debe ser un número positivo.")
                    continue
                break
            except ValueError:
                print("❌ Por favor ingrese un precio válido (número).")
        
        # Validar stock
        while True:
            try:
                stock_str = input("Ingrese el stock: ").strip()
                stock = int(stock_str)
                if not validar_precio_stock(stock):
                    print("❌ El stock debe ser un número entero positivo.")
                    continue
                break
            except ValueError:
                print("❌ Por favor ingrese un stock válido (número entero).")
        
        return nombre, precio, stock
    
    except KeyboardInterrupt:
        print("\n\n⚠️  Operación cancelada por el usuario.")
        return None

def ver_productos(archivo_csv):
    """
    Muestra los productos guardados en el archivo CSV
    Args:
        archivo_csv (str): Ruta del archivo CSV
    """
    if not os.path.exists(archivo_csv):
        print("📄 No hay productos guardados aún.")
        return
    
    try:
        with open(archivo_csv, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read().strip()
            if not contenido:
                print("📄 El archivo está vacío.")
                return
            
            print("\n" + "="*60)
            print("           PRODUCTOS GUARDADOS")
            print("="*60)
            
            lineas = contenido.split('\n')
            encabezado = lineas[0]
            productos = lineas[1:] if len(lineas) > 1 else []
            
            if not productos:
                print("📄 No hay productos registrados.")
                return
            
            # Mostrar en formato de tabla
            print(f"{'Nombre':<20} {'Precio':<12} {'Stock':<10}")
            print("-" * 45)
            
            for producto in productos:
                if producto.strip():  # Evitar líneas vacías
                    datos = producto.split(',')
                    if len(datos) == 3:
                        nombre, precio, stock = datos
                        print(f"{nombre:<20} ${precio:<11} {stock:<10}")
            
            print("-" * 45)
            print(f"Total de productos: {len([p for p in productos if p.strip()])}")
    
    except Exception as e:
        print(f"❌ Error al leer el archivo: {e}")

def main():
    """Función principal del programa"""
    archivo_csv = "productos.csv"
    
    # Crear el archivo CSV si no existe
    crear_archivo_csv(archivo_csv)
    
    print("¡Bienvenido al Sistema de Gestión de Productos!")
    
    while True:
        mostrar_menu()
        
        try:
            opcion = input("Seleccione una opción (1-3): ").strip()
            
            if opcion == "1":
                print("\n--- AGREGAR NUEVO PRODUCTO ---")
                datos = solicitar_datos_producto()
                
                if datos:
                    nombre, precio, stock = datos
                    
                    # Confirmar antes de guardar
                    print(f"\n📋 Datos a guardar:")
                    print(f"   Nombre: {nombre}")
                    print(f"   Precio: ${precio}")
                    print(f"   Stock: {stock}")
                    
                    confirmacion = input("\n¿Confirma guardar este producto? (s/n): ").lower()
                    
                    if confirmacion == 's' or confirmacion == 'si':
                        if agregar_producto_csv(archivo_csv, nombre, precio, stock):
                            print("✅ Producto agregado exitosamente.")
                        else:
                            print("❌ Error al agregar el producto.")
                    else:
                        print("❌ Producto no guardado.")
            
            elif opcion == "2":
                ver_productos(archivo_csv)
            
            elif opcion == "3":
                print("\n¡Gracias por usar el Sistema de Gestión de Productos!")
                print("👋 ¡Hasta luego!")
                break
            
            else:
                print("❌ Opción no válida. Por favor seleccione 1, 2 o 3.")
        
        except KeyboardInterrupt:
            print("\n\n⚠️  Programa interrumpido por el usuario.")
            print("👋 ¡Hasta luego!")
            break
        except Exception as e:
            print(f"❌ Error inesperado: {e}")

if __name__ == "__main__":
    main()
