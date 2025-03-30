def analizar_texto(texto):
    # Convertir a minúsculas y eliminar puntuaciones
    import string
    texto = texto.lower().translate(str.maketrans('', '', string.punctuation))
    
    # Dividir en palabras
    palabras = texto.split()
    
    # Número total de palabras
    total_palabras = len(palabras)
    
    # Palabras únicas
    palabras_unicas = set(palabras)
    cantidad_unicas = len(palabras_unicas)
    
    # Frecuencia de palabras
    frecuencia_palabras = {}
    for palabra in palabras:
        frecuencia_palabras[palabra] = frecuencia_palabras.get(palabra, 0) + 1
    
    # Palabra más frecuente
    palabra_mas_frecuente = max(frecuencia_palabras, key=frecuencia_palabras.get)
    frecuencia_maxima = frecuencia_palabras[palabra_mas_frecuente]
    
    # Resultados
    print(f"Número total de palabras: {total_palabras}")
    print(f"Cantidad de palabras únicas: {cantidad_unicas}")
    print("Frecuencia de palabras:")
    for palabra, frecuencia in frecuencia_palabras.items():
        print(f"{palabra}: {frecuencia}")
    print(f"La palabra más frecuente es '{palabra_mas_frecuente}' con {frecuencia_maxima} apariciones.")

# Solicitar entrada del usuario
texto_usuario = input("Ingrese un texto: ")
analizar_texto(texto_usuario)
