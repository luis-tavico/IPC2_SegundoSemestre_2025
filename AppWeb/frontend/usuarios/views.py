import requests
from django.shortcuts import render, redirect

API_URL = "http://127.0.0.1:5000/usuarios"

# Leer usuarios
def lista_usuarios(request):
    respuesta = requests.get(API_URL)
    usuarios = respuesta.json() if respuesta.status_code == 200 else []
    return render(request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios})

# Crear usuario
def crear_usuario(request):
    if request.method == "POST":
        nombre = request.POST['nombre']
        email = request.POST['email']
        edad = request.POST['edad']
        requests.post(API_URL, json={"nombre": nombre, "email": email, "edad": edad})
        return redirect('lista_usuarios')
    return render(request, 'usuarios/crear_usuario.html')

# Actualizar usuario
def actualizar_usuario(request, id):
    if request.method == "POST":
        nombre = request.POST['nombre']
        email = request.POST['email']
        edad = request.POST['edad']
        requests.put(f"{API_URL}/{id}", json={"nombre": nombre, "email": email, "edad": edad})
        return redirect('lista_usuarios')

    usuario = requests.get(f"{API_URL}/{id}").json()
    return render(request, 'usuarios/actualizar_usuario.html', {'usuario': usuario})

# Eliminar usuario
def eliminar_usuario(request, id):
    requests.delete(f"{API_URL}/{id}")
    return redirect('lista_usuarios')