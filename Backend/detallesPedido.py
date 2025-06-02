import mysql.connector

def obtener_conexion():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="infotel_db",
        port=3306
    )

def crear_detalle_pedido(id_pedido, id_producto, cantidad, precio_unitario):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = """
        INSERT INTO detalles_pedido (id_pedido, id_producto, cantidad, precio_unitario)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(sql, (id_pedido, id_producto, cantidad, precio_unitario))
    conexion.commit()
    cursor.close()
    conexion.close()

def listar_detalles_pedido():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM detalles_pedido")
    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()
    return resultados

def obtener_detalle_pedido(id_detalle):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM detalles_pedido WHERE id_detalle = %s", (id_detalle,))
    detalle = cursor.fetchone()
    cursor.close()
    conexion.close()
    return detalle

def actualizar_detalle_pedido(id_detalle, id_pedido, id_producto, cantidad, precio_unitario):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = """
        UPDATE detalles_pedido SET id_pedido = %s, id_producto = %s, cantidad = %s, precio_unitario = %s
        WHERE id_detalle = %s
    """
    cursor.execute(sql, (id_pedido, id_producto, cantidad, precio_unitario, id_detalle))
    conexion.commit()
    cursor.close()
    conexion.close()

def eliminar_detalle_pedido(id_detalle):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM detalles_pedido WHERE id_detalle = %s", (id_detalle,))
    conexion.commit()
    cursor.close()
    conexion.close()
