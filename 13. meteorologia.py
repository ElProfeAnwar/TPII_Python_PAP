import requests
import json

email='elprofeanwar@gmail.com'
token='64d712ed9135b616faa7c68b'

#estaciones con datos GEO
datos=requests.get(f"https://climatologia.meteochile.gob.cl/application/geoservicios/getCatastroEstacionesGeo?usuario={email}&token={token}")
print (datos.headers)
print (datos)



