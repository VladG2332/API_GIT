from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://root:te9GmgGXIUlsC0vyP8Mx55o1VYbFIe0d@dpg-cups6bdsvqrc73f5b4gg-a.oregon-postgres.render.com/cetech_oj50' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Estudiante(db.Model):
    __tablename__ = 'alumnos'
    no_control = db.Column(db.String(10), primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    ap_paterno = db.Column(db.String(100), nullable=False)
    ap_materno = db.Column(db.String(100), nullable=False)
    semestre = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'no_control': self.no_control,
            'nombre': self.nombre,
            'ap_paterno': self.ap_paterno,
            'ap_materno': self.ap_materno,
            'semestre': self.semestre
        }

# Crear la base de datos y las tablas
with app.app_context():
    db.create_all()

# Ruta para listar todos los estudiantes
@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Bienvenido a la API de Estudiantes'})

# Ruta para listar todos los estudiantes
@app.route('/estudiantes', methods=['GET'])
def listar_estudiantes():
    estudiantes = Estudiante.query.all()
    return jsonify([estudiante.to_dict() for estudiante in estudiantes])

# Ruta para obtener un estudiante por su número de control
@app.route('/estudiantes/<string:no_control>', methods=['GET'])
def obtener_estudiante(no_control):
    estudiante = Estudiante.query.get_or_404(no_control)
    return jsonify(estudiante.to_dict())

# Ruta para añadir un nuevo estudiante
@app.route('/estudiantes', methods=['POST'])
def nuevo_estudiante():
    data = request.get_json()
    estudiante = Estudiante(
        no_control=data['no_control'],
        nombre=data['nombre'],
        ap_paterno=data['ap_paterno'],
        ap_materno=data['ap_materno'],
        semestre=data['semestre']
    )
    db.session.add(estudiante)
    db.session.commit()
    return jsonify(estudiante.to_dict()), 201
if __name__ == '__main__':
    app.run(debug=True)