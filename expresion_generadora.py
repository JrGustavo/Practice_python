# Expresion generadora (Es un generador anonimo)

multiplicacion  = (valor*valor for valor in range(4) )
print(type(multiplicacion))
print(next(multiplicacion))
# print(next(multiplicacion))

# Tambien se puede pasar una expresiòn generadora a una funciòn (sin parentesis)

import math
suma = sum(valor*valor for valor in range(4))
print(f'Resultado suma: {suma}')

#Tambien podemos usar una lista o cualquier otro iterador
lista = ['Juan', 'Perez']
generador = ( valor for valor in lista)
print(next(generador))
print(next(generador))

# Crear un string a partir de una genrador creado a partir de una lista

lista = ['Karla', 'Gomez']
contador = 0

# Definimos una funciòn para incrementar el contador
 def incrementar():
     global contador
     contador +1
     return contador
# La primera para es el yield, la segunda es el for, entre parentesis
generador = (f'{incrementar()}. {nombre}' for nombre in lista)
lista = list(generador)
print(lista)
cadena = ', '.join(lista)
print(f'Cadena generada: {cadena}')





