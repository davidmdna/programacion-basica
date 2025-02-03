# Problema 6: Cálculo de interés compuesto
def interes_compuesto(capital, tasa, tiempo):
    # Fórmula: M = C * (1 + r)^t
    monto = capital * ((1 + tasa) ** tiempo)
    return monto

if __name__ == "__main__":
    try:
        capital = float(input("Ingrese el capital inicial: "))
        tasa = float(input("Ingrese la tasa de interés (en formato decimal, ej: 0.05 para 5%): "))
        tiempo = float(input("Ingrese el tiempo (en años): "))
        monto_final = interes_compuesto(capital, tasa, tiempo)
        print(f"El monto final después de {tiempo} años es: {monto_final:.2f}")
    except ValueError:
        print("Entrada no válida.")

