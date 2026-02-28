from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

# -----------------------------
#    BASE DE DATOS
# -----------------------------
DB_NAME = "inventario.db"

def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def inicializar_db():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        cantidad INTEGER NOT NULL,
        precio REAL NOT NULL
    );
    """)
    conn.commit()
    conn.close()

inicializar_db()

# -----------------------------
#    RUTAS PRINCIPALES
# -----------------------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/productos")
def productos():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    datos = cursor.fetchall()
    conn.close()
    return render_template("productos.html", productos=datos)

@app.route("/nosotros")
def nosotros():
    return render_template("nosotros.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

# -----------------------------
#      CRUD
# -----------------------------
@app.route("/agregar", methods=["POST"])
def agregar():
    nombre = request.form["nombre"]
    cantidad = request.form["cantidad"]
    precio = request.form["precio"]

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO productos (nombre, cantidad, precio) VALUES (?, ?, ?)",
                   (nombre, cantidad, precio))
    conn.commit()
    conn.close()
    return redirect(url_for("productos"))

@app.route("/eliminar/<int:id>")
def eliminar(id):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM productos WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for("productos"))

@app.route("/actualizar/<int:id>", methods=["POST"])
def actualizar(id):
    nombre = request.form["nombre"]
    cantidad = request.form["cantidad"]
    precio = request.form["precio"]

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE productos
        SET nombre = ?, cantidad = ?, precio = ?
        WHERE id = ?
    """, (nombre, cantidad, precio, id))
    conn.commit()
    conn.close()
    return redirect(url_for("productos"))

# -----------------------------
#    EJECUCIÓN LOCAL
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)