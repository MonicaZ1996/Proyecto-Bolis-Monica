from flask import Flask, render_template, request, redirect, url_for
from inventario.bd import db
from inventario.productos import Producto
from inventario.inventario import Inventario
import os

app = Flask(__name__)

# -------- CONFIGURACIÓN SQLITE COMPATIBLE CON RENDER --------
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(BASE_DIR, "inventario.db")
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# Crear base de datos en tiempo de ejecución (NO en build)
with app.app_context():
    try:
        db.create_all()
    except Exception as e:
        print("Error creando base de datos:", e)

# -------- OBJETO INVENTARIO --------
inventario = Inventario()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/productos")
def productos():
    productos_lista = Producto.query.all()
    return render_template("productos.html", productos=productos_lista)


@app.route("/agregar", methods=["GET", "POST"])
def agregar():
    if request.method == "POST":
        nombre = request.form["nombre"]
        precio = request.form["precio"]
        cantidad = request.form["cantidad"]

        nuevo = Producto(nombre=nombre, precio=precio, cantidad=cantidad)
        db.session.add(nuevo)
        db.session.commit()

        inventario.guardar_txt(nombre, precio, cantidad)
        inventario.guardar_json(nombre, precio, cantidad)
        inventario.guardar_csv(nombre, precio, cantidad)

        return redirect(url_for("productos"))

    return render_template("producto_form.html")


@app.route("/contactos")
def contactos():
    return render_template("contactos.html")


@app.route("/datos")
def datos():
    txt = inventario.leer_txt()
    json_datos = inventario.leer_json()
    csv_datos = inventario.leer_csv()

    return render_template("datos.html", txt=txt, json=json_datos, csv=csv_datos)


# -------- NO EJECUTAR DEBUG EN RENDER --------
if __name__ == "__main__":
    app.run()