import re

def validar_correos():
    regex_correo = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
    correo = input("Ingrese un correo electrónico: ")
    print("Válido" if re.match(regex_correo, correo) else "Inválido")

def extraer_enteros():
    regex_numeros = r'\d+'
    texto = input("Ingrese un texto con números: ")
    numeros = re.findall(regex_numeros, texto)
    print(f"Números encontrados: {numeros}")

def extraer_decimales():
    regex_decimal = r'\b\d+\.\d+\b'
    texto = input("Ingrese un texto con números decimales: ")
    decimales_encontrados = re.findall(regex_decimal, texto)
    print(f"Números decimales encontrados: {decimales_encontrados}")

def censurar_texto():
    regex_prohibidas = r'\b(mal|error|fallo)\b'
    texto = input("Ingrese un texto: ")
    texto_censurado = re.sub(regex_prohibidas, "****", texto)
    print(f"Texto censurado: {texto_censurado}")

def validar_telefono():
    regex_telefono = r'^\+\d{3} \d{4}-\d{4}$'
    telefono = input("Ingrese un número de teléfono (+502 1234-5678): ")
    print("Válido" if re.match(regex_telefono, telefono) else "Inválido")

def extraer_fechas():
    regex_fecha = r'\b\d{2}/\d{2}/\d{4}\b'
    texto = input("Ingrese un texto con fechas (DD/MM/AAAA): ")
    fechas_encontradas = re.findall(regex_fecha, texto)
    print(f"Fechas encontradas: {fechas_encontradas}")

def validar_contraseña():
    regex_password = r'^[a-zA-Z0-9]{6,}$'
    password = input("Ingrese una contraseña: ")
    print("Válida" if re.match(regex_password, password) else "Inválida")

def validar_ip():
    regex_ip = r'^\d{1,3}(\.\d{1,3}){3}$'
    ip = input("Ingrese una dirección IP: ")
    print("Válida" if re.match(regex_ip, ip) else "Inválida")

def menu():
    while True:
        print("\nMenu de Expresiones Regulares")
        print("1. Validar correo electronico")
        print("2. Extraer numeros enteros")
        print("3. Extraer numeros decimales")
        print("4. Censurar texto")
        print("5. Validar numero de telefono")
        print("6. Extraer fechas")
        print("7. Validar contraseña")
        print("8. Validar direccion IP")
        print("9. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            validar_correos()
        elif opcion == "2":
            extraer_enteros()
        elif opcion == "3":
            extraer_decimales()
        elif opcion == "4":
            censurar_texto()
        elif opcion == "5":
            validar_telefono()
        elif opcion == "6":
            extraer_fechas()
        elif opcion == "7":
            validar_contraseña()
        elif opcion == "8":
            validar_ip()
        elif opcion == "9":
            break
        else:
            print("Opcion invalida")

if __name__ == "__main__":
    menu()

# Ejemplo de texto para probar las funciones
'''
usuario@gmail.com
Compre 3 libros por 150 quetzales y 2 cuadernos por 30 quetzales.
Los precios son 15.99, 32.50 y 100.75 en la tienda.
Hubo un fallo en el sistema, pero no fue tan mal.
+502 1234-5678
Las fechas importantes son 12/05/2021 y 01/01/2022.
Seguridad123
192.168.1.100
'''