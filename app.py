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

if __name__ == '__main__':
    app.run(debug=True)