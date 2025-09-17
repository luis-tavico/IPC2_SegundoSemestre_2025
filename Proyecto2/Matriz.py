from ListaSimpleEnlazada import ListaEnlazada
from Planta import Planta

class Matriz:
    def __init__(self, num_filas, num_columnas):
        self.num_filas = num_filas
        self.num_columnas = num_columnas
        self.matriz = ListaEnlazada()
        
        # Crear matriz inicializada con valores nulos
        for i in range(1, num_filas + 1):
            fila = ListaEnlazada()
            for j in range(1, num_columnas + 1):
                planta = Planta(i, j, 0, 0, "")
                fila.insertar(planta)
            self.matriz.insertar(fila)
    
    def establecer(self, num_fila, num_columna, planta):
        # Establece un valor en la posicion [fila, columna]
        fila = self.matriz.obtener(num_fila)
        if fila:
            columna = fila.primero
            for j in range(1, num_columna):
                if columna:
                    columna = columna.siguiente
            if columna:
                columna.dato = planta
    
    def obtener(self, num_fila, num_columna):
        # Obtiene el valor en la posicion [fila, columna]
        fila = self.matriz.obtener(num_fila)
        if fila:
            return fila.obtener(num_columna)
        return None