from xml.dom.minidom import parse, Document
import xml.etree.ElementTree as ET
from lxml import etree

def leer_dom():
    print("\n--- Leyendo XML con DOM ---")
    dom = parse('libros.xml')
    libros = dom.getElementsByTagName('libro')
    for libro in libros:
        titulo = libro.getElementsByTagName('titulo')[0].firstChild.data
        autor = libro.getElementsByTagName('autor')[0].firstChild.data
        precio = libro.getElementsByTagName('precio')[0].firstChild.data
        print(f"Titulo: {titulo}, Autor: {autor}, Precio: {precio}")

def editar_dom():
    print("\n--- Editando XML con DOM ---")
    dom = parse('libros.xml')
    libros = dom.getElementsByTagName('libro')
    for i, libro in enumerate(libros):
        titulo = libro.getElementsByTagName('titulo')[0].firstChild.data
        print(f"{i+1}. {titulo}")
    seleccion = int(input("Selecciona el numero del libro a editar: ")) - 1
    
    nuevo_titulo = input("Nuevo titulo: ")
    nuevo_autor = input("Nuevo autor: ")
    nuevo_precio = input("Nuevo precio: ")

    libros[seleccion].getElementsByTagName('titulo')[0].firstChild.data = nuevo_titulo
    libros[seleccion].getElementsByTagName('autor')[0].firstChild.data = nuevo_autor
    libros[seleccion].getElementsByTagName('precio')[0].firstChild.data = nuevo_precio

    with open('libros.xml', 'w') as archivo:
        archivo.write(dom.toxml())
    print("¡Libro editado exitosamente!")

def leer_elementtree():
    print("\n--- Leyendo XML con ElementTree ---")
    tree = ET.parse('libros.xml')
    root = tree.getroot()
    for libro in root.findall('libro'):
        titulo = libro.find('titulo').text
        autor = libro.find('autor').text
        precio = libro.find('precio').text
        print(f"Titulo: {titulo}, Autor: {autor}, Precio: {precio}")

def editar_elementtree():
    print("\n--- Editando XML con ElementTree ---")
    tree = ET.parse('libros.xml')
    root = tree.getroot()
    libros = root.findall('libro')
    for i, libro in enumerate(libros):
        titulo = libro.find('titulo').text
        print(f"{i+1}. {titulo}")
    seleccion = int(input("Selecciona el numero del libro a editar: ")) - 1
    
    nuevo_titulo = input("Nuevo titulo: ")
    nuevo_autor = input("Nuevo autor: ")
    nuevo_precio = input("Nuevo precio: ")

    libros[seleccion].find('titulo').text = nuevo_titulo
    libros[seleccion].find('autor').text = nuevo_autor
    libros[seleccion].find('precio').text = nuevo_precio

    tree.write('libros.xml')
    print("¡Libro editado exitosamente!")

def leer_xpath():
    print("\n--- Leyendo XML con XPath ---")
    tree = etree.parse('libros.xml')
    titulos = tree.xpath('//libro/titulo/text()')
    autores = tree.xpath('//libro/autor/text()')
    precios = tree.xpath('//libro/precio/text()')
    for titulo, autor, precio in zip(titulos, autores, precios):
        print(f"Titulo: {titulo}, Autor: {autor}, Precio: {precio}")

def editar_xpath():
    print("\n--- Editando XML con XPath ---")
    tree = etree.parse('libros.xml')
    root = tree.getroot()
    titulos = tree.xpath('//libro/titulo')
    
    for i, titulo in enumerate(titulos):
        print(f"{i+1}. {titulo.text}")
    seleccion = int(input("Selecciona el numero del libro a editar: ")) - 1

    nuevo_titulo = input("Nuevo titulo: ")
    nuevo_autor = input("Nuevo autor: ")
    nuevo_precio = input("Nuevo precio: ")

    titulos[seleccion].text = nuevo_titulo
    tree.xpath('//libro/autor')[seleccion].text = nuevo_autor
    tree.xpath('//libro/precio')[seleccion].text = nuevo_precio

    with open('libros.xml', 'wb') as archivo:
        archivo.write(etree.tostring(root, pretty_print=True))
    print("¡Libro editado exitosamente!")

def menu():
    while True:
        print("\n--- Menu de Procesamiento de XML ---")
        print("1. Usar DOM")
        print("2. Usar ElementTree")
        print("3. Usar XPath")
        print("4. Salir")
        opcion = input("Elige una opcion: ")

        if opcion == '1':
            accion = input("\n¿Quieres (1) Leer o (2) Editar? ")
            if accion == '1':
                leer_dom()
            elif accion == '2':
                editar_dom()
            else:
                print("Opcion no valida.")
        
        elif opcion == '2':
            accion = input("\n¿Quieres (1) Leer o (2) Editar? ")
            if accion == '1':
                leer_elementtree()
            elif accion == '2':
                editar_elementtree()
            else:
                print("Opcion no valida.")
        
        elif opcion == '3':
            accion = input("\n¿Quieres (1) Leer o (2) Editar? ")
            if accion == '1':
                leer_xpath()
            elif accion == '2':
                editar_xpath()
            else:
                print("Opcion no valida.")
        
        elif opcion == '4':
            print("Saliendo...")
            break
        else:
            print("Opcion no valida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()