#Funciones anidadas

def calculadora(a, b, operacion='sumar'):
    #1. Definir Funcion anidada
    def sumar(a, b):
        return a + b

    def restart(a , b):
        return a - b

    #2.llamamos a la funcion anidada
    if operacion == 'sumar':
        print(f'Resultado sumar:{sumar(a, b)}')
    elif operacion == 'restar':
        print(f'Resultado restar: {restart(a, b)}')

calculadora(5, 6)
calculadora(4, 3, operacion='restar')