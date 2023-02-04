def merge_sort(lista):
    print(lista)
    if len(lista) <= 1:
        return lista

    mitad = len(lista) // 2
    izquierda = lista[:mitad]
    derecha = lista[mitad:]
    izquierda = merge_sort(izquierda)
    derecha = merge_sort(derecha)
    resultado = []
    i, j = 0, 0
    print(lista)


    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
            print(resultado)
        else:
            resultado.append(derecha[j])
            j += 1
            print(resultado)
    resultado += izquierda[i:]
    resultado += derecha[j:]
    print(resultado)
    return resultado

merge_sort([54,26,93,17,77,31,44,55,20])


