from flask import Flask, render_template

app = Flask(__name__)

estudiantes = [
    {'id': 1, 'nombre': 'Ana Garcia', 'edad': 20, 'carrera': 'Ingenieria'},
    {'id': 2, 'nombre': 'Carlos Lopez', 'edad': 22, 'carrera': 'Medicina'},
    {'id': 3, 'nombre': 'Maria Rodriguez', 'edad': 19, 'carrera': 'Psicologia'},
    {'id': 4, 'nombre': 'Jose Martinez', 'edad': 21, 'carrera': 'Derecho'},
    {'id': 5, 'nombre': 'Sofia Gomez', 'edad': 23, 'carrera': 'Arquitectura'}
]

@app.route('/', methods=['GET'])
def inicio():
    return render_template('inicio.html', titulo='Pagina de Inicio')

@app.route('/estudiantes', methods=['GET'])
def lista_estudiantes():
    return render_template('estudiantes.html', 
                         titulo='Lista de Estudiantes', 
                         estudiantes=estudiantes)

@app.route('/estudiante/<int:id>', methods=['GET'])
def detalle_estudiante(id):
    estudiante_encontrado = None
    
    for estudiante in estudiantes:
        if estudiante['id'] == id:
            estudiante_encontrado = estudiante
            break
    
    if estudiante_encontrado is not None:
        titulo_pagina = f'Detalle - {estudiante_encontrado["nombre"]}'
        return render_template('detalle.html', 
                             titulo=titulo_pagina, 
                             estudiante=estudiante_encontrado)
    else:
        return render_template('error.html', 
                             titulo='Error', 
                             mensaje='Estudiante no encontrado'), 404
        
if __name__ == '__main__':
    app.run(debug=True)