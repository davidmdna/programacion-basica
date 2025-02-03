# Problema 4: Generar la secuencia de Fibonacci
def fibonacci(n):
    secuencia = []
    a, b = 0, 1
    for _ in range(n):
        secuencia.append(a)
        a, b = b, a + b
    return secuencia

if __name__ == "__main__":
    try:
        n_terms = int(input("Ingrese el número de términos para la secuencia de Fibonacci: "))
        if n_terms <= 0:
            print("Ingrese un número positivo.")
        else:
            secuencia = fibonacci(n_terms)
            print("Secuencia de Fibonacci:", secuencia)
    except ValueError:
        print("Entrada no válida.")
