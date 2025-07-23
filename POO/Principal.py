from Estudiante import Estudiante
from Trabajador import Trabajador

# Polimorfismo: permite que diferentes clases compartan un mismo método (presentarse).
def acerca_de(persona):
    print(persona.informacion())

# Bloque principal del programa.
if __name__ == "__main__":

    estudiante = None
    trabajador = None

    while True:
        print('---------------Menu Principal---------------')
        print('|1. Crear Estudiante                       |')
        print('|2. Crear Trabajador                       |')
        print('!3. Actualizar Estudiante                  |')
        print('|4. Actualizar Trabajador                  |')
        print('|5. Eliminar Estudiante                    |')
        print('|6. Eliminar Trabajador                    |')
        print('|7. Mostrar Informacion Estudiante         |')
        print('|8. Mostrar Informacion Trabajador         |')
        print('|9. Salir                                  |')
        print('--------------------------------------------')

        opcion = int(input("Ingrese una opcion:"))

        if opcion == 1:
            nombre = input("Ingrese un nombre: ")
            genero = input("Ingrese un genero: ")
            edad = int(input("Ingrese una edad: "))
            nacionalidad = input("Ingrese una nacionalidad: ")
            universidad = input("Ingrese una universidad: ")
            estudiante = Estudiante(nombre, genero, edad, nacionalidad, universidad)
        elif opcion == 2:
            nombre = input("Ingrese un nombre: ")
            genero = input("Ingrese un genero: ")
            edad = int(input("Ingrese una edad: "))
            nacionalidad = input("Ingrese una nacionalidad: ")
            trabajo = input("Ingrese un trabajo: ")
            trabajador = Trabajador(nombre, genero, edad, nacionalidad, trabajo)
        elif opcion == 3:
            if estudiante is not None:
                nombre = input("Ingrese un nombre: ")
                genero = input("Ingrese un genero: ")
                edad = int(input("Ingrese una edad: "))
                nacionalidad = input("Ingrese una nacionalidad: ")
                universidad = input("Ingrese una universidad: ")
                estudiante.setNombre(nombre)
                estudiante.setGenero(genero)
                estudiante.setEdad(edad)
                estudiante.setNacionalidad(nacionalidad)
                estudiante.setUniversidad(universidad)
            else:
                print("No se ha creado ningun estudiante.")
        elif opcion == 4:
            if trabajador is not None:
                nombre = input("Ingrese un nombre: ")
                genero = input("Ingrese un genero: ")
                edad = int(input("Ingrese una edad: "))
                nacionalidad = input("Ingrese una nacionalidad: ")
                trabajo = input("Ingrese un trabajo: ")
                trabajador.setNombre(nombre)
                trabajador.setGenero(genero)
                trabajador.setEdad(edad)
                trabajador.setNacionalidad(nacionalidad)
                trabajador.setTrabajo(trabajo)
            else:
                print("No se ha creado ningun trabajador.")
        elif opcion == 5:
            estudiante = None
        elif opcion == 6:
            trabajador = None
        elif opcion == 7:
            if estudiante is not None:
                acerca_de(estudiante)
            else:
                print("No se ha creado ningun estudiante.")
        elif opcion == 8:
            if trabajador is not None:
                acerca_de(trabajador)
            else:
                print("No se ha creado ningun trabajador.")
        elif opcion == 9:
            break
        else:
            print("Opcion invalida.")