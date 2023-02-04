def hash(unaCadena, tamanoTabla):
    suma = 0
    for pos in range(len(unaCadena)):
        suma = suma + ord(unaCadena[pos])

    return suma%tamanoTabla

print("Hola")
