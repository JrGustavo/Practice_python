class Clase1:
    def __init__(self):
        print('Clase1.__init__')
        super().__init__()

    def metodo(self):
        print('Metodo clase1')
        super().metodo()

class Clase2(Clase1):
    def __init__(self):
        print('Clase2.__init__')
        super().__init__()

    def metodo(self):
        print('Metodo clase2')
        super().metodo()


class Clase3(Clase1):
    def __init__(self):
        print('Clase3.__init__')
        super().__init__()

    def metodo(self):
        print('Metodo clase3')

class Clase4(Clase2,Clase3):
    def metodo(self):
        print('Metodo clase4')
        super().metodo()

#Creamos objeto clase4
clase4 = Clase4()
# __bases__
print(Clase4.__bases__)
#mro
print(Clase4.__mro__)
#Cual metodo se ejecuta
