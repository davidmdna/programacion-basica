# Problema 13: Convertir una temperatura entre distintas escalas

def convertir_temperatura(valor, origen, destino):
    origen = origen.lower()
    destino = destino.lower()
    
    # Convertir la temperatura a Celsius primero
    if origen == "c":
        celsius = valor
    elif origen == "f":
        celsius = (valor - 32) * 5/9
    elif origen == "k":
        celsius = valor - 273.15
    else:
        return None

    # Convertir de Celsius a la escala destino
    if destino == "c":
        return celsius
    elif destino == "f":
        return (celsius * 9/5) + 32
    elif destino == "k":
        return celsius + 273.15
    else:
        return None

if __name__ == '__main__':
    try:
        valor = float(input("Ingrese el valor de la temperatura: "))
        origen = input("Ingrese la escala de origen (C, F, K): ")
        destino = input("Ingrese la escala de destino (C, F, K): ")
        resultado = convertir_temperatura(valor, origen, destino)
        if resultado is not None:
            print(f"{valor}°{origen.upper()} equivale a {resultado:.2f}°{destino.upper()}")
        else:
            print("Escala no reconocida.")
    except ValueError:
        print("Entrada no válida.")
