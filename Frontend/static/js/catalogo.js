
document.addEventListener("DOMContentLoaded", function () {
    obtenerProductos();
});

// ✅ Función para obtener productos desde la API y cargarlos en el catálogo
async function obtenerProductos() {
    try {
        const response = await fetch('http://127.0.0.1:5000/catalogo');
        const data = await response.json();
        console.log("📦 Productos obtenidos:", data);

        mostrarProductos(data);
    } catch (error) {
        console.error("❌ Error al obtener productos:", error);
    }
}

// ✅ Función para mostrar los productos en la interfaz
function mostrarProductos(productos) {
    const contenedor = document.getElementById("productos-container");
    contenedor.innerHTML = ""; 

    if (!productos || productos.length === 0) {
        contenedor.innerHTML = `<p class="text-center text-danger">No hay productos disponibles.</p>`;
        return;
    }

    productos.forEach(producto => {
        // ✅ Usa la primera imagen del array si hay imágenes disponibles
        const imagenProducto = (producto.imagenes && producto.imagenes.length > 0) 
            ? `http://localhost:5000/${producto.imagenes[0]}` 
            : "/img/default.png";  

        contenedor.innerHTML += `
            <div class="col-md-4 mb-4">
                <div class="card shadow h-100">
                    <img src="${imagenProducto}" class="card-img-top" alt="${producto.nombre}">
                    <div class="card-body text-center">
                        <h5 class="card-title">${producto.nombre}</h5>
                        <p class="card-text">${producto.descripcion}</p>
                        <p class="text-primary mb-3"><strong>PEN ${producto.precio}</strong></p>
                        <button class="btn btn-dark w-100 mt-auto ver-mas-btn" data-id="${producto.id_catalogo}">Ver más</button>
                    </div>
                </div>
            </div>
        `;
    });

    agregarEventosVerMas();
}

// ✅ Agregar eventos para los botones "Ver más"
function agregarEventosVerMas() {
    document.querySelectorAll(".ver-mas-btn").forEach(button => {
        button.addEventListener("click", function () {
            const productoId = this.getAttribute("data-id");
            mostrarDetallesProducto(productoId);

            // ✅ Asegurar que el modal se abre correctamente
            const modal = new bootstrap.Modal(document.getElementById("productModal"));
            modal.show();
        });
    });
}

// ✅ Función para mostrar detalles del producto en el modal
function mostrarDetallesProducto(productoId) {
    fetch(`http://127.0.0.1:5000/catalogo/${productoId}`)
        .then(response => response.json())
        .then(producto => {
            console.log("📦 Detalles del producto obtenidos:", producto);

            document.getElementById("producto-nombre-modal").innerText = producto.nombre || "Sin nombre";
            document.getElementById("producto-material").innerText = producto.material || "No especificado";
            document.getElementById("producto-stock").innerText = producto.stock ? `${producto.stock} unidades` : "Stock no disponible";
            document.getElementById("producto-color").innerText = producto.color || "No especificado";
            document.getElementById("producto-precio-modal").innerText = `PEN ${producto.precio || "No definido"}`;

            // ✅ Llamar a la API de imágenes del producto con ID correcto
            fetch(`http://127.0.0.1:5000/catalogo/${productoId}/imagenes`)
                .then(response => response.json())
                .then(data => {
                    console.log("📷 Imágenes obtenidas:", data.imagenes);

                    const contenedorImagenes = document.getElementById("modalImagenContainer");
                    contenedorImagenes.innerHTML = "";

                    if (!Array.isArray(data.imagenes) || data.imagenes.length === 0) {
                        contenedorImagenes.innerHTML = `<p class="text-center text-muted">No hay imágenes disponibles.</p>`;
                        return;
                    }

                    data.imagenes.forEach((img, index) => {
                        contenedorImagenes.innerHTML += `
                            <div class="carousel-item ${index === 0 ? 'active' : ''}">
                                <img src="${img.url}" class="d-block w-100 rounded shadow" alt="Imagen del producto">
                            </div>
                        `;
                    });
                })
                .catch(error => console.error("❌ Error al obtener imágenes del producto:", error));
        })
        .catch(error => console.error("❌ Error al obtener detalles del producto:", error));
}
