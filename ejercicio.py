print("Hola prueba")

#burbuja
numb = [2, 6, 3, 1, 9, 8]

def bubbleSort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            print(lista[j], "con", lista[j + 1])
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

bubbleSort(numb)

print(numb)


#insercion
def insertionSort(lista):
    for i in range(1, len(lista)):
        actual = lista[i]
        j = i-1
        while j >= 0 and actual < lista[j]:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = actual
    return lista

list = [5, 4, 9, 2, 3, 8, 7]
insertionSort(list)
print(list)

#quicksort
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    debajo = [x for x in arr if x < pivot]
    medio = [x for x in arr if x == pivot]
    encima = [x for x in arr if x > pivot]
    return quickSort(debajo) + medio + quickSort(encima)

list = [3, 6, 8, 10, 1, 2, 1, 0, -2]
print("Lista original: ", list)
print("Lista ordenado: ", quickSort(list))

#mergesort
def mergeSort(lista):
    if len(lista) > 1:
        mid = len(lista)//2
        izquierda = lista[:mid]
        derecha = lista[mid:]

        mergeSort(izquierda)
        mergeSort(derecha)

        i = j = k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            k += 1

        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

    return lista

list = [14, 25, 30, 12, 7, 2, 41, 62, 54, 23, 11, 0, -2, 33, 28, 6]
mergeSort(list)
print(list)

#Seleccion
list = [4,2,3,1,7,5]

def selectionSort(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

selectionSort(list)
print(list)

