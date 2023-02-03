def OrdenamientoPorMezcla(lista):
    if len(lista) > 1:
        mid = len(lista)//2
        izquierda = lista[:mid]
        derecha = lista[mid:]

        OrdenamientoPorMezcla(izquierda)
        OrdenamientoPorMezcla(derecha)

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
OrdenamientoPorMezcla(list)
print(list)