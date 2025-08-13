class Nodo:
    def __init__(self, dato=None, siguiente=None, anterior=None):
        self.dato = dato
        self.siguiente = siguiente
        self.anterior = anterior

class ListaCircularDoble:
    def __init__(self):
        self.primero = None

    def insertar(self, dato):
        nodo = Nodo(dato=dato)
        if self.primero is None:
            self.primero = nodo
            self.primero.siguiente = self.primero
            self.primero.anterior = self.primero
        else:
            actual = self.primero
            while actual.siguiente != self.primero:
                actual = actual.siguiente
            actual.siguiente = nodo
            nodo.anterior = actual
            nodo.siguiente = self.primero
            self.primero.anterior = nodo


    def eliminar(self, dato):
        if self.primero is None:
            return
        actual = self.primero
        while True:
            if actual.dato == dato:
                if actual.siguiente == actual:
                    self.primero = None
                else:
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior
                    if actual == self.primero:
                        self.primero = actual.siguiente
                return
            actual = actual.siguiente
            if actual == self.primero:
                break

    def buscar(self, dato):
        if self.primero is None:
            return False
        actual = self.primero
        while True:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
            if actual == self.primero:
                break
        return False

    def recorrer(self):
        if self.primero is None:
            return
        actual = self.primero
        while True:
            print(actual.dato)
            actual = actual.siguiente
            if actual == self.primero:
                break


lista_circular_simple = ListaCircularDoble()

lista_circular_simple.insertar(1)
lista_circular_simple.insertar(2)
lista_circular_simple.insertar(3)
lista_circular_simple.insertar(4)

lista_circular_simple.recorrer()

lista_circular_simple.eliminar(3)

print("Esta 3 en la lista:", lista_circular_simple.buscar(3))