# Problema 10: Leer, escribir y modificar un archivo de texto

def escribir_archivo(nombre, contenido):
    with open(nombre, 'w', encoding='utf-8') as f:
        f.write(contenido)

def leer_archivo(nombre):
    with open(nombre, 'r', encoding='utf-8') as f:
        return f.read()

def modificar_archivo(nombre, buscar, reemplazar):
    contenido = leer_archivo(nombre)
    contenido_modificado = contenido.replace(buscar, reemplazar)
    escribir_archivo(nombre, contenido_modificado)

if __name__ == '__main__':
    archivo = 'ejemplo.txt'
    # Escribir contenido inicial
    contenido_inicial = "Hola, mundo\nEste es un archivo de texto."
    escribir_archivo(archivo, contenido_inicial)
    print("Contenido inicial:")
    print(leer_archivo(archivo))
    
    # Modificar el archivo: se reemplaza 'mundo' por 'Python'
    modificar_archivo(archivo, "mundo", "Python")
    print("\nContenido modificado:")
    print(leer_archivo(archivo))
