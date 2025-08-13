class Nodo:
    def __init__(self, dato=None, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente


class ListaEnlazadaSimple:
    def __init__(self):
        self.primero = None

    def insertar(self, dato):
        nodo = Nodo(dato=dato)
        if self.primero is None:
            self.primero = nodo
        else:
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nodo

    def eliminar(self, dato):
        actual = self.primero
        anterior = None
        while actual and actual.dato != dato:
            anterior = actual
            actual = actual.siguiente
        if anterior is None:
            self.primero = actual.siguiente
            actual.siguiente = None
        elif actual:
            anterior.siguiente = actual.siguiente
            actual.siguiente = None

    def buscar(self, dato):
        actual = self.primero
        anterior = None
        while actual and actual.dato != dato:
            anterior = actual
            actual = actual.siguiente
        if actual:
            return True
        else:
            return False

    def recorrer(self):
        actual = self.primero
        while actual:
            print(actual.dato)
            actual = actual.siguiente


lista_simple = ListaEnlazadaSimple()

lista_simple.insertar(1)
lista_simple.insertar(2)
lista_simple.insertar(3)
lista_simple.insertar(4)

lista_simple.recorrer()

lista_simple.eliminar(3)

print("Esta 3 en la lista:", lista_simple.buscar(3))