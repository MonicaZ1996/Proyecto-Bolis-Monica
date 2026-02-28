const express = require("express");
const app = express();
const path = require("path");

app.use(express.json());
app.use(express.static("public"));

let inventario = [
    { id: 1, nombre: "Boli de Coco", cantidad: 25, precio: 1.00 },
    { id: 2, nombre: "Boli de Fresa", cantidad: 30, precio: 1.00 },
    { id: 3, nombre: "Boli de Oreo", cantidad: 20, precio: 1.50 },
];

// Obtener inventario
app.get("/api/inventario", (req, res) => {
    res.json(inventario);
});

// Crear producto
app.post("/api/inventario", (req, res) => {
    const nuevo = req.body;
    nuevo.id = inventario.length + 1;
    inventario.push(nuevo);
    res.json({ mensaje: "Producto agregado", inventario });
});

// Actualizar producto
app.put("/api/inventario/:id", (req, res) => {
    const id = parseInt(req.params.id);
    const data = req.body;

    inventario = inventario.map(item =>
        item.id === id ? { ...item, ...data } : item
    );

    res.json({ mensaje: "Producto actualizado", inventario });
});

// Eliminar producto
app.delete("/api/inventario/:id", (req, res) => {
    const id = parseInt(req.params.id);
    inventario = inventario.filter(p => p.id !== id);

    res.json({ mensaje: "Producto eliminado", inventario });
});

app.listen(3000, () =>
    console.log("Servidor corriendo en http://localhost:3000")
);