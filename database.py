import sqlite3

class Database:
    def __init__(self, db_name="inventario.db"):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def conectar(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def crear_tablas(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                cantidad INTEGER DEFAULT 0,
                precio REAL NOT NULL
            )
        """)
        self.conn.commit()

    def cerrar(self):
        if self.conn:
            self.conn.close()