# conversor.py

def km_a_millas(km):
    return km * 0.621371

def celsius_a_fahrenheit(c):
    return (c * 9/5) + 32

def litros_a_galones(l):
    return l * 0.264172

# programa_principal.py
import conversor

def main():
    print("Conversor de Unidades")
    print("1. Kilómetros a Millas")
    print("2. Celsius a Fahrenheit")
    print("3. Litros a Galones")
    opcion = input("Seleccione una opción (1-3): ")
    
    if opcion == "1":
        km = float(input("Ingrese la cantidad de kilómetros: "))
        print(f"{km} km = {conversor.km_a_millas(km)} millas")
    elif opcion == "2":
        c = float(input("Ingrese la temperatura en Celsius: "))
        print(f"{c}°C = {conversor.celsius_a_fahrenheit(c)}°F")
    elif opcion == "3":
        l = float(input("Ingrese la cantidad de litros: "))
        print(f"{l} L = {conversor.litros_a_galones(l)} galones")
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()
