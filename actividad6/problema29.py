import statistics

if __name__ == '__main__':
    entrada = input("Ingrese una serie de números separados por espacios: ")
    try:
        datos = list(map(float, entrada.split()))
        if not datos:
            print("No se ingresaron datos.")
        else:
            media = statistics.mean(datos)
            mediana = statistics.median(datos)
            try:
                moda = statistics.mode(datos)
            except statistics.StatisticsError:
                moda = "No hay moda única"
            desviacion = statistics.stdev(datos) if len(datos) > 1 else 0
            print(f"Media: {media:.2f}")
            print(f"Mediana: {mediana:.2f}")
            print(f"Moda: {moda}")
            print(f"Desviación Estándar: {desviacion:.2f}")
    except ValueError:
        print("Entrada no válida.")
