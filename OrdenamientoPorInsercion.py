def Ordenamiento_insersion(lista):
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i-1
        while j >= 0 and actual < lista[j]:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = actual
    return lista

lista = [6, 5, 10, 3, 4, 9, 8]
Ordenamiento_insersion(lista)
print(lista)