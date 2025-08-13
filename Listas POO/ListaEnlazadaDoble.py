class Nodo:
    def __init__(self, dato=None, siguiente=None, anterior=None):
        self.dato = dato
        self.siguiente = siguiente
        self.anterior = anterior

class ListaDobleEnlazada:
    def __init__(self):
        self.primero = None
    
    def insertar(self, numero):
        nodo = Nodo(dato=numero)
        if self.primero is None:
            self.primero = nodo
        else:
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nodo
            nodo.anterior = actual

    def eliminar(self, dato):
        actual = self.primero
        while actual and actual.dato != dato:
            actual = actual.siguiente
        if actual is None:
            return
        if actual.anterior is None: 
            self.primero = actual.siguiente
            if self.primero:
                self.primero.anterior = None
        else:
            actual.anterior.siguiente = actual.siguiente
        if actual.siguiente:
            actual.siguiente.anterior = actual.anterior
        actual.siguiente = None
        actual.anterior = None

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


lista_doble = ListaDobleEnlazada()

lista_doble.insertar(1)
lista_doble.insertar(2)
lista_doble.insertar(3)
lista_doble.insertar(4)

lista_doble.recorrer()

lista_doble.eliminar(3)

print("Esta 3 en la lista:", lista_doble.buscar(3))