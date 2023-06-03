from dataclasses import dataclass
from typing import ClassVar

@dataclass (eq=True, frozen=)
class Persona:
    nombre: str
    apellido: str
    contador_personas: ClassVar[int] = 0

    def __post_init__(self):
        if not self.nombre:
            raise ValueError(f'Valor nombre vacio: ')



persona1 = Persona('Juan', 'Perez')
print(f'{persona1}!r')
# Variable de clase
print(f'Variable clase: {Persona.contador_personas}')
#Variables de instancia
print(f'Variables de instancia: {persona1.__dict__ }')
persona_vacia = Persona(nombre= 'Karla', apellido='')
print(f'Persona vacia:  {persona_vacia}')
#REvisar igualdad entre objetos
persona2 = Persona('Juan', 'Perez')
print(f'Objetos iguales?: {persona1 == persona2}')
#Agregar esta clase a una colecciòn
coleccion = {persona1, persona2}