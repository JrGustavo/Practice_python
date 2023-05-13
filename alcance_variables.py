#Alcance de variables (scope)

var_global = 'Variable global'

def imprimir():
    #Acceder a una variable global
    global var_global
    print(f'Variable global desde funcion: {var_global}')
    #Definicion de variable local
    var_local = 'Variables local'
    print(f'Variable local desde función: {var_local}')
    var_global = 'Nuevo valor de la variable global'


    def funcion_anidada():
        print(f'Variable local dentro funcion anidada: {var_local}')
    funcion_anidada()

imprimir()
print(f'Var global fuera funciòn: {var_global}')
#No es posible acceder a variables locales fuera

#print(f'Var local fuera funciòn: {var_local}')