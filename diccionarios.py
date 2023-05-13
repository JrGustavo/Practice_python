#Profundizando en diccionarios

#Los diccionarios guardan un orden a diferencia de un set

diccionario = {'Nombre': 'Juan', 'Apellido': 'Perez', 'Edad': 28}
print(diccionario)

#los dic son mutables, pero las llaves deben ser inmutables
#Diccionario = {[1,2]:'Valor1' }
diccionario =  {(1,2): 'Valor1'}
print(diccionario)

# Se agrega una llave si no se encuentra
diccionario['Departamento'] = 'Sistemas'
print(diccionario)

# No hay valores duplicados en las llaves de un diccionario
diccionario['Nombre'] = 'Juan Carlos'
print(diccionario)

# REcuperar un valor indicandon una llave
print(diccionario['Nombre'])

#Si no encuentra la llave lanza una excepcion
#print(diccionario['Nombre'])

# MEtodo get recupera una llave, y si no existe no lanza excepcion
print(diccionario.get('Nombre', 'No se encontro la llave'))
print(diccionario)

#setdefault si modifica el diccionario, ademas de agregar un valor por default
nombre = diccionario.setdefault('Nombre', 'Valor por default')
print(nombre)
print(diccionario)

# Impmir con pprint
from pprint import pprint as pp
#help(pp)
pp(diccionario, sort_dicts=False)

