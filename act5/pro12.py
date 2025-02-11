# Problema 12: Encontrar el mayor entre tres números

def mayor_de_tres(a, b, c):
    return max(a, b, c)

if __name__ == '__main__':
    try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        c = float(input("Ingrese el tercer número: "))
        mayor = mayor_de_tres(a, b, c)
        print(f"El mayor de los tres números es: {mayor}")
    except ValueError:
        print("Entrada no válida.")
