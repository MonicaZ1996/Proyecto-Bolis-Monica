from database import Database

productos_iniciales = [
    ("coco", 30, 1.50),
    ("oreo", 25, 1.75),
    ("mora", 20, 1.50),
    ("fresa", 18, 1.50),
    ("mango", 22, 1.50),
    
]

db = Database()
db.conectar()
db.crear_tablas()

for nombre, cant, precio in productos_iniciales:
    db.cursor.execute(
        "INSERT INTO productos (nombre, cantidad, precio) VALUES (?, ?, ?)",
        (nombre, cant, precio)
    )

db.conn.commit()
db.cerrar()

print("🌟 Productos iniciales cargados con éxito.")