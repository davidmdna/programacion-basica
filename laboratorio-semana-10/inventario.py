class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, nombre, categoria, precio, cantidad):
        self.productos.append({
            'nombre': nombre,
            'categoria': categoria,
            'precio': precio,
            'cantidad': cantidad
        })
        print(f"Producto '{nombre}' agregado correctamente.")

    def eliminar_producto(self, nombre):
        self.productos = [p for p in self.productos if p['nombre'] != nombre]
        print(f"Producto '{nombre}' eliminado si existía en el inventario.")

    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto['nombre'] == nombre:
                print(f"Producto encontrado: {producto}")
                return producto
        print("Producto no encontrado.")
        return None

    def mostrar_productos_ordenados(self):
        productos_ordenados = sorted(self.productos, key=lambda x: x['precio'])
        print("Productos ordenados por precio:")
        for producto in productos_ordenados:
            print(producto)

# Ejemplo de uso
inventario = Inventario()
inventario.agregar_producto("Laptop", "Electrónica", 15000, 5)
inventario.agregar_producto("Mouse", "Accesorios", 500, 10)
inventario.agregar_producto("Teclado", "Accesorios", 1200, 7)

inventario.mostrar_productos_ordenados()
inventario.buscar_producto("Mouse")
inventario.eliminar_producto("Mouse")
inventario.mostrar_productos_ordenados()
