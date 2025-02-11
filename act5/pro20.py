# Problema 20: Implementar búsqueda binaria y lineal

def busqueda_lineal(lista, objetivo):
    for indice, elemento in enumerate(lista):
        if elemento == objetivo:
            return indice
    return -1

def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

if __name__ == '__main__':
    # Ejemplo de uso con una lista ordenada
    lista = [1, 3, 5, 7, 9, 11, 13]
    try:
        objetivo = int(input("Ingrese el número a buscar: "))
    except ValueError:
        print("Entrada no válida.")
        exit()
    
    indice_lineal = busqueda_lineal(lista, objetivo)
    if indice_lineal != -1:
        print(f"Búsqueda lineal: {objetivo} encontrado en el índice {indice_lineal}")
    else:
        print(f"Búsqueda lineal: {objetivo} no encontrado en la lista")
    
    indice_binaria = busqueda_binaria(lista, objetivo)
    if indice_binaria != -1:
        print(f"Búsqueda binaria: {objetivo} encontrado en el índice {indice_binaria}")
    else:
        print(f"Búsqueda binaria: {objetivo} no encontrado en la lista")
