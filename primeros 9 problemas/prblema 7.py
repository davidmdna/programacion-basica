# Problema 7: Verificar si un número es par, impar y si es múltiplo de otro
def verificar_numero(num, divisor):
    if num % 2 == 0:
        print(f"{num} es par.")
    else:
        print(f"{num} es impar.")

    if divisor != 0:
        if num % divisor == 0:
            print(f"{num} es múltiplo de {divisor}.")
        else:
            print(f"{num} no es múltiplo de {divisor}.")
    else:
        print("El divisor no puede ser cero para la verificación de múltiplos.")

if __name__ == "__main__":
    try:
        numero = int(input("Ingrese un número: "))
        divisor = int(input("Ingrese otro número para verificar si es múltiplo: "))
        verificar_numero(numero, divisor)
    except ValueError:
        print("Entrada no válida.")
