numeros = range(10)
lista_pares = []

# Creamos una nueva lista con los valores pares

for numero in numeros:
    #Revisamos si es un numero par
    if numero % 2 == 0:
        lista_pares.append(numero)

print(f'Lista Pares: {lista_pares}')

# Hacemos lo mismo per¡o list comprehensions
# [expresion for var in colecciòn if condicional]
# La condicion de if es opcional

lista_pares = []
lista_pares = [numero*numero for numero in numeros if numero %2 ==0]
print(f'Lista Pares con list comprehensions: {lista_pares}')

# Un ejemplo simila con dos condiciones ( Las condiciones son opcionales)
# Solo se agrega el valor a la lista cuando el valor cumple ambas condiciones
# es decir, debe ser divisible entre 2 y divisible entre 6
pares = [numero for numero in range(50) if numero% 2==0 if numero%6==0 ]
print(f'Lista divisible entre 2 y 6: {pares}')

# Agregando if else
lista_apres = []
lista_impares = []
for numero in range(10):
    if numero%2==0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)
print(f'Pares: {lista_pares}')
print(f'Impares: {lista_impares}')

# El mismo ejercicio usando List comprehension
lista_pares = []
lista_impares = []
[lista_pares.append(numero) if numero%2==0 else lista_impares.append(numero)
    for numero in range(10)]
print(f'Pares: {lista_pares}')
print(f'Impares: {lista_impares}')