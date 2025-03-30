import random

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2]
    izquierda = [x for x in lista if x < pivote]
    centro = [x for x in lista if x == pivote]
    derecha = [x for x in lista if x > pivote]
    return quicksort(izquierda) + centro + quicksort(derecha)

def busqueda_binaria(lista, objetivo):
    inicio, fin = 0, len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

def mergesort(lista):
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izquierda = mergesort(lista[:medio])
    derecha = mergesort(lista[medio:])
    return merge(izquierda, derecha)

def merge(izquierda, derecha):
    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

# Generar lista de números aleatorios
numeros = [random.randint(1, 100) for _ in range(10)]
print("Lista original:", numeros)

# Ordenar la lista con Mergesort
numeros_ordenados = mergesort(numeros)
print("Lista ordenada:", numeros_ordenados)

# Buscar un número en la lista
num_buscar = int(input("Ingrese un número a buscar: "))
posicion = busqueda_binaria(numeros_ordenados, num_buscar)
if posicion != -1:
    print(f"Número {num_buscar} encontrado en la posición {posicion}.")
else:
    print(f"Número {num_buscar} no encontrado.")
