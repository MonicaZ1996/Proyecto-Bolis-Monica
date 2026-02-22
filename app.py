from flask import Flask, render_template

app = Flask(__name__)

# Lista de productos
lista_producto = [
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
        "imagen": "/static/img/coco.jpg"
    },
    {
        "nombre": "Boli de Mora",
        "descripcion": "Boli hecho con mora sacada de la planta a la olla.",
        "precio": 1.00,
        "imagen": "/static/img/mora.jpg"
    },
    {
        "nombre": "Boli de Oreo",
        "descripcion": "Boli hecho con la mejor galleta Oreo.",
        "precio": 1.00,
        "imagen": "/static/img/oreo.jpg"
    }
]

@app.route("/")
def index():
    return render_template("index.html", productos=lista_producto)

# Solo para ejecución local; Render usa gunicorn
if __name__ == "__main__":
    app.run(debug=True)