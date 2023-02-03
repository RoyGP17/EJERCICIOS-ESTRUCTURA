def Ordenamiento_rapido(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    debajo = [x for x in arr if x < pivot]
    medio = [x for x in arr if x == pivot]
    encima = [x for x in arr if x > pivot]
    return Ordenamiento_rapido(debajo) + medio + Ordenamiento_rapido(encima)

list = [3, 6, 8, 10, 1, 2, 1, 0, -2]
print("Lista original: ", list)
print("Lista ordenado: ", Ordenamiento_rapido(list))