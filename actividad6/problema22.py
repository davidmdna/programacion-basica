import random

def lanzar_dado():
    return random.randint(1, 6)

def lanzar_moneda():
    return random.choice(["Cara", "Cruz"])

if __name__ == '__main__':
    input("Presiona Enter para lanzar el dado...")
    print("Resultado del dado:", lanzar_dado())
    
    input("Presiona Enter para lanzar la moneda...")
    print("Resultado de la moneda:", lanzar_moneda())
