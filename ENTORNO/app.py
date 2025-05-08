from flask import Flask, request, jsonify, render_template_string
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ejemplo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class Articulo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    content = db.Column(db.Text, nullable = False)

@app.route('/')
def home():
    return "Hola Mundo"

@app.route('/articulo', methods=['GET'])
def articulo():
    articulos = Articulo.query.all()
    return jsonify(
        [
            {
                "id": articulo.id,
                "title": articulo.title,
                "content": articulo.content
            } 
            for articulo in articulos
        ]
    )

def __repr__(self):
    return f"Articulo {self.id} - {self.title}"

with app.app_context():
    db.create_all()


@app.route('/crear-articulo', methods=['POST'])
def crear ():
    data =  request.get_json()
    nuevo =  Articulo(
        title=data['title'],
        content=data['content']
    )
    db.session.add(nuevo)
    db.session.commit()
    return jsonify({
        "id": nuevo.id,
        "title": nuevo.title,
        "content": nuevo.content
    }), 201

@app.route('/Crear-articulo', methods=['GET', 'POST'])
def crear_articulo():

    if request.method == 'POST':
        title = request.form.get("title")
        contenido = request.form.get("contenido")
        new_articulo = Articulo(title=title, content=contenido)
        db.session.add(new_articulo)
        db.session.commit()
        return f"Articulo creado: {title} - {contenido}"
    return """
    <form method="POST" acction="/crear-articulo">
        <input type="text" name="title" placeholder="Titulo"><br>
        <textarea name="contenido" placeholder="Contenido"> </textarea> <br>
        <button type="submit">Crear</button>
    </form>
"""


@app.route('/articulo/<int:id>', methods=['PUT'])
def actualizar (id):
    articulo = Articulo.params.get_or_404(id)
    data = request.get_json()
    articulo.title = data['title']
    articulo.content = data['content']
    db.session.commit()
    return jsonify({
        "id": articulo.id,
        "title": articulo.title,
        "content": articulo.content
    }), 201
    
@app.route("/articulo/<int:id>", methods=['DELETE'])
def eliminar(id):
    articulo = Articulo.query.get_or_404(id)
    db.session.delete(articulo)
    db.session.commit()
    return jsonify({"message": "Articulo eliminado"}), 2001




if __name__ == '__main__' :
    app.run(debug=True)