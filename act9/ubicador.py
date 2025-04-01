def ubicadorDeVocales(cadena):
    # Definir las vocales, incluyendo acentuadas
    vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"
    # Inicializar diccionario vacío
    ubicaciones = {}
    
    # Recorrer la cadena con índice
    for i, caracter in enumerate(cadena):
        if caracter in vocales:
            if caracter not in ubicaciones:
                ubicaciones[caracter] = []  # Inicializar lista si no existe
            ubicaciones[caracter].append(i)  # Agregar índice
    
    return ubicaciones

# Pruebas con las cadenas dadas
print(ubicadorDeVocales("murcielago"))  # {'u': [1], 'i': [3], 'e': [5], 'a': [7], 'o': [9]}
print(ubicadorDeVocales("eucalipto"))   # {'e': [0], 'u': [1], 'a': [3], 'i': [5], 'o': [8]}
print(ubicadorDeVocales("Albericoque")) # {'A': [0], 'e': [3, 10], 'i': [6], 'o': [8], 'u': [9]}
