# Problema 9: Generar listas de números pares e impares hasta un límite dado
def generar_listas(limite):
    pares = [n for n in range(0, limite + 1) if n % 2 == 0]
    impares = [n for n in range(0, limite + 1) if n % 2 != 0]
    return pares, impares

if __name__ == "__main__":
    try:
        limite = int(input("Ingrese el límite: "))
        pares, impares = generar_listas(limite)
        print("Números pares:", pares)
        print("Números impares:", impares)
    except ValueError:
        print("Entrada no válida.")
