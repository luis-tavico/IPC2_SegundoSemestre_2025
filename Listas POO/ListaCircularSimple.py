class Nodo:
    def __init__(self, dato=None, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente

class ListaCircularSimple:
    def __init__(self):
        self.primero = None

    def insertar(self, nota):
        nodo = Nodo(dato=nota)
        if self.primero is None:
            self.primero = nodo
            self.primero.siguiente = self.primero
        else:
            actual = self.primero
            while actual.siguiente != self.primero:
                actual = actual.siguiente
            actual.siguiente = nodo
            nodo.siguiente = self.primero

    def eliminar(self, dato):
        if self.primero is None:
            return
        actual = self.primero
        anterior = None
        while True:
            if actual.dato == dato:
                if anterior is not None:
                    anterior.siguiente = actual.siguiente
                else:
                    if actual.siguiente == self.primero:
                        self.primero = None
                    else:
                        temp = self.primero
                        while temp.siguiente != self.primero:
                            temp = temp.siguiente
                        self.primero = actual.siguiente
                        temp.siguiente = self.primero
                return
            anterior = actual
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


lista_circular_simple = ListaCircularSimple()

lista_circular_simple.insertar(1)
lista_circular_simple.insertar(2)
lista_circular_simple.insertar(3)
lista_circular_simple.insertar(4)

lista_circular_simple.recorrer()

lista_circular_simple.eliminar(3)

print("Esta 3 en la lista:", lista_circular_simple.buscar(3))