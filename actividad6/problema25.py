import random
import math
import matplotlib_pyplot as plt

def calcular_media(lista):
   return sum(lista) / len(lista)

def calcular_mediana(lista):
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    if n % 2 == 1:
        return lista_ordenada[n // 2]
    else:
        return (lista_ordenada[n // 2 - 1] + lista_ordenada[n // 2]) / 2

def calcular_desviacion(lista, media_valor):
    suma_cuadrados = sum((numero - media_valor) ** 2 for numero in lista)
    varianza = suma_cuadrados / len(lista)
    return math.sqrt(varianza)

def main():
    # Generar 1000 datos aleatorios con distribución normal (media=0, desviación=1)
    datos = [random.gauss(0, 1) for _ in range(1000)]
    
    # Calcular estadísticas básicas
    media_valor = calcular_media(datos)
    mediana_valor = calcular_mediana(datos)
    desviacion_valor = calcular_desviacion(datos, media_valor)
    
    print("Media:", media_valor)
    print("Mediana:", mediana_valor)
    print("Desviación Estándar:", desviacion_valor)
    
    # Crear el histograma
    plt.hist(datos, bins=30, edgecolor='black')
    plt.title("Histograma de Datos")
    plt.xlabel("Valor")
    plt.ylabel("Frecuencia")
    
    # Dibujar líneas para la media y la mediana
    plt.axvline(media_valor, color='red', linestyle='dashed', linewidth=1, label="Media")
    plt.axvline(mediana_valor, color='green', linestyle='dashed', linewidth=1, label="Mediana")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
