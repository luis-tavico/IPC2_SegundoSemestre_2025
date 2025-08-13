# Creacion de listas en Python
lista = [10, 20, 30, "hola", True]

# Agregar elementos
lista.append(40)
print(lista)
lista.insert(2, 25) # Insertar en una posicion específica
print(lista)

# Eliminar elementos
lista.remove("hola")
print(lista)
lista.pop(0) # Eliminar por indice
print(lista)

# Modificar elementos
lista[1] = 35
print(lista)

# Operaciones
# Longitud
print(len(lista))
print(lista)
# Busqueda
print(20 in lista)
# Índice
print(lista.index(35))

# Iteracion
for elemento in lista:
    print(elemento)