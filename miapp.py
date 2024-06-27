#imports
from flask import Flask, render_template, request,redirect
from flask_sqlalchemy import SQLAlchemy

#application init
db = SQLAlchemy()
def create_miapp():
    miapp = Flask(__name__)
    miapp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/test.db'

#iniciar SQLAlchemy con la Aplicacion Flask
    db.init_app(miapp)

    with miapp.app_context():
        db.create_all()
    return miapp


miapp = create_miapp()

#database tables
class Product(db.Model):
    id = db.column(db.Integer, primary_key = True)
    titulo = db.column(db.string(80), nullable = False)
    descripcion = db.column(db.Text,nullable = False)
    Precio = db.column (db.Float, nullable = False)

    def __repr__(self):
        return f'<producto {self.titulo}>'
    
#ruta de productos

@miapp.route('/Producto', methods=['GET','POST'])
def crear_producto():
    if request.method():
        titulo = request.form.get('titulo')
        descrpcion = request.form.get('descripcion')
        precio = request.form.get('precio')
        producto = producto(titulo = titulo, descrpcion = descrpcion, precio=precio)
        db.session.add(producto)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('crear_producto')


#rutas
@miapp.route('/')
def home():
    productos = productos.query.all()
    return render_template('home.html', productos=productos)

@miapp.route('/login')
def login():
    return render_template()

#run application 
if __name__ == '__main__':
    miapp.run(debug=True)