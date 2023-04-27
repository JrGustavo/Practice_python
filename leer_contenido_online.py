# Leer contenido online

from urllib.request import urlopen

palabras = []

with urlopen('http://globalmentoring.com.mx/recursos/GlobalMentoring.txt') as mensaje:
    contenido = mensaje.read().decode('utf-8')


print('No. veces Universidad: ', contenido.count('Universidad'))

print(contenido.upper())
print(contenido)

print(contenido.lower())

print('Existe python?: ','python'.lower() in contenido.lower())
print('Existe python?: ','python'.lower() in contenido.upper())

mensaje = 'Hola Mundo'
