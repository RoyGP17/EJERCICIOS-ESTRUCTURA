def merge_sort(lista):
    if len(lista) <= 1:
        return lista

    mitad = len(lista) // 2
    izquierda = lista[:mitad]
    derecha = lista[mitad:]

    izquierda = merge_sort(izquierda)
    derecha = merge_sort(derecha)

    resultado = []
    i, j = 0, 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado += izquierda[i:]
    resultado += derecha[j:]

    return resultado
