class CuentaBancaria:
    def __init__(self, saldo=0):
        self.saldo = saldo
    
    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito realizado. Saldo actual: {self.saldo:.2f}")
        else:
            print("Cantidad inválida para depósito.")
    
    def retirar(self, cantidad):
        if cantidad > 0:
            if cantidad <= self.saldo:
                self.saldo -= cantidad
                print(f"Retiro realizado. Saldo actual: {self.saldo:.2f}")
            else:
                print("Saldo insuficiente.")
        else:
            print("Cantidad inválida para retiro.")
    
    def mostrar_saldo(self):
        print(f"Saldo actual: {self.saldo:.2f}")

if __name__ == '__main__':
    cuenta = CuentaBancaria()
    while True:
        print("\nCuenta Bancaria")
        print("1. Depositar")
        print("2. Retirar")
        print("3. Mostrar Saldo")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            try:
                cantidad = float(input("Ingrese la cantidad a depositar: "))
                cuenta.depositar(cantidad)
            except ValueError:
                print("Entrada no válida.")
        elif opcion == "2":
            try:
                cantidad = float(input("Ingrese la cantidad a retirar: "))
                cuenta.retirar(cantidad)
            except ValueError:
                print("Entrada no válida.")
        elif opcion == "3":
            cuenta.mostrar_saldo()
        elif opcion == "4":
            print("Saliendo.")
            break
        else:
            print("Opción no válida.")
