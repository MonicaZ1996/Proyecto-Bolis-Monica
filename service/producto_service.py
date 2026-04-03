from conexion.conexion import get_connection

def obtener_productos():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM producto")
    datos = cursor.fetchall()

    conn.close()
    return datos


def insertar_producto(nombre, precio, stock):
    conn = get_connection()
    cursor = conn.cursor()

    sql = "INSERT INTO producto (nombre, precio, stock) VALUES (%s, %s, %s)"
    cursor.execute(sql, (nombre, precio, stock))

    conn.commit()
    conn.close()


def obtener_producto(id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM producto WHERE id_producto=%s", (id,))
    dato = cursor.fetchone()

    conn.close()
    return dato


def actualizar_producto(id, nombre, precio, stock):
    conn = get_connection()
    cursor = conn.cursor()

    sql = "UPDATE producto SET nombre=%s, precio=%s, stock=%s WHERE id_producto=%s"
    cursor.execute(sql, (nombre, precio, stock, id))

    conn.commit()
    conn.close()


def eliminar_producto(id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM producto WHERE id_producto=%s", (id,))
    conn.commit()

    conn.close()