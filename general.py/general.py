def resolver_ecuacion_cuadratica(a, b, c):
    if a == 0:
        print("Error: 'a' no puede ser 0. No es una ecuación cuadrática.")
        return
    
    discriminante = (b ** 2) - (4 * a * c)

    if discriminante > 0:
        x1 = (-b + (discriminante ** 0.5)) / (2 * a)
        x2 = (-b - (discriminante ** 0.5)) / (2 * a)
        print(f"Las soluciones son reales y diferentes:\n x1 = {x1}\n x2 = {x2}")

    elif discriminante == 0:
        x = -b / (2 * a)
        print(f"La ecuación tiene una única solución real:\n x = {x}")

    else:
        print("La ecuación no tiene soluciones reales.")

# Pedir coeficientes al usuario
try:
    a = float(input("Ingrese el coeficiente a: "))
    b = float(input("Ingrese el coeficiente b: "))
    c = float(input("Ingrese el coeficiente c: "))

    resolver_ecuacion_cuadratica(a, b, c)

except ValueError:
    print("Error: Ingresa valores numéricos válidos.")