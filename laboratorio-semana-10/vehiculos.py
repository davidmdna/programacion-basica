class Vehiculo:
    def __init__(self, marca, modelo, anio, precio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.precio = precio
    
    def mostrar_info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}, Precio: ${self.precio}"

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, anio, precio, num_puertas):
        super().__init__(marca, modelo, anio, precio)
        self.num_puertas = num_puertas
    
    def mostrar_info(self):
        return super().mostrar_info() + f", Número de puertas: {self.num_puertas}"

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, anio, precio, cilindrada):
        super().__init__(marca, modelo, anio, precio)
        self.cilindrada = cilindrada
    
    def mostrar_info(self):
        return super().mostrar_info() + f", Cilindrada: {self.cilindrada}cc"

# Ejemplo de uso
auto = Automovil("Toyota", "Corolla", 2022, 25000, 4)
moto = Motocicleta("Yamaha", "YZF-R3", 2023, 6000, 321)

print(auto.mostrar_info())
print(moto.mostrar_info())
