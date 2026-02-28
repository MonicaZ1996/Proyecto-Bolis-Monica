from database import Database


# =============================
# Clase Producto
# =============================
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"[{self.id}] {self.nombre} | Cant: {self.cantidad} | Precio: ${self.precio:.2f}"


# =============================
# Clase Inventario
# =============================
class Inventario:
    def __init__(self):
        self.db = Database()
        self.db.conectar()
        self.db.crear_tablas()

    # CRUD ==========================

    def agregar_producto(self, nombre, cantidad, precio):
        self.db.cursor.execute(
            "INSERT INTO productos (nombre, cantidad, precio) VALUES (?, ?, ?)",
            (nombre, cantidad, precio)
        )
        self.db.conn.commit()
        print("\n✅ Producto agregado correctamente.\n")

    def eliminar_producto(self, id_producto):
        self.db.cursor.execute("DELETE FROM productos WHERE id=?", (id_producto,))
        self.db.conn.commit()
        print("\n🗑 Producto eliminado.\n")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if cantidad is not None:
            self.db.cursor.execute(
                "UPDATE productos SET cantidad=? WHERE id=?", (cantidad, id_producto)
            )
        if precio is not None:
            self.db.cursor.execute(
                "UPDATE productos SET precio=? WHERE id=?", (precio, id_producto)
            )

        self.db.conn.commit()
        print("\n🔄 Producto actualizado.\n")

    def buscar_producto(self, nombre):
        self.db.cursor.execute(
            "SELECT * FROM productos WHERE nombre LIKE ?", ('%' + nombre + '%',)
        )
        resultados = self.db.cursor.fetchall()

        if resultados:
            for r in resultados:
                print(Producto(*r))
        else:
            print("\n❌ No se encontraron coincidencias.\n")

    def mostrar_todos(self):
        self.db.cursor.execute("SELECT * FROM productos")
        productos = self.db.cursor.fetchall()

        if productos:
            print("\n📦 INVENTARIO COMPLETO:\n")
            for p in productos:
                print(Producto(*p))
        else:
            print("\n📭 No hay productos en el inventario.\n")


# =============================
# MENÚ DE USUARIO
# =============================
def menu():
    inv = Inventario()

    while True:
        print("""
===============================
🍦 SISTEMA DE INVENTARIO - HELADERÍA
===============================
1. Añadir producto
2. Eliminar producto
3. Actualizar producto
4. Buscar producto por nombre
5. Mostrar inventario completo
6. Salir
""")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inv.agregar_producto(nombre, cantidad, precio)

        elif opcion == "2":
            idp = int(input("ID del producto a eliminar: "))
            inv.eliminar_producto(idp)

        elif opcion == "3":
            idp = int(input("ID del producto: "))
            cantidad = input("Nueva cantidad (ENTER para no cambiar): ")
            precio = input("Nuevo precio (ENTER para no cambiar): ")

            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None

            inv.actualizar_producto(idp, cantidad, precio)

        elif opcion == "4":
            nombre = input("Buscar por nombre: ")
            inv.buscar_producto(nombre)

        elif opcion == "5":
            inv.mostrar_todos()

        elif opcion == "6":
            print("\n👋 Saliendo del sistema...\n")
            break

        else:
            print("\n❌ Opción inválida.\n")


if __name__ == "__main__":
    menu()