# Profundizar en set
# Un  set es una colecciòn de elementos unicos y mutables
# Los elementos de un set deben ser inmutables

conjunto = { 'Juan', True, 19.0}
print(conjunto)
#Set vacio
conjunto = {}
print(type(conjunto))
conjunto = set()
print(conjunto)
print(type(conjunto))
#Mutable
conjunto.add('Juan ')
print(conjunto)
conjunto.add('Juan')
print(conjunto)
#Crear un set a partir de un iterable

conjunto = set([4,5,6,7])
print(conjunto)

# Podemos agregar mas elementos o incluso otro set
conjunto2 = {100, 200, 300, 300}
conjunto.update(conjunto2)
print(conjunto)
conjunto.update([20,30,40,50])
print(conjunto)

# Copiar un setr (copia poco profunda, solo copia referencias
conjunto_copia = conjunto.copy()
print(conjunto_copia)
#Verificar igualdad

print(f'Es igual en contenido? {conjunto == conjunto_copia}')
print(f' Es la misma referencia? {conjunto is conjunto_copia}')

#Operaciones de conjuntos con set
# Personas con distintas caracteristicas

pelo_negro = {'Juan', 'Karla', 'Pedro', 'Maria'}
ojos_cafe = {'Karla', 'Laura'}
pelo_rubio = { 'Lorenzo', 'Laura', 'Marco'}
menores_30 = { 'Juan', 'Karla', 'Maria'}

#Todos con ojos_cafe  y pelo rubio (union) (no se repiten los elementos)
print(ojos_cafe.union(pelo_rubio))

print(pelo_rubio.union(pelo_rubio))

print(pelo_rubio.union(ojos_cafe))

#(Intersection)  Solo las personas con ojos cafe y pelo rubio
print(ojos_cafe.intersection(pelo_rubio))

#(difference) pelo negro sin ojos cafe

print(pelo_negro.difference(ojos_cafe))

#diferencia simetrica)
print(pelo_negro.symmetric_difference(ojos_cafe))

#Pregunar si un set esta contenido en otro (subset)
#Revisemos si los elem,entos del primer set estan contendidos en el segundo set

print(menores_30.issubset(pelo_negro))

print(menores_30.issubset(pelo_negro))






