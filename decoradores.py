#Decoradores
#Un decorador es una funciòn que recibe una funciòn y regresa otra
# Lo utilizamos para extender funcionalidad
# 1. Funciòn decorador (a)
# 2. funciòn a decorar (b)
# 3. Funciòn decorada (c)

def funcion_decorador_a(funcion_a_decorar_b):
    def funcion_decorada_c(*args, **kwargs):
        print('Antes de ejecutar la funciòn ')
        resultado = funcion_a_decorar_b(*args, **kwargs)
        print('Despues de ejecutar la funciòn')
        return resultado

    return funcion_decorada_c

#Definimos una funciòn y vamos a extender su funcionalidad con su decorador
@funcion_decorador_a
def sumar(a,b):
    return a + b

resultado = sumar(5, 6)
print(f'resultado suma: {resultado}')

