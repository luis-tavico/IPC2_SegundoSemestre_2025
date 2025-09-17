from Cola import Cola
from ListaSimpleEnlazada import ListaEnlazada

class Dron:
    def __init__(self, id, nombre, hilera_asignada, posicion_actual, posicion_objetivo, litros_agua_usados, gramos_fertilizante_usados, plantas_a_regar, pasos):
        self.id = id
        self.nombre = nombre
        self.hilera_asignada = hilera_asignada
        self.posicion_actual = posicion_actual
        self.posicion_objetivo = posicion_objetivo
        self.litros_agua_usados = litros_agua_usados
        self.gramos_fertilizante_usados = gramos_fertilizante_usados
        self.plantas_a_regar = plantas_a_regar
        self.pasos = pasos

    def mover_adelante(self):
        self.posicion_actual += 1
        return f"Adelante (H{self.hilera_asignada}P{self.posicion_actual})"
    
    def mover_atras(self):
        self.posicion_actual -= 1
        return f"Atras (H{self.hilera_asignada}P{self.posicion_actual})"
    
    def esperar(self):
        return "Esperar"
    
    def regar(self, planta):
        self.litros_agua_usados += planta.litros_agua
        self.gramos_fertilizante_usados += planta.gramos_fertilizante
        return "Regar"
    
    def reiniciar_datos(self):
        self.posicion_actual = 0
        self.posicion_objetivo = None
        self.litros_agua_usados = 0
        self.gramos_fertilizante_usados = 0
        self.plantas_a_regar = Cola()
        self.pasos = ListaEnlazada()