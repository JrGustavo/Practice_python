# Orden de inicializacion de objetos

class Padre:
    def __init__(self):
        print('Inicializador Padre')
    def metodo(self):
        print('Metodo padre')

class Hijo(Padre):
    #Se manda a llamar el metodo __init__ de la clase padre
    # Siempre y cuando la clase hija no defina su propio metodo init


# Definimos el metodo init


def __init__(self):
    super().__init__()
    print('Inizializando hijo')

    #Socreescribimos el metodo heredado de la clase padre
    def metodo(self):
        print('Metodo sobreescrito hijo')

#padre1 = Padre()
#padre1.metodo()
