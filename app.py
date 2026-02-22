from flask import Flask, render_template

app = Flask(__name__)

# ---- LISTA DE PRODUCTOS ----
lista_productos = [
    {
        "nombre": "Boli de Fresa",
        "descripcion": "Delicioso boli de fresa natural.",
        "precio": 1.00,
        "imagen": "/static/img/fresa.jpg"
    },
    {
        "nombre": "Boli de Mango",
        "descripcion": "Refrescante boli de mango maduro.",
        "precio": 1.00,
        "imagen": "/static/img/mango.jpg"
    },
    {
        "nombre": "Boli de Coco",
        "descripcion": "Boli hecho con coco fresco.",
        "precio": 1.00,
        "imagen": "/static/img/sandia.jpg"
    },
    {
        "nombre": "Boli de Mora",
        "descripcion": "Boli hecho con mora natural.",
        "precio": 1.00,
        "imagen": "/static/img/mora.jpg"
    },
    {
        "nombre": "Boli de Oreo",
        "descripcion": "Boli hecho con galletas Oreo.",
        "precio": 1.00,
        "imagen": "/static/img/sandia.jpg"
    }
]

# -------------------- RUTAS --------------------

@app.route("/")
def index():
    return render_template("index.html", productos=lista_productos)

@app.route("/productos")
def productos():
    return render_template("productos.html", productos=lista_productos)

@app.route("/nosotros")
def nosotros():
    return render_template("nosotros.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")


if __name__ == "__main__":
    app.run(debug=True)