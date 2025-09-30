
from modulos.utils import (
    validar_archivo_existe,
    leer_archivo_txt,
    limpiar_datos,
    generar_csv,
    leer_csv_para_estadisticas,
    calcular_estadisticas,
    mostrar_estadisticas
)

def procesar_txt_y_generar_csv():
    """
    Función que procesa el archivo TXT y genera el CSV limpio
    """
    ruta_txt = "C:\Users\anwyu\OneDrive - Universidad San Sebastian\USS\2025 USS\2do Semestre\Taller de Prog II\Solemne 1\Solemne A\data\eventos_sismicos.txt"
    ruta_csv = "data/eventos_limpios.csv"
    
    print("Procesando archivo TXT y generando CSV...")
    
    # 1. Validar que existe el archivo
    if not validar_archivo_existe(ruta_txt):
        print(f"Error: El archivo {ruta_txt} no existe.")
        return False
    
    # 2. Leer el archivo TXT
    lineas = leer_archivo_txt(ruta_txt)
    if lineas is None:
        return False
    
    # 3. Limpiar los datos
    datos_limpios = limpiar_datos(lineas)
    if not datos_limpios:
        print("No se pudieron limpiar los datos.")
        return False
    
    # 4. Generar el CSV
    if generar_csv(datos_limpios, ruta_csv):
        print("Proceso completado exitosamente.")
        return True
    else:
        return False

def mostrar_estadisticas_eventos():
    """
    Función que lee el CSV y muestra las estadísticas
    """
    ruta_csv = "data/eventos_limpios.csv"
    
    print("Calculando estadísticas desde el archivo CSV...")
    
    # Validar que existe el CSV
    if not validar_archivo_existe(ruta_csv):
        print(f"Error: El archivo {ruta_csv} no existe. Debe generar el CSV primero.")
        return
    
    # Leer datos del CSV
    datos = leer_csv_para_estadisticas(ruta_csv)
    if datos is None:
        print("Error al leer los datos del CSV.")
        return
    
    # Calcular estadísticas
    estadisticas = calcular_estadisticas(datos)
    if estadisticas is None:
        print("Error al calcular las estadísticas.")
        return
    
    # Mostrar estadísticas
    mostrar_estadisticas(estadisticas)

def main():
    """
    Función principal del programa
    """
    while True:
        print("\n--- ANÁLISIS DE EVENTOS SÍSMICOS ---")
        print("1. Procesar TXT y generar CSV limpio")
        print("2. Mostrar estadísticas de eventos")
        print("3. Salir")
        
        try:
            opcion = input("\nSeleccione una opción (1-3): ").strip()
            
            if opcion == "1":
                procesar_txt_y_generar_csv()
            elif opcion == "2":
                mostrar_estadisticas_eventos()
            elif opcion == "3":
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, seleccione 1, 2 o 3.")
                
        except KeyboardInterrupt:
            print("\n\nPrograma interrumpido por el usuario.")
            break
        except Exception as e:
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()
