class AgendaContactos:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, nombre, numero, correo):
        self.contactos.append((nombre, numero, correo))
        print(f"Contacto '{nombre}' agregado correctamente.")

    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto[0] == nombre:
                print(f"Contacto encontrado: Nombre: {contacto[0]}, Número: {contacto[1]}, Correo: {contacto[2]}")
                return contacto
        print("Contacto no encontrado.")
        return None

    def listar_contactos(self):
        contactos_ordenados = sorted(self.contactos, key=lambda x: x[0])
        print("Lista de contactos ordenados alfabéticamente:")
        for contacto in contactos_ordenados:
            print(f"Nombre: {contacto[0]}, Número: {contacto[1]}, Correo: {contacto[2]}")


