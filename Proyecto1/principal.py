from SistemaAgricultura import SistemaAgricultura

def main():
    sistema = SistemaAgricultura()
    
    while True:
        print("---------------------------------------")
        print("| SISTEMA DE AGRICULTURA DE PRECISION |")
        print("---------------------------------------")
        print("|1. Cargar archivo                    |")
        print("|2. Mostrar matrices                  |")
        print("|3. Salir                             |")
        print("---------------------------------------")
        opcion = input("Seleccione una opcion: ")
        
        if opcion == "1":
            print("\nCargar archivo:")
            ruta = input("Ingrese la ruta del archivo: ")
            nombre = input("Ingrese el nombre del archivo: ")
            archivo = ruta + "/" + nombre if ruta else nombre
            sistema.cargar_archivo(archivo)
        elif opcion == "2":
            print("\nMostrar matrices:")
            sistema.listar_campos()
            id_campo = input("Ingrese el ID del campo: ")
            sistema.mostrar_campo(id_campo)
        elif opcion == "3":
            print("Ejecucion Finalizada...")
            break
        else:
            print("Opcion no valida")

if __name__ == "__main__":
    main()