document.addEventListener("DOMContentLoaded", function () {
    obtenerProductos();
});

// ✅ Variables globales
let catalogoProductos = [];
const tipoMap = {
    "Todos": null,
    "Textil": 1,
    "Accesorio": 3
};

// ✅ Obtener productos desde la API
async function obtenerProductos() {
    try {
        const response = await fetch('http://127.0.0.1:5000/catalogo');
        if (!response.ok) {
            throw new Error(`Error en API: ${response.status}`);
        }

        const data = await response.json();
        console.log("📦 Productos obtenidos desde la API:", data);

        if (!Array.isArray(data) || data.length === 0) {
            document.getElementById("productos-container").innerHTML = `<p class="text-center text-danger">❌ No hay productos disponibles en la API.</p>`;
            return;
        }

        catalogoProductos = data.filter(producto => producto.id_tipo !== 2); // Filtra los productos de tipo `2`
        mostrarProductos(catalogoProductos); // ✅ Mostrar todos los productos al inicio
    } catch (error) {
        document.getElementById("productos-container").innerHTML = `<p class="text-center text-danger">❌ Error al obtener productos.</p>`;
        console.error("❌ Error al obtener productos:", error);
    }
}

// ✅ Mostrar productos en la interfaz
function mostrarProductos(productos) {
    const contenedor = document.getElementById("productos-container");
    contenedor.innerHTML = "";

    if (!productos || productos.length === 0) {
        contenedor.innerHTML = `<p class="text-center text-danger">❌ No hay productos disponibles.</p>`;
        return;
    }

    productos.forEach(producto => {
        // ✅ Convertir la ruta de la base de datos (assets/img/catalogo/) a la nueva (static/img/catalogo/)
        const imagenProducto = (Array.isArray(producto.imagenes) && producto.imagenes.length > 0) 
            ? producto.imagenes[0].replace("assets/img/catalogo/", "static/img/catalogo/")  
            : "/static/img/default.png";  

        contenedor.innerHTML += `
            <div class="col-md-4 mb-4 catalogo-item">
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

            const modal = new bootstrap.Modal(document.getElementById("productModal"));
            modal.show();
        });
    });
}

// ✅ Mostrar detalles del producto en el modal
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
                      const imagenRutaCorregida = img.url.replace("assets/img/catalogo/", "static/img/catalogo/");
                      
                      contenedorImagenes.innerHTML += `
                          <div class="carousel-item ${index === 0 ? 'active' : ''}">
                              <img src="${imagenRutaCorregida}" class="d-block w-100 rounded shadow" alt="Imagen del producto">
                          </div>
                      `;
                  });
                })
                .catch(error => console.error("❌ Error al obtener imágenes del producto:", error));
        })
        .catch(error => console.error("❌ Error al obtener detalles del producto:", error));
}

// ✅ Función para aplicar filtros
function aplicarFiltros(tipoFiltro, nombreFiltro) {
    const tipoID = tipoMap[tipoFiltro];

    const productosFiltrados = catalogoProductos.filter(producto => {
        const tipoProducto = producto.id_tipo !== undefined ? Number(producto.id_tipo) : null;

        const coincideTipo = tipoID === null || tipoProducto === tipoID;
        const coincideNombre = producto.nombre.toLowerCase().includes(nombreFiltro);
        return coincideTipo && coincideNombre;
    });

    console.log("✅ Productos después del filtrado:", productosFiltrados);
    mostrarProductos(productosFiltrados);
}

// ✅ Eventos para filtrar por tipo
document.querySelectorAll(".filtro-btn").forEach(button => {
    button.addEventListener("click", function () {
        document.querySelectorAll(".filtro-btn").forEach(btn => btn.classList.remove("active"));
        this.classList.add("active");

        const filtroTipo = this.getAttribute("data-tipo");
        const nombreFiltro = document.getElementById("nombreFiltro").value.toLowerCase();

        aplicarFiltros(filtroTipo, nombreFiltro);
    });
});

// ✅ Eventos para filtrar por nombre
document.getElementById("nombreFiltro").addEventListener("input", function () {
    const nombreSeleccionado = this.value.toLowerCase();
    const tipoFiltro = document.querySelector(".filtro-btn.active").getAttribute("data-tipo");

    aplicarFiltros(tipoFiltro, nombreSeleccionado);
});
