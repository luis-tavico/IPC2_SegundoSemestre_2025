from flask import Flask, request, jsonify
import json

app = Flask(__name__)

estudiantes = [
    {"id": 1, "nombre": "Diego Perez", "carrera": "Ingenieria", "edad": 21, "activo": True, "promedio": 75.0},
    {"id": 2, "nombre": "Maria Lopez", "carrera": "Medicina", "edad": 22, "activo": True, "promedio": 66.0},
]

# GET: Obtener todos los estudiantes
@app.route('/estudiantes', methods=['GET'])
def obtener_estudiantes():
    return jsonify(estudiantes)

# POST: Agregar un estudiante
@app.route('/estudiantes', methods=['POST'])
def agregar_estudiante():
    nuevo = request.get_json()
    estudiantes.append(nuevo)
    return jsonify({"mensaje": "Estudiante agregado", "estudiante": nuevo}), 201

# PUT: Modificar estudiante por ID
@app.route('/estudiantes/<int:id>', methods=['PUT'])
def actualizar_estudiante(id):
    data = request.get_json()
    for estudiante in estudiantes:
        if estudiante["id"] == id:
            estudiante.update(data)
            return jsonify({"mensaje": "Estudiante actualizado", "estudiante": estudiante}), 200
    return jsonify({"error": "Estudiante no encontrado"}), 404

# DELETE: Eliminar estudiante por ID
@app.route('/estudiantes/<int:id>', methods=['DELETE'])
def eliminar_estudiante(id):
    for estudiante in estudiantes:
        if estudiante["id"] == id:
            estudiantes.remove(estudiante)
            return jsonify({"mensaje": "Estudiante eliminado"}), 200
    return jsonify({"error": "Estudiante no encontrado"}), 404

# CARGA MASIVA: Desde archivo JSON
@app.route('/estudiantes/carga_masiva', methods=['POST'])
def carga_masiva():
    archivo = request.files['archivo']
    if not archivo:
        return jsonify({"error": "No se proporciono archivo"}), 400
    
    data = json.load(archivo)
    if "estudiantes" in data:
        estudiantes.extend(data["estudiantes"])
        return jsonify({"mensaje": "Carga masiva realizada", "total_agregados": len(data["estudiantes"])}), 201
    else:
        return jsonify({"error": "Formato JSON incorrecto"}), 400

if __name__ == '__main__':
    app.run(debug=True)