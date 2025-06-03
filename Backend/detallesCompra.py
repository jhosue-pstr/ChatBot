import mysql.connector

def obtener_conexion():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="infotel_db",
        port=3306
    )


def crear_detalle_compra(id_compra, id_producto, cantidad, precio_unitario):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = """
        INSERT INTO detalles_compra (id_compra, id_producto, cantidad, precio_unitario)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(sql, (id_compra, id_producto, cantidad, precio_unitario))
    conexion.commit()
    cursor.close()
    conexion.close()

def listar_detalles_compra():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM detalles_compra")
    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()
    return resultados

def obtener_detalle_compra(id_detalle_compra):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM detalles_compra WHERE id_detalle_compra = %s", (id_detalle_compra,))
    detalle_compra = cursor.fetchone()
    cursor.close()
    conexion.close()
    return detalle_compra

def actualizar_detalle_compra(id_detalle_compra, id_compra, id_producto, cantidad, precio_unitario):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = """
        UPDATE detalles_compra
        SET id_compra = %s, id_producto = %s, cantidad = %s, precio_unitario = %s
        WHERE id_detalle_compra = %s
    """
    cursor.execute(sql, (id_compra, id_producto, cantidad, precio_unitario, id_detalle_compra))
    conexion.commit()
    cursor.close()
    conexion.close()

def eliminar_detalle_compra(id_detalle_compra):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM detalles_compra WHERE id_detalle_compra = %s", (id_detalle_compra,))
    conexion.commit()
    cursor.close()
    conexion.close()
