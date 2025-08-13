# Creacion de diccionarios en Python
diccionario = {
    "nombre": "Sofia",
    "edad": 30,
    "ciudad": "Guatemala"
}

# Acceder a un valor usando su clave
nombre = diccionario["nombre"]
print(nombre)

# Modificar un valor
diccionario["edad"] = 31
print(diccionario)

# Añadir un nuevo par clave-valor
diccionario["profesion"] = "Ingeniera"
print(diccionario)

# Iterar sobre las claves
for clave in diccionario:
    print(clave)

# Iterar sobre los valores
for valor in diccionario.values():
    print(valor)

# Iterar sobre los pares clave-valor
for clave, valor in diccionario.items():
    print(f"Clave: {clave}, Valor: {valor}")