# Problema 17: Implementar estructuras de datos básicas: pila, cola y lista enlazada

# Implementación de la Pila
class Pila:
    def __init__(self):
        self.items = []
    
    def apilar(self, item):
        self.items.append(item)
    
    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None
    
    def esta_vacia(self):
        return len(self.items) == 0

    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]
        return None

# Implementación de la Cola
from collections import deque
class Cola:
    def __init__(self):
        self.items = deque()
    
    def encolar(self, item):
        self.items.append(item)
    
    def desencolar(self):
        if not self.esta_vacia():
            return self.items.popleft()
        return None
    
    def esta_vacia(self):
        return len(self.items) == 0

# Implementación de una Lista Enlazada simple
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
    
    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
    
    def eliminar(self, dato):
        actual = self.cabeza
        anterior = None
        while actual:
            if actual.dato == dato:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                return True
            anterior = actual
            actual = actual.siguiente
        return False
    
    def mostrar(self):
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(actual.dato)
            actual = actual.siguiente
        return elementos

if __name__ == '__main__':
    # Demostración de Pila
    print("Demostración de Pila:")
    pila = Pila()
    pila.apilar(1)
    pila.apilar(2)
    pila.apilar(3)
    print("Pila después de apilar 1, 2, 3:", pila.items)
    print("Desapilando:", pila.desapilar())
    print("Pila actual:", pila.items)

    # Demostración de Cola
    print("\nDemostración de Cola:")
    cola = Cola()
    cola.encolar("a")
    cola.encolar("b")
    cola.encolar("c")
    print("Cola después de encolar 'a', 'b', 'c':", list(cola.items))
    print("Desencolando:", cola.desencolar())
    print("Cola actual:", list(cola.items))

    # Demostración de Lista Enlazada
    print("\nDemostración de Lista Enlazada:")
    lista = ListaEnlazada()
    lista.agregar("primero")
    lista.agregar("segundo")
    lista.agregar("tercero")
    print("Elementos de la lista enlazada:", lista.mostrar())
    lista.eliminar("segundo")
    print("Lista enlazada después de eliminar 'segundo':", lista.mostrar())
