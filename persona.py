class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

if __name__ == '__main__':
    persona1 = Persona('Juan', 'Perez')
    print(persona1)

def mostrar_mensaje(mensaje):
    print(mensaje)
