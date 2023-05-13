#Las funciones en Python son ciudadanas de primera clase
# First class Citizens

# Definimos la funciòn

def sumar (a , b):
    return a + b

#1. Asignar una funciòn a una variable (no se usan parentesis)
mi_funcion = sumar

# Verificar el tipo de variablle
print(type(mi_funcion))

# Lllamos la funciòn a traves de la variable
resultado = mi_funcion(5,8)
print(f'Resultado: {resultado}')

#2. Funciòn como argumento
def operacion(a, b, sumar_arg):
    print(f'REsultado sumar: {sumar_arg(a,b)}')

operacion(4, 5, sumar)

# 3. Podemos retornar una funciòn
def retornar_funcion():
    # Retornamos una funciòn
    return sumar

mi_funcion_retorna = retornar_funcion()
print(f'Resultado funciòn retornada: {mi_funcion_retorna(5,7)}')