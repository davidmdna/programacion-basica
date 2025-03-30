# Ejemplo de implementación de múltiples paradigmas en Python

# Paradigma Imperativo
print("--- Paradigma Imperativo ---")
numeros = [1, 2, 3, 4, 5]
suma = 0
for num in numeros:
    suma += num
print(f"Suma de la lista: {suma}")

# Paradigma Estructurado (Funciones bien definidas)
def calcular_suma(lista):
    """Calcula la suma de una lista de números."""
    suma = 0
    for num in lista:
        suma += num
    return suma

print("\n--- Paradigma Estructurado ---")
numeros = [1, 2, 3, 4, 5]
resultado = calcular_suma(numeros)
print(f"Suma usando función: {resultado}")

# Paradigma Modular (Uso de módulos externos)
import math

def calcular_raiz(numero):
    """Calcula la raíz cuadrada de un número usando el módulo math."""
    return math.sqrt(numero)

print("\n--- Paradigma Modular ---")
numero = 25
print(f"Raíz cuadrada de {numero}: {calcular_raiz(numero)}")

# Paradigma Orientado a Objetos (Clases y Objetos)
class Calculadora:
    """Clase para realizar operaciones matemáticas básicas."""
    def __init__(self, numero):
        self.numero = numero
    
    def cuadrado(self):
        return self.numero ** 2
    
    def cubo(self):
        return self.numero ** 3

print("\n--- Paradigma Orientado a Objetos ---")
calc = Calculadora(3)
print(f"Cuadrado de 3: {calc.cuadrado()}")
print(f"Cubo de 3: {calc.cubo()}")
