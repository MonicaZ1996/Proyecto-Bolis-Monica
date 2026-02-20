from flask import Flask, render_template

app = Flask(__name__)

# ----------------------------
# RUTA PRINCIPAL
# ----------------------------
@app.route('/')
def inicio():
    return render_template('index.html')

# ----------------------------
# RUTA ACERCA DE
# ----------------------------
@app.route('/about')
def about():
    return render_template('about.html')

# ----------------------------
# RUTA PRODUCTOS
# ----------------------------
@app.route('/productos')
def productos():
    lista_productos = [
        {"nombre": "Boli de Fresa", "precio": 0.50},
        {"nombre": "Boli de Mango", "precio": 0.60},
        {"nombre": "Boli de Oreo", "precio": 0.90},
        {"nombre": "Boli de Maracuyá", "precio": 0.70},
    ]
    return render_template('productos.html', productos=lista_productos)

# ----------------------------
# RUTA CLIENTE DINÁMICA
# ----------------------------
@app.route('/cliente/<nombre>')
def cliente(nombre):
    return render_template('cliente.html', nombre=nombre)

# ----------------------------
# RUTA FACTURA
# ----------------------------
@app.route('/factura/<producto>')
def factura(producto):
    return render_template('factura.html', producto=producto)

# ----------------------------
# EJECUCIÓN LOCAL
# ----------------------------
if __name__ == '__main__':
    app.run(debug=True)