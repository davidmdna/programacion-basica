# Problema 2: Calculadora simple
def calculadora():
    print("Calculadora Simple")
    try:
        num1 = float(input("Ingrese el primer número: "))
        operador = input("Ingrese el operador (+, -, *, /): ")
        num2 = float(input("Ingrese el segundo número: "))
    except ValueError:
        print("Entrada no válida.")
        return

    if operador == "+":
        resultado = num1 + num2
    elif operador == "-":
        resultado = num1 - num2
    elif operador == "*":
        resultado = num1 * num2
    elif operador == "/":
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Error: División por cero.")
            return
    else:
        print("Operador no reconocido.")
        return

    print("Resultado:", resultado)

if __name__ == "__main__":
    calculadora()
