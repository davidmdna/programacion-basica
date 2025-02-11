# Problema 11: Verificar si una cadena es un palíndromo

def es_palindromo(cadena):
    # Se eliminan espacios y signos de puntuación, y se pasa a minúsculas
    cadena_limpia = ''.join(c for c in cadena if c.isalnum()).lower()
    return cadena_limpia == cadena_limpia[::-1]

if __name__ == '__main__':
    entrada = input("Ingrese una cadena para verificar si es palíndromo: ")
    if es_palindromo(entrada):
        print("La cadena es un palíndromo.")
    else:
        print("La cadena no es un palíndromo.")
