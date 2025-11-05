import requests
import json

# --- Configuración ---
# ¡IMPORTANTE! Reemplaza estos valores con tus credenciales reales
EMAIL = 'elprofeanwar@gmail.com'
TOKEN = '64d712ed9135b616faa7c68b'
# ---------------------

# Validamos que el usuario haya cambiado las credenciales de ejemplo
if EMAIL == "correo@correo.cl" or TOKEN == "apiKey_personal":
    print("="*50)
    print("  ¡DETENTE! \U0001F6A8")
    print("  Debes editar este script y poner tu email y token reales")
    print("  en las variables EMAIL y TOKEN antes de ejecutarlo.")
    print("="*50)
    exit() # Detenemos la ejecución

# Construimos la URL correcta (basada en la Sección 2 de la documentación)
url_api = f"https://climatologia.meteochile.gob.cl/application/servicios/getEstacionesRedEma?usuario={EMAIL}&token={TOKEN}"

print(f"Conectando a la API de MeteoChile...")
print(f"URL: {url_api}")

try:
    # 1. Hacer la petición GET
    response = requests.get(url_api)
    
    # 2. Verificar si la respuesta fue un error (ej. 401, 403, 404, 500)
    # Si el código es 4xx o 5xx, saltará al 'except' de abajo
    response.raise_for_status() 
    
    # 3. Convertir la respuesta a JSON (diccionario de Python)
    # Usamos .json() que es más directo que json.loads(response.text)
    datos = response.json()
    
    # 4. Mostrar los datos de forma ordenada
    print("\n" + "="*50)
    print("  \U0001F4E1 ¡Conexión Exitosa! \U0001F4E1")
    print("="*50)
    
    # Imprimir la cabecera (basado en el JSON de ejemplo)
    ancho_etiqueta = 20 # Para alinear la impresión
    print(f"{'Organismo':<{ancho_etiqueta}}: {datos.get('organismo')}")
    print(f"{'Producto':<{ancho_etiqueta}}: {datos.get('producto')}")
    print(f"{'Total Estaciones':<{ancho_etiqueta}}: {datos.get('estaciones')}")
    print(f"{'Fecha Creación':<{ancho_etiqueta}}: {datos.get('fechaCreacion')}")
    
    # Imprimir algunas estaciones para confirmar
    if 'datosEstacion' in datos and len(datos['datosEstacion']) > 0:
        print("\n--- Primeras 3 Estaciones Encontradas ---")
        
        # Usar un bucle para mostrar las primeras 3 (o menos si no hay 3)
        for estacion in datos['datosEstacion'][:10]:
            print("\n  ---------------------------------")
            print(f"  Nombre: {estacion.get('nombreEstacion')}")
            print(f"  Región: {estacion.get('NombreRegion')}")
            print(f"  Código: {estacion.get('codigoNacional')}")
            print(f"  Coords: {estacion.get('latitud')}, {estacion.get('longitud')}")
    
    else:
        print("\nRespuesta recibida, pero no se encontraron 'datosEstacion' en el JSON.")

# --- Manejo de Errores ---

except requests.exceptions.HTTPError as errh:
    print("\n" + "="*50)
    print("  \U0000274C ¡ERROR HTTP! \U0000274C")
    print(f"  Código de error: {errh.response.status_code}")
    if errh.response.status_code == 401 or errh.response.status_code == 403:
        print("  Mensaje: Acceso denegado. Revisa que tu EMAIL y TOKEN sean correctos.")
    else:
        print(f"  Mensaje: {errh}")
    print(f"  Respuesta del servidor: {errh.response.text}")

except requests.exceptions.ConnectionError as errc:
    print("\n" + "="*50)
    print("  \U0000274C ¡ERROR DE RED! \U0000274C")
    print("  No se pudo conectar. ¿Estás conectado a internet?")

except json.JSONDecodeError:
    print("\n" + "="*50)
    print("  \U0000274C ¡ERROR DE JSON! \U0000274C")
    print("  La respuesta no se pudo decodificar. No es un JSON válido.")
    print(f"  Respuesta recibida del servidor: {response.text}")

except Exception as err:
    print(f"\nUn error inesperado ocurrió: {err}")