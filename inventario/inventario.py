import json
import csv
import os

class Inventario:

    def __init__(self):
        self.txt_path = "inventario/data/datos.txt"
        self.json_path = "inventario/data/datos.json"
        self.csv_path = "inventario/data/datos.csv"

    def guardar_txt(self, nombre, precio, cantidad):
        with open(self.txt_path, "a", encoding="utf-8") as f:
            f.write(f"{nombre}, {precio}, {cantidad}\n")

    def leer_txt(self):
        if not os.path.exists(self.txt_path):
            return []
        with open(self.txt_path, "r", encoding="utf-8") as f:
            return f.readlines()

    def guardar_json(self, nombre, precio, cantidad):
        data = self.leer_json()
        data.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})

        with open(self.json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def leer_json(self):
        if not os.path.exists(self.json_path):
            return []
        with open(self.json_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def guardar_csv(self, nombre, precio, cantidad):
        existe = os.path.exists(self.csv_path)
        with open(self.csv_path, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if not existe:
                writer.writerow(["nombre", "precio", "cantidad"])
            writer.writerow([nombre, precio, cantidad])

    def leer_csv(self):
        if not os.path.exists(self.csv_path):
            return []
        with open(self.csv_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            return list(reader)