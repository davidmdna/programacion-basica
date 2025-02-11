# Problema 16: Contar el número de vocales y consonantes en una cadena

def contar_vocales_consonantes(cadena):
    cadena = cadena.lower()
    vocales = "aeiou"
    contador_vocales = 0
    contador_consonantes = 0
    for char in cadena:
        if char.isalpha():
            if char in vocales:
                contador_vocales += 1
            else:
                contador_consonantes += 1
    return contador_vocales, contador_consonantes

if __name__ == '__main__':
    entrada = input("Ingrese una cadena: ")
    vocales, consonantes = contar_vocales_consonantes(entrada)
    print(f"Número de vocales: {vocales}")
    print(f"Número de consonantes: {consonantes}")
