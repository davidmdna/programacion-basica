# Problema 3: Calcular el factorial de un número
def factorial(n):
    if n < 0:
        return None  # No se define factorial para números negativos.
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

if __name__ == "__main__":
    try:
        numero = int(input("Ingrese un número para calcular su factorial: "))
        fact = factorial(numero)
        if fact is not None:
            print(f"El factorial de {numero} es {fact}")
        else:
            print("El factorial no está definido para números negativos.")
    except ValueError:
        print("Entrada no válida.")
