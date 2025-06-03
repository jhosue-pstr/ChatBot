document.addEventListener("DOMContentLoaded", () => {
  fetch("http://127.0.0.1:5000/catalogo")
    .then((response) => response.json())
    .then((data) => {
      const carouselInner = document.getElementById("carousel-inner");
      carouselInner.innerHTML = "";

      const grupos = [];
      for (let i = 0; i < data.length; i += 4) {
        grupos.push(data.slice(i, i + 4));
      }

      grupos.forEach((grupo, index) => {
        const activeClass = index === 0 ? "active" : "";
        const slide = document.createElement("div");
        slide.className = `carousel-item ${activeClass}`;

        const row = document.createElement("div");
        row.className = "row gy-4 justify-content-center";

        grupo.forEach((producto) => {
          const col = document.createElement("div");
          col.className = "col-xl-3 col-md-6 d-flex";
          col.innerHTML = generarCardHTML(producto);
          row.appendChild(col);
        });

        slide.appendChild(row);
        carouselInner.appendChild(slide);
      });
    })
    .catch((error) => console.error("Error al obtener los productos:", error));
});

function mostrarDetalles(idCatalogo) {
  fetch(`http://127.0.0.1:5000/catalogo/${idCatalogo}`)
    .then((response) => response.json())
    .then((producto) => {
      document.getElementById("producto-img-modal").src = producto.imagen_url;
      document.getElementById("producto-nombre-modal").innerText =
        producto.nombre;
      document.getElementById("producto-material").innerText =
        producto.material;
      document.getElementById("producto-stock").innerText = producto.stock;
      document.getElementById("producto-color").innerText = producto.color;
      document.getElementById("producto-precio-modal").innerText =
        "PEN " + producto.precio;
    })
    .catch((error) =>
      console.error("Error al obtener detalles del producto:", error)
    );
}

function generarCardHTML(producto) {
  return `
    <div class="product-card card border-0 shadow-sm rounded-4 text-center w-100">
      <a href="#" class="text-decoration-none text-dark" onclick="mostrarDetalles(${
        producto.id_catalogo
      })" data-bs-toggle="modal" data-bs-target="#productModal">
        <div class="position-relative bg-light rounded-top-4" style="height: 180px;">
          <img src="${producto.imagen_url}" alt="${
    producto.nombre
  }" class="img-fluid h-100 w-100 object-fit-cover rounded-top-4" />
          <span class="position-absolute bottom-0 end-0 m-2 bg-white rounded-circle p-2 shadow">
            <i class="bi bi-cart2 fs-5"></i>
          </span>
        </div>
        <div class="p-3">
          <h6 class="text-truncate" style="max-width: 100%;">${
            producto.nombre
          }</h6>
          <div class="d-flex justify-content-center align-items-center mb-1">
            <div class="text-warning small">★★★★☆</div>
            <small class="text-muted ms-1">${
              producto.vendidos || 0
            } vendido(s)</small>
          </div>
          <h5 class="fw-bold text-primary">PEN ${producto.precio}</h5>
        </div>
      </a>
    </div>
  `;
}
