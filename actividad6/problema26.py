def mostrar_agenda(agenda):
    if not agenda:
        print("La agenda está vacía.")
    else:
        for nombre, info in agenda.items():
            print(f"Nombre: {nombre}, Teléfono: {info['telefono']}, Email: {info.get('email', 'N/A')}")

def agregar_contacto(agenda, nombre, telefono, email=""):
    agenda[nombre] = {"telefono": telefono, "email": email}

def buscar_contacto(agenda, nombre):
    return agenda.get(nombre, None)

def eliminar_contacto(agenda, nombre):
    if nombre in agenda:
        del agenda[nombre]
        return True
    return False

if __name__ == '__main__':
    agenda = {}
    while True:
        print("\nAgenda de Contactos")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Eliminar contacto")
        print("4. Mostrar agenda")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Ingrese el nombre: ")
            telefono = input("Ingrese el teléfono: ")
            email = input("Ingrese el email (opcional): ")
            agregar_contacto(agenda, nombre, telefono, email)
            print("Contacto agregado.")
        elif opcion == "2":
            nombre = input("Ingrese el nombre a buscar: ")
            contacto = buscar_contacto(agenda, nombre)
            if contacto:
                print(f"Contacto encontrado: Nombre: {nombre}, Teléfono: {contacto['telefono']}, Email: {contacto.get('email', 'N/A')}")
            else:
                print("Contacto no encontrado.")
        elif opcion == "3":
            nombre = input("Ingrese el nombre a eliminar: ")
            if eliminar_contacto(agenda, nombre):
                print("Contacto eliminado.")
            else:
                print("Contacto no encontrado.")
        elif opcion == "4":
            mostrar_agenda(agenda)
        elif opcion == "5":
            print("Saliendo de la agenda.")
            break
        else:
            print("Opción no válida.")
