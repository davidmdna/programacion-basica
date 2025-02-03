# Problema 8: Calcular el área y la circunferencia de un círculo
import math

def calcular_circulo(radio):
    area = math.pi * radio ** 2
    circunferencia = 2 * math.pi * radio
    return area, circunferencia

if __name__ == "__main__":
    try:
        radio = float(input("Ingrese el radio del círculo: "))
        if radio < 0:
            print("El radio no puede ser negativo.")
        else:
            area, circunferencia = calcular_circulo(radio)
            print(f"Área del círculo: {area:.2f}")
            print(f"Circunferencia del círculo: {circunferencia:.2f}")
    except ValueError:
        print("Entrada no válida.")
