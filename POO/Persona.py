from abc import ABC, abstractmethod

# Clase abstracta (Abstraccion)
class Persona(ABC):
    def __init__(self, nombre, genero, edad, nacionalidad):  # Constructor para inicializar atributos.
        # Atributos privados (Encapsulamiento).
        self.__nombre = nombre
        self.__genero = genero
        if edad >= 0:
            self.__edad = edad
        else:
            self.__edad = None
        self.__nacionalidad = nacionalidad

    # Metodos para acceder y modificar los atributos privados (Encapsulamiento).
    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getGenero(self):
        return self.__genero

    def setGenero(self, genero):
        self.genero = genero

    def getEdad(self):
        if self.__edad is None:
            return "Edad invalida"
        else:
            return self.__edad

    def setEdad(self, edad):
        if edad >= 0:
            self.__edad = edad
        else:
            self.__edad = None
    
    def getNacionalidad(self):
        return self.__nacionalidad
    
    def setNacionalidad(self, nacionalidad):
        self.__nacionalidad = nacionalidad

    # Metodo que deben implementar las subclases (Abstraccion)
    @abstractmethod
    def informacion(self):
        pass