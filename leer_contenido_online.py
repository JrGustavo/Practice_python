# Leer contenido online

from urllib2 import urlopen

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
print(mensaje.lower().islower())
print(mensaje.upper().isupper())


#Eliminar caracteres al inicio y final de un str - strip
 titulo = ' *** GlobalMentoring.com.mx***'
 print('Cadena original:', titulo, len(titulo))
 titulo = titulo.strip()
 print('Cadena modificada:',titulo,len(titulo))
 titulo = '***GlobalMentoring.com.mx***'.strip('*')
 print('Cadena modificada:', titulo)
 titulo = '***GlobalMentoring.com.mx***'.lstrip('*')
 print('Cadena modificada:', titulo)

 titulo = ' ***GlobalMentroing.com.mx ***'.strip().strip('*').strip()
