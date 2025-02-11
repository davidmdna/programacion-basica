# Problema 15: Determinar si un año es bisiesto

def es_bisiesto(ano):
    return (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0))

if __name__ == '__main__':
    try:
        ano = int(input("Ingrese un año: "))
        if es_bisiesto(ano):
            print(f"{ano} es un año bisiesto.")
        else:
            print(f"{ano} no es un año bisiesto.")
    except ValueError:
        print("Entrada no válida.")
