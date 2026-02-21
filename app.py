from flask import Flask, render_template

app = Flask(__name__)

# -------------------------
#   RUTA PRINCIPAL
# -------------------------
@app.route('/')
def inicio():
    return render_template("index.html")

# -------------------------
#   RUTA DE PRODUCTOS
# -------------------------
@app.route('/productos')
def productos():
    lista_productos = [
        {"nombre": "Boli de Fresa", "precio": 1.00, "imagen": "fresa.png"},
        {"nombre": "Boli de Mango", "precio": 1.00, "imagen": "mango.jpg"},
        {"nombre": "Boli de Oreo", "precio": 1.50, "imagen": "oreo.png"},
        {"nombre": "Boli de Coco", "precio": 1.00, "imagen": "coco.jpg"},
        {"nombre": "Boli de Mora", "precio": 1.00, "imagen": "mora.png"},
    ]
    return render_template("productos.html", productos=lista_productos)
# -------------------------
#   RUTA DINÁMICA
# -------------------------
@app.route('/producto/<nombre>')
def producto(nombre):
    return render_template("detalle_producto.html", nombre=nombre)

if __name__ == '__main__':
    app.run(debug=True)