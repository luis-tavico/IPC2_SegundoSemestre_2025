from ListaSimpleEnlazada import ListaEnlazada

class Sensor:
    def __init__(self, id_sensor, nombre):
        self.id = id_sensor
        self.nombre = nombre
        self.frecuencias = ListaEnlazada()