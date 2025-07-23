from Persona import Persona

# Clase derivada (Herencia)
class Estudiante(Persona):
    def __init__(self, nombre, genero, edad, nacionalidad, universidad):
        # Llama al constructor de la clase base.
        super().__init__(nombre, genero, edad, nacionalidad)
        self.__universidad = universidad  # Atributo especifico de la clase Estudiante.

    # Metodos para acceder y modificar los atributos privados (Encapsulamiento).
    def getUniversidad(self):
        return self.__universidad

    def setUniversidad(self, universidad):
        self.__universidad = universidad

    # Implementacion del metodo abstracto (Polimorfismo)
    def informacion(self):
        return f"Nombre: {self.getNombre()}, \nGenero: {self.getGenero()}, \nEdad: {self.getEdad()}, \nNacionalidad {self.getNacionalidad()}, \nUniversidad: {self.getUniversidad()}."