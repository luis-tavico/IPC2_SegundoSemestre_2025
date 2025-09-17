class Nodo:
    def __init__(self, dato=None, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente

class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self.longitud = 0

    def insertar(self, dato):
        nodo = Nodo(dato)
        if self.primero is None:
            self.primero = nodo
        else:
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nodo
        self.longitud += 1

    def obtener(self, indice):
        if indice < 1 or indice > self.longitud:
            return None
        actual = self.primero
        for i in range(1, indice): 
            actual = actual.siguiente
        return actual.dato

    def buscar_indice(self, id_buscar):
        actual = self.primero
        indice = 1
        while actual:
            if hasattr(actual.dato, 'id') and actual.dato.id == id_buscar:
                return indice
            actual = actual.siguiente
            indice += 1
        return -1