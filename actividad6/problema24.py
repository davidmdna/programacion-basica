def sumar_serie(numeros):
    return sum(numeros)

if __name__ == '__main__':
    entrada = input("Ingrese una serie de números separados por espacios: ")
    try:
        numeros = list(map(float, entrada.split()))
        suma = sumar_serie(numeros)
        print("La suma de la serie es:", suma)
    except ValueError:
        print("Entrada no válida.")
