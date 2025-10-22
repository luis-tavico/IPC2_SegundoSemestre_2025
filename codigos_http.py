from flask import Flask, jsonify, redirect, request, make_response, Response
import json

app = Flask(__name__)

# ----------------------------------- CODIGOS DE EXITO 2XX -----------------------------------
@app.route('/api/exito')
def exito():
    # 200 - OK: La solicitud ha tenido éxito
    return jsonify({
        "mensaje": "Solicitud exitosa",
        "datos": {"id": 1, "nombre": "Ejemplo"}
    }), 200

@app.route('/api/crear', methods=['POST'])
def crear():
    # 201 - Created: La solicitud ha tenido éxito y se ha creado un nuevo recurso
    data = request.get_json()
    return jsonify({
        "mensaje": "Recurso creado exitosamente",
        "id": 123,
        "recurso": data
    }), 201

@app.route('/api/actualizar', methods=['PUT'])
def actualizar():
    # 204 - No Content: La solicitud se ha completado con éxito pero no hay contenido para enviar
    return "", 204

@app.route('/api/multiple-estado')
def multiple_estado():
    # 207 - Multi-Status: Proporciona información sobre múltiples recursos
    return jsonify({
        "multistatus": [
            {
                "recurso": "/archivos/documento1.txt",
                "estado": 200,
                "mensaje": "OK"
            },
            {
                "recurso": "/procesos/documento2.txt",
                "estado": 202,
                "mensaje": "Actualizado"

            }
        ]
    }), 207

# -------------------------------- CODIGOS DE REDIRECCION 3XX --------------------------------
@app.route('/api/redireccion')
def redireccion():
    # 301 - Moved Permanently: El recurso solicitado ha sido movido permanentemente
    return redirect('/api/nueva-ubicacion', code=301)

@app.route('/api/redireccion-temporal')
def redireccion_temporal():
    # 302 - Found: El recurso se ha movido temporalmente
    return redirect('/api/ubicacion-temporal', code=302)

@app.route('/api/nueva-ubicacion')
def nueva_ubicacion():
    return jsonify({"mensaje": "Esta es la nueva ubicación permanente"}), 200

@app.route('/api/ubicacion-temporal')
def ubicacion_temporal():
    return jsonify({"mensaje": "Esta es la ubicación temporal"}), 200

# ---------------------------------- ERRORES DEL CLIENTE 4XX ---------------------------------
@app.route('/api/no-autorizado')
def no_autorizado():
    # 401 - Unauthorized: El cliente debe autenticarse para obtener el recurso
    return jsonify({
        "error": "No autorizado",
        "mensaje": "Se requiere autenticación para acceder a este recurso"
    }), 401

@app.route('/api/prohibido')
def prohibido():
    # 403 - Forbidden: El servidor entiende la solicitud pero se niega a autorizarla
    return jsonify({
        "error": "Prohibido",
        "mensaje": "No tienes permisos para acceder a este recurso"
    }), 403

@app.route('/api/recurso-inexistente')
def recurso_inexistente():
    # 404 - Not Found: El servidor no pudo encontrar el recurso solicitado
    return jsonify({
        "error": "No encontrado",
        "mensaje": "El recurso solicitado no existe"
    }), 404

@app.route('/api/validacion', methods=['POST'])
def validacion():
    # 422 - Unprocessable Entity: La solicitud está bien formada pero no se puede procesar debido a errores semánticos
    return jsonify({
        "error": "Entidad no procesable",
        "errores": [
            {"campo": "email", "mensaje": "Formato de email inválido"},
            {"campo": "edad", "mensaje": "La edad debe ser un número positivo"}
        ]
    }), 422

# --------------------------------- ERRORES DEL SERVIDOR 5XX ---------------------------------
@app.route('/api/error-servidor')
def error_servidor():
    # 500 - Internal Server Error: Error inesperado en el servidor
    return jsonify({
        "error": "Error interno del servidor",
        "mensaje": "Ocurrió un error inesperado"
    }), 500

@app.route('/api/servicio-no-disponible')
def servicio_no_disponible():
    # 503 - Service Unavailable: El servidor no está listo para manejar la solicitud
    return jsonify({
        "error": "Servicio no disponible",
        "mensaje": "El servicio está temporalmente no disponible, intente más tarde",
        "tiempoEstimado": "10 minutos"
    }), 503

@app.route('/')
def inicio():
    return """
    <h1>Ejemplos de codigos de estado HTTP en Flask</h1>
    <ul>
        <li><a href="/api/exito">200 OK</a></li>
        <li><a href="/api/crear">201 Created</a></li>
        <li><a href="/api/actualizar">204 No Content</a></li>
        <li><a href="/api/multiple-estado">207 Multi-Status</a></li>
        <li><a href="/api/redireccion">301 Moved Permanently</a></li>
        <li><a href="/api/redireccion-temporal">302 Found</a></li>
        <li><a href="/api/no-autorizado">401 Unauthorized</a></li>
        <li><a href="/api/prohibido">403 Forbidden</a></li>
        <li><a href="/api/recurso-inexistente">404 Not Found</a></li>
        <li><a href="/api/validacion">422 Unprocessable Entity</a></li>
        <li><a href="/api/error-servidor">500 Internal Server Error</a></li>
        <li><a href="/api/servicio-no-disponible">503 Service Unavailable</a></li>
    </ul>
    """

if __name__ == '__main__':
    app.run(debug=True, port=5000)