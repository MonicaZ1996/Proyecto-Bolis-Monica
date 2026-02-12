from flask import Flask

app = Flask(__name__)

# Ruta principal
@app.route('/')
def inicio():
    return "<h1>Bienvenidos a Bolis de Mónica</h1><p>Los mejores bolis de sabores 🍓🍍🍉</p>"

# Ruta dinámica
@app.route('/producto/<nombre>')
def producto(nombre):
    return f"<h2>Producto solicitado: {nombre}</h2><p>Consulta exitosa en el sistema de Bolis de Mónica.</p>"

if __name__ == '__main__':
    app.run(debug=True)
