from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
import jwt
import datetime

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config['SECRET_KEY'] = 'clave-secreta-supersegura'

# Simulación de una base de datos en memoria
usuarios = {
    "admin": bcrypt.generate_password_hash("admin123").decode('utf-8')
}

productos = ["Laptop", "Smartphone", "Tablet"]

# Ruta para registro de usuario
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    usuario = data['usuario']
    password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    if usuario in usuarios:
        return jsonify({"mensaje": "Usuario ya existe"}), 400
    usuarios[usuario] = password
    return jsonify({"mensaje": "Usuario registrado exitosamente"}), 201

# Ruta para login
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    usuario = data['usuario']
    password = data['password']

    if usuario not in usuarios or not bcrypt.check_password_hash(usuarios[usuario], password):
        return jsonify({"mensaje": "Credenciales inválidas"}), 401

    token = jwt.encode({
        'usuario': usuario,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }, app.config['SECRET_KEY'], algorithm="HS256")

    return jsonify({'token': token})

# Endpoint protegido
@app.route('/productos', methods=['GET'])
def get_productos():
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({'error': 'Token requerido'}), 401

    try:
        jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        return jsonify({'productos': productos})
    except jwt.ExpiredSignatureError:
        return jsonify({'error': 'Token expirado'}), 403
    except jwt.InvalidTokenError:
        return jsonify({'error': 'Token inválido'}), 403
    
if __name__ == '__main__':
    app.run(debug=True)