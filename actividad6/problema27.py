def metros_a_kilometros(metros):
    return metros / 1000

def kilometros_a_metros(km):
    return km * 1000

def centimetros_a_pulgadas(cm):
    return cm / 2.54

def pulgadas_a_centimetros(pulgadas):
    return pulgadas * 2.54

if __name__ == '__main__':
    print("Conversor de Unidades")
    print("1. Metros a Kilómetros")
    print("2. Kilómetros a Metros")
    print("3. Centímetros a Pulgadas")
    print("4. Pulgadas a Centímetros")
    opcion = input("Seleccione una opción: ")
    
    try:
        if opcion == "1":
            metros = float(input("Ingrese la cantidad en metros: "))
            print(f"{metros} metros = {metros_a_kilometros(metros):.3f} kilómetros")
        elif opcion == "2":
            km = float(input("Ingrese la cantidad en kilómetros: "))
            print(f"{km} kilómetros = {kilometros_a_metros(km):.2f} metros")
        elif opcion == "3":
            cm = float(input("Ingrese la cantidad en centímetros: "))
            print(f"{cm} cm = {centimetros_a_pulgadas(cm):.2f} pulgadas")
        elif opcion == "4":
            pulgadas = float(input("Ingrese la cantidad en pulgadas: "))
            print(f"{pulgadas} pulgadas = {pulgadas_a_centimetros(pulgadas):.2f} cm")
        else:
            print("Opción no válida.")
    except ValueError:
        print("Entrada no válida.")
