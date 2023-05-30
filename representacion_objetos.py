# Representacion de objetos ( str, repr, format)
# print(dir(object))

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    # repr, mas enfocado a los programadores
    def __repr__(self):
        return {self.__class__.__name__ }, self.apellido



    # Str es mas para el usuario final u otros sistemas
    # La implementación por default llama al metodo repr

    def __str__(self):
        return f'{self.__class__.name__}:{self.nombre} {self.apellido}'

    # format su implementacion por default es str
    def __format__(self, format_spec):
        return f'{self.__class__.__name__} con nombre {self.nombre}'



persona1 = Persona('Juan', 'Perez')
#Repre
print(f'Mi objeto persona1: {persona1!r}')
#str (de manera automatica el metodo print llsms al metodo str)
print(persona1)
#format
print(f'{persona1}')