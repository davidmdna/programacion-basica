import math

def calcular_cubo(lado):
    area = 6 * (lado ** 2)
    volumen = lado ** 3
    return area, volumen

def calcular_esfera(radio):
    area = 4 * math.pi * (radio ** 2)
    volumen = (4/3) * math.pi * (radio ** 3)
    return area, volumen

def calcular_cilindro(radio, altura):
    area = 2 * math.pi * radio * (radio + altura)
    volumen = math.pi * (radio ** 2) * altura
    return area, volumen

if __name__ == '__main__':
    print("Elija la figura para calcular área y volumen:")
    print("1. Cubo")
    print("2. Esfera")
    print("3. Cilindro")
    opcion = input("Seleccione una opción (1/2/3): ")
    
    if opcion == "1":
        try:
            lado = float(input("Ingrese la longitud del lado del cubo: "))
            area, volumen = calcular_cubo(lado)
            print(f"Área: {area:.2f}, Volumen: {volumen:.2f}")
        except ValueError:
            print("Entrada no válida.")
    elif opcion == "2":
        try:
            radio = float(input("Ingrese el radio de la esfera: "))
            area, volumen = calcular_esfera(radio)
            print(f"Área: {area:.2f}, Volumen: {volumen:.2f}")
        except ValueError:
            print("Entrada no válida.")
    elif opcion == "3":
        try:
            radio = float(input("Ingrese el radio del cilindro: "))
            altura = float(input("Ingrese la altura del cilindro: "))
            area, volumen = calcular_cilindro(radio, altura)
            print(f"Área: {area:.2f}, Volumen: {volumen:.2f}")
        except ValueError:
            print("Entrada no válida.")
    else:
        print("Opción no válida.")
