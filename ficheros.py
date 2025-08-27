import os

def crearArchivo(nombre):
    try:
        with open(nombre, 'x', encoding='utf-8') as f:
            print(f"Archivo '{nombre}' creado exitosamente.")
    except FileExistsError:
        print("Error: El archivo ya existe.")

def escribirArchivo(nombre):
    contenido = input("Ingrese el contenido: ")
    with open(nombre, 'w', encoding='utf-8') as f:
        f.write(contenido)
    print("Contenido escrito exitosamente.")

def añadirArchivo(nombre):
    contenido = input("Ingrese el contenido adicional: ")
    with open(nombre, 'a', encoding='utf-8') as f:
        f.write('\n' + contenido)
    print("Contenido añadido exitosamente.")

def leerArchivo(nombre):
    try:
        with open(nombre, 'r', encoding='utf-8') as f:
            print("\nContenido del archivo:")
            print(f.read())
    except FileNotFoundError:
        print("Error: El archivo no existe.")

def eliminarArchivo(nombre):
    try:
        os.remove(nombre)
        print(f"El archivo '{nombre}' ha sido eliminado.")
    except FileNotFoundError:
        print("Error: El archivo no existe.")


if __name__ == "__main__":
    while True:
        print("\nGestor de archivos en Python")
        print("1. Crear un archivo nuevo")
        print("2. Escribir en un archivo (sobreescribir)")
        print("3. Añadir contenido a un archivo")
        print("4. Leer un archivo")
        print("5. Eliminar un archivo")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del archivo a crear: ")
            crearArchivo(nombre)
        elif opcion == '2':
            nombre = input("Ingrese el nombre del archivo a escribir: ")
            escribirArchivo(nombre)
        elif opcion == '3':
            nombre = input("Ingrese el nombre del archivo a añadir contenido: ")
            añadirArchivo(nombre)
        elif opcion == '4':
            nombre = input("Ingrese el nombre del archivo a leer: ")
            leerArchivo(nombre)
        elif opcion == '5':
            nombre = input("Ingrese el nombre del archivo a eliminar: ")
            eliminarArchivo(nombre)
        elif opcion == '6':
            print("Ejecución finalizada.")
            break
        else:
            print("Opcion no valida.")