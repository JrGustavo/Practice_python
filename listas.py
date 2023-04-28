#Prfundizando listas
#Listas son mutables

nombres1 = ['Juan', 'Karla', 'Pedro']
nombres2 = 'Laura maria junior medinda'.split()
#Sumar Listas
print(f'Sumar listas {nombres1 + nombres2}')

nombres1.extend( nombres2)
print(f'Extender la lista 1  con la lista2: {nombres1}')

#Lista de numeros
numeros1 = [10, 40, 15, 4, 20, 90]
#Obtener el indice del primer elemento encontrado en una lista

print(f'Indice 4: {numeros1.index(4)}')

#Ordenar los elementos de una lista
numeros1.sort()
print(f'Lista ordenada (descendente): {numeros1}')
#Ordenar de manera descendente una lista
numeros1.sort(reverse=True)
print(f'Lista ordenada (ascendente): {numeros1}')

#Obtener el valormin y max de una lista
print(f' valor maximo: {max(numeros1)}')

#Xopiar los elementos de una lista
numeros1.copy()
#help(list.copy)
print(f'Misma referencia? {numeros1 is numeros2}')
print(f'Mismo contenido?')