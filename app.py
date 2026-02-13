from flask import Flask, render_template

app = Flask(__name__)

# --------------------------
#   Página principal
# --------------------------
@app.route('/')
def inicio():
    return render_template("index.html")


# --------------------------
#   Ruta dinámica: Producto
# --------------------------
@app.route('/producto/<nombre>')
def producto(nombre):
    return render_template("producto.html", nombre=nombre.capitalize())


# --------------------------
#   Ruta dinámica: Usuario
# --------------------------
@app.route('/usuario/<nombre>')
def usuario(nombre):
    mensaje = f"Bienvenido/a {nombre.capitalize()}, gracias por visitar Bolis de Mónica."
    return render_template("usuario.html", nombre=nombre.capitalize(), mensaje=mensaje)


# --------------------------
#   Manejo de errores elegante
# --------------------------
@app.errorhandler(404)
def pagina_no_encontrada(e):
    return render_template("error.html"), 404


if __name__ == '__main__':
    app.run(debug=True)

