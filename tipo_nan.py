import math
from decimal import Decimal

# Nan - Not a number (No es un numero)
# Nan no es sensible a mayusculas/minusculas
#Nan es un tipo de dato numerico indefinitivo

a = float('Nan')
print(f'a:{a}')
print(f' Es NaN (noy a number?: {math.isnan(a)}')

a = Decimal('NaN')
print(f'a: {a}')
print(f'Es NaN (not a number)?: {math.isnan(a)}')

