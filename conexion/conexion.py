#conexion a mysql
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mmzm1996",   # ← pon tu contraseña si tienes
        database="bolis_db",
        port=3305      # ← según tu DBeaver (en tu imagen es 3305)
    )
