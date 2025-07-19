# VARIABLES, EXPRESIONES, SENTENCIAS Y TIPOS DE DATOS

nombre_lenguaje = "Python"  # Tipo string, podemos usar "" o ''
lanzamiento = 1991          # Tipo entero
años = 2025 - 1991          # Tipo entero
version_actual = 3.13       # Tipo float
vigente = True              # Tipo booleano
caracteristicas = """
Sintaxis clara y legible
Tipado dinamico
Gran cantidad de bibliotecas
Multiplataforma
Comunidad activa
"""

# IMPRIMIR VARIABLES

print("Nombre del lenguaje:", nombre_lenguaje)
print("Lanzamiento: {}".format(lanzamiento))    #usando format()
print(f"Años: {años}")                          #usando f-strings
print(f"Version actual: {version_actual}")
print("Vigente:", vigente)
print("Caracteristicas:", caracteristicas)

# OPERADORES

# OPERADORES ARITMETICOS

a = 10
b = 3

print("Suma:", a+b)
print("Resta:", a-b)
print("Multiplicacion:", a*b)
print("Division:", a/b)
print("Modulo:", a%b)
print("Exponente:", a**b)

# OPERADORES ARITMETICOS

x = 5
y = 10

print(x > y)
print(x < y)
print(x == y)
print(x != y)
print(x >= y) 
print(x <= y)

# OPERADORES LOGICOS

verdadero = True
falso = False

print(verdadero and falso)
print(verdadero or falso)
print(not verdadero)

# ENTRADA DE DATOS

nombre = input("Ingrese un nombre: ")
edad = input("Ingrese una edad: ")
print(f"¡Hola me llamo {nombre} y tengo {edad} años!")

# CONVERSION DE TIPOS (CASTING)

# cadena a entero
entero = int("10")
print(type(entero))

# cadena a flotante
flotante = float("12.5")
print(type(flotante))

# entero a cadena
cadena = str(10)
print(type(cadena))

# flotante a cadena
cadena = str(12.5)
print(type(cadena))

# EXCEPCIONES

try:
    valor = int(input("Ingrese un numero:"))
    total = valor + 5
    print(total)
except ValueError:
    print("Ingrese solo numeros.")

# CONDICIONALES

edad = int(input("Ingresa tu edad: "))

if edad < 12:
    print("Eres un niño.")
elif 12 <= edad < 18:
    print("Eres un adolescente.")
elif 18 <= edad < 60:
    print("Eres un adulto.")
else:
    print("Eres un adulto mayor.")

# ITERACIONES

# FOR

for i in range(1, 5): # range(start, stop, step)
   print(i)

# WHILE

contador = 1

while contador <= 5:
    print(f"El contador es: {contador}")
    contador += 1

# FUNCIONES

# FUNCION SIN PARAMETRO Y SIN RETORNO

def saludar():
    print("¡Hola, bienvenido!")

saludar()

# FUNCION CON PARAMETRO Y CON RETORNO

def suma(a, b):
    return a + b

resultado = suma(5, 3)
print(resultado)

# FUNCION CON PARAMETRO Y CON RETORNO MULTIPLE

def operaciones(a, b):
    return a + b, a - b, a * b, a / b

suma, resta, producto, division = operaciones(10, 5)
print(suma, resta, producto, division)

# STRINGS

# Concatenacion
saludo = "Hola" + " " + "Mundo"
print(saludo)

# Repeticion
var = "Hola " * 3
print(var)

# Acceso a Caracteres
palabra = "Python"
print(palabra[0])

# Slicing
frase = "¡Aprendamos Python!"
print(frase[1:10])  

# Metodos de String
texto = "   Hola, Mundo!   "
print(texto.upper())                    # Convierte la cadena a mayusculas.
print(texto.lower())                    # Convierte la cadena a minusculas.
print(texto.strip())                    # Elimina los espacios en blanco pero solo los iniciales y los finales de la cadena.
print(texto.replace("Mundo", "Python")) # Reemplaza un valor por otro.
print(texto.split(","))                 # Divide la cadena en una lista de subcadenas.
print(len(palabra))                     # Devuelve la longitud de la cadena.

# SECUENCIAS DE ESCAPE
# Permiten representar caracteres que de otra manera serian dificiles o imposibles de incluir directamente en una cadena.
"""
\n salto de linea
\t tabulacion
\" comilla doble
\' comilla simple
\\ barra invertida
"""