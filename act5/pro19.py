# Problema 19: Generar números aleatorios con distintas distribuciones

import random

def generar_aleatorios_uniforme(n, inicio, fin):
    return [random.uniform(inicio, fin) for _ in range(n)]

def generar_aleatorios_normal(n, media, desviacion):
    return [random.gauss(media, desviacion) for _ in range(n)]

def generar_aleatorios_exponencial(n, lambd):
    return [random.expovariate(lambd) for _ in range(n)]

if __name__ == '__main__':
    try:
        n = int(input("Ingrese la cantidad de números a generar: "))
        print("Distribución uniforme (entre 0 y 10):", generar_aleatorios_uniforme(n, 0, 10))
        print("Distribución normal (media=0, desviación=1):", generar_aleatorios_normal(n, 0, 1))
        print("Distribución exponencial (lambda=1):", generar_aleatorios_exponencial(n, 1))
    except ValueError:
        print("Entrada no válida.")
