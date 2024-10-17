import requests
import json

email='elprofeanwar@gmail.com'
token='a77a113a83f50882ea15d6cf'

#estaciones con datos GEO
datos=requests.get(f"https://climatologia.meteochile.gob.cl/application/geoservicios/getCatastroEstacionesGeo?usuario={email}&token={token}")
print (datos.headers)
print (datos)


