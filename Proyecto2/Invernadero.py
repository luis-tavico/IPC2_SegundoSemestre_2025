from Matriz import Matriz

class Invernadero:
    def __init__(self, nombre, numero_hileras, plantas_x_hilera, lista_plantas, lista_drones_asignados, lista_planes_riego):
        self.nombre = nombre
        self.numero_hileras = numero_hileras
        self.plantas_x_hilera = plantas_x_hilera
        self.lista_plantas = lista_plantas
        self.matriz_plantas = None
        self.lista_drones_asignados = lista_drones_asignados
        self.lista_planes_riego = lista_planes_riego

    def crear_matrices(self):       
        self.matriz_plantas = Matriz(self.numero_hileras, self.plantas_x_hilera)
        
        # Recorrer lista plantas
        actual_planta = self.lista_plantas.primero
        while actual_planta:
            planta = actual_planta.dato
            # Llenar matriz
            self.matriz_plantas.establecer(planta.hilera, planta.posicion, planta)
            actual_planta = actual_planta.siguiente

    def mostrar_matrices(self):
        if self.matriz_plantas:
            titulo = f"Matriz de plantas - Invernadero {self.nombre}"
            self.matriz_plantas.mostrar(titulo)