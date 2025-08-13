class Nodo:
    def __init__(self, dato=None, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente


class ListaEnlazadaSimple:
    def __init__(self):
        self.primero = None

    def insertar_al_final(self, dato):
        nodo = Nodo(dato=dato)
        if self.primero is None:
            self.primero = nodo
        else:
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nodo

    def eliminar_inicio(self):
        if self.primero is None:
            return None
        eliminado = self.primero
        self.primero = self.primero.siguiente
        eliminado.siguiente = None
        return eliminado.dato

    def esta_vacia(self):
        return self.primero is None

    def recorrer(self):
        actual = self.primero
        while actual:
            print(actual.dato)
            actual = actual.siguiente


class Cola:
    def __init__(self):
        self.lista = ListaEnlazadaSimple()

    def encolar(self, dato):
        self.lista.insertar_al_final(dato)

    def desencolar(self):
        return self.lista.eliminar_inicio()

    def esta_vacia(self):
        return self.lista.esta_vacia()

    def mostrar(self):
        print("Cola:")
        self.lista.recorrer()

cola = Cola()
cola.encolar("A")
cola.encolar("B")
cola.encolar("C")
cola.mostrar()
print("Desencolar:", cola.desencolar())
cola.mostrar()