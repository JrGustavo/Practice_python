# Leer archivo json
# JSON = JavaScript Object Notation
import urllib.request

respuesta = urllib.request.urlopen('https://globalmentoring.com.mx/api/personas.json')
print(respuesta)
