from Persona import Persona

# Clase derivada (Herencia)
class Trabajador(Persona):
    def __init__(self, nombre, genero, edad, trabajo):
        super().__init__(nombre, genero, edad)
        self.__trabajo = trabajo  # Atributo especifico de la clase Trabajador.

    # Metodos para acceder y modificar los atributos privados (Encapsulamiento).
    def getTrabajo(self):
        return self.__trabajo
    
    def setTrabajo(self, trabajo):
        self.__trabajo = trabajo

    # Implementacion del metodo abstracto (Polimorfismo)
    def informacion(self):
        return f"Nombre: {self.getNombre()}, \nGenero: {self.getGenero()}, \nEdad: {self.getEdad()}, \nNacionalidad {self.getNacionalidad()}, \nTrabajo: {self.getTrabajo()}."