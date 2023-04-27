#Profundizando en el tipo str

# Caracteres byte
carateres_en_bytes = b'Hola Mundo'
print(carateres_en_bytes)

mensaje = b'Universidad Python'
print(mensaje[1])
print(chr(mensaje[1]))

lista_caracteres = mensaje.split()
print(lista_caracteres)

#Convertir str a bytes
string = 'Programacion con Python'
print('string original:', string)
bytes = string.encode('UTF-8')
print('bytes codificado: ', bytes)

string2 = bytes.decode('UTF-8')
print('string decodificando:', string2)
print(string == string2)

