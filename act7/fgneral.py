import cmath

def calcular_raices(a, b, c):
    """
    Calcula las raíces de una ecuación cuadrática ax^2 + bx + c = 0
    Devuelve dos raíces que pueden ser reales o complejas.
    """
    # Calcular el discriminante
    discriminante = b**2 - 4*a*c
    
    # Evaluar el discriminante
    if discriminante > 0:
        # Dos raíces reales distintas
        x1 = (-b + discriminante**0.5) / (2 * a)
        x2 = (-b - discriminante**0.5) / (2 * a)
        return f"Dos raíces reales: x1 = {x1}, x2 = {x2}"
    elif discriminante == 0:
        # Una única raíz real (doble)
        x = -b / (2 * a)
        return f"Una raíz real doble: x = {x}"
    else:
        # Dos raíces complejas
        x1 = (-b + cmath.sqrt(discriminante)) / (2 * a)
        x2 = (-b - cmath.sqrt(discriminante)) / (2 * a)
        return f"Dos raíces complejas: x1 = {x1}, x2 = {x2}"

# Pruebas con diferentes valores de a, b y c
print(calcular_raices(1, -3, 2))   # Discriminante > 0 → Dos raíces reales
print(calcular_raices(1, -2, 1))   # Discriminante = 0 → Una raíz real doble
print(calcular_raices(1, 2, 5))    # Discriminante < 0 → Dos raíces complejas
