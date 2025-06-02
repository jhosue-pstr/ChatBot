import mysql.connector

def obtener_conexion():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="infotel_db",
        port=3306
    )


def crear_detalle_venta(id_venta, id_pedido, id_producto, cantidad, precio_unitario):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = """
        INSERT INTO detalles_venta (id_venta, id_pedido, id_producto, cantidad, precio_unitario)
        VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (id_venta, id_pedido, id_producto, cantidad, precio_unitario))
    conexion.commit()
    cursor.close()
    conexion.close()

def listar_detalles_venta():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM detalles_venta")
    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()
    return resultados

def obtener_detalle_venta(id_detalle_venta):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM detalles_venta WHERE id_detalle_venta = %s", (id_detalle_venta,))
    detalle_venta = cursor.fetchone()
    cursor.close()
    conexion.close()
    return detalle_venta

def actualizar_detalle_venta(id_detalle_venta, id_venta, id_pedido, id_producto, cantidad, precio_unitario):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = """
        UPDATE detalles_venta
        SET id_venta = %s, id_pedido = %s, id_producto = %s, cantidad = %s, precio_unitario = %s
        WHERE id_detalle_venta = %s
    """
    cursor.execute(sql, (id_venta, id_pedido, id_producto, cantidad, precio_unitario, id_detalle_venta))
    conexion.commit()
    cursor.close()
    conexion.close()

def eliminar_detalle_venta(id_detalle_venta):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM detalles_venta WHERE id_detalle_venta = %s", (id_detalle_venta,))
    conexion.commit()
    cursor.close()
    conexion.close()
