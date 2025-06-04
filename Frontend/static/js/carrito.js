document.addEventListener("DOMContentLoaded", () => {
  cargarCarrito();
});

function cargarCarrito() {
  fetch("http://127.0.0.1:5000/carrito")
    .then((response) => response.json())
    .then((data) => {
      const tbody = document.getElementById("carrito-items");
      const totalElement = document.getElementById("total-pagar");

      tbody.innerHTML = "";
      let total = 0;

      data.forEach((item) => {
        total += parseFloat(item.subtotal);

        const fila = document.createElement("tr");

        fila.innerHTML = `
          <td>${item.nombre_producto}</td>
          <td>PEN ${parseFloat(item.precio_unitario).toFixed(2)}</td>
          <td>
            <input type="number" min="1" value="${item.cantidad_producto}" class="form-control cantidad-input" data-id="${item.id_carrito}" />
          </td>
          <td>PEN ${parseFloat(item.subtotal).toFixed(2)}</td>
          <td>
            <button class="btn btn-sm btn-danger" onclick="eliminarItem(${item.id_carrito})">Eliminar</button>
          </td>
        `;

        tbody.appendChild(fila);
      });

      totalElement.innerText = `PEN ${total.toFixed(2)}`;

      // Agregar eventos a inputs de cantidad
      document.querySelectorAll(".cantidad-input").forEach((input) => {
        input.addEventListener("change", (event) => {
          const nuevaCantidad = parseInt(event.target.value);
          const idCarrito = event.target.getAttribute("data-id");
          const item = data.find((i) => i.id_carrito == idCarrito);

          if (nuevaCantidad > 0) {
            fetch(`http://127.0.0.1:5000/carrito/${idCarrito}`, {
              method: "PUT",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify({
                id_catalogo: item.id_catalogo,
                cantidad_producto: nuevaCantidad,
                precio_unitario: item.precio_unitario
              })
            })
              .then((res) => res.json())
              .then(() => cargarCarrito())
              .catch((err) => console.error("Error al actualizar:", err));
          }
        });
      });
    })
    .catch((error) => {
      document.getElementById("carrito-items").innerHTML = `
        <tr><td colspan="5">Error al cargar el carrito</td></tr>
      `;
      console.error("Error:", error);
    });
}

function eliminarItem(idCarrito) {
  fetch(`http://127.0.0.1:5000/carrito/${idCarrito}`, {
    method: "DELETE"
  })
    .then((res) => res.json())
    .then(() => cargarCarrito())
    .catch((error) => console.error("Error al eliminar:", error));
}
