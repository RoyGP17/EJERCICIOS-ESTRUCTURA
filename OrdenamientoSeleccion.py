list = [4,2,3,1,7,5]

def Ordenamiento_Por_Seleccion(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

Ordenamiento_Por_Seleccion(list)
print(list)



