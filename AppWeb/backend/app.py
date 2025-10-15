from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite peticiones desde el frontend

# Base de datos simulada
usuarios = [
    {"id": 1, "nombre": "Juan Perez", "email": "juan@gmail.com", "edad": 30},
    {"id": 2, "nombre": "Maria Gomez", "email": "maria@gmail.com", "edad": 25},
    {"id": 3, "nombre": "Carlos Lopez", "email": "carlos@gmail.com", "edad": 35}
]

def obtener_usuario_por_id(id):
    for usuario in usuarios:
        if usuario["id"] == id:
            return usuario
    return None

# Obtener todos los usuarios
@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify(usuarios)

# Obtener un solo usuario por ID
@app.route('/usuarios/<int:id>', methods=['GET'])
def obtener_usuario(id):
    usuario = obtener_usuario_por_id(id)
    if usuario:
        return jsonify(usuario)
    return jsonify({"error": "Usuario no encontrado"}), 404

# Crear un usuario
@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    nuevo_usuario = request.json
    nuevo_usuario["id"] = len(usuarios) + 1
    usuarios.append(nuevo_usuario)
    return jsonify(nuevo_usuario), 201

# Actualizar un usuario
@app.route('/usuarios/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    for usuario in usuarios:
        if usuario["id"] == id:
            usuario.update(request.json)
            return jsonify(usuario)
    return jsonify({"error": "Usuario no encontrado"}), 404

# Eliminar un usuario
@app.route('/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    global usuarios
    usuarios = [u for u in usuarios if u["id"] != id]
    return jsonify({"message": "Usuario eliminado"}), 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)