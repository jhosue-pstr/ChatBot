CREATE DATABASE infotel_db
use infotel_db

CREATE TABLE proveedores (
    id_proveedor INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    contacto VARCHAR(255),
    direccion VARCHAR(255)
);

CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    tipo_documento VARCHAR(20),
    nro_documento VARCHAR(20),
    direccion TEXT,
    telefono VARCHAR(15),
    email VARCHAR(100)
);

CREATE TABLE categorias (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100)
);

CREATE TABLE tipos (
    id_tipo INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100)
);

CREATE TABLE productos (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    descripcion TEXT,
    precio_unitario DECIMAL(10,2),
    id_categoria INT NOT NULL,
    id_tipo INT NOT NULL,
    id_proveedor INT NOT NULL,
    FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria),
    FOREIGN KEY (id_tipo) REFERENCES tipos(id_tipo),
    FOREIGN KEY (id_proveedor) REFERENCES proveedores(id_proveedor)
);

CREATE TABLE pedidos (
    id_pedido INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    fecha_pedido DATE,
    estado VARCHAR(50),
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

CREATE TABLE seguimiento_pedidos (
    id_seguimiento INT AUTO_INCREMENT PRIMARY KEY,
    id_pedido INT NOT NULL,
    fecha_actualizacion DATETIME,
    estado VARCHAR(50),
    observaciones TEXT,
    FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido)
);

CREATE TABLE detalles_pedido (
    id_detalle INT AUTO_INCREMENT PRIMARY KEY,
    id_pedido INT NOT NULL,
    id_producto INT NOT NULL,
    cantidad INT,
    precio_unitario DECIMAL(10,2),
    FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido),
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);

CREATE TABLE documentos (
    id_documento INT AUTO_INCREMENT PRIMARY KEY,
    id_pedido INT NOT NULL,
    tipo_documento VARCHAR(50),
    numero VARCHAR(50),
    fecha_emision DATE,
    archivo_url TEXT,
    FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido)
);

CREATE TABLE ventas (
    id_venta INT AUTO_INCREMENT PRIMARY KEY,
    id_pedido INT NOT NULL,
    id_cliente INT NOT NULL,
    fecha_venta DATE,
    total DECIMAL(10,2),
    metodo_pago VARCHAR(50),
    FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido),
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

CREATE TABLE comprobante_pago (
    id_comprobante INT AUTO_INCREMENT PRIMARY KEY,
    id_exportacion INT,
    id_importacion INT,
    numero VARCHAR(50),
    fecha_emision DATE,
    subtotal DECIMAL(10,2),
    descuento_total DECIMAL(10,2),
    impuesto DECIMAL(10,2),
    total DECIMAL(10,2),
    tipo_documento VARCHAR(50),
    archivo_url TEXT
);

CREATE TABLE exportaciones (
    id_exportacion INT AUTO_INCREMENT PRIMARY KEY,
    id_venta INT NOT NULL,
    id_comprobante INT NOT NULL,
    pais_destino VARCHAR(100),
    descripcion_carga TEXT,
    fecha_envio DATE,
    FOREIGN KEY (id_venta) REFERENCES ventas(id_venta),
    FOREIGN KEY (id_comprobante) REFERENCES comprobante_pago(id_comprobante)
);

CREATE TABLE compras (
    id_compra INT AUTO_INCREMENT PRIMARY KEY,
    id_proveedor INT NOT NULL,
    fecha_compra DATE,
    total DECIMAL(10,2),
    metodo_pago VARCHAR(50),
    FOREIGN KEY (id_proveedor) REFERENCES proveedores(id_proveedor)
);

CREATE TABLE importaciones (
    id_importacion INT AUTO_INCREMENT PRIMARY KEY,
    id_proveedor INT NOT NULL,
    id_compra INT NOT NULL,
    descripcion TEXT,
    fecha_ingreso DATE,
    documento_ingreso TEXT,
    id_comprobante INT NOT NULL,
    FOREIGN KEY (id_proveedor) REFERENCES proveedores(id_proveedor),
    FOREIGN KEY (id_compra) REFERENCES compras(id_compra),
    FOREIGN KEY (id_comprobante) REFERENCES comprobante_pago(id_comprobante)
);

CREATE TABLE packing_list (
    id_packing INT AUTO_INCREMENT PRIMARY KEY,
    id_exportacion INT,
    id_importacion INT,
    fecha_packing DATE,
    descripcion TEXT,
    cantidad_total INT,
    peso_total DECIMAL(10,2),
    volumen_total DECIMAL(10,2),
    inspeccionado_por VARCHAR(100),
    observaciones TEXT,
    FOREIGN KEY (id_exportacion) REFERENCES exportaciones(id_exportacion),
    FOREIGN KEY (id_importacion) REFERENCES importaciones(id_importacion)
);

CREATE TABLE catalogo (
    id_catalogo INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT NOT NULL,
    talla VARCHAR(20),
    color VARCHAR(50),
    material VARCHAR(100),
    precio DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL DEFAULT 0,
    id_tipo INT NOT NULL,
    id_categoria INT NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_tipo) REFERENCES tipos(id_tipo) ON DELETE CASCADE,
    FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria) ON DELETE CASCADE
);

CREATE TABLE catalogo_imagenes (
    id_imagen INT AUTO_INCREMENT PRIMARY KEY,
    id_catalogo INT NOT NULL,
    imagen_url TEXT NOT NULL,
    fecha_subida TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_catalogo) REFERENCES catalogo(id_catalogo) ON DELETE CASCADE
);

CREATE TABLE detalles_venta (
    id_detalle_venta INT AUTO_INCREMENT PRIMARY KEY,
    id_venta INT NOT NULL,
    id_pedido INT NOT NULL,
    id_producto INT NOT NULL,
    cantidad INT,
    precio_unitario DECIMAL(10,2),
    FOREIGN KEY (id_venta) REFERENCES ventas(id_venta),
    FOREIGN KEY (id_pedido) REFERENCES pedidos(id_pedido),
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);

CREATE TABLE detalles_compra (
    id_detalle_compra INT AUTO_INCREMENT PRIMARY KEY,
    id_compra INT NOT NULL,
    id_producto INT NOT NULL,
    cantidad INT,
    precio_unitario DECIMAL(10,2),
    FOREIGN KEY (id_compra) REFERENCES compras(id_compra),
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);

CREATE TABLE almacen (
    id_almacen INT AUTO_INCREMENT PRIMARY KEY,
    id_producto INT NOT NULL,
    cantidad_disponible INT,
    cantidad_minima INT,
    ubicacion VARCHAR(255),
    fecha_entrada DATE,
    estado VARCHAR(50),
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);
