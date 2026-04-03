from flask import Flask, render_template, request, redirect, send_file
from conexion.conexion import get_connection
from reportlab.pdfgen import canvas

app = Flask(__name__)

# INICIO
@app.route("/")
def inicio():
    return render_template("index.html")

# LISTAR PRODUCTOS
@app.route("/productos")
def productos():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM productos")
    datos = cursor.fetchall()

    conn.close()
    return render_template("productos/lista.html", productos=datos)

# CREAR
@app.route("/productos/crear", methods=["GET", "POST"])
def crear():
    if request.method == "POST":
        nombre = request.form["nombre"]
        precio = request.form["precio"]
        stock = request.form["stock"]

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO productos (nombre, precio, stock) VALUES (%s,%s,%s)",
            (nombre, precio, stock)
        )

        conn.commit()
        conn.close()

        return redirect("/productos")

    return render_template("productos/crear.html")

# EDITAR
@app.route("/productos/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == "POST":
        nombre = request.form["nombre"]
        precio = request.form["precio"]
        stock = request.form["stock"]

        cursor.execute(
            "UPDATE productos SET nombre=%s, precio=%s, stock=%s WHERE id_producto=%s",
            (nombre, precio, stock, id)
        )

        conn.commit()
        conn.close()

        return redirect("/productos")

    cursor.execute("SELECT * FROM productos WHERE id_producto=%s", (id,))
    producto = cursor.fetchone()

    conn.close()

    return render_template("productos/editar.html", producto=producto)

# ELIMINAR
@app.route("/productos/eliminar/<int:id>")
def eliminar(id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM productos WHERE id_producto=%s", (id,))
    conn.commit()

    conn.close()

    return redirect("/productos")

# PDF
@app.route("/reporte")
def reporte():
    archivo = "reporte.pdf"
    c = canvas.Canvas(archivo)

    c.drawString(100, 800, "Reporte de Productos")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT nombre, precio, stock FROM productos")
    datos = cursor.fetchall()

    y = 750
    for p in datos:
        c.drawString(100, y, f"{p[0]} - ${p[1]} - Stock: {p[2]}")
        y -= 20

    conn.close()
    c.save()

    return send_file(archivo, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)