from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# ------------------------
#   MODELO POO
# ------------------------

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio


class Inventario:
    def __init__(self):
        self.crear_tabla()

    def conectar(self):
        return sqlite3.connect("inventario.db")

    def crear_tabla(self):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS productos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                cantidad INTEGER NOT NULL,
                precio REAL NOT NULL
            )
        """)
        con.commit()
        con.close()

    def agregar(self, nombre, cantidad, precio):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("INSERT INTO productos(nombre, cantidad, precio) VALUES (?,?,?)",
                       (nombre, cantidad, precio))
        con.commit()
        con.close()

    def obtener_todos(self):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM productos")
        datos = cursor.fetchall()
        con.close()
        return datos

    def obtener_por_id(self, id):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("SELECT * FROM productos WHERE id=?", (id,))
        dato = cursor.fetchone()
        con.close()
        return dato

    def actualizar(self, id, nombre, cantidad, precio):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("""
            UPDATE productos 
            SET nombre=?, cantidad=?, precio=? 
            WHERE id=?
        """, (nombre, cantidad, precio, id))
        con.commit()
        con.close()

    def eliminar(self, id):
        con = self.conectar()
        cursor = con.cursor()
        cursor.execute("DELETE FROM productos WHERE id=?", (id,))
        con.commit()
        con.close()


inventario = Inventario()

# ------------------------
#   RUTAS PRINCIPALES
# ------------------------

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/productos")
def productos():
    return render_template("productos.html")

@app.route("/nosotros")
def nosotros():
    return render_template("nosotros.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

# ------------------------
#   CRUD INVENTARIO
# ------------------------

@app.route("/inventario")
def ver_inventario():
    datos = inventario.obtener_todos()
    return render_template("inventario.html", productos=datos)

@app.route("/agregar", methods=["GET", "POST"])
def agregar():
    if request.method == "POST":
        nombre = request.form["nombre"]
        cantidad = int(request.form["cantidad"])
        precio = float(request.form["precio"])
        inventario.agregar(nombre, cantidad, precio)
        return redirect("/inventario")
    return render_template("agregar.html")

@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    producto = inventario.obtener_por_id(id)

    if request.method == "POST":
        nombre = request.form["nombre"]
        cantidad = request.form["cantidad"]
        precio = request.form["precio"]
        inventario.actualizar(id, nombre, cantidad, precio)
        return redirect("/inventario")

    return render_template("editar.html", producto=producto)

@app.route("/eliminar/<int:id>")
def eliminar(id):
    inventario.eliminar(id)
    return redirect("/inventario")


# Render necesita esto:
if __name__ == "__main__":
    app.run(debug=True)