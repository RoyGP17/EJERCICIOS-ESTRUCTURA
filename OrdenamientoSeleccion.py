def Ordenamiento_Por_Seleccion(list):

    for i in range(len(list)-1,0,-1):
        min_idx = 0
        for j in range(1, i+1):
            if list[j] > list[min_idx]:
                min_idx = j
        list[i], list[min_idx] = list[min_idx], list[i]
    return list

lista = [4,2,3,1,7,5]
Ordenamiento_Por_Seleccion(lista)
print(lista)
