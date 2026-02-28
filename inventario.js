const tabla = document.querySelector("tbody");

async function cargarInventario() {
    const res = await fetch("/api/inventario");
    const data = await res.json();

    tabla.innerHTML = "";

    data.forEach(item => {
        tabla.innerHTML += `
            <tr>
                <td>${item.id}</td>
                <td>${item.nombre}</td>
                <td>${item.cantidad}</td>
                <td>$${item.precio}</td>
                <td>
                    <button onclick="editar(${item.id})">✏</button>
                    <button onclick="eliminar(${item.id})">🗑</button>
                </td>
            </tr>
        `;
    });
}

async function agregar() {
    const nombre = prompt("Nombre del producto:");
    const cantidad = prompt("Cantidad:");
    const precio = prompt("Precio:");

    await fetch("/api/inventario", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ nombre, cantidad, precio })
    });

    cargarInventario();
}

async function editar(id) {
    const nombre = prompt("Nuevo nombre:");
    const cantidad = prompt("Nueva cantidad:");
    const precio = prompt("Nuevo precio:");

    await fetch(`/api/inventario/${id}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ nombre, cantidad, precio })
    });

    cargarInventario();
}

async function eliminar(id) {
    await fetch(`/api/inventario/${id}`, { method: "DELETE" });
    cargarInventario();
}

cargarInventario();