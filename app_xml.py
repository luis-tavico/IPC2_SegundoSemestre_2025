from flask import Flask, request, Response
import xmltodict

app = Flask(__name__)

estudiantes = [
    {"id": 1, "nombre": "Diego Perez", "carrera": "Ingenieria", "edad": 21, "activo": True, "promedio": 75.0},
    {"id": 2, "nombre": "Maria Lopez", "carrera": "Medicina", "edad": 22, "activo": True, "promedio": 66.0},
]

# Convertir a XML
def to_xml(data):
    return Response(
        xmltodict.unparse({"response": data}, pretty=True),
        mimetype="application/xml"
    )

# GET: Obtener todos los estudiantes
@app.route('/estudiantes', methods=['GET'])
def obtener_estudiantes():
    return to_xml({"estudiantes": {"estudiante": estudiantes}})

# POST: Agregar un estudiante
@app.route('/estudiantes', methods=['POST'])
def agregar_estudiante():
    data = xmltodict.parse(request.data)
    nuevo = data["estudiante"]

    # Conversión de tipos
    nuevo["id"] = int(nuevo["id"])
    nuevo["edad"] = int(nuevo["edad"])
    nuevo["activo"] = nuevo["activo"].lower() == "true"
    nuevo["promedio"] = float(nuevo["promedio"])

    estudiantes.append(nuevo)
    return to_xml({"mensaje": "Estudiante agregado", "estudiante": nuevo})

# PUT: Actualizar estudiante por ID
@app.route('/estudiantes/<int:id>', methods=['PUT'])
def actualizar_estudiante(id):
    data = xmltodict.parse(request.data)
    cambios = data["estudiante"]

    for estudiante in estudiantes:
        if estudiante["id"] == id:
            estudiante.update(cambios)
            return to_xml({"mensaje": "Estudiante actualizado", "estudiante": estudiante})
    return to_xml({"error": "Estudiante no encontrado"})

# DELETE: Eliminar estudiante por ID
@app.route('/estudiantes/<int:id>', methods=['DELETE'])
def eliminar_estudiante(id):
    for estudiante in estudiantes:
        if estudiante["id"] == id:
            estudiantes.remove(estudiante)
            return to_xml({"mensaje": "Estudiante eliminado"})
    return to_xml({"error": "Estudiante no encontrado"})

# CARGA MASIVA desde archivo XML
@app.route('/estudiantes/carga_masiva', methods=['POST'])
def carga_masiva():
    data = xmltodict.parse(request.data)
    
    if "estudiantes" in data and "estudiante" in data["estudiantes"]:
        nuevos = data["estudiantes"]["estudiante"]
        if isinstance(nuevos, list):
            estudiantes.extend(nuevos)
            total = len(nuevos)
        else:
            estudiantes.append(nuevos)
            total = 1
        return to_xml({"mensaje": "Carga masiva realizada", "total_agregados": total})
    else:
        return to_xml({"error": "Formato XML incorrecto"})

if __name__ == '__main__':
    app.run(debug=True)