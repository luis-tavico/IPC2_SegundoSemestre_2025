class Nodo:
    def __init__(self, dato=None, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente


class ListaEnlazadaSimple:
    def __init__(self):
        self.primero = None

    def insertar_al_inicio(self, dato):
        nodo = Nodo(dato=dato, siguiente=self.primero)
        self.primero = nodo

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


class Pila:
    def __init__(self):
        self.lista = ListaEnlazadaSimple()

    def push(self, dato):
        self.lista.insertar_al_inicio(dato)

    def pop(self):
        return self.lista.eliminar_inicio()

    def esta_vacia(self):
        return self.lista.esta_vacia()

    def mostrar(self):
        print("Pila:")
        self.lista.recorrer()

pila = Pila()
pila.push(10)
pila.push(20)
pila.push(30)
pila.mostrar()
print("Pop:", pila.pop())
pila.mostrar()