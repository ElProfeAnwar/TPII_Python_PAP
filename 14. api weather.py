import requests
api_key = "02b857cccf4531636da8438ef56fc770"
ciudad = "Madrid"
url =f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}"
respuesta = requests.get(url)
datos_clima = respuesta.json()
print(datos_clima)