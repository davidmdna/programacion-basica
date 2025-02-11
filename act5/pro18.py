# Problema 18: Resolver ecuaciones cuadráticas

import math
import cmath

def resolver_ecuacion_cuadratica(a, b, c):
    if a == 0:
        return None, "No es una ecuación cuadrática."
    discriminante = b**2 - 4*a*c
    if discriminante >= 0:
        raiz_disc = math.sqrt(discriminante)
    else:
        raiz_disc = cmath.sqrt(discriminante)
    x1 = (-b + raiz_disc) / (2*a)
    x2 = (-b - raiz_disc) / (2*a)
    return x1, x2

if __name__ == '__main__':
    try:
        a = float(input("Ingrese el coeficiente a: "))
        b = float(input("Ingrese el coeficiente b: "))
        c = float(input("Ingrese el coeficiente c: "))
        resultado = resolver_ecuacion_cuadratica(a, b, c)
        if resultado[0] is None:
            print(resultado[1])
        else:
            x1, x2 = resultado
            print("Las soluciones son:")
            print("x1 =", x1)
            print("x2 =", x2)
    except ValueError:
        print("Entrada no válida.")
