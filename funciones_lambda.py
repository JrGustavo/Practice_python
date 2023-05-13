#Funciones lambda
#Son funciones anonimas, y son pequeñas (una linea de codigo)

# Con una funciòn lambda(anonima, sin nombre, y una sola linea de codigo
# No se necesita agregar parentesis para los parametros
# No se necesita usar la palabra return, perso si debe regresar una expresiòn

mi_funcion_lambda = lambda a, b: a + b

resultado = mi_funcion_lambda(4,6)
print(f'Resultado sumar funciòn lambda: {resultado}')

#Funciòn lambda que nor ecibe argumentos (debemos regresar una expresiòn validar)

mi_funcion_lambda = lambda: 'Funciòn sin argumentos '
print(f'Llamar funciòn lambda sin argumentos: {mi_funcion_lambda()}')

#Funciòn lambda con parametros por default
mi_funcion_lambda = lambda a=2, b=3:  a + b
print(f'Resultado argumentos por default: {mi_funcion_lambda(4, 6)}')

#Funcion lambda con argumentos variables *args y **kwargs
mi_funcion_lambda
funcion_lambda = lambda *args, **kwargs: len((args) + len(kwargs))
print(f'Resultado argumentos variables: {mi_funcion_lambda(1,2,3, a=5, b=6)}')

#Funciones lambda con argumentos, argumentos variables y valores por default
mi_funcion_lambda = lambda a, b, c=3,*args, **kwargs: a+b+c+len+(args)+len(kwargs)
print(f'Resultado funciòn lambda: {mi_funcion_lambda(1,2,4,5,6,7,8,9, e=5, f=7)}')

