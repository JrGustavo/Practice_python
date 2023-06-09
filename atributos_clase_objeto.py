class Persona:
    contador_personas = 0

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

# Mostrar los atributos de un objeto
persona1 = Persona('Juan', 'Perez')
print(persona1.__dict__)

# Crear un atributo al vuelo
print(persona1.contador_personas)
persona1.contador_personas = 10
print(persona1.__dict__)
# El atributo anterior oculta al atributo de clase
print(Persona.contador_personas) #Atributo clase
print(persona1.contador_personas) #Atributo del objeto 1

# un segundo objeto

persona2 = Persona('Karla',  'Gomez')
print(persona2.__dict__)
print(persona2.contador_personas)

# Asociar un atributo de clase al vuelo
Persona.contador2 = 20
print(Persona.contador2)


