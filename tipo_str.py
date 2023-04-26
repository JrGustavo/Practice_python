#Profundizando en el tipo str

# Dar formato a un str

nombre = 'Juan'
edad = 28
sueldo = 3000
mensaje  = 'Nombre {} Edad {}   Sueldo {:.2f}'.format(nombre, edad, sueldo)


mensaje = 'Sueldo {2:.2f} Edad {1} Nombre {0}'.format(nombre, edad, sueldo)
print(mensaje)

mensaje = 'Nombre {n} Edad {e} Sueldo {s:.2f}'-format(n=nombre,e=edad,s=sueldo)