from ListaSimpleEnlazada import ListaEnlazada

class SimulacionRiego:
    def __init__(self, plan_riego, invernadero):
        self.plan_riego = plan_riego.secuencia_ubicacion_riego
        self.matriz_plantas = invernadero.matriz_plantas
        self.lista_drones_asignados = invernadero.lista_drones_asignados
        self.lista_plantas_a_regar = ListaEnlazada()

    def inicializar_datos_drones(self):
        actual_dron_asignado = self.lista_drones_asignados.primero
        while actual_dron_asignado:
            dron = actual_dron_asignado.dato
            dron.reiniciar_datos()
            actual_dron_asignado = actual_dron_asignado.siguiente

    def crear_lista_plantas_a_regar(self):
        ubicaciones_riego = self.plan_riego.split(',')
        for ubicacion_riego in ubicaciones_riego:
            ubicacion_riego = ubicacion_riego.strip()
            if ubicacion_riego:
                partes = ubicacion_riego.split('-')
                hilera = int(partes[0][1:])
                posicion = int(partes[1][1:])
                self.lista_plantas_a_regar.insertar(self.matriz_plantas.obtener(hilera, posicion))
   
    def asignar_plantas_a_regar_a_dron(self):
        actual_planta = self.lista_plantas_a_regar.primero
        while actual_planta:
            planta = actual_planta.dato
            actual_dron = self.lista_drones_asignados.primero
            while actual_dron:
                dron = actual_dron.dato
                if planta.hilera == dron.hilera_asignada:
                    dron.plantas_a_regar.encolar(planta)
                actual_dron = actual_dron.siguiente
            actual_planta = actual_planta.siguiente
    
    def simular(self):
        actual_planta_a_regar = self.lista_plantas_a_regar.primero

        while actual_planta_a_regar:
            planta_a_regar = actual_planta_a_regar.dato
            planta_no_regada = True
            
            while planta_no_regada:
                actual_dron_asignado = self.lista_drones_asignados.primero

                while actual_dron_asignado:
                    dron = actual_dron_asignado.dato
                    hilera_asignada = dron.hilera_asignada
                    posicion_actual = dron.posicion_actual

                    if dron.posicion_objetivo == None:
                        planta = dron.plantas_a_regar.desencolar()
                        if planta:
                            dron.posicion_objetivo = planta.posicion
                            posicion_objetivo = dron.posicion_objetivo
                        else:
                            posicion_objetivo = None
                    else:
                        posicion_objetivo = dron.posicion_objetivo

                    if posicion_objetivo != None:
                        # Mover hacia adelante
                        if posicion_actual < posicion_objetivo:
                            paso = dron.mover_adelante()
                            dron.pasos.insertar(paso)
                        # Mover hacia atras
                        elif posicion_actual > posicion_objetivo:
                            paso = dron.mover_atras()
                            dron.pasos.insertar(paso)
                        # Esperar
                        elif posicion_actual == posicion_objetivo and planta_a_regar.hilera != hilera_asignada:
                            paso = dron.esperar()
                            dron.pasos.insertar(paso)
                        # Regar
                        elif posicion_actual == posicion_objetivo and planta_a_regar.hilera == hilera_asignada:
                            paso = dron.regar(planta_a_regar)
                            dron.pasos.insertar(paso)
                            planta_no_regada = False
                            dron.posicion_objetivo = None
                    else:
                        planta_no_regada = False

                    actual_dron_asignado = actual_dron_asignado.siguiente

            actual_planta_a_regar = actual_planta_a_regar.siguiente

    def imprimir_pasos(self):
        actual_dron = self.lista_drones_asignados.primero
        while actual_dron:
            dron = actual_dron.dato
            print("Dron: ", dron.nombre)
            actual_paso = dron.pasos.primero
            while actual_paso:
                paso = actual_paso.dato
                print(paso)
                actual_paso = actual_paso.siguiente
            actual_dron = actual_dron.siguiente