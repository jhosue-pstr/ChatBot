import mysql.connector

def obtener_conexion():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="infotel_db",
        port=3306
    )

def crear_venta(id_pedido, id_cliente, fecha_venta, total, metodo_pago):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = """
        INSERT INTO ventas (id_pedido, id_cliente, fecha_venta, total, metodo_pago)
        VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (id_pedido, id_cliente, fecha_venta, total, metodo_pago))
    conexion.commit()
    cursor.close()
    conexion.close()

def listar_ventas():
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM ventas")
    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()
    return resultados

def obtener_venta(id_venta):
    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM ventas WHERE id_venta = %s", (id_venta,))
    venta = cursor.fetchone()
    cursor.close()
    conexion.close()
    return venta

def actualizar_venta(id_venta, id_pedido, id_cliente, fecha_venta, total, metodo_pago):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = """
        UPDATE ventas
        SET id_pedido = %s, id_cliente = %s, fecha_venta = %s, total = %s, metodo_pago = %s
        WHERE id_venta = %s
    """
    cursor.execute(sql, (id_pedido, id_cliente, fecha_venta, total, metodo_pago, id_venta))
    conexion.commit()
    cursor.close()
    conexion.close()

def eliminar_venta(id_venta):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM ventas WHERE id_venta = %s", (id_venta,))
    conexion.commit()
    cursor.close()
    conexion.close()
