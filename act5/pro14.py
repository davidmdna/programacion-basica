# Problema 14: Implementar distintos métodos de ordenamiento

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

def insertion_sort(lista):
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1
        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key
    return lista

if __name__ == '__main__':
    import random
    # Generar una lista aleatoria de números
    lista = [random.randint(1, 100) for _ in range(10)]
    print("Lista original:", lista)
    print("Ordenada con bubble sort:", bubble_sort(lista.copy()))
    print("Ordenada con selection sort:", selection_sort(lista.copy()))
    print("Ordenada con insertion sort:", insertion_sort(lista.copy()))
