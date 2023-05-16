#Generadores
# Es una funcion especial, retorna una secuencia de valores
# Suspende la ejecuciòn de la funciòn yield (producir) (no se usa return)
# suspende la ejecuciòn de la funciòn yield (producir) (no se usa return)

def generador():
    yield 1
    print('Se renauda la ejecución')
    yield 2
    print('Se renauda la ejecución')
    yield 3

# Consumimos el generador a demanda
gen = generador()
# Con cada llamada consumimos un valor
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# Si tratamos de consumir mas valores de los que produce el generador
# Lanza un error de StopIteracion
print(next(gen))

#consumiendo los valores del generador con un ciclo for
gen = generador()
#Con cada llamada consumimos un valor
print(next(gen))
print(next(gen))
print(next(gen))

