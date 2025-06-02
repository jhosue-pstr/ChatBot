from flask import Flask, request, jsonify
from flask_cors import CORS
import cliente
import almacen
import catalogo
import categorias
import compras
import comprobantePago
import detallesCompra
import detallesPedido
import documentos
import exportaciones
import importaciones
import packingList
import pedidos
import productos
import proveedores
import seguimientoPedidos
import tipos
import ventaDetalle
import ventas



app = Flask(__name__)
CORS(app)

@app.route('/')
def inicio():
    return "API Clientes - INFOTEL BUSINESS"


#============cliente============#
@app.route('/clientes', methods=['POST'])
def crear_cliente():
    data = request.json
    cliente.crear_cliente(data)
    return jsonify({"mensaje": "Cliente creado con éxito"}), 201

@app.route('/clientes', methods=['GET'])
def listar_clientes():
    resultado = cliente.listar_clientes()
    return jsonify(resultado)

@app.route('/clientes/<int:id_cliente>', methods=['GET'])
def obtener_cliente(id_cliente):
    cliente_data = cliente.obtener_cliente_por_id(id_cliente)
    if cliente_data:
        return jsonify(cliente_data)
    else:
        return jsonify({"mensaje": "Cliente no encontrado"}), 404

@app.route('/clientes/<int:id_cliente>', methods=['PUT'])
def actualizar_cliente(id_cliente):
    data = request.json
    cliente.actualizar_cliente(id_cliente, data)
    return jsonify({"mensaje": "Cliente actualizado correctamente"})

@app.route('/clientes/<int:id_cliente>', methods=['DELETE'])
def eliminar_cliente(id_cliente):
    cliente.eliminar_cliente(id_cliente)
    return jsonify({"mensaje": "Cliente eliminado correctamente"})
#==============almacen===========#
@app.route('/almacen', methods=['POST'])
def crear_almacen():
    data = request.json
    almacen.crear_almacen(data)
    return jsonify({"mensaje": "Registro de almacén creado con éxito"}), 201

@app.route('/almacen', methods=['GET'])
def listar_almacen():
    resultado = almacen.listar_almacen()
    return jsonify(resultado)

@app.route('/almacen/<int:id_almacen>', methods=['GET'])
def obtener_almacen(id_almacen):
    almacen_data = almacen.obtener_almacen_por_id(id_almacen)
    if almacen_data:
        return jsonify(almacen_data)
    else:
        return jsonify({"mensaje": "Registro de almacén no encontrado"}), 404

@app.route('/almacen/<int:id_almacen>', methods=['PUT'])
def actualizar_almacen(id_almacen):
    data = request.json
    almacen.actualizar_almacen(id_almacen, data)
    return jsonify({"mensaje": "Registro de almacén actualizado correctamente"})

@app.route('/almacen/<int:id_almacen>', methods=['DELETE'])
def eliminar_almacen(id_almacen):
    almacen.eliminar_almacen(id_almacen)
    return jsonify({"mensaje": "Registro de almacén eliminado correctamente"})
#===============catalgo================#
@app.route('/catalogo', methods=['POST'])
def crear_catalogo():
    data = request.json
    catalogo.crear_catalogo(data)
    return jsonify({"mensaje": "Catálogo creado con éxito"}), 201

@app.route('/catalogo', methods=['GET'])
def listar_catalogo():
    resultado = catalogo.listar_catalogo()
    return jsonify(resultado)

@app.route('/catalogo/<int:id_catalogo>', methods=['GET'])
def obtener_catalogo(id_catalogo):
    catalogo_data = catalogo.obtener_catalogo(id_catalogo)
    if catalogo_data:
        return jsonify(catalogo_data)
    else:
        return jsonify({"mensaje": "Catálogo no encontrado"}), 404

@app.route('/catalogo/<int:id_catalogo>', methods=['PUT'])
def actualizar_catalogo(id_catalogo):
    data = request.json
    catalogo.actualizar_catalogo(id_catalogo, data)
    return jsonify({"mensaje": "Catálogo actualizado correctamente"})

@app.route('/catalogo/<int:id_catalogo>', methods=['DELETE'])
def eliminar_catalogo(id_catalogo):
    catalogo.eliminar_catalogo(id_catalogo)
    return jsonify({"mensaje": "Catálogo eliminado correctamente"})

#===============categorias================#
@app.route('/categorias', methods=['POST'])
def crear_categoria():
    data = request.json
    categorias.crear_categorias(data)
    return jsonify({"mensaje": "Categoría creada con éxito"}), 201

@app.route('/categorias', methods=['GET'])
def listar_categorias():
    resultado = categorias.obtener_categorias()
    return resultado  # ya devuelve jsonify

@app.route('/categorias/<int:id>', methods=['GET'])
def obtener_categoria(id):
    categoria_data = categorias.obtener_categorias_por_id(id)
    if categoria_data.status_code == 404:
        return categoria_data
    return categoria_data

@app.route('/categorias/<int:id>', methods=['PUT'])
def actualizar_categoria(id):
    data = request.json
    categorias.actualizar_categorias(id, data)
    return jsonify({"mensaje": "Categoría actualizada correctamente"})

@app.route('/categorias/<int:id>', methods=['DELETE'])
def eliminar_categoria(id):
    categorias.eliminar_categorias(id)
    return jsonify({"mensaje": "Categoría eliminada correctamente"})
#===============compras================#
@app.route('/compras', methods=['POST'])
def crear_compra():
    data = request.json
    compras.crear_compra(
        data['id_proveedor'],
        data['fecha_compra'],
        data['total'],
        data['metodo_pago']
    )
    return jsonify({"mensaje": "Compra creada con éxito"}), 201

@app.route('/compras', methods=['GET'])
def listar_compras():
    resultado = compras.listar_compras()
    return jsonify(resultado)

@app.route('/compras/<int:id>', methods=['GET'])
def obtener_compra(id):
    compra_data = compras.obtener_compra(id)
    if compra_data is None:
        return jsonify({"mensaje": "Compra no encontrada"}), 404
    return jsonify(compra_data)

@app.route('/compras/<int:id>', methods=['PUT'])
def actualizar_compra(id):
    data = request.json
    compras.actualizar_compra(
        id,
        data['id_proveedor'],
        data['fecha_compra'],
        data['total'],
        data['metodo_pago']
    )
    return jsonify({"mensaje": "Compra actualizada correctamente"})

@app.route('/compras/<int:id>', methods=['DELETE'])
def eliminar_compra(id):
    compras.eliminar_compra(id)
    return jsonify({"mensaje": "Compra eliminada correctamente"})


#===============comprobantePago================#
@app.route('/comprobantePago', methods=['POST'])
def crear_comprobante_pago():
    data = request.json
    comprobantePago.crear_comprobante_pago(
        data['id_exportacion'],
        data['id_importacion'],
        data['numero'],
        data['fecha_emision'],
        data['subtotal'],
        data['descuento_total'],
        data['impuesto'],
        data['total'],
        data['tipo_documento'],
        data['archivo_url']
    )
    return jsonify({"mensaje": "Comprobante de pago creado con éxito"}), 201

@app.route('/comprobantePago', methods=['GET'])
def listar_comprobantes_pago():
    resultado = comprobantePago.listar_comprobantes_pago()
    return jsonify(resultado)

@app.route('/comprobantePago/<int:id>', methods=['GET'])
def obtener_comprobante_pago(id):
    comprobante_data = comprobantePago.obtener_comprobante_pago(id)
    if comprobante_data is None:
        return jsonify({"mensaje": "Comprobante de pago no encontrado"}), 404
    return jsonify(comprobante_data)

@app.route('/comprobantePago/<int:id>', methods=['PUT'])
def actualizar_comprobante_pago(id):
    data = request.json
    comprobantePago.actualizar_comprobante_pago(
        id,
        data['id_exportacion'],
        data['id_importacion'],
        data['numero'],
        data['fecha_emision'],
        data['subtotal'],
        data['descuento_total'],
        data['impuesto'],
        data['total'],
        data['tipo_documento'],
        data['archivo_url']
    )
    return jsonify({"mensaje": "Comprobante de pago actualizado correctamente"})

@app.route('/comprobantePago/<int:id>', methods=['DELETE'])
def eliminar_comprobante_pago(id):
    comprobantePago.eliminar_comprobante_pago(id)
    return jsonify({"mensaje": "Comprobante de pago eliminado correctamente"})


#===============detalleCompra================#
@app.route('/detalleCompra', methods=['POST'])
def crear_detalle_compra():
    data = request.json
    detallesCompra.crear_detalle_compra(
        data['id_compra'],
        data['id_producto'],
        data['cantidad'],
        data['precio_unitario']
    )
    return jsonify({"mensaje": "Detalle de compra creado con éxito"}), 201

@app.route('/detalleCompra', methods=['GET'])
def listar_detalles_compra():
    resultado = detallesCompra.listar_detalles_compra()
    return jsonify(resultado)

@app.route('/detalleCompra/<int:id>', methods=['GET'])
def obtener_detalle_compra(id):
    detalle_data = detallesCompra.obtener_detalle_compra(id)
    if detalle_data is None:
        return jsonify({"mensaje": "Detalle de compra no encontrado"}), 404
    return jsonify(detalle_data)

@app.route('/detalleCompra/<int:id>', methods=['PUT'])
def actualizar_detalle_compra(id):
    data = request.json
    detallesCompra.actualizar_detalle_compra(
        id,
        data['id_compra'],
        data['id_producto'],
        data['cantidad'],
        data['precio_unitario']
    )
    return jsonify({"mensaje": "Detalle de compra actualizado correctamente"})

@app.route('/detalleCompra/<int:id>', methods=['DELETE'])
def eliminar_detalle_compra(id):
    detallesCompra.eliminar_detalle_compra(id)
    return jsonify({"mensaje": "Detalle de compra eliminado correctamente"})

#===============detallePedido================#
@app.route('/detallePedido', methods=['POST'])
def crear_detalle_pedido():
    data = request.json
    detallesPedido.crear_detalle_pedido(
        data['id_pedido'],
        data['id_producto'],
        data['cantidad'],
        data['precio_unitario']
    )
    return jsonify({"mensaje": "Detalle de pedido creado con éxito"}), 201

@app.route('/detallePedido', methods=['GET'])
def listar_detalles_pedido():
    resultado = detallesPedido.listar_detalles_pedido()
    return jsonify(resultado)

@app.route('/detallePedido/<int:id>', methods=['GET'])
def obtener_detalle_pedido(id):
    detalle_data = detallesPedido.obtener_detalle_pedido(id)
    if detalle_data is None:
        return jsonify({"mensaje": "Detalle de pedido no encontrado"}), 404
    return jsonify(detalle_data)

@app.route('/detallePedido/<int:id>', methods=['PUT'])
def actualizar_detalle_pedido(id):
    data = request.json
    detallesPedido.actualizar_detalle_pedido(
        id,
        data['id_pedido'],
        data['id_producto'],
        data['cantidad'],
        data['precio_unitario']
    )
    return jsonify({"mensaje": "Detalle de pedido actualizado correctamente"})

@app.route('/detallePedido/<int:id>', methods=['DELETE'])
def eliminar_detalle_pedido(id):
    detallesPedido.eliminar_detalle_pedido(id)
    return jsonify({"mensaje": "Detalle de pedido eliminado correctamente"})

#===============documentos================#
@app.route('/documentos', methods=['POST'])
def crear_documento():
    data = request.json
    documentos.crear_documento(
        data['id_pedido'],
        data['tipo_documento'],
        data['numero'],
        data['fecha_emision'],
        data['archivo_url']
    )
    return jsonify({"mensaje": "Documento creado con éxito"}), 201

@app.route('/documentos', methods=['GET'])
def listar_documentos():
    resultado = documentos.listar_documentos()
    return jsonify(resultado)

@app.route('/documentos/<int:id>', methods=['GET'])
def obtener_documento(id):
    documento_data = documentos.obtener_documento(id)
    if documento_data is None:
        return jsonify({"mensaje": "Documento no encontrado"}), 404
    return jsonify(documento_data)

@app.route('/documentos/<int:id>', methods=['PUT'])
def actualizar_documento(id):
    data = request.json
    documentos.actualizar_documento(
        id,
        data['id_pedido'],
        data['tipo_documento'],
        data['numero'],
        data['fecha_emision'],
        data['archivo_url']
    )
    return jsonify({"mensaje": "Documento actualizado correctamente"})

@app.route('/documentos/<int:id>', methods=['DELETE'])
def eliminar_documento(id):
    documentos.eliminar_documento(id)
    return jsonify({"mensaje": "Documento eliminado correctamente"})


#===============exportaciones================#
@app.route('/exportaciones', methods=['POST'])
def crear_exportacion():
    data = request.json
    exportaciones.crear_exportacion(
        data['id_venta'],
        data['id_comprobante'],
        data['pais_destino'],
        data['descripcion_carga'],
        data['fecha_envio']
    )
    return jsonify({"mensaje": "Exportación creada con éxito"}), 201

@app.route('/exportaciones', methods=['GET'])
def listar_exportaciones():
    resultado = exportaciones.listar_exportaciones()
    return jsonify(resultado)

@app.route('/exportaciones/<int:id>', methods=['GET'])
def obtener_exportacion(id):
    exportacion_data = exportaciones.obtener_exportacion(id)
    if exportacion_data is None:
        return jsonify({"mensaje": "Exportación no encontrada"}), 404
    return jsonify(exportacion_data)

@app.route('/exportaciones/<int:id>', methods=['PUT'])
def actualizar_exportacion(id):
    data = request.json
    exportaciones.actualizar_exportacion(
        id,
        data['id_venta'],
        data['id_comprobante'],
        data['pais_destino'],
        data['descripcion_carga'],
        data['fecha_envio']
    )
    return jsonify({"mensaje": "Exportación actualizada correctamente"})

@app.route('/exportaciones/<int:id>', methods=['DELETE'])
def eliminar_exportacion(id):
    exportaciones.eliminar_exportacion(id)
    return jsonify({"mensaje": "Exportación eliminada correctamente"})

#===============importaciones================#
@app.route('/importaciones', methods=['POST'])
def crear_importacion():
    data = request.json
    importaciones.crear_importacion(
        data['id_proveedor'],
        data['id_compra'],
        data['descripcion'],
        data['fecha_ingreso'],
        data['documento_ingreso'],
        data['id_comprobante']
    )
    return jsonify({"mensaje": "Importación creada con éxito"}), 201

@app.route('/importaciones', methods=['GET'])
def listar_importaciones():
    resultado = importaciones.listar_importaciones()
    return jsonify(resultado)

@app.route('/importaciones/<int:id>', methods=['GET'])
def obtener_importacion(id):
    importacion_data = importaciones.obtener_importacion(id)
    if importacion_data is None:
        return jsonify({"mensaje": "Importación no encontrada"}), 404
    return jsonify(importacion_data)

@app.route('/importaciones/<int:id>', methods=['PUT'])
def actualizar_importacion(id):
    data = request.json
    importaciones.actualizar_importacion(
        id,
        data['id_proveedor'],
        data['id_compra'],
        data['descripcion'],
        data['fecha_ingreso'],
        data['documento_ingreso'],
        data['id_comprobante']
    )
    return jsonify({"mensaje": "Importación actualizada correctamente"})

@app.route('/importaciones/<int:id>', methods=['DELETE'])
def eliminar_importacion(id):
    importaciones.eliminar_importacion(id)
    return jsonify({"mensaje": "Importación eliminada correctamente"})


#===============packingList================#
@app.route('/packingList', methods=['POST'])
def crear_packing_list():
    data = request.json
    packingList.crear_packing_list(
        data['id_exportacion'],
        data['id_importacion'],
        data['fecha_packing'],
        data['descripcion'],
        data['cantidad_total'],
        data['peso_total'],
        data['volumen_total'],
        data['inspeccionado_por'],
        data['observaciones']
    )
    return jsonify({"mensaje": "Packing List creado con éxito"}), 201

@app.route('/packingList', methods=['GET'])
def listar_packing_list():
    resultado = packingList.listar_packing_list()
    return jsonify(resultado)

@app.route('/packingList/<int:id>', methods=['GET'])
def obtener_packing_list(id):
    packing = packingList.obtener_packing_list(id)
    if packing is None:
        return jsonify({"mensaje": "Packing List no encontrado"}), 404
    return jsonify(packing)

@app.route('/packingList/<int:id>', methods=['PUT'])
def actualizar_packing_list(id):
    data = request.json
    packingList.actualizar_packing_list(
        id,
        data['id_exportacion'],
        data['id_importacion'],
        data['fecha_packing'],
        data['descripcion'],
        data['cantidad_total'],
        data['peso_total'],
        data['volumen_total'],
        data['inspeccionado_por'],
        data['observaciones']
    )
    return jsonify({"mensaje": "Packing List actualizado correctamente"})

@app.route('/packingList/<int:id>', methods=['DELETE'])
def eliminar_packing_list(id):
    packingList.eliminar_packing_list(id)
    return jsonify({"mensaje": "Packing List eliminado correctamente"})


#===============pedidos================#
@app.route('/pedidos', methods=['POST'])
def crear_pedido():
    data = request.json
    pedidos.crear_pedidos(
        data['id_cliente'],
        data['fecha_pedido'],
        data['estado']
    )
    return jsonify({"mensaje": "Pedido creado correctamente"}), 201

@app.route('/pedidos', methods=['GET'])
def listar_pedidos():
    resultado = pedidos.obtener_pedidos()
    return jsonify(resultado)

@app.route('/pedidos/<int:id>', methods=['GET'])
def obtener_pedido(id):
    pedido = pedidos.obtener_pedidos_por_id(id)
    if pedido is None or (isinstance(pedido, dict) and pedido.get("mensaje")):
        return jsonify({"mensaje": "Pedido no encontrado"}), 404
    return jsonify(pedido)

@app.route('/pedidos/<int:id>', methods=['PUT'])
def actualizar_pedido(id):
    data = request.json
    pedidos.actualizar_pedidos(
        id,
        data
    )
    return jsonify({"mensaje": "Pedido actualizado correctamente"})

@app.route('/pedidos/<int:id>', methods=['DELETE'])
def eliminar_pedido(id):
    pedidos.eliminar_pedidos(id)
    return jsonify({"mensaje": "Pedido eliminado correctamente"})


#===============productos================#
@app.route('/productos', methods=['POST'])
def crear_producto():
    data = request.json
    productos.crear_productos(
        data['nombre'],
        data['descripcion'],
        data['precio_unitario'],
        data['id_categoria'],
        data['id_tipo'],
        data['id_proveedor']
    )
    return jsonify({"mensaje": "Producto creado correctamente"}), 201

@app.route('/productos', methods=['GET'])
def listar_productos():
    resultado = productos.obtener_productos()
    return jsonify(resultado)

@app.route('/productos/<int:id>', methods=['GET'])
def obtener_producto(id):
    producto = productos.obtener_productos_por_id(id)
    if producto is None or (isinstance(producto, dict) and producto.get("mensaje")):
        return jsonify({"mensaje": "Producto no encontrado"}), 404
    return jsonify(producto)

@app.route('/productos/<int:id>', methods=['PUT'])
def actualizar_producto(id):
    data = request.json
    productos.actualizar_productos(id, data)
    return jsonify({"mensaje": "Producto actualizado correctamente"})

@app.route('/productos/<int:id>', methods=['DELETE'])
def eliminar_producto(id):
    productos.eliminar_productos(id)
    return jsonify({"mensaje": "Producto eliminado correctamente"})

#===============proveedores================#
@app.route('/proveedores', methods=['POST'])
def crear_proveedor():
    data = request.json
    proveedores.crear_proveedores(data)
    return jsonify({"mensaje": "Proveedor creado correctamente"}), 201

@app.route('/proveedores', methods=['GET'])
def listar_proveedores():
    resultado = proveedores.obtener_proveedores()
    return jsonify(resultado)

@app.route('/proveedores/<int:id>', methods=['GET'])
def obtener_proveedor(id):
    proveedor = proveedores.obtener_proveedores_por_id(id)
    if proveedor is None or (isinstance(proveedor, dict) and proveedor.get("mensaje")):
        return jsonify({"mensaje": "Proveedor no encontrado"}), 404
    return jsonify(proveedor)

@app.route('/proveedores/<int:id>', methods=['PUT'])
def actualizar_proveedor(id):
    data = request.json
    proveedores.actualizar_proveedores(id, data)
    return jsonify({"mensaje": "Proveedor actualizado correctamente"})

@app.route('/proveedores/<int:id>', methods=['DELETE'])
def eliminar_proveedor(id):
    proveedores.eliminar_proveedores(id)
    return jsonify({"mensaje": "Proveedor eliminado correctamente"})

#===============seguimiento_pedidos================#
@app.route('/seguimiento', methods=['POST'])
def crear_seguimiento():
    data = request.json
    seguimiento.crear_seguimiento(data)
    return jsonify({"mensaje": "Seguimiento creado correctamente"}), 201

@app.route('/seguimiento', methods=['GET'])
def listar_seguimiento():
    resultado = seguimiento.listar_seguimiento()
    return jsonify(resultado)

@app.route('/seguimiento/<int:id>', methods=['GET'])
def obtener_seguimiento(id):
    registro = seguimiento.obtener_seguimiento_por_id(id)
    if registro is None:
        return jsonify({"mensaje": "Registro de seguimiento no encontrado"}), 404
    return jsonify(registro)

@app.route('/seguimiento/<int:id>', methods=['PUT'])
def actualizar_seguimiento(id):
    data = request.json
    seguimiento.actualizar_seguimiento(id, data)
    return jsonify({"mensaje": "Seguimiento actualizado correctamente"})

@app.route('/seguimiento/<int:id>', methods=['DELETE'])
def eliminar_seguimiento(id):
    seguimiento.eliminar_seguimiento(id)
    return jsonify({"mensaje": "Seguimiento eliminado correctamente"})



if __name__ == '__main__':
    app.run(debug=True, port=5000)

from flask import Flask, request, jsonify
import cliente
import almacen
import catalogo
import categorias
import compras
import comprobantePago
import detallesCompra
import detallesPedido
import documentos
import exportaciones
import importaciones
import packingList
import pedidos
import productos
import proveedores
import seguimientoPedidos
import tipos
import ventaDetalle
import ventas



app = Flask(__name__)

@app.route('/')
def inicio():
    return "API Clientes - INFOTEL BUSINESS"


#============cliente============#
@app.route('/clientes', methods=['POST'])
def crear_cliente():
    data = request.json
    cliente.crear_cliente(data)
    return jsonify({"mensaje": "Cliente creado con éxito"}), 201

@app.route('/clientes', methods=['GET'])
def listar_clientes():
    resultado = cliente.listar_clientes()
    return jsonify(resultado)

@app.route('/clientes/<int:id_cliente>', methods=['GET'])
def obtener_cliente(id_cliente):
    cliente_data = cliente.obtener_cliente_por_id(id_cliente)
    if cliente_data:
        return jsonify(cliente_data)
    else:
        return jsonify({"mensaje": "Cliente no encontrado"}), 404

@app.route('/clientes/<int:id_cliente>', methods=['PUT'])
def actualizar_cliente(id_cliente):
    data = request.json
    cliente.actualizar_cliente(id_cliente, data)
    return jsonify({"mensaje": "Cliente actualizado correctamente"})

@app.route('/clientes/<int:id_cliente>', methods=['DELETE'])
def eliminar_cliente(id_cliente):
    cliente.eliminar_cliente(id_cliente)
    return jsonify({"mensaje": "Cliente eliminado correctamente"})
#==============almacen===========#
@app.route('/almacen', methods=['POST'])
def crear_almacen():
    data = request.json
    almacen.crear_almacen(data)
    return jsonify({"mensaje": "Registro de almacén creado con éxito"}), 201

@app.route('/almacen', methods=['GET'])
def listar_almacen():
    resultado = almacen.listar_almacen()
    return jsonify(resultado)

@app.route('/almacen/<int:id_almacen>', methods=['GET'])
def obtener_almacen(id_almacen):
    almacen_data = almacen.obtener_almacen_por_id(id_almacen)
    if almacen_data:
        return jsonify(almacen_data)
    else:
        return jsonify({"mensaje": "Registro de almacén no encontrado"}), 404

@app.route('/almacen/<int:id_almacen>', methods=['PUT'])
def actualizar_almacen(id_almacen):
    data = request.json
    almacen.actualizar_almacen(id_almacen, data)
    return jsonify({"mensaje": "Registro de almacén actualizado correctamente"})

@app.route('/almacen/<int:id_almacen>', methods=['DELETE'])
def eliminar_almacen(id_almacen):
    almacen.eliminar_almacen(id_almacen)
    return jsonify({"mensaje": "Registro de almacén eliminado correctamente"})
#===============catalgo================#
@app.route('/catalogo', methods=['POST'])
def crear_catalogo():
    data = request.json
    catalogo.crear_catalogo(data)
    return jsonify({"mensaje": "Catálogo creado con éxito"}), 201

@app.route('/catalogo', methods=['GET'])
def listar_catalogo():
    resultado = catalogo.listar_catalogo()
    return jsonify(resultado)

@app.route('/catalogo/<int:id_catalogo>', methods=['GET'])
def obtener_catalogo(id_catalogo):
    catalogo_data = catalogo.obtener_catalogo(id_catalogo)
    if catalogo_data:
        return jsonify(catalogo_data)
    else:
        return jsonify({"mensaje": "Catálogo no encontrado"}), 404

@app.route('/catalogo/<int:id_catalogo>', methods=['PUT'])
def actualizar_catalogo(id_catalogo):
    data = request.json
    catalogo.actualizar_catalogo(id_catalogo, data)
    return jsonify({"mensaje": "Catálogo actualizado correctamente"})

@app.route('/catalogo/<int:id_catalogo>', methods=['DELETE'])
def eliminar_catalogo(id_catalogo):
    catalogo.eliminar_catalogo(id_catalogo)
    return jsonify({"mensaje": "Catálogo eliminado correctamente"})

#===============categorias================#
@app.route('/categorias', methods=['POST'])
def crear_categoria():
    data = request.json
    categorias.crear_categorias(data)
    return jsonify({"mensaje": "Categoría creada con éxito"}), 201

@app.route('/categorias', methods=['GET'])
def listar_categorias():
    resultado = categorias.obtener_categorias()
    return resultado  # ya devuelve jsonify

@app.route('/categorias/<int:id>', methods=['GET'])
def obtener_categoria(id):
    categoria_data = categorias.obtener_categorias_por_id(id)
    if categoria_data.status_code == 404:
        return categoria_data
    return categoria_data

@app.route('/categorias/<int:id>', methods=['PUT'])
def actualizar_categoria(id):
    data = request.json
    categorias.actualizar_categorias(id, data)
    return jsonify({"mensaje": "Categoría actualizada correctamente"})

@app.route('/categorias/<int:id>', methods=['DELETE'])
def eliminar_categoria(id):
    categorias.eliminar_categorias(id)
    return jsonify({"mensaje": "Categoría eliminada correctamente"})
#===============compras================#
@app.route('/compras', methods=['POST'])
def crear_compra():
    data = request.json
    compras.crear_compra(
        data['id_proveedor'],
        data['fecha_compra'],
        data['total'],
        data['metodo_pago']
    )
    return jsonify({"mensaje": "Compra creada con éxito"}), 201

@app.route('/compras', methods=['GET'])
def listar_compras():
    resultado = compras.listar_compras()
    return jsonify(resultado)

@app.route('/compras/<int:id>', methods=['GET'])
def obtener_compra(id):
    compra_data = compras.obtener_compra(id)
    if compra_data is None:
        return jsonify({"mensaje": "Compra no encontrada"}), 404
    return jsonify(compra_data)

@app.route('/compras/<int:id>', methods=['PUT'])
def actualizar_compra(id):
    data = request.json
    compras.actualizar_compra(
        id,
        data['id_proveedor'],
        data['fecha_compra'],
        data['total'],
        data['metodo_pago']
    )
    return jsonify({"mensaje": "Compra actualizada correctamente"})

@app.route('/compras/<int:id>', methods=['DELETE'])
def eliminar_compra(id):
    compras.eliminar_compra(id)
    return jsonify({"mensaje": "Compra eliminada correctamente"})


#===============comprobantePago================#
@app.route('/comprobantePago', methods=['POST'])
def crear_comprobante_pago():
    data = request.json
    comprobantePago.crear_comprobante_pago(
        data['id_exportacion'],
        data['id_importacion'],
        data['numero'],
        data['fecha_emision'],
        data['subtotal'],
        data['descuento_total'],
        data['impuesto'],
        data['total'],
        data['tipo_documento'],
        data['archivo_url']
    )
    return jsonify({"mensaje": "Comprobante de pago creado con éxito"}), 201

@app.route('/comprobantePago', methods=['GET'])
def listar_comprobantes_pago():
    resultado = comprobantePago.listar_comprobantes_pago()
    return jsonify(resultado)

@app.route('/comprobantePago/<int:id>', methods=['GET'])
def obtener_comprobante_pago(id):
    comprobante_data = comprobantePago.obtener_comprobante_pago(id)
    if comprobante_data is None:
        return jsonify({"mensaje": "Comprobante de pago no encontrado"}), 404
    return jsonify(comprobante_data)

@app.route('/comprobantePago/<int:id>', methods=['PUT'])
def actualizar_comprobante_pago(id):
    data = request.json
    comprobantePago.actualizar_comprobante_pago(
        id,
        data['id_exportacion'],
        data['id_importacion'],
        data['numero'],
        data['fecha_emision'],
        data['subtotal'],
        data['descuento_total'],
        data['impuesto'],
        data['total'],
        data['tipo_documento'],
        data['archivo_url']
    )
    return jsonify({"mensaje": "Comprobante de pago actualizado correctamente"})

@app.route('/comprobantePago/<int:id>', methods=['DELETE'])
def eliminar_comprobante_pago(id):
    comprobantePago.eliminar_comprobante_pago(id)
    return jsonify({"mensaje": "Comprobante de pago eliminado correctamente"})


#===============detalleCompra================#
@app.route('/detalleCompra', methods=['POST'])
def crear_detalle_compra():
    data = request.json
    detallesCompra.crear_detalle_compra(
        data['id_compra'],
        data['id_producto'],
        data['cantidad'],
        data['precio_unitario']
    )
    return jsonify({"mensaje": "Detalle de compra creado con éxito"}), 201

@app.route('/detalleCompra', methods=['GET'])
def listar_detalles_compra():
    resultado = detallesCompra.listar_detalles_compra()
    return jsonify(resultado)

@app.route('/detalleCompra/<int:id>', methods=['GET'])
def obtener_detalle_compra(id):
    detalle_data = detallesCompra.obtener_detalle_compra(id)
    if detalle_data is None:
        return jsonify({"mensaje": "Detalle de compra no encontrado"}), 404
    return jsonify(detalle_data)

@app.route('/detalleCompra/<int:id>', methods=['PUT'])
def actualizar_detalle_compra(id):
    data = request.json
    detallesCompra.actualizar_detalle_compra(
        id,
        data['id_compra'],
        data['id_producto'],
        data['cantidad'],
        data['precio_unitario']
    )
    return jsonify({"mensaje": "Detalle de compra actualizado correctamente"})

@app.route('/detalleCompra/<int:id>', methods=['DELETE'])
def eliminar_detalle_compra(id):
    detallesCompra.eliminar_detalle_compra(id)
    return jsonify({"mensaje": "Detalle de compra eliminado correctamente"})

#===============detallePedido================#
@app.route('/detallePedido', methods=['POST'])
def crear_detalle_pedido():
    data = request.json
    detallesPedido.crear_detalle_pedido(
        data['id_pedido'],
        data['id_producto'],
        data['cantidad'],
        data['precio_unitario']
    )
    return jsonify({"mensaje": "Detalle de pedido creado con éxito"}), 201

@app.route('/detallePedido', methods=['GET'])
def listar_detalles_pedido():
    resultado = detallesPedido.listar_detalles_pedido()
    return jsonify(resultado)

@app.route('/detallePedido/<int:id>', methods=['GET'])
def obtener_detalle_pedido(id):
    detalle_data = detallesPedido.obtener_detalle_pedido(id)
    if detalle_data is None:
        return jsonify({"mensaje": "Detalle de pedido no encontrado"}), 404
    return jsonify(detalle_data)

@app.route('/detallePedido/<int:id>', methods=['PUT'])
def actualizar_detalle_pedido(id):
    data = request.json
    detallesPedido.actualizar_detalle_pedido(
        id,
        data['id_pedido'],
        data['id_producto'],
        data['cantidad'],
        data['precio_unitario']
    )
    return jsonify({"mensaje": "Detalle de pedido actualizado correctamente"})

@app.route('/detallePedido/<int:id>', methods=['DELETE'])
def eliminar_detalle_pedido(id):
    detallesPedido.eliminar_detalle_pedido(id)
    return jsonify({"mensaje": "Detalle de pedido eliminado correctamente"})

#===============documentos================#
@app.route('/documentos', methods=['POST'])
def crear_documento():
    data = request.json
    documentos.crear_documento(
        data['id_pedido'],
        data['tipo_documento'],
        data['numero'],
        data['fecha_emision'],
        data['archivo_url']
    )
    return jsonify({"mensaje": "Documento creado con éxito"}), 201

@app.route('/documentos', methods=['GET'])
def listar_documentos():
    resultado = documentos.listar_documentos()
    return jsonify(resultado)

@app.route('/documentos/<int:id>', methods=['GET'])
def obtener_documento(id):
    documento_data = documentos.obtener_documento(id)
    if documento_data is None:
        return jsonify({"mensaje": "Documento no encontrado"}), 404
    return jsonify(documento_data)

@app.route('/documentos/<int:id>', methods=['PUT'])
def actualizar_documento(id):
    data = request.json
    documentos.actualizar_documento(
        id,
        data['id_pedido'],
        data['tipo_documento'],
        data['numero'],
        data['fecha_emision'],
        data['archivo_url']
    )
    return jsonify({"mensaje": "Documento actualizado correctamente"})

@app.route('/documentos/<int:id>', methods=['DELETE'])
def eliminar_documento(id):
    documentos.eliminar_documento(id)
    return jsonify({"mensaje": "Documento eliminado correctamente"})


#===============exportaciones================#
@app.route('/exportaciones', methods=['POST'])
def crear_exportacion():
    data = request.json
    exportaciones.crear_exportacion(
        data['id_venta'],
        data['id_comprobante'],
        data['pais_destino'],
        data['descripcion_carga'],
        data['fecha_envio']
    )
    return jsonify({"mensaje": "Exportación creada con éxito"}), 201

@app.route('/exportaciones', methods=['GET'])
def listar_exportaciones():
    resultado = exportaciones.listar_exportaciones()
    return jsonify(resultado)

@app.route('/exportaciones/<int:id>', methods=['GET'])
def obtener_exportacion(id):
    exportacion_data = exportaciones.obtener_exportacion(id)
    if exportacion_data is None:
        return jsonify({"mensaje": "Exportación no encontrada"}), 404
    return jsonify(exportacion_data)

@app.route('/exportaciones/<int:id>', methods=['PUT'])
def actualizar_exportacion(id):
    data = request.json
    exportaciones.actualizar_exportacion(
        id,
        data['id_venta'],
        data['id_comprobante'],
        data['pais_destino'],
        data['descripcion_carga'],
        data['fecha_envio']
    )
    return jsonify({"mensaje": "Exportación actualizada correctamente"})

@app.route('/exportaciones/<int:id>', methods=['DELETE'])
def eliminar_exportacion(id):
    exportaciones.eliminar_exportacion(id)
    return jsonify({"mensaje": "Exportación eliminada correctamente"})

#===============importaciones================#
@app.route('/importaciones', methods=['POST'])
def crear_importacion():
    data = request.json
    importaciones.crear_importacion(
        data['id_proveedor'],
        data['id_compra'],
        data['descripcion'],
        data['fecha_ingreso'],
        data['documento_ingreso'],
        data['id_comprobante']
    )
    return jsonify({"mensaje": "Importación creada con éxito"}), 201

@app.route('/importaciones', methods=['GET'])
def listar_importaciones():
    resultado = importaciones.listar_importaciones()
    return jsonify(resultado)

@app.route('/importaciones/<int:id>', methods=['GET'])
def obtener_importacion(id):
    importacion_data = importaciones.obtener_importacion(id)
    if importacion_data is None:
        return jsonify({"mensaje": "Importación no encontrada"}), 404
    return jsonify(importacion_data)

@app.route('/importaciones/<int:id>', methods=['PUT'])
def actualizar_importacion(id):
    data = request.json
    importaciones.actualizar_importacion(
        id,
        data['id_proveedor'],
        data['id_compra'],
        data['descripcion'],
        data['fecha_ingreso'],
        data['documento_ingreso'],
        data['id_comprobante']
    )
    return jsonify({"mensaje": "Importación actualizada correctamente"})

@app.route('/importaciones/<int:id>', methods=['DELETE'])
def eliminar_importacion(id):
    importaciones.eliminar_importacion(id)
    return jsonify({"mensaje": "Importación eliminada correctamente"})


#===============packingList================#
@app.route('/packingList', methods=['POST'])
def crear_packing_list():
    data = request.json
    packingList.crear_packing_list(
        data['id_exportacion'],
        data['id_importacion'],
        data['fecha_packing'],
        data['descripcion'],
        data['cantidad_total'],
        data['peso_total'],
        data['volumen_total'],
        data['inspeccionado_por'],
        data['observaciones']
    )
    return jsonify({"mensaje": "Packing List creado con éxito"}), 201

@app.route('/packingList', methods=['GET'])
def listar_packing_list():
    resultado = packingList.listar_packing_list()
    return jsonify(resultado)

@app.route('/packingList/<int:id>', methods=['GET'])
def obtener_packing_list(id):
    packing = packingList.obtener_packing_list(id)
    if packing is None:
        return jsonify({"mensaje": "Packing List no encontrado"}), 404
    return jsonify(packing)

@app.route('/packingList/<int:id>', methods=['PUT'])
def actualizar_packing_list(id):
    data = request.json
    packingList.actualizar_packing_list(
        id,
        data['id_exportacion'],
        data['id_importacion'],
        data['fecha_packing'],
        data['descripcion'],
        data['cantidad_total'],
        data['peso_total'],
        data['volumen_total'],
        data['inspeccionado_por'],
        data['observaciones']
    )
    return jsonify({"mensaje": "Packing List actualizado correctamente"})

@app.route('/packingList/<int:id>', methods=['DELETE'])
def eliminar_packing_list(id):
    packingList.eliminar_packing_list(id)
    return jsonify({"mensaje": "Packing List eliminado correctamente"})


#===============pedidos================#
@app.route('/pedidos', methods=['POST'])
def crear_pedido():
    data = request.json
    pedidos.crear_pedidos(
        data['id_cliente'],
        data['fecha_pedido'],
        data['estado']
    )
    return jsonify({"mensaje": "Pedido creado correctamente"}), 201

@app.route('/pedidos', methods=['GET'])
def listar_pedidos():
    resultado = pedidos.obtener_pedidos()
    return jsonify(resultado)

@app.route('/pedidos/<int:id>', methods=['GET'])
def obtener_pedido(id):
    pedido = pedidos.obtener_pedidos_por_id(id)
    if pedido is None or (isinstance(pedido, dict) and pedido.get("mensaje")):
        return jsonify({"mensaje": "Pedido no encontrado"}), 404
    return jsonify(pedido)

@app.route('/pedidos/<int:id>', methods=['PUT'])
def actualizar_pedido(id):
    data = request.json
    pedidos.actualizar_pedidos(
        id,
        data
    )
    return jsonify({"mensaje": "Pedido actualizado correctamente"})

@app.route('/pedidos/<int:id>', methods=['DELETE'])
def eliminar_pedido(id):
    pedidos.eliminar_pedidos(id)
    return jsonify({"mensaje": "Pedido eliminado correctamente"})


#===============productos================#
@app.route('/productos', methods=['POST'])
def crear_producto():
    data = request.json
    productos.crear_productos(
        data['nombre'],
        data['descripcion'],
        data['precio_unitario'],
        data['id_categoria'],
        data['id_tipo'],
        data['id_proveedor']
    )
    return jsonify({"mensaje": "Producto creado correctamente"}), 201

@app.route('/productos', methods=['GET'])
def listar_productos():
    resultado = productos.obtener_productos()
    return jsonify(resultado)

@app.route('/productos/<int:id>', methods=['GET'])
def obtener_producto(id):
    producto = productos.obtener_productos_por_id(id)
    if producto is None or (isinstance(producto, dict) and producto.get("mensaje")):
        return jsonify({"mensaje": "Producto no encontrado"}), 404
    return jsonify(producto)

@app.route('/productos/<int:id>', methods=['PUT'])
def actualizar_producto(id):
    data = request.json
    productos.actualizar_productos(id, data)
    return jsonify({"mensaje": "Producto actualizado correctamente"})

@app.route('/productos/<int:id>', methods=['DELETE'])
def eliminar_producto(id):
    productos.eliminar_productos(id)
    return jsonify({"mensaje": "Producto eliminado correctamente"})

#===============proveedores================#
@app.route('/proveedores', methods=['POST'])
def crear_proveedor():
    data = request.json
    proveedores.crear_proveedores(data)
    return jsonify({"mensaje": "Proveedor creado correctamente"}), 201

@app.route('/proveedores', methods=['GET'])
def listar_proveedores():
    resultado = proveedores.obtener_proveedores()
    return jsonify(resultado)

@app.route('/proveedores/<int:id>', methods=['GET'])
def obtener_proveedor(id):
    proveedor = proveedores.obtener_proveedores_por_id(id)
    if proveedor is None or (isinstance(proveedor, dict) and proveedor.get("mensaje")):
        return jsonify({"mensaje": "Proveedor no encontrado"}), 404
    return jsonify(proveedor)

@app.route('/proveedores/<int:id>', methods=['PUT'])
def actualizar_proveedor(id):
    data = request.json
    proveedores.actualizar_proveedores(id, data)
    return jsonify({"mensaje": "Proveedor actualizado correctamente"})

@app.route('/proveedores/<int:id>', methods=['DELETE'])
def eliminar_proveedor(id):
    proveedores.eliminar_proveedores(id)
    return jsonify({"mensaje": "Proveedor eliminado correctamente"})

#===============seguimiento_pedidos================#
@app.route('/seguimiento', methods=['POST'])
def crear_seguimiento():
    data = request.json
    seguimiento.crear_seguimiento(data)
    return jsonify({"mensaje": "Seguimiento creado correctamente"}), 201

@app.route('/seguimiento', methods=['GET'])
def listar_seguimiento():
    resultado = seguimiento.listar_seguimiento()
    return jsonify(resultado)

@app.route('/seguimiento/<int:id>', methods=['GET'])
def obtener_seguimiento(id):
    registro = seguimiento.obtener_seguimiento_por_id(id)
    if registro is None:
        return jsonify({"mensaje": "Registro de seguimiento no encontrado"}), 404
    return jsonify(registro)

@app.route('/seguimiento/<int:id>', methods=['PUT'])
def actualizar_seguimiento(id):
    data = request.json
    seguimiento.actualizar_seguimiento(id, data)
    return jsonify({"mensaje": "Seguimiento actualizado correctamente"})

@app.route('/seguimiento/<int:id>', methods=['DELETE'])
def eliminar_seguimiento(id):
    seguimiento.eliminar_seguimiento(id)
    return jsonify({"mensaje": "Seguimiento eliminado correctamente"})



if __name__ == '__main__':
    app.run(debug=True, port=5000)
