# Un closure es una funciòn que define a otra y ademas la regresa
# La funciòn anidada puede acceder a las variables locales definidas
# En la funciòn principal o externa

#Funciòn principal:

#def operacion(a, b):
# definimos una funciòn interna o anidada
#    def sumar():
 #       return a + b

# Retornar la funciòn
#    return sumar

#Funcion principal
def operacion(a,b):
    #1. Definimos una funciòn lambda interna o anidada y la retornamos
    return lambda: a  + b 

mi_funcion_closure = operacion(5, 2)
print(f'Resultado de la funciòn closure: {mi_funcion_closure()}')

#Llamar la funciòn regresada al vuelo
print(f'Resultado de la funciòn closure al vuelo: {operacion(2,3)()}')

