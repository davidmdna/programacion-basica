import statistics

def calcular_estadisticas(*args):
    if not args:
        print("No se ingresaron números.")
        return None
    
    promedio = lambda nums: sum(nums) / len(nums)
    mediana = statistics.median(args)
    desviacion_estandar = statistics.stdev(args) if len(args) > 1 else 0
    
    return {
        "Promedio": promedio(args),
        "Mediana": mediana,
        "Desviación Estándar": desviacion_estandar
    }

# Solicitar entrada del usuario
numeros = list(map(float, input("Ingrese una lista de números separados por espacios: ").split()))
resultado = calcular_estadisticas(*numeros)

if resultado:
    for clave, valor in resultado.items():
        print(f"{clave}: {valor}")
