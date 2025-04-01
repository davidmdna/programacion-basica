def contadorDeVocales(cadena):
    """
    Función que cuenta la cantidad de veces que aparece cada vocal en una cadena.
    Se incluyen vocales con tilde.
    """
    # Definir las vocales en un conjunto para una búsqueda eficiente
    vocales = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U', 'á', 'é', 'í', 'ó', 'ú', 'Á', 'É', 'Í', 'Ó', 'Ú'}
    
    # Inicializar diccionario vacío para almacenar el conteo de vocales
    conteo = {}
    
    # Recorrer cada carácter en la cadena
    for caracter in cadena:
        if caracter in vocales:
            conteo[caracter] = conteo.get(caracter, 0) + 1  # Incrementar el conteo
    
    return conteo

# Pruebas con las cadenas dadas
print(contadorDeVocales("murciélago"))  # {'u': 1, 'i': 1, 'é': 1, 'a': 1, 'o': 1}
print(contadorDeVocales("eucalipto"))   # {'e': 1, 'u': 1, 'a': 1, 'i': 1, 'o': 1}
print(contadorDeVocales("Albericoque")) # {'A': 1, 'e': 2, 'i': 1, 'o': 1, 'u': 1}